"""Laboratorio 8 - Módulo de persistencia para lista de tareas."""


def read_todo_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"File {file_path} not found! Returning an empty to-do list.")
        return []


def write_todo_file(file_path, tasks):
    try:
     with open(file_path, 'w') as f:        
            for task in tasks:
                f.write(task + '\n')    
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")
