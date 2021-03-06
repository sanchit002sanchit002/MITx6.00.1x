"""
Problem 2 - Paying Debt Off in a Year
15.0/15.0 points (graded)
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

    1 balance - the outstanding balance on the credit card

    2 annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
Lowest Payment: 180 

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:
    1 Monthly interest rate = (Annual interest rate) / 12.0
    2 Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    3 Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

                  
	      Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310

          Test Case 2:
	      balance = 4773
	      annualInterestRate = 0.2
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 440

          Test Case 3:
	      balance = 3926
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 360
    
"""
#test code
#balance = 3926
#annualInterestRate = 0.2

test_high=balance//12*2 - (balance//12*2)%10 
test_low=balance//12-(balance//12)%10
month =12

def yesorno(lowestPayment,balance):

    for i in range(12):
        balance=(balance-lowestPayment)*(1+annualInterestRate/12)

    if balance <= 0:
        return True
    return False

for i in range(0 ,test_high,10):
    if  yesorno(i,balance):
        print (i)
        break 

#test output
#lowestPayment= 310