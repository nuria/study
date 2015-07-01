#!/usr/local/bin/python


'''
Write a function that computes the list of the first 100 Fibonacci numbers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
'''


def main():
    # caches prior fib numbers to avoid recurring for ever
    # using an array
    cache = []

    def fib(i):
        if i>= len(cache):
            f = cache[i-1] + cache[i-2]
            cache.append(f)
        return cache[i]

    cache.append(0)
    cache.append(1)

    for n in range(0, 101):
        print fib(n)


if __name__ == "__main__":
    main()
