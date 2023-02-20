""" 
Given a rectangular matrix of characters, add a border of asterisks (*) to it.
"""
def solution(picture):
	for i in range(0, len(picture)):
		picture[i] = "*{}*".format(picture[i])
	length = len(picture[i])
	insert = ""
	for i in range(length):
		insert += "*"
	picture.append(insert)
	picture.insert(0, insert)
	return picture