import argparse
import pickle
import os
from datetime import datetime, timedelta

# Define task class
class Task:
    """Representation of a task."""
    task_counter = 0

    def __init__(self, name, priority=1, due_date=None):
        Task.task_counter += 1
        self.id = Task.task_counter
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.created = datetime.now()
        self.completed = None

    def mark_complete(self):
        self.completed = datetime.now()

    def __repr__(self):
        return f"<Task ID={self.id}, Name={self.name}, Priority={self.priority}>"

# Define tasks class
class Tasks:
    """A collection of Task objects."""

    def __init__(self, file=".todo.pickle"):
        self.tasks = []
        self.file = file
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from pickle file."""
        if os.path.exists(self.file):
            with open(self.file, "rb") as f:
                self.tasks = pickle.load(f)

    def save_tasks(self):
        """Save tasks to pickle file."""
        with open(self.file, "wb") as f:
            pickle.dump(self.tasks, f)

    def add_task(self, name, priority=1, due_date=None):
        """Add a new task."""
        task = Task(name, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Created task {task.id}")

    def list_tasks(self, include_completed=False):
        """List tasks."""
        tasks = [t for t in self.tasks if include_completed or not t.completed]
        tasks.sort(key=lambda t: (t.due_date if t.due_date else datetime.max, -t.priority))
        print("ID   Age  Due Date   Priority   Task")
        print("--   ---  --------   --------   ----")
        for task in tasks:
            age = (datetime.now() - task.created).days
            due_date = task.due_date.strftime("%m/%d/%Y") if task.due_date else "-"
            print(f"{task.id:<4} {age:<4} {due_date:<10} {task.priority:<9} {task.name}")

    def mark_done(self, task_id):
        """Mark a task as completed."""
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.mark_complete()
            self.save_tasks()
            print(f"Completed task {task.id}")
        else:
            print(f"No task found with ID {task_id}")

    def delete_task(self, task_id):
        """Delete a task."""
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.save_tasks()
        print(f"Deleted task {task_id}")

    def report(self):
        """List all tasks including completed."""
        print("ID   Age  Due Date   Priority   Task                Created                       Completed")
        print("--   ---  --------   --------   ----                ---------------------------   -------------------------")
        for task in self.tasks:
            age = (datetime.now() - task.created).days
            due_date = task.due_date.strftime("%m/%d/%Y") if task.due_date else "-"
            created = task.created.strftime("%a %b %d %H:%M:%S %Z %Y")
            completed = task.completed.strftime("%a %b %d %H:%M:%S %Z %Y") if task.completed else "-"
            print(f"{task.id:<4} {age:<4} {due_date:<10} {task.priority:<9} {task.name:<20} {created:<30} {completed}")

    def query_tasks(self, terms):
        """Search tasks based on terms."""
        terms = [term.lower() for term in terms]
        tasks = [t for t in self.tasks if not t.completed and any(term in t.name.lower() for term in terms)]
        print("ID   Age  Due Date   Priority   Task")
        print("--   ---  --------   --------   ----")
        for task in tasks:
            age = (datetime.now() - task.created).days
            due_date = task.due_date.strftime("%m/%d/%Y") if task.due_date else "-"
            print(f"{task.id:<4} {age:<4} {due_date:<10} {task.priority:<9} {task.name}")

# Main Function
def main():
    parser = argparse.ArgumentParser(description="Command Line Task Manager")
    parser.add_argument("--add", type=str, help="Add a new task")
    parser.add_argument("--due", type=str, help="Due date for the task (MM/DD/YYYY)")
    parser.add_argument("--priority", type=int, choices=[1, 2, 3], help="Priority of the task (1-3)")
    parser.add_argument("--list", action="store_true", help="List all not completed tasks")
    parser.add_argument("--done", type=int, help="Mark a task as done by ID")
    parser.add_argument("--delete", type=int, help="Delete a task by ID")
    parser.add_argument("--report", action="store_true", help="Report all tasks")
    parser.add_argument("--query", nargs="+", help="Search tasks by terms")
    args = parser.parse_args()

    tasks = Tasks()

    if args.add:
        due_date = datetime.strptime(args.due, "%m/%d/%Y") if args.due else None
        priority = args.priority if args.priority else 1
        tasks.add_task(args.add, priority, due_date)
    elif args.list:
        tasks.list_tasks()
    elif args.done:
        tasks.mark_done(args.done)
    elif args.delete:
        tasks.delete_task(args.delete)
    elif args.report:
        tasks.report()
    elif args.query:
        tasks.query_tasks(args.query)

if __name__ == "__main__":
    main()