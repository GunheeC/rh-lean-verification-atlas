"""Regression checks for exact publication consent and the Git author identity."""
from collections import Counter
from pathlib import Path
import unittest

from scan_privacy import PUBLIC_EMAILS, count_tokens
from scan_public_history import OWNER


class PublicContactTests(unittest.TestCase):
    def test_known_contacts_and_boundaries(self):
        contacts = {
            b"GunheeC" + b"@users.noreply.github.com": "authorized_owner_noreply",
            b"wvx17" + b"@txstate.edu": "authorized_academic_email",
            b"geonhee" + b"@transcendq.com": "authorized_company_email",
        }
        self.assertEqual(contacts, PUBLIC_EMAILS)
        for address, category in contacts.items():
            for wrapper in (b"%s.", b"<%s>", b"mailto:%s", b"`%s`", b"'%s'"):
                with self.subTest(category=category, wrapper=wrapper):
                    self.assertEqual(count_tokens(wrapper % address), Counter({category: 1}))
            local, domain = address.split(b"@")
            other = (
                address.upper(), local + b"+mail@" + domain, b"other." + address,
                local + b"@sub." + domain, address + b".org", b"other!" + address,
                "é".encode() + address, address + "é".encode(), b"another@" + domain,
                local + b"@" + "tхstate.edu".encode(), address + "。example".encode(),
                "상대".encode() + b"@" + "수학.한국".encode(),
            )
            for candidate in other:
                with self.subTest(category=category, case=candidate):
                    self.assertEqual(count_tokens(candidate), Counter(email_candidate=1))
        self.assertEqual(OWNER, b"Gunhee Cho <GunheeC" + b"@users.noreply.github.com>")

    def test_scanner_sources_introduce_no_candidates(self):
        for name in ("scan_privacy.py", "scan_public_history.py", Path(__file__).name):
            self.assertFalse(count_tokens(Path(__file__).with_name(name).read_bytes()))


if __name__ == "__main__":
    unittest.main()
