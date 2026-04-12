# Attempt

prev_num = 0
next_num = 1

for i in range(1, 20):
    num = prev_num + next_num
    print(f"{prev_num} plus {next_num} equal {num}")
    prev_num = next_num
    next_num = next_num + num

