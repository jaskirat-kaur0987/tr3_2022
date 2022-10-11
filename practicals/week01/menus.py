"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
name = (input("Enter name: "))
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice = (input(">>>")).upper()
while choice != 'Q':
    if choice == 'H':
        print("hello", name)
    elif choice == 'G':
        print("goodbye", name)
    else:
        print("invalid message")
    print(menu)
    choice = (input(">>>")).upper()
print("finished message")
