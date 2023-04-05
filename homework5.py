class Person:
    biology_class = 'Human'
    def __init__(self, name, age, gender):
        self._name = name
        self.age = age

        self.gender = gender
    def work(self):
        return 'I work a lot!'
    def train(self):
        return "I love to train outside!"
    def get_name(self):
        return f'Hello! My name is {self._name}, I am {self.age} years old, I am {self.gender}'

    def set_name(self, new_name):
        self._name = new_name

# person1 = Person('Jack', 36, "male")
# print(person1._name)
# print(person1.get_name())
# print(person1.work())

person2 = Person('Valeria', 27, 'female')
print(person2.biology_class)
print(person2.get_name())
print(person2.train())
print(person2.__dict__)
print(person2.set_name('Barbara'))
# person2.name = 'Barbara'
print(person2.get_name())
