a = int(input())
country_set = set()

for i in range(a):
    country_name = input()
    country_set.add(country_name)
print(len(country_set))
