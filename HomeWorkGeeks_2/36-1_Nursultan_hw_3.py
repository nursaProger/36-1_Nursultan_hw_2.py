class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value


    def __str__(self):
        return (f'CPU: {self.__cpu}\n'
                f'Memory: {self.__memory} gb')


    def make_computations(self):
        result = self.__cpu + self.__memory
        return result


    def __eq__(self, other):
        return self.__memory == other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory





class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list


    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value


    def __str__(self):
        return super().__str__() + f'\nSim cards: {self.__sim_cards_list}'


    def call(self, sim_card_number, call_to_number):
        print(f'"Идет звонок на номер {sim_card_number} с сим-карты-{call_to_number} -Beeline"')


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'"Navigation to {location} using GPS"')

    def __str__(self):
        return super().__str__() + f'\nSim cards: {self.sim_cards_list}'


comp = Computer(5 , 512)

phone_nokia = Phone(['O!', 'Megacom'])

iphone = SmartPhone(15, 256, ['O!', 'Beeline'])
samsung = SmartPhone(990, 128, ['Beeline', 'Megacom'])


print(comp)
print(phone_nokia)
print(iphone)
print(samsung)

print(phone_nokia.call('0705905890', '1'))

iphone.use_gps('ibraimova 103')
print(comp.make_computations())
phone_nokia.call('0501300160', '2')

print(iphone == samsung)
print(iphone != samsung)
print(iphone < samsung)
print(iphone <= samsung)
print(iphone > samsung)
print(iphone >= samsung)






























