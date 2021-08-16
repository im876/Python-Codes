num = 1234

thousands = num // 1000
hundreds = (num % 1000) // 100
tens = (num % 100) // 10
units = (num % 10)

print(thousands)
print(hundreds) 
print(tens) 
print(units)
# expected output: 1 2 3 4
