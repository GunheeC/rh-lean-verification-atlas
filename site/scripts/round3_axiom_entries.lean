import Lean

open Lean

/-- Read the axiom sets that Lean 4.33.1 serialized for the declarations in one object.
    Run only on a manifest-verified object made by the matching Lean toolchain. -/
unsafe def main (args : List String) : IO UInt32 := do
  let [path] := args | throw <| IO.userError "Expected one .olean path"
  let (data, region) ← readModuleData path
  let mut count := 0
  for (extensionName, rows) in data.entries do
    if extensionName.toString.endsWith ".exportedAxiomsExt" then
      for entry in rows do
        -- The registered persistent extension has entry type Name × Array Name.
        let (name, axioms) := unsafeCast (β := Name × Array Name) entry
        IO.println s!"{name}: {axioms}"
        count := count + 1
  region.free
  if count == 0 then
    throw <| IO.userError "No exported axiom entries in this object"
  return 0
