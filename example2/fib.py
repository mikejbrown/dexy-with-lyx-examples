def fib(n):
    """ Generate the n-th number in the Fibonacci sequence. """
    assert n == int(n), "n in fib(n) must be an integer"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return fib(n - 1) + fib(n - 2)
    else:
        raise RuntimeError("fib(%d) not defined" % n)


if __name__ == "__main__":
    for n in xrange(10):
        print n, fib(n)
