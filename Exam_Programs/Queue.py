queue = []
print("1. Enqueue \n2. Dequeue \n3. Traverse \n4.Exit")
while True:
    ch = int(input("Enter your choice :- "))
    if ch == 1:
        num = int(input("Enter the number :- "))
        queue.append(num)
    elif ch == 2:
        pop_item = queue.pop(0)
        print("Dequeued Item :- ", pop_item)
    elif ch == 3:
        print("Queue :- ", *queue)
    elif ch == 4:
        print("Exited !")
        break
    else:
        print("Wrong value.")