# Recursive way of rod cutting
INT_MIN = -32767
def rod_cutting(p, n):
	if n == 0:
		return 0
	q = INT_MIN
	for i in range(n):
		q = max(q, p[i]+rod_cutting(p, n-i-1))
	return q
