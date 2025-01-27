import random
lucky_number = int(input("Enter an lucky number from 1 to 10 : "))
if lucky_number<1 or lucky_number>10:
    lucky_number = int(input("you have entered invalid number please enter number between 1,10 : "))
while True:
    random_number = random.randint(1,10)
    print("random number = ",random_number)
    if random_number == lucky_number:
        print("lucky number is matchs with random number ")
        break
                         
