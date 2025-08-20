import json, os, sys

DATA = "tasks.json"

def load():
    return json.loads(open(DATA).read()) if os.path.exists(DATA) else []

def save(ts):
    with open(DATA, "w") as f:
        json.dump(ts, f, indent=2)

def list_cmd():
    ts = load()
    if not ts:
        print("No tasks.")
        return
    for i, t in enumerate(ts):
        mark = "✅" if t.get("done") else "❌"
        print(f"{i}. {mark} {t['title']}")

def add_cmd(title):
    ts = load()
    ts.append({"title": title, "done": False})
    save(ts)
    print(f"Added: {title}")

def done_cmd(index):
    ts = load()
    i = int(index)
    if i < 0 or i >= len(ts):
        print(f"Bad index {index}")
        return
    ts[i]["done"] = True
    save(ts)
    print(f"Done: {ts[i]['title']}")

def help_cmd():
    print("Usage:")
    print("  python tracker.py list")
    print('  python tracker.py add "Buy milk"')
    print("  python tracker.py done 0")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        help_cmd(); sys.exit(0)
    cmd, *rest = args
    if cmd == "list": list_cmd()
    elif cmd == "add": add_cmd(" ".join(rest) or "Untitled")
    elif cmd == "done": done_cmd(rest[0] if rest else "-1")
    else: help_cmd()
