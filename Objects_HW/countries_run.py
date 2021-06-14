class Country:

    def __init__(self):
        self.area = None
        self.neighbours = None
        self.population = None
        self.language = None
        self.cities = []

    def show_all_cities(self):
        print('Some cities are: ')
        for city in self.cities:
            print(f' - {city}')


class Romania(Country):

    readable_objects = []
    developer_objects = []

    def __init__(self, area, population, language):

        if (isinstance(area, str)) or (isinstance(population, str)) or (not isinstance(language, str)):
            raise ValueError('Invalid input format')

        super().__init__()
        self.country_name = self.__class__.__name__
        self.area = area
        self.population = population
        self.language = language
        self.neighbours = ('Bulgaria', 'Hungary', 'Moldova', 'Serbia', 'Ukraine')
        self.attractions = ['Black Sea', 'Dracula Castle', 'Monasteries']
        self.universities = ['Cluj University', 'Bucuresti University', 'Iasi University']
        self.density = self.population / self.area
        self.readable_objects.append(self.__str__())
        self.developer_objects.append(self.__repr__())

    def __str__(self):
        return f'{self.country_name}-> Area: {self.area}, Population: {self.population}, Density: {self.density}'

    def show_neighbours(self):
        print(f'{self.country_name} has the neighbours: ')
        for neighbour in self.neighbours:
            print(f'{neighbour}')

    def show_attractions(self):
        print(f'In {self.country_name} some attractions are: ')
        for i in range(len(self.attractions)):
            print(f' - {self.attractions[i]} ')

    def show_universities(self):
        print(f'The main universities are:')
        for uni in self.universities:
            print(f' - {uni}')

    def show_density(self):
        print(f'{self.country_name} has a density of {self.density}')

    def add_city(self, city):
        self.cities.append(city)

    def add_attraction(self, attraction):
        self.attractions.append(attraction)

    @classmethod
    def get_readable_objects(cls):
        return cls.readable_objects

    @classmethod
    def get_developer_objects(cls):
        return cls.developer_objects

    @staticmethod
    def greeting(name):
        print(f'Hi {name}! This is a classes and objects exercise!')
        return name


def __main__():
    Romania.greeting('Oana')
    ro = Romania(556.565, 18256000, 'Romanian')
    ro.add_city('Cluj-Napoca')
    ro.show_density()
    ro.show_all_cities()
    ro.show_neighbours()
    ro.show_attractions()
    ro.add_city('Bucuresti')
    ro.show_all_cities()
    ro.show_universities()
    ro2 = Romania(50200, 9000896, 'German')
    ro3 = Romania(20000, 985000000, 'Sweedish')
    print(f'Readable objects are: {Romania.get_readable_objects()}')
    print(f'Developer objects are: {Romania.get_developer_objects()}')

    # test validation in constructor for each parameter
    ro4 = Romania('20', 56565, 'Romanian')
    ro4 = Romania(565650, '7979', 'Romanian')
    ro4 = Romania(235660, 894110, 5556)


__main__()
