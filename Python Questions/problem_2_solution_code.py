# problem_2_solution_code

a, b = 1, 1
s = 0

while s<4000000:
    if b%2==0:
        s+=b
    a, b = b, a+b

print(s)
