import time
print("Wel-Come")
print("******************************************************************")
print("please insert your card ")
time.sleep(5)
balance=4000
password=1234
pin=int(input("Enter your pin number "))
if (pin==password):
    print("Instructions:--")
    print("1==See your account detail")
    print("2==deposit")
    print("3==withdraw")
    print("4==Exit")
    while(True):
        option=int(input("enter your choice: "))
        if(option==1):
            
            print(f"your current balance is {balance}")
            print("=====================================")

        if(option==2):
            deposit=int(input("enter amount for deposit: "))
            balance=balance+deposit
            print(f"{deposit} credited into your account")
            print(f"your current balance is {balance}")
            print("=====================================")
        if(option==3):
            withdraw=int(input("enter amount for withdraw: "))
            if (balance>=withdraw):
                balance=balance-withdraw
                print(f"{withdraw} debited from your account")
                print("your current balance is ",balance)
                print("=====================================")

            else:
                print("Insufficient Amount ")
                print("=====================================")

        if(option==4):
            break

else :
    print("Invalid password ")
                         
    
