"""
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
solution(time) = true;
For time = "25:51", the output should be
solution(time) = false;
For time = "02:76", the output should be
solution(time) = false.
"""
def solution(time):
	if ":" not in time:
		return False
	new_time = []
	for i in range(0, len(time)):
		new_time.append(time[i])
	return 0 <= int(str(time[0]+""+time[1])) < 24 and 0 <= int(str(time[3]+""+time[4])) < 60
print(solution(time="13:48"))
print(solution(time="02:76"))