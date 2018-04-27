"""
Grader
10.0/10.0 points (ungraded)
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 
    0.25*n*s**2/tan(pi/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

Hint: What to import?
This is an optional exercise, but great for extra practice!
"""

import math

def polysum(n, s):
    
    perimeter = n*s
    area =round(((1/4)*n*s**2)/math.tan(math.pi/n), 4)
    sums =round(area + (n*s)**2, 4)
    
    return sums

#test code
#print (polysum(23, 11))