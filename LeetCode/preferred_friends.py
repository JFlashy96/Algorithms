"""
    Jonathan Alston
    February 2022
    The purpose of this function is to return the number of unhappy friends
    given a list of preferences.
"""
def unhappyFriends(n, preferences, pairs):
    """
    :type n: int
    :type preferences: List[List[int]]
    :type pairs: List[List[int]]
    :rtype: int
    """
    dd = {}

    for i,x in pairs:
        dd[i] = preferences[i][:preferences[i].index(x)]
        dd[x] = preferences[x][:preferences[x].index(i)]
 
    ans = 0

    for i in dd:
        for x in dd[i]:
            if i in dd[x]:
                ans += 1
                break

    return ans
    
# Driver code
n = 4 
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]
print(unhappyFriends(n, preferences, pairs))