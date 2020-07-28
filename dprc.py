# A Dynamic Programming solution for Rod cutting problem 
INT_MIN = -32767

def cutRod(price, n): 
	val = []
	for x in range(n+1):
		val.append(0) 
	for i in range(1, n+1): 
		max_val = INT_MIN 
		for j in range(i): 
			max_val = max(max_val, price[j] + val[i-j-1]) 
		val[i] = max_val 

	return val[n] 


