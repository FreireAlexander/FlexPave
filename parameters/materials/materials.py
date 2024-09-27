from uuid import uuid4

class Material():
    """
    Material class definition

    Attributes:
    - name              str
    - elasticModule     float

    protected:
    - id
    - classification
    """
    __slots__ = ('_id', 'name', '_classification', 'elasticModule')

    def __init__(self,
                 name: str, 
                 elasticModule: float = 0, 
                 classification: str = 'null'
                 ):
        self._id = uuid4()
        self.name = name
        self._classification = classification
        self.elasticModule = elasticModule
        


    def __str__(self) -> str:
        json = {
            'id': self.id,
            'name': self.name,
            'classification': self.classification,
            'elastic module': self.elasticModule
        }
        return str(json)

    @property
    def classification(self):
        return self._classification


    def setClassification(self, classification: str):
        self._classification = classification


    @property
    def id(self):
        return self._id
    

    def setId(self, value):
        self._id = value



def main():
    material = Material('New Material')
    print(f"New Material created {material}")


if __name__ == "__main__":
    main()