# ✔ Создайте функцию генератор чисел Фибоначчи

def gen_Fib(num: int):
    f = f_one = 0
    f_two = 1
    yield f
    for _ in range(num + 1):
        f = f_one + f_two
        f_two, f_one = f_one, f
        yield f

print(*gen_Fib(10))
