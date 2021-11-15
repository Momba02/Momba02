class satelite:
    fuel = 0
    def __init__(self, name, height = 0):
        self.__name = name
        self._height = height
#    def __check_height__(self,height):

    def add_height(self, value = 20):
        self._height += value
        if(self._height > 50):
            self._height = 50
    def get_height(self):
        return self._height
    def get_name(self):
        return self.__name
    def set_fuel(self,fuel):
        self.fuel = fuel
    def get_fuel(self):
        return self.fuel
    #def __eq__(self,fuel):
    #    t = copy.deepcopy(self)
    #    t.fuel = int(fuel)
    #    return t
    def set_name(self,name):
        self.__name = name
   # def __add__(self,fuel):
   #     t = copy.deepcopy(self)
   #     t.fuel += int(fuel.fuel)
   #     return t
    def get_values(self):
        i = 'name:%s, height:%d, fuel:%d' % (self.__name,self.__height,self.fuel)
        return i

#class FilmSate(satelite):


class NetworkSate(satelite):
    def __init__(self, name, height, com = 0):
        super().__init__(name, height)
        self.__comunication = com
    def add_height(self, value = 20):
        self._height += value


