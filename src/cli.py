'''
    provides the format manager cli
'''

import argparse
from src.display import HtmlDisplay, PlainTextDisplay
from src.serializer import JsonSerializer, XmlSerializer


SERIALIZER_FORMAT = {
    'json' : JsonSerializer,
    'xml' : XmlSerializer
}


DISPLAY_METHODS = {
    'text': PlainTextDisplay,
    'html': HtmlDisplay
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", nargs='?', default=None)  # Made this and next two arguments optional
    parser.add_argument("output_file", nargs='?', default=None)
    parser.add_argument("display", choices=DISPLAY_METHODS.keys(), nargs='?', default=None)
    parser.add_argument("display_output", nargs='?', default=None, help="Output file for display results. If not provided, results will print to console.")
    parser.add_argument("--formats", action="store_true", help="List supported formats")
    args = parser.parse_args()

    if args.formats:
        print("Supported formats:")
        for key in SERIALIZER_FORMAT.keys():
            print(key)
        exit(0)

    # if not args.input_file or not args.output_file or not args.display:
    #     print("Error: Missing required arguments. Use --help for usage info.")
    #     exit(1)

    input_format = str(args.input_file).split('.')[-1]
    output_format  =  str(args.output_file).split('.')[-1]

    # read
    with open(args.input_file, 'r') as file:
        data = SERIALIZER_FORMAT[input_format]().read(file)
    
    # write
    with open(args.output_file, 'w') as file:
        SERIALIZER_FORMAT[output_format]().write(data, file)

    DISPLAY_METHODS[args.display]().print(data, args.display_output)

if __name__ == "__main__":
    main()
    

            