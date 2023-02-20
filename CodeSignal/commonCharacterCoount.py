"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c"
"""
def solution(s1, s2):   
    common_char = 0
    hash = set()
    for i in range(0, len(s1)):
        if s1[i] not in hash:
            hash.add(s1[i])
            if s1[i] in s2:
                common_char += min(s2.count(s1[i]), s1.count(s1[i]))
    return common_char

s1 = "aabcc"
s2 = "adcaa"
print(solution(s1, s2))