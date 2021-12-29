#  problem_1_solution_code
"""
1.	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000. 
(Answer: 233168)
"""
s = 0
N = int(input("Enter a value:"))

for i in range(1,N):
    if i%3==0 or i%5==0:
        s+=i

print(s)
