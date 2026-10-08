def generate_fibonacci(n: int):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

if __name__ == "__main__":
    terms = 10
    print(f"First {terms} terms of Fibonacci series:")
    print(generate_fibonacci(terms))