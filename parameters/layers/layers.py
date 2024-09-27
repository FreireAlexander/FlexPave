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
        self._id = uuid4()
        self.material = material
        self.thickness = thickness


    def __str__(self) -> str:
        json = {
            'UUID': self.id, 
            'material': self.material,
            'thickness': self.thickness
        }
        return str(json)
    

    @property
    def id(self):
        return self._id
    
    @id.setter
    def setUUID(self, value):
        self._id = value



def main():
    print("Layers.py")


if __name__ == "__main__":
    main()