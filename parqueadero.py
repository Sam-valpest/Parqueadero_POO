from abc import ABC, abstractmethod
from datetime import datetime
from math import ceil
import re

class Vehiculo(ABC):

    def __init__(self, placa, propietario):
        super().__init__()
        self.placa = placa
        self.propietario = propietario

    def set_placa(self, valor):
        valor = valor.replace(" ", "").upper()

        if not re.fullmatch(r"[A-Z]{3}\d{2}[A-Z0-9]", valor):
            raise ValueError(f"Placa invalida: {valor}")
        self.__placa = valor

    @staticmethod
    def horas_a_cobrar(minutos):
        return max(1, ceil(minutos / 60))

    @staticmethod
    def cobro_con_tope(horas, tarifa, tope):
        dias, horas_restantes = divmod(horas, 24)

        return dias * tope + min(horas_restantes * tarifa, tope)

    @abstractmethod
    def calcular_cobro(self, horas):
        pass

    def __repr__(self):
        return super().__repr__()
    
    


class Carro(Vehiculo):

    TARIFA_HORA = 4000
    TOPE_DIARIO = 30000

    def __init__(self, placa, propietario):
        super().__init__(placa, propietario)

    def calcular_cobro(self, horas):
        return self.cobro_con_tope(horas, self.TARIFA_HORA, self.TOPE_DIARIO)

class Moto(Vehiculo):

    TARIFA_HORA = 2000
    TOPE_DIARIO = 12000

    def __init__(self, placa, propietario):
        super().__init__(placa, propietario)

    def calcular_cobro(self, horas):
        return self.cobro_con_tope(horas, self.TARIFA_HORA, self.TOPE_DIARIO)

class Camion(Vehiculo):

    TARIFA_HORA = 8000
    RECARGO_FIJO = 5000

    def __init__(self, placa, propietario):
        super().__init__(placa, propietario)

    def calcular_cobro(self, horas):
        return horas * self.TARIFA_HORA + self.RECARGO_FIJO


class Parqueadero:
    def __init__(self, nombre, capacidad):
        if capacidad <= 0:
            raise ValueError("")
        self.nombre = nombre
        self.__capacidad = capacidad
        self.__dentro = {}
        self.__recaudo = 0

    @property
    
        

mazda = Carro("PBK25G", "andres")
nkd = Moto("HGT58H", "Samuel")
mula = Camion("HIO75G", "Karol")

print(nkd.calcular_cobro(26))
print(mazda.calcular_cobro(26))
print(mula.calcular_cobro(26))