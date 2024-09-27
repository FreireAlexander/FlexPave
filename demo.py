"""
FlexPave
version: 0.0.0-dev
description: Flexpave is a pavement design software

author: Freire Alexander Palomino Palma
email: freirealexander0214@gmail.com
"""
from parameters.materials import Material
from parameters.layers import Layer
from infrastructure.storage.persistence import save_material_to_xml, load_material_from_xml


def main():
    print("FlexPave")
    material = Material('Concrete', 5000, 'A')
    save_material_to_xml(material, 'material.xml')
    loaded_material = load_material_from_xml('material.xml')
    print(f"Material loaded: {loaded_material}")

    subgrade = Material("Existing Soil", 15874.5478, "subgrade")
    subgradeLayer = Layer(subgrade,'una simple convencion')
    print(f"Layers attributes: {subgradeLayer}")

if __name__ == "__main__":
    main()