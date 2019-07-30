#!/usr/bin/env python3
message = "Do you know why I pulled you over?"
message2 = "How many drinks have you had tonight?"

print(message)
acknowledge = input()
  


if acknowledge == "yes":
    print(message2)

elif acknowledge == "no":
    print(message2)

else:
    print("You're drunk! Put your hands behind your back and get in the car now!")

drinks = input()


if drinks <="2":
    print("I'm gonna let you off with a warning. Drive safe")

elif drinks >="3":
    print("You're drunk! Put your hands behind your back and get in the car now!")

else:
    print("You're drunk! Put your hands behind your back and get in the car now!")



