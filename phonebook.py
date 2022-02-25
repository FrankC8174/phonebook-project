#Define Menu
def menu():
    print("Welcome to my Contact Book")
    print("My program commands are 1,2,3,4, or 5")
    print("----What Would You like to do?----")
    print("[1] Look up an entry")
    print("[2] Set an entry")
    print("[3] delete an entry")
    print("[4] List all entries")
    print("[5] Quit")
    print("what would you like to do (1-5)?")
#Call menu function
menu()
#Define Dictionary
d1 = {}
#Initiate a while loop to  continuously run the program
while True:
#Create conditions for decision making  
    n = int(input("enter number [1-5]:-"))
    if n == 2:
        name = input("enter name:-")
        phono = (input("enter phone number:-"))
        d1[name] = phono
    elif n == 1:
        name1 = input(
            "enter name to SEARCH for phone number in the phone book")
        if name1 != d1.get(name1,None): # Validate name exist
            print("entry not found")
        else:
            print("phone number of", name1, "is", d1[name])
    if n == 3:
        name1 = input("enter name to delete:-")
        d1.pop(name)
    if n == 4:
        x = d1.values()
        print(x)
    #if name1 != d1.get(name1,None):
        print("entry not found")
    if n == 5:
        print("Exit")
    break
    menu()
    





