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
        

