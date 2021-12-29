#  problem_1_solution_code

s = 0
N = int(input("Enter a value:"))

for i in range(1,N):
    if i%3==0 or i%5==0:
        s+=i

print(s)
