from src.calculator.utils import parse_to_number

def test_parse_to_number_integer():
    result = parse_to_number('30')
    assert result == 30
    
def test_parse_to_number_float():
    result = parse_to_number('30.4')
    assert result == 30.4