#Write code to reverse the list in-place without using built-in reverse() or slicing.

numbers = [3, 7, 2, 8, 4, 1, 9, 5]
left, right = 0, len(numbers) - 1
while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1
print(numbers)
