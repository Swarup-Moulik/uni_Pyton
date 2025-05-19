stack = []
print("1. Push \n2. Pop \n3. Traverse \n4.Exit")
while True:
    ch = int(input("Enter your choice :- "))
    if ch == 1:
        num = int(input("Enter the number :- "))
        stack.append(num)
    elif ch == 2:
        pop_item = stack.pop()
        print("Popped Item :- ", pop_item)
    elif ch == 3:
        print("Stack :- ", *stack)
    elif ch == 4:
        print("Exited !")
        break
    else:
        print("Wrong value.")