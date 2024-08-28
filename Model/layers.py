from uuid import uuid4
from typing import TypeAlias

Material: TypeAlias = None

class Layer():
    """
    Layer
    - material -> Material 
    - thickness -> float
    """

    def __init__(self, material: Material, thickness: float=0) -> None:
        self.__UUID = uuid4()
        self.material = material
        self.thickness = thickness


    def __str__(self) -> str:
        json = {
            'UUID': self.UUID, 
            'material': self.material,
            'thickness': self.thickness
        }
        return str(json)
    

    @property
    def UUID(self):
        return self.__UUID
    
    @UUID.setter
    def setUUID(self, value):
        self.__UUID = value



def main():
    subgrade = Layer('holis','una simple convencion')
    print(f"Layers attributes: {subgrade}")



if __name__ == "__main__":
    main()