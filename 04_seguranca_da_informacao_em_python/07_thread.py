# Nesse exemplo vamos considerar a corrida entre dois carros que vão competir em velocidades diferentes

from threading import Thread
import time


def car(speed, pilot):
    trajeto = 0
    while trajeto <=50:
        trajeto+= speed
        time.sleep(0.5)
        print("Piloto: {} km: {}\n".format(pilot, trajeto))



t_car1 = Thread(target=car, args=[1, "Caio"])
t_car2 = Thread(target=car, args=[1.5, "Vinicius"])

t_car1.start()
t_car2.start()
