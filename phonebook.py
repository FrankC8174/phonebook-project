def menu():
    print("-------Lil Black Book--------")
    print("[1] Look up an entry")
    print("[2] Set an entry")
    print("[3] delete an entry")
    print("[4] List all entries")
    print("[5] Quit")
    print("what would you like to do (1-5)?")

menu()    
PB = {}
while True:
    n=int(input("enter number [1-5]:-"))
    if n ==1:
        name=input("enter name:-")
        pn=(input("enter phone number:-"))
        
        break
