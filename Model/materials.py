from uuid import uuid4, uuid1

class Material():
    """
    Material class definition

    Attributes:
    - name              str
    - elasticModule     float

    protected:
    - UUID
    - classification
    """
    
    def __init__(self,
                 name: str, 
                 elasticModule: float, 
                 classification: str = 'null'
                 ):
        self.name = name
        self.__classification = classification
        self.ElasticModule = elasticModule
        self.__UUID = uuid4()

    def __str__(self) -> str:
        json = {
            'UUID': self.UUID,
            'name': self.name,
            'classification': self.classification,
            'elastic Module': self.ElasticModule

        }
        return str(json)

    @property
    def classification(self):
        return self.__classification

    def setClassification(self, classification: str):
        self.__classification = classification


    @property
    def UUID(self):
        return self.__UUID
    
    def setUUID(self, value):
        self.__UUID = value



def main():
    
    asphalt = Material("asphalt",125000)
    print(f"Material {asphalt.UUID} and Elastic Module {asphalt.ElasticModule}")
    asphalt.__UUID = 0
    print(f"new UUID {asphalt.UUID}")
    asphalt.setUUID(15000)
    print(f"new UUID {asphalt.UUID}")
    print(f"asphalt classification is {asphalt.classification}")
    print(f"Asphalt material {asphalt}")

if __name__ == "__main__":
    main()