class Computer:
    def __init__(self, cpu, memory):
        self._cpu = cpu
        self._memory = memory

    @property
    def cpu(self):
        return self._cpu

    @property
    def memory(self):
        return self._memory

    @cpu.setter
    def cpu(self, value):
        self._cpu = value

    @memory.setter
    def memory(self, value):
        self._memory = value

    def make_computations(self):
        result = self._cpu + self._memory
        print(f"Arithmetic computations result: {result}")

    def __str__(self):
        return f"Computer: CPU - {self._cpu}, Memory - {self._memory}"


class Phone:
    def __init__(self):
        self._sim_cards_list = []

    @property
    def sim_cards_list(self):
        return self._sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self._sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self._sim_cards_list):
            print(f"Calling {call_to_number} from sim card {sim_card_number}: {self._sim_cards_list[sim_card_number - 1]}")
        else:
            print("Invalid sim card number.")

    def __str__(self):
        return f"Phone: Sim Cards - {self._sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self)

    def use_gps(self, location):
        print(f"GPS navigation to {location}")

    def __str__(self):
        return f"SmartPhone: CPU - {self._cpu}, Memory - {self._memory}, Sim Cards - {self._sim_cards_list}"


# Создание объектов
computer = Computer(cpu=5, memory=8)
phone = Phone()
smartphone1 = SmartPhone(cpu=5, memory=4)
smartphone2 = SmartPhone(cpu=5, memory=8)

# Распечатать информацию о созданных объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Опробовать методы
computer.make_computations()
phone.call(sim_card_number=1, call_to_number="+996 777 99 88 11")
smartphone1.use_gps(location="Home")

# Опробовать магические методы сравнения
print(smartphone1 > smartphone2)
print(smartphone1 == smartphone2)