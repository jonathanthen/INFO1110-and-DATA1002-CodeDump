Write a program that computes the solutions to the 
quadratic equation: ax^2 + bx + c = 0 .

The program asks for values for the coeﬃcients a , b and c . 
The user enters these values one by one. All values must be integers, 
and the value for a cannot be 0 .

If the user enters an invalid value for a coeﬃcient, the program 
asks for another value for that coeﬃcient. It will keep asking until
the entered value is valid.

Once the program receives valid values for a , b and c , it prints
the quadratic equation with those coeﬃcients. It then prints the 
solution(s) to that equation. Each solution is printed to two 
decimal places (rounding to the nearest number). The larger 
solution is printed ﬁrst.

If there are two solutions (e.g. 1 and 2.50 ), it prints x=2.50, x=1.00
If there is one solution (e.g. 0 ), it prints x=0.00 
If there are no solutions, it prints There are no real solutions!

Input | Justification
2 spam -7 5 | The example above, Non integers
1 2 1 | Only 1 solution
54 3 20 | No solutions
1 0 -64 | Tests for one solution
