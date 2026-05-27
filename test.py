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

list = [1,1,1,2,3,5,5,3,3,4,5,8,6,5,5]
even =[x%2 == 0 for x in list]
print(even)