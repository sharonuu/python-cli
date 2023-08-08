import pytest
from unittest.mock import patch, mock_open
from src.cli import main
from src.serializer import JsonSerializer, XmlSerializer
import json
from src.display import PlainTextDisplay


def test_basic_serialization_flow():
    test_args = ['your_script_name.py', 'input.json', 'output.xml', 'text']

    # Mock data
    data_content = {"key": "value"}
    
    # Mock reading and writing
    with patch('sys.argv', test_args), \
         patch('builtins.open', mock_open(read_data=json.dumps(data_content))) as mocked_file, \
         patch.object(JsonSerializer, 'read', return_value=data_content), \
         patch.object(XmlSerializer, 'write') as mock_write, \
         patch.object(PlainTextDisplay, 'print') as mock_print:
        
        main()

    # Check if the serializers and display methods were called
    mock_write.assert_called_once()
    mock_print.assert_called_once()
