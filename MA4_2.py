#!/usr/bin/env python3.9

from person import Person
from time import perf_counter as pc
from tkinter import N
from numba import njit


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

def main():
	n = 35
	f = Person(n)
	print(f.get())
	f.set(7)
	start_py = pc()

	print(fib_py(n))

	end_py = pc()
	print(f"Process took {round(end_py-start_py, 2)} seconds using fib py")
	
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
