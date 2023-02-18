# put an upper bar by using several equal signs
print("===============================================")
#insert greetings 
print("Welcome to the UMBC Car Customization Form!")
#put a lower bar by using several equal signs
print("===============================================")
#insert a blank space
print()

#add an instruction for answring the multiple choice questions
print("For multiple choice problems, please enter the letter of the selection you're looking for. ")
#add space
print()
print("~ Make & Model ~")
#First question: What model of car are you ordering?
Question1 = "1. What Model of car are you ordering?"
print(Question1)
#write possible answers for Question1 below:
print("    a. Lightning Speedster")
print("    b. Eco Leaf")
print("    c. Harp Chord")
print("    d. Chevron Jolt")
# use input function here
Answer1 = input("Please enter 'a' - 'd': ")
print(Answer1)
#add space
print()
#add second question here:
Question2 = "2. Would you like to upgrade to the hatchback version?"
print(Question2)
# add answer2 below
Answer2 = input("Please enter 'Yes' or 'No': ")
print(Answer2)
#add space
print()
#add a separating bar
print("===============================================")
#add a space
print()
# add the next section (Exterior)
print("~ Exterior ~")
#add question 3 below:
Question3 = "3. What color would you like your car to be?"
print(Question3)
#add answer 3 below using input function
Answer3 = input("You may enter the name of any color you'd like: ")
print(Answer3)
#add space
print()
#add question 4 below:
Question4 = "4. Which of the following tire sizes would you like?"
print(Question4)
#write possible answer choices for Question4 below:
print("       a. 285 mm")
print("       b. 295 mm")
print("       c. 305 mm")
print("       d. 315 mm")
#use input function here
Answer4 = input("Please enter 'a' - 'd': ")
print(Answer4)
#add space between sections
print()
#add a separating bar
print("===============================================")
#add a space
print()
#add the last section (Interior) below
print("~ Interior ~")
#add question 5 below.
Question5 = "5. Would you like heated seats? "
print(Question5)
#add answer 5 using input function
Answer5 = input("Please enter 'Yes' or 'No' :")
print(Answer5)
#add space
print()
#add question 6 below
Question6 = "6. What custom message would you like your car plate to have?"
print(Question6)
#add answer 6 using input function
Answer6 = input("Please enter a custom license plate message. ")
print(Answer6)
#add space
print()
# add a bar to separet sections from summary
print("===============================================")
#add space
print()
#add Summary header below
print("~ Summary ~")
#add model option 
print("Model Option:  a")
#add upgrade version
print("Upgrade to hatchback version:  No")
#add desired color
print("Desired Color:  Red")
#add desired tire size
print("Desired tire size:  C")
#add type of seat
print("Heated Seats:   Yes")
#add desired custom message
print("Desired Custom Message:    Forever Happy!")













