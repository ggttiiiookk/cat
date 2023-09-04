import random


class cat:
    def __init__(self, name):
        self.name = name
        self.fat = 10
        self.hungry = 5
        self.gladness = 10
        self.alive = True
    def to_play(self):
        print("Time to study")
        self.hungry -= 0.20
        self.fat -= 0.30
        self.gladness += 2
    def to_sleep (self):
        print("Time to sleep")
        self.fat += 3
        self.hungry -= 3
    def to_eat (self):
        print ("Rest time")
        self.fat += 2
        self.hungry += 5
    def is_alive (self):
        if self.hungry < 0.5:
            print("you hungry")
            self.alive = False
        elif self.fat >= 100:
            print("you very big")
            self.alive = False
        elif self.gladness >= 100:
            print("Excellent!!!")
            self.alive = False
    def end_of_day(self):
        print(f"fat = {self.fat}")
        print(f"hungry = {self.hungry}")
        print(f"gladness = {self.gladness}")
    def live (self, day):
        day = (f"day {day} of {self.name} lifr")
        print(f"{day:=^30}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_sleep()
        elif live_cube == 2:
            self.to_eat()
        elif live_cube == 3:
            self.to_play()
        self.end_of_day()
        self.is_alive()


murzik = cat (name="murzik")

for day in range(365):
    if murzik.alive == False:
        break
    murzik.live(day)