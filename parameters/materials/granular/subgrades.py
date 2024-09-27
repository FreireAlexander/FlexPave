from layers import Layer
from math import inf


class Subgrade(Layer):

    def __init__(self, material: None) -> None:
        super().__init__(material, inf)



def main():
    subgrade = Subgrade("Terreno Natural")
    print(f"Layers attributes: {subgrade}")


if __name__ == "__main__":
    main()