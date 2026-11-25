"""Read the data-only YAML forms used for human records, without extra packages."""
import json
import re


def pairs(items):
    ans = {}
    for k,v in items:
        if k in ans:
            raise ValueError(f"Repeated key {k}")
        ans[k] = v
    return ans


def parts(text, delimiter):
    quoted = None
    escaping = False
    depth = 0
    start = 0
    for i,c in enumerate(text):
        if escaping:
            escaping=False
        elif quoted:
            if c == "\\" and quoted=='"': escaping=True
            elif c==quoted: quoted=None
        elif c in ('"', "'") and (i==0 or text[i-1] in " :,[{"): quoted=c
        elif c in "[{": depth+=1
        elif c in "]}": depth-=1
        elif depth==0 and c==delimiter:
            yield text[start:i]
            start=i+1
    yield text[start:]


def scalar(s):
    s=re.split(r"\s+#",s,1)[0].strip() if not s.startswith(('"',"'","[","{")) else s.strip()
    if s.startswith('"'):
        return json.loads(s)
    if s.startswith("'"):
        if not s.endswith("'"):raise ValueError("Unclosed single quote")
        return s[1:-1].replace("''","'")
    if s.startswith("[") and s.endswith("]"):
        t=s[1:-1].strip()
        return [scalar(x.strip()) for x in parts(t,",")] if t else []
    if s.startswith("{") and s.endswith("}"):
        t=s[1:-1].strip()
        if not t:return {}
        out=[]
        for item in parts(t,","):
            pair=list(parts(item,":"))
            if len(pair)<2:raise ValueError("Invalid inline YAML mapping")
            out.append((scalar(pair[0].strip()),scalar(":".join(pair[1:]).strip())))
        return pairs(out)
    if re.fullmatch(r"-?(?:0|[1-9]\d*)(?:\.\d+)?",s):
        return float(s) if "." in s else int(s)
    if s in ("null","~"): return None
    if s in ("true","false"):return s=="true"
    if s.startswith(("!","&","*","[","{")):raise ValueError("Use plain data in the documented YAML format")
    return s


def read_yaml(text):
    text=text.lstrip("\ufeff")
    try:
        return json.loads(text,object_pairs_hook=pairs)
    except json.JSONDecodeError:
        pass
    lines=text.splitlines()
    def skip(i):
        while i<len(lines) and (not lines[i].strip() or lines[i].lstrip().startswith("#") or lines[i].strip() in {"---","..."}):
            i+=1
        return i
    def indentation(i):
        line=lines[i]
        if re.match(r"^ *\t",line):raise ValueError("Indent YAML with spaces")
        return len(line)-len(line.lstrip(" "))
    def group(i,level):
        seq=lines[i][level:].startswith("- ")
        result=[] if seq else {}
        while True:
            i=skip(i)
            if i>=len(lines) or indentation(i)<level:break
            if indentation(i)!=level:raise ValueError(f"Unexpected indentation on line {i+1}")
            item=lines[i][level:].strip()
            if seq:
                if not item.startswith("- "):raise ValueError("Invalid YAML sequence")
                result.append(scalar(item[2:].strip()));i+=1;continue
            match=re.fullmatch(r"([A-Za-z0-9_-]+):(?:\s+(.*))?",item)
            if not match:raise ValueError(f"Use a field name and a colon on line {i+1}")
            key,raw=match.groups();i+=1
            if key in result:raise ValueError("Repeated YAML key "+key)
            if raw in {"|",">","|-",">-"}:
                j=i
                while j<len(lines) and (not lines[j].strip() or indentation(j)>level):j+=1
                content=lines[i:j]
                indent=min((len(l)-len(l.lstrip(" ")) for l in content if l.strip()),default=0)
                content=[l[indent:] for l in content]
                result[key]=("\n" if raw[0]=="|" else " ").join(content).rstrip()+("" if raw.endswith("-") else "\n")
                i=j
            elif raw is None or raw.startswith("#"):
                i=skip(i)
                if i<len(lines) and indentation(i)>level:
                    result[key],i=group(i,indentation(i))
                else:
                    result[key]=None
            else:result[key]=scalar(raw)
        return result,i
    start=skip(0)
    if start==len(lines):raise ValueError("Empty YAML")
    result,end=group(start,indentation(start))
    if skip(end)!=len(lines):raise ValueError("Unexpected YAML after the record")
    return result
