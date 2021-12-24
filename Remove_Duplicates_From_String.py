"""
	Given a string S, remove all the duplicates in thje givcen string.
"""
string="geeksforgeeks"
second_string=""
third_string="ooo"

string_list = [string, second_string, third_string]

for string in string_list:
	k2 = []
	for ele in string:
		if ele not in k2:
			k2.append(ele)

	print(k2)