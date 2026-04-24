import sys 
from todo_manager import read_todo_file, write_todo_file
def main():
    try:
        if len(sys.argv) != 2:
            raise IndexError("Insufficient arguments provided!")
        todo_file_path = sys.argv[1]
        
        print("Command-line arguments:")
        for arg in sys.argv:
            print(arg)
        print("Tasks:")
        new_task = input("Enter a new task to add (or press Enter to skip): ")
        if new_task:
            tasks = read_todo_file(todo_file_path)
            for task in tasks:
                print(f"- {task}")
    except IndexError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")
if __name__ == "__main__":  
    main()
        

