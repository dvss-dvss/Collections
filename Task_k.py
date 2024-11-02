queue = []
while True:
    command = input('-->').strip()
    if command.startswith("push"):
        number = int(command.split()[1])
        queue.append(number)
        print("ok")
    elif command == "pop":
        print(queue.pop(0))
    elif command == "back":
        print(queue[0])
    elif command == "size":
        print(len(queue))
    elif command == "clear":
        queue.clear()
        print("ok")
    elif command == "exit":
        print("bye")
        break
    else:
        print("error")