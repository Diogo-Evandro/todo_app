tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})


def main():
    print("Personal Task Manager")
    while True:
        command = input("Comando (add/exit): ")
        if command == "add":
            task = input("Tarefa: ")
            add_task(task)
        elif command == "exit":
            break




if __name__ == "__main__":
    main()