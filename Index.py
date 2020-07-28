import time
from dprc import cutRod
from mrrc import memoized_rod_cutting
from rrc import rod_cutting

def timeCalculation(arr, size):
	dtime=0
	mtime=0
	rtime=0

	for i in range(30):
		q = 0


		start_time = time.time()
		q = cutRod(arr, size)
		final_time = time.time() - start_time
		dtime = dtime+final_time


		start_time = time.time()
		q = memoized_rod_cutting(arr, size)
		final_time = time.time() - start_time
		mtime = mtime+final_time
		

		start_time = time.time()
		q = rod_cutting(arr, size)
		final_time = time.time() - start_time
		rtime = rtime+final_time
	
	print("Maximum Obtainable Value is " + str(cutRod(arr, size)))
	print("Maximum Obtainable Value is " + str(memoized_rod_cutting(arr, size)))
	print("Maximum Obtainable Value is " + str(rod_cutting(arr, size)))
	
	print("Average time after 30 trials in Dynamic programing method is: "+ str(dtime/30))
	print("Average time after 30 trials in Memoized recursive method is: "+ str(mtime/30))
	print("Average time after 30 trials in Recursive method is: "+ str(rtime/30))
