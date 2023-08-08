from abc import ABC, abstractmethod

from src.model import PersonalData

# display interface
class Display(ABC):
    @abstractmethod
    def print(self, data:PersonalData, display_file = None):
        pass

# implement plain text display
class PlainTextDisplay(Display):
    # def print(self, data:PersonalData):
        # print(f"Name: {data.name}\nAddress: {data.address}\nPhone: {data.phone_number}")
    def print(self, data_list, output_file=None):
        content = ""
        for data in data_list:
            content += f"Name: {data.name}\nAddress: {data.address}\nPhone: {data.phone_number}\n\n"
        
        # If output_file is provided, write to the file
        if output_file:
            with open(output_file, 'w') as file:
                file.write(content)
        else:
            print(content)


# implement HTML display
class HtmlDisplay(Display):
    def print(self, data_list, output_file=None):
        content = "<table>"

        # header
        content += "<tr>"
        for key in ["Name", "Address", "Phone"]:
            content += f"<th>{key}</th>"
        content += "</tr>"

        # data rows
        for data in data_list:
            content += "<tr>"
            for value in [data.name, data.address, data.phone_number]:
                content += f"<td>{value}</td>"
            content += "</tr>"

        content += "</table>"

        # If output_file is provided, write to the file
        if output_file:
            with open(output_file, 'w') as file:
                file.write(content)
        else:
            print(content)