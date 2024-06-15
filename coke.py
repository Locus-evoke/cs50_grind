
user_inp = 0
amount_due = 50
while True:
    if user_inp < 50:
        if amount_due > 0:
            money = input("insert coin: ")
            if int(money) == 5 or int(money) == 10 or int(money) == 25:
                user_inp += int(money)
            else:
                print(f'Amount Due: {amount_due}')
                continue
            if int(money) == 5:
                amount_due -= 5
                if amount_due > 0:
                    print(f'Amount Due: {amount_due}')
            elif int(money) == 10:
                amount_due -= 10
                if amount_due > 0:
                    print(f'Amount Due: {amount_due}')
            elif int(money) == 25:
                amount_due -= 25
                if amount_due > 0:
                    print(f'Amount Due: {amount_due}')
            else:
                continue
    elif user_inp >= 50:
        change_owed =  user_inp - 50
        print(f'Change Owed: {change_owed}')
        break



#       check50 cs50/problems/2022/python/coke


        # else:
        #     print("Amount paid \n enjoy ur coke bro")
        #     break
