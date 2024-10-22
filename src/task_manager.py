from datetime import datetime

from tabulate import tabulate

from task_file_manager import TaskFileManager


class TaskManager:

    def add_task(self, description):
        tasks = TaskFileManager.load_tasks()
        new_task = {
            "id": TaskFileManager.generate_task_id(tasks),
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat(),
        }
        tasks.append(new_task)
        TaskFileManager.save_tasks(tasks)
        print(f'Task added successfully (ID: {new_task["id"]})')

    def update_task(self, task_id, new_description):
        tasks = TaskFileManager.load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                task["updatedAt"] = datetime.now().isoformat()
                TaskFileManager.save_tasks(tasks)
                print(f"Task {task_id} updated successfully")
                return
        print(f"Task {task_id} not found")

    def delete_task(self, task_id):
        tasks = TaskFileManager.load_tasks()
        tasks = [task for task in tasks if task["id"] != task_id]
        TaskFileManager.save_tasks(tasks)
        print(f"Task {task_id} deleted successfully")

    def mark_in_progress(self, task_id):
        self.update_task_status(task_id, "in-progress")

    def mark_done(self, task_id):
        self.update_task_status(task_id, "done")

    def update_task_status(self, task_id, new_status):
        tasks = TaskFileManager.load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = new_status
                task["updatedAt"] = datetime.now().isoformat()
                TaskFileManager.save_tasks(tasks)
                print(f"Task {task_id} marked as {new_status}")
                return
        print(f"Task {task_id} not found")

    def list_tasks(self, status=None):
        tasks = TaskFileManager.load_tasks()
        filtered_tasks = (
            tasks
            if status is None
            else [task for task in tasks if task["status"] == status]
        )
        if not filtered_tasks:
            print("No tasks found")
            return

        table_data = [
            [task["id"], task["description"], task["status"], task["createdAt"], task["updatedAt"]]
            for task in filtered_tasks
        ]

        headers = ["ID", "Description", "Status", "Created At", "Updated At"]

        print(tabulate(table_data, headers=headers, tablefmt="grid"))
