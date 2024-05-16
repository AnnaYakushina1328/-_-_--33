# написать функциональную модель насоса (сначала пустая функция) потом определенные функции (ротарный, плунжерный, центробежнвый) несколько,
# потом передача параметров (кпд, мощность и тд) (по поводу передачи параметров для хороших баллов сделать чтобы в зависимости от того что передаешь
# (допустим первое и второе значение) выдает (допустим) третье значение) ЛИБО можно сделать это с помощью частных фунций

def find_h(k):
    return f"Задано: k\nНайдено: h = {-k} ед."


def find_k(h):
    return f"Задано: h\nНайдено: k = {-h} ед."


def pump(*funcs):
    def wrapper(h=0, k=0):
        for func in funcs:
            if "centrifugal" in func.__name__:
                print("Текущий насос: центробежный")
                print(find_h(func(h, k)))
            else:
                print("Текущий насос: плунжерный")
                print(find_k(func(h, k)))
            print()
    return wrapper


@pump
def centrifugal_pump(h=0, k=0):
    return h if h else k


@pump
def plower_pump(h=0, k=0):
    return h if h else k


centrifugal_pump(k=2)
plower_pump(h=12)
