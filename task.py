tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})


def list_tasks():
    for i, task in enumerate(tasks):
        status = "Concluída" if task["completed"] else "Não Concluída"
        print(f"{i + 1}. {task['task']} [{status}]")


def remove_task(index):
    if 0 >= index < len(tasks):
        tasks.pop(index)
    else:
        print("Índice inválido")


def main():
    print("Personal Task Manager")
    while True:
        command = input("Comando (add/list/remove/exit): ")
        if command == "add":
            task = input("Tarefa: ")
            add_task(task)
        elif command == "list":
            list_tasks()
        elif command == "remove":
            index = int(input("Índice da tarefa a remover: ")) - 1
            remove_task(index)
        elif command == "exit":
            break



if __name__ == "__main__":
    main()