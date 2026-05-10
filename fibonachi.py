# Attempt

sum_1 = 1
sum_2 = 1

for i in range(1, 20):
    num = sum_1 + sum_2
    print(f"{sum_1} + {sum_2} = {num}")
    sum_1 = sum_2
    sum_2 = num

