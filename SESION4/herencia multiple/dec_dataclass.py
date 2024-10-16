

from dataclasses import dataclass
from typing import Any

@dataclass
class Vehiculo:
    marca : Any
    color : Any
    
auto = Vehiculo(2,5)
auto2 = Vehiculo(2,5)

print(auto == auto2)