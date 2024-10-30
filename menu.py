name=input("Enter the name:").upper()
print(f"Hi {name} welcome to menu ordering system.")
plate=0
drink1=0
desert1=0
menu=input('''Enter the menu
             B:Breakfast
             L:Lunch
             D:Dinner:
''').lower()
if menu=="b":
    plate=int(input("How many plates do you have:"))
    print(f"Your order for {plate} registered.")
    drink=input("Would you have drinks(YES/NO):").lower()
    if drink=="yes":
        drink1=int(input("How many drinks have:"))
        desert=input("Would you have deserts(YES/NO):").lower()
        if desert=="yes":
           desert1=int(input("How many deserts have:"))
        else:
            print("No")   
    else:
        desert=input("Would you have deserts(YES/NO):").lower()
        if desert=="yes":
           desert1=int(input("How many deserts have:"))
        else:
            print("No")      
    print(f"Your order have {plate} plates , {drink1} drinks and {desert1} deserts registered.")   
    a=plate*50
    b=drink1*30
    c=desert1*40
    a1=a+b+c
    cgst=a*0.08
    sgst=a*0.1
    total=a+cgst+sgst
    print(f'''
    Your food bill is {a1}/-rupees
      CGST 8% is {cgst} /-rupees
       SGST 10% {sgst} /-rupees
        Grand total is {total} /-rupees
        ''')         
elif menu=="l":
    plate=int(input("How many plates do you have:"))
    print(f"Your order for {plate} registered.")
    drink=input("Would you have drinks(YES/NO):").lower()
    if drink=="yes":
        drink1=int(input("How many drinks have:"))    
        desert=input("Would you have deserts(YES/NO):").lower()
        if desert=="yes":
           desert1=int(input("How many drinks have:"))
        else:
          print("No")
    else:
        desert=input("would you have deserts(YES/NO):").lower()
        if desert=="yes":
           desert1=int(input("How many deserts have:"))
        else:
            print("No")   

    print(f"Your order have {plate} plates , {drink1} drinks and {desert1} deserts registered.")
           
    a=plate*50
    b=drink1*30
    c=desert1*40
    a1=a+b+c
    cgst=a*0.08
    sgst=a*0.1
    total=a+cgst+sgst
    print(f'''
    Your food bill is {a1}/-rupees
      CGST 8% is {cgst} /-rupees
       SGST 10% {sgst} /-rupees
        Grand total is {total} /-rupees
        ''')                
elif menu=="d":
    plate=int(input("How many plates do you have:"))
    print(f"Your order for {plate} registered.")
    drink=input("Would you have drinks(YES/NO):").lower()
    if drink=="yes":
        drink1=int(input("How many drinks have:"))    
        desert=input("Would you have deserts(YES/NO):").lower()
        if drink=="yes":
           desert1=int(input("How many desert have:"))
        else:
           print("No")
    else:
        desert=input("Would you have deserts(YES/NO):").lower()
        if desert=="yes":
           desert1=int(input("How many deserts have:"))
        else:
            print("No")              
    print(f"Your order have {plate} plates , {drink1} drinks and {desert1} deserts registered.") 
    a=plate*50
    b=drink1*30
    c=desert1*40
    a1=a+b+c
    cgst=a*0.08
    sgst=a*0.1
    total=a+cgst+sgst
    print(f'''
    Your food bill is {a1}/-rupees
      CGST 8% is {cgst} /-rupees
       SGST 10% {sgst} /-rupees
        Grand total is {total} /-rupees
        ''')                
else:
    print("please enter valid menu")
