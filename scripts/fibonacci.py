# fibonacci() function takes in an index, n, and returns the nth value in the sequence.
# any negative index values should return -1. no loops allowed.

def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
            
if __name__ == "__main__":
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')