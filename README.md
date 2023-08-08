## **Introduction**
This project provides a command-line tool designed to serialize and deserialize personal data in multiple formats, including JSON and XML. Moreover, it offers various display options, either as plain text or in an HTML layout, to the console or saved as an output file.

## **Project Structure**

- `serializer.py`: This houses the serialization interfaces and implementations for JSON and XML formats.
- `display.py`: Here, you'll find display interfaces and implementations for output in plain text and HTML.
- `cli.py`: The tool's main driver script, which uses the argparse module for command-line argument parsing and effectively binds functions from the serializer and display modules.

### **Serializer**

#### `JsonSerializer`

- **write**: Transforms a \`PersonalData\` object into JSON and writes it to a file.
- **read**: Reads from a JSON file and returns the data as a \`PersonalData\` object.

#### `XmlSerializer`

- **write**: Converts a \`PersonalData\` object into XML format and commits it to a file.
- **read**: Ingests data from an XML file and delivers it as a \`PersonalData\` object.

### **Display**

#### `PlainTextDisplay`

- **print**: Exposes personal data in a plain text format.

#### `HtmlDisplay`

- **print**: Represents the personal data in a neat HTML table.

## **Usage**

To use the tool, invoke it from the command line with the following syntax:
```bash
python cli.py [input_file] [output_file] [display] [display_output]
```

**Arguments**:
- `input_file`: Path pointing to the source data file.
- `output_file`: Destination path where serialized data will be stored.
- `display`: Chosen method to showcase data (`text` or `html`).
- `display_output`: (Optional) Specified path to save the display's output.

To enumerate supported formats, use:
```bash
python cli.py --formats
```

## **Mock Data**
Provided mock data sets in both JSON and XML formats to test and demonstrate the tool's functionality.
