import json
import os


class TaskFileManager:
    TASKS_FILE = "tasks.json"

    @classmethod
    def load_tasks(cls):
        if os.path.exists(cls.TASKS_FILE):
            with open(cls.TASKS_FILE, "r") as file:
                return json.load(file)
        return []

    @classmethod
    def save_tasks(cls, tasks):
        with open(cls.TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)

    @classmethod
    def generate_task_id(cls, tasks):
        if not tasks:
            return 1
        return max(task["id"] for task in tasks) + 1
