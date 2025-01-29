#exercise - 1
import random
def get_random():
    count = 0
    print("random numbers from 100 , 999 which is divisible by 5\n")
    while count < 3:
        random_number = random.randint(100, 999)
        if random_number % 5 == 0:
            count += 1
            print(count,".",random_number)
get_random()

#exercise - 2
def generate_tickets():
    lottery_tickets = []
    while len(lottery_tickets)<100:
        random_ticket = random.randint(100000, 999999)
        lottery_tickets.append(random_ticket)
    return lottery_tickets    
tickets = generate_tickets()
winners= random.sample(tickets, 2)
print("generated lottery tickets: " , tickets)
print("\nwinning tickets: " , winners)

#excercise - 3
def generate_otp():
    random_otp = random.randint(100000 , 999999)
    return random_otp
otp = generate_otp()
print("random otp of six digit : ", otp)
