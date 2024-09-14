from functions import get_todos, write_todos
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print("It is", now)

while True :
    user_action = input("type add, show,edit,complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]  #List slicing

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)


    elif user_action.startswith("show"):

        todos = get_todos()


        new_todos = [item.strip("\n") for item in todos]  # List comprehension

        for index, item in enumerate(new_todos):
            item = item.title()
            print(f"{index}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo")
            todos[number] = new_todo +  "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid. You need to type the index")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todos.pop(number)

            write_todos(todos)

        except IndexError :
            print("Enter a valid input")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")



print("Thank You")


