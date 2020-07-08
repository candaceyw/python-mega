import datetime

mynow = datetime.datetime.now()

print(f'The date and time is {mynow}')

mynumber = 10
mytext = "hello"

print(mynumber, mytext)

x = 10
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y
print(sum1, sum2)
print(type(x), type(y), type(z))



student_grades = { "Mary": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean)

monday_temperatures = (1, 4, 5)
print(monday_temperatures)