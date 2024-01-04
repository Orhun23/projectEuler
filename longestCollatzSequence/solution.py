def collatz_sequence_length(x, memo):
    if x in memo:
        return memo[x]

    count = 1
    original_x = x

    while x > 1:
        if x % 2 == 0:
            x = x / 2
            count += 1
        else:
            x = 3 * x + 1
            count += 1

    memo[original_x] = count
    return count

max_starting_x = 0
max_sequence_length = 0
memo = {}

for start_x in range(999999, 1, -1):
    sequence_length = collatz_sequence_length(start_x, memo)

    if sequence_length > max_sequence_length:
        max_sequence_length = sequence_length
        max_starting_x = start_x

print("Starting value under 1 million for the longest Collatz sequence:", max_starting_x)
print("Length of the sequence:", max_sequence_length)
