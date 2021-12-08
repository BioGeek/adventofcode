with open("2017/data/day25_demo.txt") as f:
    blueprint = f.read().splitlines()


class WMC:
    def __init__(self, write_val, move_to, continue_with):
        self.write_val = write_val
        self.move_to = move_to
        self.continue_with = continue_with

    def write(self):
        pass

    def move(self):
        pass

    def contin(self):
        pass


class State:
    def __init__(self, name, wmc0, wmc1):
        self.name
        self.wmc0 = WMC(*wmc0)
        self.wmc1 = WMC(*wmc1)
