import json
import xml.etree.ElementTree as ET
from src.serializer import JsonSerializer, XmlSerializer
from src.model import PersonalData


def test_json_serializer_write_read():
    data = [PersonalData("John Doe", "123 Elm St.", "123-456-7890")]
    
    serializer = JsonSerializer()
    with open('test_temp.json', 'w') as file:
        serializer.write(data, file)

    with open('test_temp.json', 'r') as file:
        read_data = serializer.read(file)
    
    assert len(read_data) == 1
    assert read_data[0].name == "John Doe"
    assert read_data[0].address == "123 Elm St."
    assert read_data[0].phone_number == "123-456-7890"

def test_xml_serializer_write_read():
    data = [PersonalData("John Doe", "123 Elm St.", "123-456-7890")]
    
    serializer = XmlSerializer()
    with open('test_temp.xml', 'w') as file:
        serializer.write(data, file)

    with open('test_temp.xml', 'r') as file:
        read_data = serializer.read(file)

    assert len(read_data) == 1
    assert read_data[0].name == "John Doe"
    assert read_data[0].address == "123 Elm St."
    assert read_data[0].phone_number == "123-456-7890"
