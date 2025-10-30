import random, datetime. math
def generate_password(password_length):
    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_case_letters = lower_case_letters.upper()
    digits = "0123456789"
    
    if not isinstance(password_length, int):
        raise ValueError("Password length must be an integer")
    if password_length < 8:
        raise ValueError("Password length must be at least 8 characters")
    
    chars = lower_case_letters + upper_case_letters + digits
    
    password = "".join(random.choice(chars) for num in range(password_length))
        
    return password

# print (generate_password(12))

def days_between(day_1, day_2):
    day_1 = datetime.datetime.strptime(day_1, "%y-%m-%d")
    day_2 = datetime.datetime.strptime(day_2, "%y-%m-%d")
    difference = day_2 - day_1
    return abs(difference.days)
    
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

print(calculate_circle_area(50))

    
