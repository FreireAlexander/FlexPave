from uuid import uuid4

class Weather():
    """
    Weather conditions
    """

    def __init__(self):
        self.__UUID = uuid4()
        self._temperature = ''
    

    def __str__(self) -> str:
        json = {
            'UUID': self.UUID,
            'temperature': self.temperature
        }
        return str(json)
    
    
    @property
    def UUID(self):
        return self.__UUID
    
    
    def setUUID(self, value):
        self.__UUID = value
        

    @property
    def temperature(self):
        return self._temperature


    def setTemperature(self, value):
        self._temperature = value


def main():
    weather = Weather()
    weather.setTemperature(25)
    print(f"Hola Clima {weather}\n temperature = {weather.temperature}")


if __name__ == "__main__":
    main()