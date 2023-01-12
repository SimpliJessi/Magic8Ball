import random

# Who asks the Great Magic 8 Ball a question!
name = input("What is your name? ")

# The unknown question
question = input("What is your question? ")

# Magic 8 Ball says this
answer = ""

# random number generated between 1 and 10
random_number = random.randint(1, 10)

if random_number == 1:
  answer = "Yes - definitely!"
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "It is decidedly so."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "You've got to be kidding me, right?"
else:
  print("Error")

# print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)