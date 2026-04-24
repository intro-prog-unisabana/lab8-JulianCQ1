import sys 
from todo_manager import read_todo_file, write_todo_file
def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        todo_file_path = sys.argv[1]
        if len(sys.argv) < 3:
            return 
        
        command = sys.argv[2]
        if command == "view":
            print("tasks:")
            tasks = read_todo_file(todo_file_path)
            for task in tasks:
                print(f"- {task}")
        elif command == "add":
            if len(sys.argv) < 4:
                raise IndexError("No task provided to add!")
            new_task = sys.argv[3]
            tasks = read_todo_file(todo_file_path)
            tasks.append(new_task)
            write_todo_file(todo_file_path, tasks)
            print(f"Task '{new_task}' added.")
        elif command == "remove":
            if len(sys.argv)<4:
                raise IndexError('Task description required for "remove".')
            task_to_remove = sys.argv[3]
            tasks = read_todo_file(todo_file_path)
            try:
                tasks.remove(task_to_remove)
                write_todo_file(todo_file_path, tasks)
                print(f"Task '{task_to_remove}' removed.")
            except ValueError:
                print(f"Task '{task_to_remove}' not found.")
        else:
            raise ValueError("Command not found!")
    except ValueError as e:
        print(e)    

    except IndexError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")
if __name__ == "__main__":  
    main()
        

