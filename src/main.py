#!/usr/bin/env python3

from parcers import Parser
from task_manager import TaskManager


def main():
    parser = Parser().get_parser()
    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == "add":
        task_manager.add_task(args.description)
    elif args.command == "update":
        task_manager.update_task(args.id, args.description)
    elif args.command == "delete":
        task_manager.delete_task(args.id)
    elif args.command == "mark-in-progress":
        task_manager.mark_in_progress(args.id)
    elif args.command == "mark-done":
        task_manager.mark_done(args.id)
    elif args.command == "list":
        task_manager.list_tasks(args.status)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
