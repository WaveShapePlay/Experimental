
print('Example 1:')

for x in range(0,10):
    print(x)
    
print('\n')
print('Example 2:')

for u in range(0,5):
    print(2**u)

print('\n')
print('Example 3:')

salary = 50000
# Printing out 5% raise over 4 years
for y in range(0,4):
    salary = salary + salary*0.05
    print(salary)
