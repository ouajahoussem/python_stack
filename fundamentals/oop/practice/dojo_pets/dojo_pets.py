class pet:
    def __init__(self, name, type, tricks, noise):
        self.name= name
        self.type= type
        self.tricks= tricks
        self. health= 100
        self.energy= 50
        self.noise= noise
    
    def sleep(self):
        self.energy+= 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 10
        return self

    def noise(self):
        print(self.noise)


class ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name= first_name
        self.last_name= last_name
        self.treats= treats
        self.pet_food= pet_food
        self.pet= pet
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self


    def bathe(self):
        self.pet.noise()
        return self





my_pet_food =['pizza', 'burger']
my_treats= ['Snausage','Bacon',"Trash Bag"]

nibbles= pet("mr. nibbles", "horse",['nibbles on things','is invisible'],"hey hey" )
adrien= ninja("adrien", "dion",my_treats, my_pet_food, nibbles)

adrien.feed()
adrien.feed()
adrien.feed()