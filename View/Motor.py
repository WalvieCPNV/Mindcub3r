class Motor:
    def __init__(self, port) -> None:
        self.port = port
    def rotate(self, speed, angle,):
        motor = Motor(self.port)
        motor.run_angle(speed, angle)
        