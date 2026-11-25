import Lean
open Lean

/-! Read the project's elaborated constants one compiled module at a time.
Index project declarations, then visit allChi's type and value dependencies, including
inductive constructors. The packer retains core weights and stops at literature nodes. -/

def hasInfix (s sub : String) : Bool := (s.splitOn sub).length > 1

def publishedHead (t : Expr) : Bool :=
  let rec concl : Expr → Expr
    | .forallE _ _ b _ => concl b
    | e => e
  match (concl t).getAppFn.constName? with
  | some n => (`GlobalTheory.Published).isPrefixOf n
  | none => false

def kindOf : ConstantInfo → String
  | .thmInfo _ => "thm" | .defnInfo _ => "def" | .axiomInfo _ => "axiom"
  | .inductInfo _ => "ind" | .ctorInfo _ => "ctor" | .recInfo _ => "rec"
  | .opaqueInfo _ => "opaque" | .quotInfo _ => "quot"

/-- constants used by the type and value; for inductives also the constructors -/
def usedOf (ci : ConstantInfo) (typeOnly : Bool) : Array Name :=
  if typeOnly then ci.type.getUsedConstants else
  let fromVal := match ci.value? (allowOpaque := true) with
    | some v => v.getUsedConstants
    | none => #[]
  let fromCtors := match ci with
    | .inductInfo v => v.ctors.toArray
    | _ => #[]
  ci.type.getUsedConstants ++ fromVal ++ fromCtors

def moduleNameOf (root : String) (f : System.FilePath) : String :=
  let s := f.toString
  let rel := if s.startsWith (root ++ "/") then toString (s.drop (root.length + 1)) else s
  let rel := if rel.endsWith ".olean" then toString (rel.dropEnd 6) else rel
  rel.replace "/" "."

def jstr (s : String) : String := (toJson s).compress

-- For a simple name, Name.toString can return the region's original string.
def copyName (n : Name) : String := String.ofList n.toString.toList

unsafe def run (oleanRoot outDir : String) : IO UInt32 := do
  let roots := #["allChi"]
  IO.FS.createDirAll outDir
  -- list modules
  let all ← System.FilePath.walkDir oleanRoot
  let files := all.filter (·.toString.endsWith ".olean")
  let mods := files.map (moduleNameOf oleanRoot)
  IO.eprintln s!"[cone] {files.size} project modules"
  IO.FS.writeFile (outDir ++ "/modules.txt") (String.intercalate "\n" mods.toList)
  -- pass 1: name -> module index
  let mut idx : Std.HashMap String Nat := {}
  for i in [:files.size] do
    let (md, reg) ← readModuleData files[i]!
    for n in md.constNames do
      idx := idx.insert (copyName n) i
    reg.free
    if (i + 1) % 10000 == 0 then IO.eprintln s!"[cone] indexed {i+1} modules, {idx.size} names"
  IO.eprintln s!"[cone] index done: {idx.size} names"
  -- pass 2: walk
  let dh ← IO.FS.Handle.mk (outDir ++ "/decls.jsonl") .write
  let eh ← IO.FS.Handle.mk (outDir ++ "/edges.jsonl") .write
  let mut seen : Std.HashSet String := {}
  let mut pending : Std.HashMap Nat (Array String) := {}
  let mut work : Array Nat := #[]
  for r in roots do
    seen := seen.insert r
    match idx[r]? with
    | some m => pending := pending.insert m ((pending.getD m #[]).push r); work := work.push m
    | none => throw (IO.userError s!"root not found in project objects: {r}")
  let mut nCore := 0
  let mut loads := 0
  while work.size > 0 do
    let mi := work.back!
    work := work.pop
    let mut todo := pending.getD mi #[]
    pending := pending.erase mi
    if todo.isEmpty then continue
    let (md, reg) ← readModuleData files[mi]!
    loads := loads + 1
    let mut loc : Std.HashMap String Nat := {}
    for j in [:md.constNames.size] do
      loc := loc.insert (copyName md.constNames[j]!) j
    let modName := mods[mi]!
    while todo.size > 0 do
      let s := todo.back!
      todo := todo.pop
      let some j := loc[s]?
        | dh.putStrLn s!"\{\"name\":{jstr s},\"cls\":\"missing\",\"module\":{jstr modName}}"
          continue
      let ci := md.constants[j]!
      let lit := publishedHead ci.type || s.startsWith "GlobalTheory.Published"
        || hasInfix modName ".PublishedTheorems."
      let cls := if lit then "lit" else "core"
      let internal := s.toName.isInternal || hasInfix s "._proof_" || hasInfix s ".match_"
      dh.putStrLn s!"\{\"name\":{jstr s},\"kind\":{jstr (kindOf ci)},\"cls\":{jstr cls},\"module\":{jstr modName},\"internal\":{internal}}"
      if cls == "core" then nCore := nCore + 1
      for d in usedOf ci lit do
        let ds := copyName d
        eh.putStrLn s!"\{\"src\":{jstr s},\"dst\":{jstr ds}}"
        unless seen.contains ds do
          seen := seen.insert ds
          match idx[ds]? with
          | none => dh.putStrLn s!"\{\"name\":{jstr ds},\"kind\":\"lib\",\"cls\":\"lib\",\"module\":\"\",\"internal\":false}"
          | some mj =>
            if mj == mi then todo := todo.push ds
            else
              pending := pending.insert mj ((pending.getD mj #[]).push ds)
              work := work.push mj
    reg.free
    if loads % 2000 == 0 then
      IO.eprintln s!"[cone] loads {loads}, core {nCore}, seen {seen.size}, work {work.size}"
  IO.eprintln s!"[cone] done: core {nCore}, seen {seen.size}, module loads {loads}"
  return 0

def main (args : List String) : IO UInt32 := do
  match args with
  | [oleanRoot, outDir] => unsafe run oleanRoot outDir
  | _ =>
    IO.eprintln "usage: lean --run trace_position_graph.lean PROJECT_OBJECTS TRACE_DIRECTORY"
    return 1
