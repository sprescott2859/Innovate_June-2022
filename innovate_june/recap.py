



# greeting = "Hello Everyone"

# print(greeting)

# print("This is a string for displaying characters")
# print("1234") #this is a string
# print(1234+1) #this is an integer/whole number
# print(12.34) #this is a float
# print(True) #one of the boolean data values
# print(False) #one fo the booleans
# print(None) #nongit e - blank/null data

# my_name="Stephen"
# my_age="42"
# student=True

# # print(my_name,my_age,student)
# def new_func():
#     print("Hello my name is and I am years old
# ").

# new_func()


# print(1+2)
# print(3-2)
# print(3*3)
# print(3**3)
# print(6/2)
# print(16%3)

# balance=100000
# print(balance)
# amount=200000

# balance=amount+balance
# balance +=amount
# print(balance)

# music="my chemical romance"

# if music == "classical":
#     print("oh no it's classical")
# elif music =="no music":
#     print("Put the radio on")
# elif music =="my chemical romance":
#     print("Katy, stop crying")
# else:
#     print("turn it up")

# print ("That was an if statement") 

# print (10%3==0)

# day = "saturday"

# if day == "saturday" or day == "sunday":
#     print("its the weekend")
# else:
#     print("off to innovate we go")

#FUNCTIONS

# def light_switch():
#     print("Switching the lights")

# light_switch()
# light_switch()

# def cash_withdrawal(amount,accnum):
#     print(f"You have withdrawn {amount} from {accnum}")

# cash_withdrawal(300, 12345678)

# LISTS 

# fav_songs = [
#     "Mr Blobby"
#     "Bob the builder"
#     "The Macerana"
# ]

# print(fav_songs)

# fav_songs[1] = "Prince Charming"

# print(len(fav_songs))

# fav_songs.append("Ice,ice baby")

# print(fav_songs)

# fav_songs.pop(1)

# print(fav_songs)

# num = 0

# while num < 10:
#     num +=1


# welcome_msg = "Welcome to Code Nation"

# msg_length = print(len(welcome_msg))

# msg_length = print(f)

# name = "Welcome to code nation"
# length = len(name)%2
# # If a number has a remainder of 0 when divided by 2
# # the number is even.
# # If there is a remainder then it is odd.
# if length == 0:
#     print (name, "even")
# else:
#     print (name, "odd")

# welcome_msg = "Welcome to Code Nation"

# msg_length = len(welcome_msg)
# msg_length_even = len(welcome_msg)%2
# if msg_length_even == 0:
#     print(welcome_msg)
#     print("welcome message length is even")
#     print(msg_length)
# else:
#     print(welcome_msg)
#     print("Your message length isnt even")


# alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]
# for i in alpha:
#     print(i)

# def main():
#     for i in range(len(97,123)):
#         print(chr(i), end=" ")

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]
for i in alpha:
    print(i)

user_num = int(input("Choose and number between 0 and 25\n"))

print(alpha[user_num], "is what your number represents in the alphabet")
