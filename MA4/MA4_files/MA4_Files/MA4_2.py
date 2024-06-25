#!/usr/bin/env python3
from numba import njit
import time
from person import Person

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
	
@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	n = 45#------------------( : please change it, fib(69) is not an integer and it wont compute : ) ---------- I wanna try though, miss you so much 
	print("N value:", n)
	f.set(n) 
	start = time.perf_counter()
	print(f.fib())
	end = time.perf_counter()
	
	print("Time with C++ : ", "{:.10f}".format(-start+end))
	fib_numba(n) #precompile before timing for performance 
	start = time.perf_counter()
	print(fib_numba(n))
	end = time.perf_counter()
	print("Time with python and numba : ", "{:.10f}".format(-start+end))

	start = time.perf_counter()
	print(fib_py(n))
	end = time.perf_counter()
	print("Time with python: ", "{:.10f}".format(-start+end))
	

if __name__ == '__main__':
	main()

