# Memoiezed recursive method

def memoized_rod_cutting(price, n):
	r = []
	for i in range(n+1):
		r.append(-200)
	return memoized_aux(price, n, r)

def memoized_aux(p, n, r):
	if r[n] >= 0:
		return r[n]
	
	if n == 0:
		q = 0
	else:
		q = -200
		
		for j in range(n):
			q = max(q, p[j] + memoized_aux(p, n-j-1, r))
		r[n] = q
	return q
