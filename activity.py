def eat(food, is_healthy):
    if not isinstance(is_healthy,bool):
        raise ValueError("this should be a boolean")
    ending = "cuz Yolo"
    if not is_healthy:
        return f"I am eating {food} {ending}"
    return f"I am eating {food} cuz it is healthy"

def nap(num_hours):
    pass

class ElectronicCar():
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def charge(self):
        self.battery = 100
        return self

    def drive(self):
        if self.battery>0:
            self.battery -= 1
            return f"running, {self.name}!"
        return "Low battery!"

