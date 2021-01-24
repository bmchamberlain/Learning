#Program to prompt for age and a number then advise which year the user will be 100 years old, repeats output on a number of lines equal to the prompted number. Year is calculated using system time.


import datetime
now = datetime.datetime.now()
year = now.year
age = int(input("Enter your age: "))
copies = int(input("Enter a number: "))
age_math = str(100 - age + year)

print(("You will be 100 years old in the year: " + age_math + "\n") * copies)


