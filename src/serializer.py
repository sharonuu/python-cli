from abc import ABC, abstractmethod
import json
from src.model import PersonalData
import xml.etree.ElementTree as ET


# Serializer interface
class Serializer(ABC):
    @abstractmethod
    def write(self, data, file):
        pass

    @abstractmethod
    def read(self, file):
        pass

# Implement Json formatter
class JsonSerializer(Serializer):
    def write(self, data, file):
        json_data = [item.to_dict() for item in data]
        json.dump(json_data, file)

    def read(self, file):
        data_list = json.load(file)
        return [PersonalData.from_dict(item) for item in data_list]

# Implement XML serializer  
class XmlSerializer(Serializer):
    def write(self, data_list, file):
        root = ET.Element("persons")
        
        for data in data_list:
            person = ET.SubElement(root, "person")
            ET.SubElement(person, "name").text = data.name
            ET.SubElement(person, "address").text = data.address
            ET.SubElement(person, "phone_number").text = data.phone_number

        tree = ET.ElementTree(root)
        tree.write(file, encoding="unicode")


    def read(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        
        data_list = []

        for person in root.findall('person'):
            data = PersonalData(
                person.find("name").text,
                person.find("address").text,
                person.find("phone_number").text
            )
            data_list.append(data)

        return data_list