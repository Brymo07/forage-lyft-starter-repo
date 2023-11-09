from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear


    def needs_service(self):
        if sum(self.tire_wear) >= 3:
            return True
        else:
            return False
