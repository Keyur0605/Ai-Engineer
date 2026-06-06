# var1= "25"
# var2 = 10
# var3 = 10.3
# var4= True
# var5= None

# print(type(int(var1)))

# print(float(var2)+var3)

# user = int(input("Enter your age: "))
# print(f"{user+5} is your age after 5 years.")
# print("Even number" if user % 2 == 0 else "Odd number")

# user1= int(input("Enter first number: "))
# user2= int(input("Enter second number: "))
# user1,user2 = user2,user1
# user1 = user1+user2
# user2 = user1-user2
# user1 = user1 - user2
# print(f"first number is {user1} and second number is {user2}")
# print("first number is greater than second one" if user1>user2 else "second number is greater than first one" )

# circle = int(input("Enter the radius of the circle: "))
# pi = 3.14
# area = pi * circle ** 2
# print(f"The area of the circle is: {area}")

# user = input("Enter a string: ")
# reverse = list(user)
# reverse.reverse()
# reverse = ''.join(reverse)
# print(f"The reverse of the string is: {reverse}")

# count = 0
# vowels = "aeiouAEIOU"
# user = input("Enter a string: ")
# frequency = {}
# for i in user:
#     if i in vowels:
#         count += 1
#         frequency[i] = frequency.get(i, 0) + 1
# print(f"The number of vowels in the string is: {count}")
# print(f"The frequency of each vowel is: {frequency}")

# pelindrome = input("Enter a string: ")
# pelindrome = pelindrome.replace(" ", "").lower()
# if pelindrome == pelindrome[::-1]:
#     print("The string is a palindrome.")
# else:    
#     print("The string is not a palindrome.")

# list1 = [1, 22, 34567, 4, 5]
# large = list1[0]
# second_large = list1[0]
# for i in list1:
#     if i>large:
#         second_large = large
#         large = i
# print(f"The largest number in the list is: {large}")
# print(f"The second largest number in the list is: {second_large}")

# list = [1,1,1,2,3,5,5,3,3,4,5,8,6,5,5]
# even =[x%2 == 0 for x in list]
# print(even)

# dataset = [("img_001.jpg", 0), ("img_002.jpg", 1), ("img_003.jpg", 0)]

# for image_path, label in dataset:
#     print(f"Load {image_path} → class {label}")


# def train_val_split(data, ratio=0.8):
#     cut = int(len(data) * ratio)
#     return data[:cut], data[cut:]   # returns a TUPLE

# train, val = train_val_split(dataset)
# print("Train:", train)
# print("Val:", val)

# files = ["cat_01.jpg", "dog_02.jpg", "bird_03.jpg"]

# names= [f.replace(".jpg", "") for f in files]
# print(names)

# label_map = {"cat":0, "dog":1, "bird":2}
# str_labels = ["cat", "dog", "cat", "bird"]
# int_labels = [label_map[l] for l in str_labels]
# print(int_labels)

# all_preds = [
#     ("cat",  0.12), ("dog",  0.67),
#     ("bird", 0.05), ("cat",  0.91),
#     ("dog",  0.73),
# ]
# THRESHOLD = 0.5

# low_level = [(label,score) for label,score in all_preds if score <= THRESHOLD]
# print(low_level)

# import math
# dataset = [[1.2, 3.4], [float('nan'), 2.1], [0.5, 1.8]]
# clean = [row for row in dataset
#          if not any(math.isnan(v) for v in row)]
# print(clean)

# batch = [[0.1, 0.2,0.1,1], [0.3,2 ,0.4,0.3], [0.5,3, 0.6,0.5]]
# raw = [x for row in batch for x in row]
# print(raw)

# list1 = ["a", "b", "c", "d"]
# new_list = [(idx, value) for idx, value in enumerate(list1)]
# print(new_list)


# # day 1 python exercises
# # Exercise 1
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height = float(input("Enter your height in cm: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = weight / (height / 100) ** 2

# print("--- Info Card ---")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Height: {height} cm")
# print(f"Weight: {weight} kg")
# print(f"BMI: {bmi:.2f}")

# # Exercise 2
# second = int(input("Enter the number of seconds: "))
# days = second // (24 * 3600)
# hours = (second % (24 * 3600)) // 3600
# minutes = (second % 3600) // 60
# seconds = second % 60
# print(f"{second} seconds is equal to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

# # Exercise 3
# try:

#     degree_celsius = float(input("Enter temperature in Celsius: "))
#     degree_fahrenheit = (degree_celsius * 9/5) + 32
#     degree_kelvin = degree_celsius + 273.15
#     print(f"{degree_celsius}°C is equal to {degree_fahrenheit:.2f}°F and {degree_kelvin:.2f} K.")

#     euro = float(input("Enter amount in Euros: "))
#     GBP = euro * 0.85
#     USD = euro * 1.1
#     print(f"{euro} Euros is equal to {GBP:.2f} GBP and {USD:.2f} USD.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")

# # day 2 python exercises

# exercise 1 = Shopping bill splitter
# try:

#     total_bill = float(input("Enter the total bill amount: "))
#     discount = int(input("Enter the discount percentage (0-100): "))
#     members = int(input("Enter the number of members sharing the bill: "))
#     total_after_discount = total_bill - (total_bill * (discount / 100))
#     print(f"The total bill after discount is: {total_after_discount:.2f}")
#     if members > 0:
#         bill_per_member = total_after_discount / members
#         print(f"Each member should pay: {bill_per_member:.2f}")
#         if bill_per_member > 20:
#             print(f"Above each 20 Euro : {bill_per_member > 20}")
#     else:
#         print("Number of members must be greater than 0.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")   

# # # exercise 2 = leap year checker and even or odd year checker
# try: 
#     year = int(input ("Enter a year: "))
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")
#     if year % 2 == 0:
#         print(f"{year} is an even year.")
#     else:
#         print(f"{year} is an odd year.")
# except ValueError:
#     print("Invalid input. Please enter a valid year.")

# # execise 3 loan interest calculator
# loan_amount = float(input("Enter the loan amount: "))
# annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
# loan_term_years = int(input("Enter the loan term (in years): "))

# simple_interest = (loan_amount * annual_interest_rate * loan_term_years) / 100
# total_amount = loan_amount + simple_interest
# compound_interest = loan_amount * (1 + annual_interest_rate / 100) ** loan_term_years - loan_amount
# compound_total_amount = loan_amount + compound_interest

# print("--- Loan Simple Interest Calculation ---")
# print(f"Simple Interest: {simple_interest:.2f}")
# print(f"Total Amount with Simple Interest: {total_amount:.2f}")

# print("\n--- Loan Compound Interest Calculation ---")
# print(f"Compound Interest: {compound_interest:.2f}")
# print(f"Total Amount with Compound Interest: {compound_total_amount:.2f}")


# Day 3 python exercises

# Excercise 1 = cinema ticket price calculator
# age = int(input("Enter your age: "))
# day = input("Enter the day of the week (e.g., Monday, Tuesday, etc.): ").strip().lower()
# try:
#     age = int(age)
#     if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
#         print("Invalid input for day. Please enter a valid day of the week.")
#     else:
#         if 5 <= age <= 12:
#             print("The cinema ticket price is: 5 Euros.")
#         elif 13 <= age <= 17:
#             print("The cinema ticket price is: 8 Euros.")
#         elif 18 <= age <= 64:
#             if day in ["saturday", "sunday"]:
#                 print("The cinema ticket price is: 15 Euros.")
#             else:
#                 print("The cinema ticket price is: 12 Euros.")
#         elif age >= 65:
#             print("The cinema ticket price is: 6 Euros.")
#         else:
#             print("The cinema ticket price is: 0 Euros.")
# except ValueError:
#     print("Invalid input for age. Please enter a valid number.")
#     exit()

# exercise 2 = login system 

# CORRECT_USERNAME = "admin"
# CORRECT_PASSWORD = "secret123"
# total_attempts = 3
# try:
#     while total_attempts > 0:
#         username = input("Enter your username: ")
#         password = input("Enter your password: ").strip()
#         if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
#             print("Login successful!")
#             break
#         elif username != CORRECT_USERNAME :
#             total_attempts -= 1
#             print(f"Invalid username. You have {total_attempts} attempts left.,..........")
#         else:
#             total_attempts -= 1
#             print(f"Invalid password. You have {total_attempts} attempts left.,..........")
#     if total_attempts == 0:
#         print("Too many failed attempts. Your account has been locked.")      
            
# except ValueError:
#     print("Invalid input. Please enter a valid username and password.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# exercise 3 = smart shopping list manager

item_weights = int(input("Enter the items weights(kg): "))
destination= input("Enter the destination(domestic/international): ").strip().lower()
member  = input("Enter the member status premium (yes/no): ").strip().lower()
cost  = 0
discount = 0 
if destination not in ["domestic", "international"] and member not in ["yes", "no"]:
    print("Invalid input for destination or member status. Please enter valid values.")
else:
    if destination == "domestic":
        if item_weights <= 1:
            cost = 3 * 0.25
        elif item_weights <= 5:
            cost = 6
        else:
            cost = 10
    else:  # international
        if item_weights <= 1:
            cost = 10
        elif item_weights <= 5:
            cost = 20
        else:
            cost = 35
        
    if member == "yes":
        discount = cost * 0.25  # Apply 25% discount for premium members

print(f"Base price: {cost :.2f} Euros.")
print(f"Discount: {discount:.2f} Euros.")
print(f"The total shipping cost is: {cost - discount:.2f} Euros.")
print("Thank you for using our smart shopping list manager!")