start_number = int(input('please choose number: '))
end_number = int(input('please choose second number: ')) 

total_sum= 0
total_product=1

for i in range(start_number,end_number + 1):
    total_sum += i
    total_product *= i

print(f" from {start_number} to {end_number} sum of numbers: {total_sum}")

print(f" from {start_number} to {end_number} the answer of  multiplied numbers are: {total_product}")

