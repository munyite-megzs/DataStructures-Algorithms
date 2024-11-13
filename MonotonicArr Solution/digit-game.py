def alice_wins(nums):
    # Separate the single-digit and double-digit numbers
    single_digit_sum = sum(num for num in nums if 1 <= num <= 9)
    double_digit_sum = sum(num for num in nums if 10 <= num <= 99)
    # Total sum of all numbers
    total_sum = single_digit_sum + double_digit_sum
   
    # If Alice chooses all single digits, Bob gets the double digits
    # Alice wins if her sum is strictly greater than Bob's sum
    if single_digit_sum > double_digit_sum:
        return True
    # If Alice chooses all double digits, Bob gets the single digits
    if double_digit_sum > single_digit_sum:
        return True
    # If neither condition is true, Alice cannot win
    return False

print(alice_wins([1, 2, 3, 4, 10]))
print(alice_wins([1, 2, 3, 4, 5, 14]))
print(alice_wins([7,11,3,8,5]))