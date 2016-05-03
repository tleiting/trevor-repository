# I determined my range for a, b, c, and d because they all must be positive two digit integers, so I made sure that when I calculated u and v there was no possibility that my range would allow u and v to be a single digit integer.  For a and b I chose my minimum range to be 50 and for c and d I chose my maximum range to be 40.  This way there was no possible way for u (a - c) and v (b - d) to be a single digit integer. For example, my minimum for a is 50 and my max for c is 40, so the smallest possible difference could be 10.

import random

# A sequence of assignments to generate a random problem :
# I used random.randint throughout my assignment because I needed to randomly generate an integer from the different ranges given. (This occurs on lines 13-16)
# For 'a' and 'b', they must both be two-digit integers, so I chose the range of (50,99) to guarantee this would happen. (This occurs on lines 13 and 14).
# For 'c' and 'd', they must both be two-digit integers, so I chose the range of (10,40) to guarantee this would happen. (This occurs on lines 15 and 16).
# I chose the range of (50,99) for 'a' and 'b' and (10, 40) for 'c' and 'd' to guarantee that the difference of the minimum of 'a' and the maximum of 'c', and the difference of the minimum of 'b' and the maximum of 'd' would still return a two digit integer.
# I chose this value for 'u' because 'a' and 'c' both share the same variable (x), so I combined like-terms. (This occurs on line 17).
# I chose this value for 'v' because 'b' and 'd' are both constants, so I combined them. (This occurs on line 18).

<<<<<<< Updated upstream
a = random.randint(52, 99) 
b = random.randint(52, 99) 
=======
a = random.randint(51, 99) 
b = random.randint(51, 99) 
>>>>>>> Stashed changes
c = random.randint(10, 40) 
d = random.randint(10, 40) 
u = (a - c) 
v = (b - d) 
print ('Problem : ({a} x + {b}) - ({c} x + {d}) = ?' .format (a = a , b = b ,
c = c , d = d))
print ('Answer : {u} x + {v}'. format (u = u , v = v ))
