#!/usr/bin/env python3.9

from person import Person
from time import perf_counter as pc
from tkinter import N
from numba import njit
from matplotlib import pyplot as plt


def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

@njit
def fib_numba(n):
	a = 0
	b = 1

	while(n-1):
		c=a+b
		a,b = b,c
		n=n-1
	return c

def eval_time(n, f):
	result = []
	for i in n:
		start = pc()
		f(i)
		end = pc()
		result.append(end-start)
	return result


def main():
	n_start = 30
	n_stop = 45
	f = Person(20)

	print(f' --- Making plot with n= {n_start}-{n_stop} --- ')
	n = [i for i in range(n_start,n_stop)]
	time_py = []

	time_numba = []
	time_cpp = []

	print('start py')
	time_py = eval_time(n, fib_py)

	print('py done')
	print('start numba')
	time_numba = eval_time(n, fib_numba)
	print('numba done')

	print('start c++')
	time_cpp = eval_time(n, f.fib)
	print('c++ done')

	plt.plot(n,time_py)
	plt.plot(n,time_numba)
	plt.plot(n,time_cpp)

	plt.legend(['py','numba','c++'])
	plt.xlabel('n')
	plt.ylabel('Time [s]')
	plt.title('Time to calculate fib with different methods')
	
	plt.savefig('plot')

	n = 47	
	print(f' --- Comparing numba to c++ with n= {n} ---')
	start_numba = pc()

	print(fib_numba(n))

	end_numba = pc()
	print(f"Process took {round(end_numba-start_numba, 2)} seconds using fib numba")

	start_py = pc()

	print(f.fib(n))

	end_py = pc()
	print(f"Process took {round(end_py-start_py, 2)} seconds using c++") 

	




if __name__ == '__main__':
	main()
