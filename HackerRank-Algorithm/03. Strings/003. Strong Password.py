n = int(input().strip())
pwd = input()

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
nu, lc, uc, sc = 0, 0, 0, 0
for letter in pwd:
    if letter in numbers: nu = 1
    if letter in lower_case: lc = 1
    if letter in upper_case: uc = 1
    if letter in special_characters: sc = 1

print(max(int(not nu) + int(not lc) + int(not uc) + int(not sc), 6 - n))

