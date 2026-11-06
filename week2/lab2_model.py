class ClassroomAgent:
    def __init__(self):
        self.last = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"
        same = target == self.last
        if same:
            send = False
        else:
            send = True
        self.last = target
        return target, send
