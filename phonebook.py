def menu():
    print("-------Lil Black Book--------")
    print("[1] Look up an entry")
    print("[2] Set an entry")
    print("[3] delete an entry")
    print("[4] List all entries")
    print("[5] Quit")
    print("what would you like to do (1-5)?")

menu()    
d1 = {}
while True:
    n=int(input("enter number [1-5]:-"))
    if n ==2:
        name=input("enter name:-")
        phono=(input("enter phone number:-"))
        d1[name]=phono
    elif n==1:
        name1=input("enter name to SEARCH for phone number in the phone book")
        print("phone number of" ,name1, "is", d1[name])
   
    break        
        
        
