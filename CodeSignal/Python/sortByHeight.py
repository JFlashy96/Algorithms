"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""
def solution(a):
    new_a = []
    non_neg = []
    for i in range(0, len(a)):
        if a[i] != -1:
            non_neg.append(a[i])
    non_neg.sort()
    for i in range(0, len(a)):
        if a[i] == -1:
            new_a.append(a[i])
        else:
            new_a.append(non_neg[0])
            non_neg.remove(non_neg[0])
    return new_a     

a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(solution(a))