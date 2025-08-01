```python
tasks = []

def show_tasks():
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def main():
    while True:
        print("\nOptions:\n1. Add\n2. View\n3. Exit")
        choice = input("Choose: ")

        if choice == '1':
            task = input("Enter a task: ")
            tasks.append(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

main()
```
