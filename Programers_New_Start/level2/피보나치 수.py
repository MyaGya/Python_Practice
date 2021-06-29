def solution(n):
    fib_prev = 0
    fib_now = 1

    for i in range(2, n):
        fib_next = fib_prev + fib_now
        fib_prev = fib_now
        fib_now = fib_next
    else:
        return (fib_prev + fib_now) % 1234567