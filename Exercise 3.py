"""
Making a Number guessr
"""
import random as ran


# Printing some 
print("\nHey Welcome to NumGuessr\n")
print("You dared to challange me\n")
print("Now tell what number I am thinking of\n")

# Number you have to guess
num = ran.randint(1,100)
# i for number of chances left
i = 7
while (i>0):
    # Subtracting 1 from i to lower the chances left till it reaches 0
    i = i-1
    # Number entered by user
    user_num = input("\nGuess the number: ")

    """
    #if else statment if the value inputed by user is numeric or not if numeric code executed
    # n = user_num.isnumeric() #check if the input is numeric
    """
    if user_num.isnumeric() == False : 
        # Error message for user if he/she inputs non-numaric value
        print("\tYou need to type a number Not alphabet\n")

        # Showing user how much chances left though recently assined value of i
        print("\t\tNow you only have", i,"chances left\n" )

        # Continues the loop till the value of i reaches 0 [if user writes alphabets]
        continue
    else:
        # If user types numeric value changing it to int from string
        inp = int(user_num)

        """
        if else statment again to tell user if 
        the number guessd by him is less or more then the real number
        """
        # If number entered is Greater then the num
        if num < inp  > num+10 and i!=0:
            print("\t\t\t",inp, "Is much Greater then my number\n")
             
            # Showing user how much chances left though recently assined value of i
            print("\t\t\t\t Now you only have", i,"chances left\n" )

        # If number entered is a little Greater then the num
        elif num < inp  < num+10 and i!=0:
            print("\t\t\t",inp, " Is just a little Greater then my number\n")
             
            # Showing user how much chances left though recently assined value of i
            print("\t\t\t\t Now you only have", i,"chances left\n" )



        # If number entered is Smaller then the num
        elif num > inp  < num-10 and i!=0:            
            print("\t\t\t", inp, "Is very Smaller then my number\n")

            #S howing user how much chances left though recently assined value of i
            print("\t\t\t\tNow you only have", i,"chances left\n" )

        # If number entered is just a little Smaller then the num
        elif num > inp  > num-10 and i!=0:            
            print("\t\t\t", inp, "Is just a little Smaller then my number\n")

            #S howing user how much chances left though recently assined value of i
            print("\t\t\t\tNow you only have", i,"chances left\n" )

        elif i==0:

            print("\t\t\tSorry to say but you lost the game !!!\n")
            print("\t\t\tMy number was", num,"\n")

            # Asking user to continue or close the program
            again = input("\t\t\t\tpress Y to guess again or press enter to close: ")
            
            print("")
            # Capitalizes the enterd value of user
            a = again.capitalize()
            
            # print(a) # Checking the value of a

            # If else statment to continue or close the program as per user input
            if a =="Y":
                i = 7
                continue
            else:
                # Asking for feedback
                print("How good is my program ?\n")
                feed = input("\t\t\tType Your feedback: ")
                #Thanks for feedback
                print("\n\t\t\t\tThanks for your feedback, I am trying to do my best \n")
                
                z= input("Enter to exit : ")
                break

        # If user guesses the right value of num
        elif num == inp and i!=0:
            
            print("\t\t\tKamal Kar diya bhi sahi javab, mera number", num, "tha apne bilkul sahi guess kiya\n")
            print("\t\t\tYou won the game after",7-i, "tries")
            # Asking user to continue or close the program
            again = input("\t\t\t\tpress Y to guess again or press enter to close: ")
            
            print("")
            # Capitalizes the enterd value of user
            a = again.capitalize()
            
            # print(a) # Checking the value of a

            # If else statment to continue or close the program as per user input
            if a =="Y":
                i = 7
                continue
            else:
                # Asking for feedback
                print("How good is my program ?\n")
                feed = input("\t\t\tType Your feedback: ")
                #Thanks for feedback
                print("\n\t\t\t\tThanks for your feedback, I am trying to do my best \n")
                
                z= input("Enter to exit : ")
                break

    

            
            
