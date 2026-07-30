#!/usr/bin/env python3
"""
简单的 Todo CLI：add/list/done/remove，数据保存在 tasks.json
"""
import argparse
import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).parent / "tasks.json"

def load_tasks():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")

def add_task(text):
    tasks = load_tasks()
    task = {
        "id": (tasks[-1]["id"] + 1) if tasks else 1,
        "text": text,
        "done": False,
        "created_at": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: [{task['id']}] {task['text']}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for t in tasks:
        status = "✓" if t["done"] else " "
        print(f"[{t['id']}] [{status}] {t['text']} (created: {t['created_at']})")

def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Marked done: [{t['id']}] {t['text']}")
            return
    print("Task not found.")

def remove_task(task_id):
    tasks = load_tasks()
    new = [t for t in tasks if t["id"] != task_id]
    if len(new) == len(tasks):
        print("Task not found.")
    else:
        save_tasks(new)
        print(f"Removed task {task_id}.")

def parse_args():
    p = argparse.ArgumentParser(description="Todo CLI")
    sub = p.add_subparsers(dest="cmd")

    p_add = sub.add_parser("add")
    p_add.add_argument("text", help="task text", nargs="+")
    sub.add_parser("list")
    p_done = sub.add_parser("done")
    p_done.add_argument("id", type=int)
    p_rm = sub.add_parser("remove")
    p_rm.add_argument("id", type=int)

    return p.parse_args()

def main():
    args = parse_args()
    if not args.cmd:
        print("Use subcommands: add/list/done/remove")
        return
    if args.cmd == "add":
        add_task(" ".join(args.text))
    elif args.cmd == "list":
        list_tasks()
    elif args.cmd == "done":
        mark_done(args.id)
    elif args.cmd == "remove":
        remove_task(args.id)

if __name__ == "__main__":
    main()