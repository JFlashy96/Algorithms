def minCostRec(N, start, finish, ticket_cost):

	if (start == finish) or (start + 1 == finish):
		return ticket_cost[start]

	min = ticket_cost[start]

	for i in range (start+1, finish):
		c = minCostRec(N, start, i, ticket_cost) + minCostRec(N, i, finish, ticket_cost)
	if c < min:
		min = c
	return min

def minCost(N, start, finish, ticket_cost):
	return minCostRec(N, start, finish, ticket_cost)

N = 4
start = 1
finish = 4
ticket_cost = [1, 2, 2, 4]
answer = minCost(N, start, finish, ticket_cost)
print(answer)