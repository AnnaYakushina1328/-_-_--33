# модель насоса с использованием ООП

class Pump:
    def __init__(self, pump_type):
        self.pump_type = pump_type

    def find_h(self, k):
        return f"Задано: k\nНайдено: h = {-k} ед."

    def find_k(self, h):
        return f"Задано: h\nНайдено: k = {-h} ед."

    def operate(self, h=0, k=0):
        if self.pump_type == "centrifugal":
            print("Текущий насос: центробежный")
            print(self.find_h(h if h else k))
        else:
            print("Текущий насос: плунжерный")
            print(self.find_k(h if h else k))
        print()


centrifugal_pump = Pump("центробежный")
plunger_pump = Pump("плунжерный")

centrifugal_pump.operate(k=2)
plunger_pump.operate(h=12)
