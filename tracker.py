import sys, json
from pathlib import Path

TASKS_FILE = Path("tasks.json")

def load_tasks():
    if TASKS_FILE.exists():
        return json.loads(TASKS_FILE.read_text())
    return []

def save_tasks(tasks):
    TASKS_FILE.write_text(json.dumps(tasks, indent=2))

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {title}")

def print_usage():
    print("Usage:\n  python tracker.py add \"Task title\"")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage(); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "add":
        if len(sys.argv) < 3:
            print("Error: No task title provided."); print_usage(); sys.exit(1)
        title = " ".join(sys.argv[2:])
        add_task(title)
    else:
        print(f"Unknown command: {cmd}"); print_usage(); sys.exit(1)
