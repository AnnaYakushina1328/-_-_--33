class TeaKettle:
    def init(self, is_empty=True, is_on_stove=False):
        self.is_empty = is_empty
        self.is_on_stove = is_on_stove

    def fill_with_water(self, faucet):
        if not self.is_empty:
            print("Чайник уже наполнен водой.")
            return
        print("Наполнение чайника водой из-под крана...")
        self.is_empty = False

    def put_on_stove(self, stove):
        if self.is_on_stove:
            print("Чайник уже стоит на плите.")
            return
        print("Ставлю чайник на плиту...")
        self.is_on_stove = True

    def light_gas(self, matches):
        if not self.is_on_stove:
            print("На плите нет чайника. Не удается зажечь газ.")
            return
        print("Зажигание газа спичками...")
        print("Ждем, пока закипит чайник...")

    def pour_out_water(self):
        if self.is_empty:
            print("Чайник уже пуст.")
            return
        print("Выливание воды из чайника...")
        self.is_empty = True

class Faucet:
    def init(self):
        pass

class Stove:
    def init(self):
        pass

class Matches:
    def init(self):
        pass
