class TeaKettle:
    def init(self, is_empty=True, is_on_stove=False):
        self.is_empty = is_empty
        self.is_on_stove = is_on_stove

    def fill_with_water(self, faucet):
        if not self.is_empty:
            print("Tea kettle is already filled with water.")
            return
        print("Filling tea kettle with water from faucet...")
        self.is_empty = False

    def put_on_stove(self, stove):
        if self.is_on_stove:
            print("Tea kettle is already on the stove.")
            return
        print("Putting tea kettle on the stove...")
        self.is_on_stove = True

    def light_gas(self, matches):
        if not self.is_on_stove:
            print("Tea kettle is not on the stove. Cannot light gas.")
            return
        print("Lighting gas with matches...")
        print("Waiting for tea kettle to boil...")

    def pour_out_water(self):
        if self.is_empty:
            print("Tea kettle is already empty.")
            return
        print("Pouring out water from tea kettle...")
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
