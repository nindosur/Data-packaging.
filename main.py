import json
import pickle
import datetime

    # 1, 2
class Airplane:
    def __init__(self, model, capacity, wingspan):      # capacity - вместительность, wingspan - размах крыльев
        self.model = model
        self.capacity = capacity
        self.wingspan = wingspan

    def __str__(self):
        return f'Модель: {self.model} \nВместительность: {self.capacity} \nРазмах крыльев: {self.wingspan}'

    def to_json(obj):
        if isinstance(obj, Airplane):
            result = obj.__dict__
            result["className"] = obj.__class__.__name__
            return result

airplane = Airplane('AX-678', 300, '100meters')
# json
k = json.dumps(airplane, default=Airplane.to_json)
with open('airplane.json', 'w') as f:
    f.write(k)
with open('airplane.json', 'r') as f:
    z = json.load(f)
print(z)

# pickle
with open('airplane.pkl', 'wb') as f1:
    pickle.dump(airplane, f1)
with open('airplane.pkl', 'rb') as f1:
    p = pickle.load(f1)
print(p)

    # 3
class Drob:
    def __init__(self, ch, z):
        self.ch = ch
        self.z = z
    def __str__(self):
        return f'{self.ch}/{self.z}'
    def __add__(self, other):
        x = self.ch * other.z + self.z * other.ch
        y  = self.z * other.z
        return f'{x} / {y}'
    def __sub__(self, other):
        x = self.ch * other.z - self.z * other.ch
        y = self.z * other.z
        return f'{x} / {y}'
    def __mul__(self, other):
        x = self.ch * other.ch
        y = self.z * other.z
        return f'{x} / {y}'
    def __truediv__(self, other):
        x = self.ch * other.z
        y = self.z * other.ch
        return f'{x} / {y}'
    def to_json(obj):
        if isinstance(obj, Drob):
            result = obj.__dict__
            result["className"] = obj.__class__.__name__
            return result

drob1 = Drob(2, 3)
drob2 = Drob(5, 10)
drob3 = drob1, drob2
print(f'drob1 = {drob1}')
print(f'drob2 = {drob2}')

print(f'{drob1} + {drob2} = {drob1+drob2}')
print(f'{drob1} - {drob2} = {drob1-drob2}')
print(f'{drob1} * {drob2} = {drob1*drob2}')
print(f'{drob1} / {drob2} = {drob1/drob2}')

# json
k = json.dumps(drob3, default = Drob.to_json)
with open("drobe.json", "w") as f:
    f.write(k)
with open("drobe.json", "r") as f:
    z = json.load(f)
print(z)

# pickle
with open('drobe2.pkl', 'wb') as f1:
    pickle.dump(drob1, f1)
with open('drobe2.pkl', 'rb') as f:
    p = pickle.load(f)
print(p)

    # 4
class Timer:
    def __init__(self, day, mounth, years, hours, minute):
        self.day = day
        self.mounth = mounth
        self.years = years
        self.hours = hours
        self.minute = minute
    def __str__(self):
        return f'Дата: {self.day}-{self.mounth}-{self.years}\n' \
               f'Время: {self.hours}:{self.minute}'

daytime = datetime.datetime.now().strftime('%d')
mounthtime = datetime.datetime.now().strftime('%m')
yearstime = datetime.datetime.now().strftime('%y')

hourstime = datetime.datetime.now().strftime('%H')
minutetime = datetime.datetime.now().strftime('%M')

timer = Timer(daytime, mounthtime, yearstime, hourstime, minutetime)

# pickle
with open('time.pkl', 'wb') as f1:
    pickle.dump(timer, f1)
with open('time.pkl', 'rb') as f:
    p = pickle.load(f)
print(p)

# json
k = json.dumps(timer, default=lambda x: x.__dict__)
with open("time.json", "w") as f:
    f.write(k)
with open("time.json", "r") as f:
    z = json.load(f)
print(z)