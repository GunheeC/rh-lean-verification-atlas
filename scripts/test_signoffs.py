"""Exercise sign-off eligibility and failure cases with temporary, fictitious records."""
import json
from pathlib import Path
import tempfile
import unittest

from add_signoff import FIELDS, import_record, submission
from signoff_records import ATTESTATION, INDEPENDENCE, disputes, human_state, load_records, validate, validate_one, l4_summary

U="TEST-ONLY"
E="a"*64
OLD="b"*64
A="c"*64
B="d"*64
X="e"*64


class HumanRecordsTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        for d in ["units","signoffs/records","signoffs/examples","questions"]:
            (self.root/d).mkdir(parents=True)
        self.m=dict(unit=U,edition_sha256=E,statement_sha256="1"*64,steps=[dict(id="S1",sha256=A,claim="new reading",passage_sha256="3"*64,status="active",kind="appeal-to-input",ai_review=["fictitious positive AI review"]),
                                                    dict(id="S2",sha256=B,status="active",kind="inequality")],
                    history=[dict(edition_sha256=OLD,statement_sha256="1"*64,step_texts={"S1":"old reading"},step_passages={"S1":"4"*64},steps={"S1":X,"S2":B}),dict(edition_sha256=E,steps={"S1":X,"S2":B})])
        (self.root/"units"/(U+".steps.yaml")).write_text(json.dumps(self.m))

        self.set_status("Full")

    def set_status(self, status):
        (self.root/"units"/(U+".yaml")).write_text(json.dumps({"id":U,"status":status}))

    def whole(self,name="FICTITIOUS TEST READER A",level="none",orcid=None):
        for target in ("S1","S2","statement-vs-lean"):
            r=self.sample(target,name=name)
            if orcid:
                r["reader"]["orcid"]=orcid
            r.update(ai_assistance_used=level,ai_assistance_description="Fictitious test disclosure")
            import_record(self.root,r)

    def sample(self,target="S1",verdict="checked-correct",name="FICTITIOUS TEST READER A"):
        return dict(reader=dict(name=name,level="other",field="fictitious test"),
                    unit=U,edition_sha256=E,scope={"steps":[target]} if target.startswith("S") else target,
                    verdict={target:verdict},what_i_did=INDEPENDENCE+" Recomputed the example.",time_spent_hours=1.5,
                    reservations="A missing denominator condition." if verdict in ("gap-found","error-found") else "none",
                    conflicts_of_interest="none",ai_assistance_used="none",ai_assistance_description="none",
                    date="2000-01-01",attestation=ATTESTATION)

    def state(self):
        return human_state(self.root,U,self.m)

    def test_no_records_no_human_credit_even_with_ai_or_example(self):
        (self.root/"signoffs/examples/FICTITIOUS.yaml").write_text(json.dumps(self.sample()))
        self.assertFalse(self.state()["l4"])
        self.assertEqual(self.state()["steps"]["S1"]["state"],"awaiting human check")
        self.assertEqual(load_records(self.root),[])

    def test_missing_identity_or_attestation_and_wrong_fingerprint(self):
        for k in ("reader","attestation"):
            r=self.sample()
            if k=="reader":r[k]["name"]=" "
            else:del r[k]
            with self.assertRaises(ValueError):validate_one(r,self.m)
        r=self.sample();r["step_sha256"]={"S1":B}
        with self.assertRaises(ValueError):validate_one(r,self.m)
        r=self.sample();r["scope"]={"steps":["S3"]}
        with self.assertRaises(ValueError):validate_one(r,self.m)

    def test_old_editions_and_changed_steps_never_count(self):
        r=self.sample();r["edition_sha256"]=OLD
        import_record(self.root,r)
        r=self.sample();r["step_sha256"]={"S1":X}
        import_record(self.root,r)
        cell=self.state()["steps"]["S1"]
        self.assertEqual(cell["state"],"awaiting human check")
        self.assertEqual([x["status"] for x in cell["checks"]],["superseded","superseded"])

    def test_negative_record_blocks_until_explicit_resolution(self):
        neg,_=import_record(self.root,self.sample(verdict="gap-found"))
        good=self.sample(name="FICTITIOUS TEST READER B")
        import_record(self.root,good)
        self.assertEqual(self.state()["steps"]["S1"]["state"],"disputed")
        self.assertIn("Open.",disputes(self.root,load_records(self.root)))
        good["resolves"]={"S1":[neg]};good["what_i_did"]="Checked the previously questioned factor against the stated nonzero hypothesis."
        import_record(self.root,good)
        self.assertEqual(self.state()["steps"]["S1"]["state"],"human-checked")
        self.assertIn("Resolved.",disputes(self.root,load_records(self.root)))
        self.assertEqual(len(load_records(self.root)),3)

    def test_whole_note_statement_and_two_readers(self):
        r=self.sample();r.update(scope="whole-note",verdict={"S1":"checked-correct","S2":"not-attempted"})
        first,_=import_record(self.root,r)
        self.assertEqual(import_record(self.root,r),(first,False))
        self.assertFalse(self.state()["l4"])
        import_record(self.root,self.sample("S2"))
        self.assertFalse(self.state()["l4"])
        import_record(self.root,self.sample("statement-vs-lean"))
        self.assertTrue(self.state()["l4"]);self.assertFalse(self.state()["two_independent"])
        for k in ("S1","S2","statement-vs-lean"):
            import_record(self.root,self.sample(k,name="FICTITIOUS TEST READER B"))
        self.assertTrue(self.state()["two_independent"])

    def test_complete_outline_and_only_an_appeal_do_not_earn_l4(self):
        self.whole()
        self.set_status("Outlined")
        self.assertFalse(self.state()["l4"])
        self.set_status("Full")
        self.m["steps"][1]["kind"]="appeal-to-input"
        self.assertFalse(self.state()["l4"])
        self.m["steps"][1]["kind"]="literature"
        self.assertFalse(self.state()["l4"])
        self.m["steps"][1]["kind"]="inequality"
        self.assertTrue(self.state()["l4"])

    def test_reservations_do_not_supply_l4(self):
        self.whole()
        r=self.sample("S2","correct-with-reservation");r["reservations"]="A fictitious unresolved concern about one bound."
        import_record(self.root,r)
        self.assertFalse(self.state()["l4"])

    def test_aided_reader_disclosed_and_ineligible_for_independence(self):
        # Fictional records, including a simulated maintainer, exist only in the temporary fixture.
        self.whole(name="Gunhee Cho",level="substantial")
        self.whole(name="FICTITIOUS TEST READER B",level="none")
        state=self.state()
        self.assertTrue(state["l4"]);self.assertFalse(state["two_independent"])
        self.assertEqual(state["l4_evidence"],dict(reader_count=2,includes_maintainer=True,ai_assistance_levels=["none","substantial"]))
        self.assertIn("substantial",l4_summary(state["l4_evidence"]))
        self.assertTrue(all(not c["independent"] for c in state["steps"]["S1"]["checks"] if c["maintainer"]))
        self.whole(name="FICTITIOUS TEST READER C",level="some")
        self.assertTrue(self.state()["two_independent"])

    def test_quoted_or_negated_independence_is_not_an_attestation(self):
        self.whole()
        for target in ("S1", "S2", "statement-vs-lean"):
            r = self.sample(target, name="FICTITIOUS SECOND READER")
            r["what_i_did"] = "I cannot say that " + INDEPENDENCE
            import_record(self.root, r)
        self.assertTrue(self.state()["l4"])
        self.assertFalse(self.state()["two_independent"])
        for target in ("S1", "S2", "statement-vs-lean"):
            r = self.sample(target, name="FICTITIOUS SECOND READER")
            r["what_i_did"] = "I recomputed this step. " + INDEPENDENCE
            import_record(self.root, r)
        self.assertTrue(self.state()["two_independent"])

    def test_single_reader_under_two_names_is_not_an_independent_pair(self):
        # This checksum-valid synthetic identifier is used as test data only.
        self.whole(name="FICTITIOUS ALIAS A",orcid="0000-0000-0000-001X")
        self.whole(name="FICTITIOUS ALIAS B",orcid="0000-0000-0000-001X")
        self.assertEqual(self.state()["l4_evidence"]["reader_count"],1)
        self.assertFalse(self.state()["two_independent"])

    def test_self_or_maintainer_may_not_close_dispute(self):
        bad=self.sample(verdict="error-found");bad["reader"]["orcid"]="0000-0000-0000-001X"
        name,_=import_record(self.root,bad)
        for who,orcid in [(bad["reader"]["name"],None),("Gunhee Cho",None),("FICTITIOUS ALIAS","0000-0000-0000-001X")]:
            fix=self.sample(name=who);fix["resolves"]={"S1":[name]}
            if orcid:fix["reader"]["orcid"]=orcid
            with self.assertRaises(ValueError):import_record(self.root,fix)
        self.assertEqual(self.state()["steps"]["S1"]["state"],"disputed")
        self.assertEqual(len(load_records(self.root)),1)

    def test_unchanged_target_objection_survives_edition_and_accepts_second_reader(self):
        old=self.sample("S2","gap-found");old["edition_sha256"]=OLD
        name,_=import_record(self.root,old)
        self.whole(name="FICTITIOUS SECOND READER")
        state=self.state();self.assertFalse(state["l4"])
        self.assertEqual(state["steps"]["S2"]["state"],"disputed")
        self.assertIn("Open on unchanged target",disputes(self.root,load_records(self.root)))
        fix=self.sample("S2",name="FICTITIOUS SECOND READER");fix["resolves"]={"S2":[name]}
        import_record(self.root,fix);self.assertTrue(self.state()["l4"])

    def test_changed_step_and_changed_statement_supersede_only_their_objection(self):
        o=self.sample("S1","error-found");o["edition_sha256"]=OLD;import_record(self.root,o)
        st=self.sample("statement-vs-lean","gap-found");st["edition_sha256"]=OLD;import_record(self.root,st)
        self.whole(name="FICTITIOUS SECOND READER")
        state=self.state();self.assertEqual(state["steps"]["S1"]["state"],"human-checked")
        self.assertEqual(state["statement_state"],"disputed")
        self.m["history"][0]["statement_sha256"]="2"*64
        (self.root/"units"/(U+".steps.yaml")).write_text(json.dumps(self.m))
        self.assertTrue(self.state()["l4"])
        self.assertIn("Superseded by changed or withdrawn target",disputes(self.root,load_records(self.root)))

    def test_changed_metadata_without_changed_prose_never_closes_objection(self):
        self.m["history"][0]["step_texts"]["S1"] = self.m["steps"][0]["claim"]
        self.m["history"][0]["step_passages"]["S1"] = self.m["steps"][0]["passage_sha256"]
        (self.root/"units"/(U+".steps.yaml")).write_text(json.dumps(self.m))
        old=self.sample("S1","gap-found");old["edition_sha256"] = OLD
        filename,_=import_record(self.root,old);self.whole(name="FICTITIOUS SECOND READER")
        self.assertEqual(self.state()["steps"]["S1"]["state"],"disputed")
        fix=self.sample("S1",name="FICTITIOUS SECOND READER");fix["resolves"]={"S1":[filename]}
        import_record(self.root,fix);self.assertTrue(self.state()["l4"])

    def test_markdown_transcription_and_native_yaml(self):
        r=self.sample(); flat=dict(r,**r["reader"]);flat.update(scope="steps [S1]",verdict="S1: checked-correct")
        body="\n\n".join(f"### {label}\n\n{flat.get(k,'_No response_')}" for label,k in FIELDS.items())
        self.assertEqual(submission(body),r)
        text=(Path(__file__).resolve().parents[1]/"signoffs/examples/FICTITIOUS-EXAMPLE.yaml").read_text()
        y=submission(text);self.assertEqual(y["scope"],{"steps":["S1","S2","S3"]})
        self.assertEqual(y["reader"]["name"],"FICTITIOUS EXAMPLE READER")
        (self.root/"questions/disputes.md").write_text(disputes(self.root,[]))
        self.assertEqual(validate(self.root),[])


if __name__=="__main__":unittest.main()
