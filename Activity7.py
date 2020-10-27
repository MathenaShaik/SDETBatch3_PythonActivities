numbers = list(input("Enter a sequence of your list: ").split(","))
sum = 0

for number in numbers:
  sum += int(number)

print(sum)