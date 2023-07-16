def count_subsequence_AG(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'A':
            for j in range(i+1, len(s)):
                if s[j] == 'G':
                    count += 1
    return count
string_A = "GAB"
result = count_subsequence_AG(string_A)
print("Number of occurrences of subsequence 'AG':", result)
