import sys 
from todo_manager import read_todo_file, write_todo_file
def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        
        if sys.argv[1] == "--help":
            print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
            return

        todo_file_path = sys.argv[1]
        if len(sys.argv) < 3:
            return 
        tasks = read_todo_file(todo_file_path)
        modified = False
        i = 2
        while i < len(sys.argv):
            command = sys.argv[i]
            i += 1
            if command == "view":
                print("Tasks:")
                for task in tasks:
                    print(f"{task}")
            elif command == "add":
                if i >= len(sys.argv):
                    raise IndexError('Task description required for "add".')
                new_task = sys.argv[i]
                i += 1
                tasks.append(new_task)
                modified = True
                print(f'Task "{new_task}" added.')
            elif command == "remove":
                if i >= len(sys.argv):
                    raise IndexError('Task description required for "add".')
                task_to_remove = sys.argv[i]
                i += 1
                try:
                    tasks.remove(task_to_remove)
                    modified = True
                    print(f'Task "{task_to_remove}" removed.')
                except ValueError:
                    print(f'Task "{task_to_remove}" not found.')
            else:
                raise ValueError("Command not found!")
        if modified:
            write_todo_file(todo_file_path, tasks)
    except ValueError as e:
        print(e)    

    except IndexError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")
if __name__ == "__main__":  
    main()
        

