salary =int(input("Enter your monthly Salary: "))
if salary > 50000:
    classification ="High Earner"
elif salary > 20000:
    classification ="Mid Earner"
else:
    classification="Low Earner"
    
print(f'The employee is classified as: {classification}')
