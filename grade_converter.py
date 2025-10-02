# FILE NAME - grade_converter.py

# NAME: Makiko Michelle Yasumi
# DATE: October 2, 2025
# BRIEF DESCRIPTION:  This program inputs the grade percentage and outputs the letter grade.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    grade_converter()

def grade_converter():
   print("=" * 5 + " Grade Converter " + "=" * 5)
   percentage = int(input("Enter a numerical grade (1-100): "))
    
   if percentage >= 100:
      print("A+")
   elif percentage in range (90,100):
      print("A")
   elif percentage in range (80,90):
      print("B")
   elif percentage in range (70,80):
      print("C")
   elif percentage in range (65,70):
      print("D")
   else:
      print("F")

main()
            
########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

When entering the parameter for the range function, the second number is exclusive. 
Ensure the else statement uses >=, not >. Otherwise, when a user inputs 100, it will output "F".

'''
