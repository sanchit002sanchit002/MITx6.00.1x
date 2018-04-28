"""
Exercise: power recur
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 7 minutes

In Problem 1, we computed an exponential by iteratively executing successive multiplications. We can use the same idea, but in a recursive function.

Write a function recurPower(base, exp) which computes base^exp by recu/rsively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer; exp will be an integer . It should return one numerical value. Your code must be recursive - use of the ** operator or looping constructs is not allowed.
"""

def recurPower(base, exp):
    if exp <= 0 :
        return 1
    else :
        return recurPower(base, exp-1)*base

#Test code
#print (recurPower(-2.04, 7))