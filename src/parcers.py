import argparse


class Parser:
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            description="Task Tracker CLI",
            exit_on_error=False,
        )
        self._subparsers = self._parser.add_subparsers(dest="command")

        self._run_parser_factory()

    def _run_parser_factory(self):
        # Add command
        add_parser = self._subparsers.add_parser("add", help="Add a new task")
        add_parser.add_argument("description", type=str, help="Task description")

        # Update command
        update_parser = self._subparsers.add_parser(
            "update", help="Update an existing task"
        )
        update_parser.add_argument("id", type=int, help="Task ID")
        update_parser.add_argument("description", type=str, help="New task description")

        # Delete command
        delete_parser = self._subparsers.add_parser("delete", help="Delete a task")
        delete_parser.add_argument("id", type=int, help="Task ID")

        # Mark in-progress command
        in_progress_parser = self._subparsers.add_parser(
            "mark-in-progress", help="Mark a task as in-progress"
        )
        in_progress_parser.add_argument("id", type=int, help="Task ID")

        # Mark done command
        done_parser = self._subparsers.add_parser(
            "mark-done", help="Mark a task as done"
        )
        done_parser.add_argument("id", type=int, help="Task ID")

        # List command
        list_parser = self._subparsers.add_parser("list", help="List tasks")
        list_parser.add_argument(
            "status",
            nargs="?",
            type=str,
            choices=["todo", "in-progress", "done"],
            help="Filter by task status",
        )

    def get_parser(self):
        return self._parser
