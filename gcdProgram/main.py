def gcd(a, b):
	result = min(a, b)
	while result:
		if a % result == 0 and b % result == 0:
			break
		result -= 1
	return result
# Driver Code
if __name__ == '__main__':
	a = 98
	b = 56
	print(f"GCD of {a} and {b} is {gcd(a, b)}")



