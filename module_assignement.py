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
#Exercise - 4
def random_character():
    str = input("enter a string : ")
    if str.isalpha():
        random_char = random.choice(str)
        return random_char
random_string = random_character()
print(random_string)

#Exercise - 5
import string
def generate_randomstring():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
random_str = generate_randomstring()
print("random string : " , random_str)


#Exercise - 6
import random
import string

def generate_random_password():
    password = [random.choice(string.ascii_uppercase) for _ in range(2)]
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))
    password += random.choices(string.ascii_lowercase, k=6)
    return ''.join(password)
password = generate_random_password()
print("Generated Password:", password)

