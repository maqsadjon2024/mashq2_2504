# 24 - misol
class Shopltem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name} - 5000 so'm")

    def dicount(self):
        print(f"{self.price} chegerma qolandi")

s = Shopltem("Banan", "20%")
s.show()
s.dicount()


# 25 - misol
class Alarm:
    def __init__(self, time):
        self.time = time
    def set_alarm(self):
        print(f"Alarm {self.time} ga o‘rnatildi")
    def ring(self):
        print(f"Jiring!")

s1 = Alarm("7:00")
s1.set_alarm()
s1.ring()


# 26 - misol
class Message:
    def __init__(self, text):
        self.text = text
    def send(self):
        print(f"{self.text} Xabar yuborildi")
    def delete(self):
        print(f"Xabari o‘chirildi!")

q = Message("Salom")
q.send()
q.delete()


# 27 - misol
class File:
    def __init__(self, name):
        self.name = name
    def open(self):
        print(f"{self.name} file.txt ochildi")
    def close(self):
        print(f"{self.name} file.txt yopildi")

q1 = File("Yashirin")
q1.open()
q1.close()


# 28 - misol
class DoorLock:
    def __init__(self, locked):
        self.locked = locked
    def lock(self):
        print(f"{self.locked} Qulflandi")
    def unlock(self):
        print(f"{self.locked} Ochildi")

w1 = DoorLock("Eshik")
w1.lock()
w1.unlock()
