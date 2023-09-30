from random import randint


class House:
    def __init__(self):
        self.money = 100
        self.dirty = 0
        self.fridge = 50

    def dirty(self):
        self.dirty += 5
        return (self.dirty)
    
    def buy_products(self):
        if self.fridge <= 100 and self.money > 50:
            self.fridge += 30
            self.money -= 30
            return print('Wife bought {} products '.format(self.fridge))

class Person(House):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return print(f"Name: {self.name}, Fullness: {self.fullness}, Happiness: {self.happiness}")


    def eat(self):
        if self.fridge < 10:
            House.buy_products(self=self)
        if self.fullness < 30:
            self.fullness += 20
            self.fridge -= 20
            return print(f"Сытость - {self.fullness}, Осталось еды - {self.fridge}")
        
    
    def dead(self):
        if self.happiness < 10 or self.fullness < 1:
            return '{} is dead'.format(self.name)
        

    def stats(self):
        print(f"Money - {self.money}")
        print(f"Fridge - {self.fridge}")
        print(f"Dirty - {self.dirty}")

class Husband(Person, House):
    def __init__(self, name):
        super().__init__(name)
        House.__init__(self)


    def work(self):
        self.fullness -= 10
        self.money += 100
        return print('Husband earnded some money, now we have {} money'.format(self.money))

    def WoT(self):
        self.happiness += 20
        return print('Husband played WoT and became {} happier'.format(self.happiness))

    def eat(self):
        super().eat()
        return print('{} съел {} еды, Осталось еды - {}'.format(self.name, self.fullness, self.fridge))


    def act(self):
        dice = randint(1, 6)
        if dice == 3 or self.happiness < 20:
            self.WoT()
        elif dice == 1 or dice ==2 or self.money < 40:
            self.work()
        self.eat()
        self.dead()        
        

class Wife(Person, House):
    def __init__(self, name):
        super().__init__(name)
        House.__init__(self)



    def __str__(self):
        super.__str__() 




    def eat(self):
        super().eat()
        return print('{} съела {} еды, осталось еды - {} '.format(self.name, self.fridge, self.fullness))

    def outwear(self):
        print('Wife bought outwear for {} money'.format(self.money))
        if self.money > 700:
            self.money -= 500
            self.happiness += 60
        return print(f"Money - {self.money}, Happiness - {self.happiness}")
    def clean(self):
        House.dirty(self)
        if self.dirty > 25:
            print('Wife cleaned the house and removed {} dirt'.format(self.dirty))
            self.dirty = 0


    def act(self):
        dice = randint(1, 6)
        if dice == 1:
            self.clean()
        if self.fridge < 20:
            House.buy_products()
        if self.happiness < 20:
            self.outwear() or self.Dota2()
        self.clean()
        self.dead()
        self.eat()
        self.stats()


home = House()
Alex = Husband('Alex')
masha = Wife('Masha')
for day in range (1, 100):
    print('=============== Day {} ================'.format(day))
    Alex.act()
    masha.act()
