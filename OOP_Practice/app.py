class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, position):
        return self.cars[position]

    def __repr__(self):
        return f'<Garages {self.cars}>'

    def __str__(self):
        return f'Garage has {len(self)} cars'


nissan = Garage()
nissan.cars.append("Rogue")
nissan.cars.append("Titan")
print(nissan.cars)
print(len(nissan))  # __len__
print(nissan[0])  # __getitem__
print(nissan)  # __str__