import xml.etree.ElementTree as ET
from parameters.materials.materials import Material
from uuid import uuid4

def save_material_to_xml(material: Material, filename: str):
    material_element = ET.Element("Material")
    ET.SubElement(material_element, "ID").text = str(material.id)
    ET.SubElement(material_element, "Name").text = material.name
    ET.SubElement(material_element, "Classification").text = material.classification
    ET.SubElement(material_element, "ElasticModule").text = str(material.elasticModule)

    tree = ET.ElementTree(material_element)
    tree.write(filename)

def load_material_from_xml(filename: str) -> Material:
    tree = ET.parse(filename)
    root = tree.getroot()

    material = Material(
        name=root.find("Name").text, 
        elasticModule=float(root.find("ElasticModule").text), 
        classification=root.find("Classification").text
    )
    material.setId(uuid4())  # Igual que antes, puedes guardar el UUID si lo prefieres
    return material
