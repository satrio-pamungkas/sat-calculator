from src.calculator.operation import Operation

def test_addition():
    ops = Operation(3,4)
    result = ops.addition()
    assert result == 7
    
def test_subtraction():
    ops = Operation(7,2)
    result = ops.subtraction()
    assert result == 5
    
def test_multiplication():
    ops = Operation(5,2)
    result = ops.multiplication()
    assert result == 10
    
def test_division():
    ops = Operation(10,2)
    result = ops.division()
    assert result == 5
