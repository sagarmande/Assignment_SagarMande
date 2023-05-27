def is_valid_string(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    values = list(char_counts.values())
    distinct_values = set(values)

    if len(distinct_values) == 1:
        return "YES"
    elif len(distinct_values) == 2:
        count1, count2 = distinct_values
        if values.count(count1) == 1 and count1 == 1:
            return "YES"
        elif values.count(count2) == 1 and count2 == 1:
            return "YES"

    
    return "NO"


s = "aabbbcc"
print(is_valid_string(s))

s = "aabbccd"
print(is_valid_string(s))


