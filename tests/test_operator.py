import sys

from calculate.controller import Operators

sys.path.append("..")


def test_simple_addition():
    op_obj = Operators()
    expression = "4.5 + 9.7"
    expect_result = 14.2
    assert op_obj.addition(expression) == expect_result, "Test simple addition A+B"


def test_multiple_addition():
    op_obj = Operators()
    expression = "4.5 + 3.4 + 23 + 45.5"
    expect_result = 76.4
    assert op_obj.addition(expression) == expect_result, "Test multiple addition"


def test_simple_subtraction():
    op_obj = Operators()
    expression = "45 - 13.4"
    expect_result = 31.6
    assert op_obj.substraction(expression) == expect_result, "Test simple subtraction"


def test_multiple_subtraction():
    op_obj = Operators()
    expression = "234-3-43-45-4"
    expect_result = 139
    assert op_obj.substraction(expression) == expect_result, "Test multiple subtraction"


def test_simple_multiplication():
    op_obj = Operators()
    expression = "30*2"
    expect_result = 60
    assert op_obj.multiplication(expression) == expect_result, "Test simple multiplication"


def test_multiple_multiplication():
    op_obj = Operators()
    expression = "3*45*10"
    expect_result = 1350
    assert op_obj.multiplication(expression) == expect_result, "Test multiple multiplication"


def test_simple_division():
    op_obj = Operators()
    expression = "15/2"
    expect_result = 7.5
    assert op_obj.division(expression) == expect_result, "Test simple division"


def test_multiple_division():
    op_obj = Operators()
    expression = "48/2/3"
    expect_result = 8
    assert op_obj.division(expression) == expect_result, "Test multiple division"


def test_expression_diff_operators():
    op_obj = Operators()
    expression = "40+2*3"
    expect_result = None
    assert op_obj.division(expression) == expect_result, "Test multiple division"


def test_division_zero():
    op_obj = Operators()
    expression = "40/0"
    expect_result = None
    assert op_obj.division(expression) == expect_result, "Test multiple division"


