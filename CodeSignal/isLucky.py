"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false
"""
def solution(n):
    res = [int(x) for x in str(n)]
    count = 0
    second_count = 0
    for i in range(0, int(len(res)/2)):
        count += res[i]
    for i in range(int(len(res)/2), len(res)):
        second_count += res[i]
    if count == second_count:
        return True
    else:
        return False

n = 239017
print(solution(n))