queue = []
while True:
    command = input('-->').strip()
    try:

        if command.startswith("push_front"):
            number = int(command.split()[1])
            queue = [number] + queue
            print("ok")
        elif command.startswith("push_back"):
            number = int(command.split()[1])
            queue.append(number)
            print("ok")
        elif command == "pop_back":
            print(queue.pop(len(queue)-1))
        elif command == "pop_front":
            print(queue.pop(0))
        elif command == "pop":
            print(queue.pop(0))
        elif command == "back":
            print(queue[-1])
        elif command == "front":
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

    except:
        print("error")
