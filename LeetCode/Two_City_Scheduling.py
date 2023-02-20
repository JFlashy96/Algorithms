"""
	Jonathan Alston
	January 2022
	This program returns the minimum cost to fly every person to a city
	such that exactly n people arrive in each city.
	Scenario: A company is planning to interview 2n people. Given the array costs where 
	costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti,
	and the cost of flying the ith person to city b is bCosti.
	Example:
	Input: cost = [[10,20], [30,200], [400, 50], [30,20]]
	Output: 10 + 30 + 50 + 20 = 110
	Explanation: The minimum total cost to fly half the people interviewing in each city.
"""
def find_min(costs):
	"""
	Input: list
	Return int n - the minimum cost to fly every person to a city such that exactly
				   n people arrive in each city.
	"""
	firstCity = [i for i, j in costs]
	diff = [j - i for i, j in costs]
	return sum(firstCity) + sum(sorted(diff)[:len(costs)//2])

costs = [[10,20], [30,200], [400, 50], [30,20]]
print("The minimum cost for the first list is {}:".format(find_min(costs)))
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print("The minimum cost for the first list is {}:".format(find_min(costs)))
costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
print("The minimum cost for the first list is {}:".format(find_min(costs)))
