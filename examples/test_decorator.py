# функция декоратор
def dec(f_arg):
    def wrapper():
        # доп логика №1
        print("Before")
        f_arg()
        # доп логика №2
        print("After")
    return wrapper

@dec
# целевая функция
def func_1():
    print("Hello!")

# func_1 = dec(func_1)

# вызов функции
func_1()