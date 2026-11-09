

students = [
{"name": "Ali", "allowance": 10000, "expenses": [1500, 2200, 1800, 3000], "category": 
"Regular"},
{"name": "Sara", "allowance": 13000, "expenses": [2500, 3100, 2800], "category": 
"Scholarship"},
{"name": "Usman", "allowance": 12000, "expenses": [1000, 1200], "category": 
"Regular"},
{"name": "Ayesha", "allowance": 8000, "expenses": [2000, 2500, 1800], "category": 
"Scholarship"},
{"name": "Zain", "allowance": 15000, "expenses": [4000, 5000, 4500], "category": 
"Regular"}
]

'''Q1:Write Python code using a loop to calculate and print each student's name, total 
expenditure (sum of the items in their 'expenses' list), and remaining balance (allowance 
minus total expenditure).'''

for st in students:
    print ( f"Name : {st['name']} , Total Allownace : {st['allowance']} , Expenditures : {sum(st['expenses'])} Remaining Balance : {st['allowance'] - sum(st['expenses'])}" )

'''Q2:Write Python code to iterate through 'students' and display the message 
"WARNING: High Expenditure!" for any student whose total expenditure exceeds 80% 
of their monthly allowance.'''

for st in students:
    expenses = sum(st['expenses'])
    percentage = ( expenses / st['allowance']) * 100.0
    if ( percentage > 80 ):
        print(f"Name : {st['name']}, WARNING: High Expenditure!")


'''Q3:Scholarship students receive a 10% cashback bonus on their remaining allowance 
balance. Write Python code to filter all "Scholarship" category students and construct a 
new dictionary named 'scholarship_bonuses', where each key is the student's name and 
each value is 10% of their remaining balance.'''

scholarship_bonuses = {}
for st in students:
    if st['category'] == 'Scholarship':
        remaining = st['allowance'] - sum(st['expenses'])
        remaining = 0.10 * remaining
        scholarship_bonuses[st['name']] = remaining
print(scholarship_bonuses)

'''Q4:Student "Sara" makes a new cafeteria purchase of Rs. 500. Write Python code 
using dictionary lookup and list operations to locate Sara's record in 'students' and 
append 500 to her 'expenses' list.'''

for st in students:
    if st['name'] == 'Sara':
        st.update({'expenses': st['expenses'] + [500]})
print(students)



'''Q5:Write Python code using a loop and conditions to find and display the name of the 
student who has spent the highest total amount across the dataset, along with their 
calculated total expenditure.'''

highest_spender = None
highest_expenditure = 0

for st in students:
    total_expenditure = sum(st['expenses'])
    if total_expenditure > highest_expenditure:
        highest_expenditure = total_expenditure
        highest_spender = st['name']
print(f"Highest spender: {highest_spender}, Total Expenditure: {highest_expenditure}")



