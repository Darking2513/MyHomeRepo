
def caching_fibonacci():
    # створли кцію, яка обчислює n-ий член послідовності Фібоначчі
    cache = {}
    def fibonacci(n):
        # перевіряємо, чи n є дійсним числом
        if n <= 0: 
           return 0
        if n == 1:
            return 1
        # перевіряємо, чи n вже обчислювався раніше
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(20))  # 6765