from operator import truediv
import pytest

# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine
from IcecreamMachine import STAGE
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm

@pytest.fixture
def first_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay("2.00","2.00")
    return machine

@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay("2.00","2.00")
    return machine

def test_production_line(second_order):
    assert second_order is not None

# My ucid is ar2576 and all the eight test cases was passed on 10/23/2022
def test_case_three(machine):
    if machine.remaining_toppings <= 0:
        assert False
    assert True

def test_case_one(machine):
    if machine.currently_selecting != STAGE.Container:
        assert False
    else:
        assert True

def test_case_two(machine):
    if machine.remaining_uses <= 0:
        assert False
    else:
        assert True

def test_case_four(machine):
    if machine.remaining_scoops <= 0:
        assert False
    else:
        assert True

def test_case_six(machine):
  cost = machine.calculate_cost('sugar cone',['strawberry','chocolate','next'],['peanuts','done'])
  assert cost == 3.25

  cost = machine.calculate_cost('cup',['vanilla','next'],['done'])
  assert cost == 2.0

  cost = machine.calculate_cost('waffle cone','next','done')
  assert cost == 1.5

  cost = machine.calculate_cost('cup',['strawberry','vanilla','chocolate','next'],['m&ms','gummy bears','done'])
  assert cost == 4.50

def test_case_seven(machine):
  cost = machine.calculate_cost('waffle cone',['chocolate','next'],'done')
  machine.handle_pay(cost,'2.5')

  cost = machine.calculate_cost('cup','next','done')
  machine.handle_pay(cost,'1')

  cost = machine.calculate_cost('sugar cone',['vanilla','chocolate','strawberry','next'],['peanuts','m&ms','sprinkles'])
  machine.handle_pay(cost, '4.75')

  assert machine.total_sales == 8.25

def test_case_eight(machine):
    cost = machine.calculate_cost('cup',['vanilla','strawberry','next'],'done')
    machine.handle_pay(cost,'3')

    cost = machine.calculate_cost('waffle cone',['chocolate','next'],['peanuts','m&ms','done'])
    machine.handle_pay(cost,'3.0')

    cost = machine.calculate_cost('sugar cone','next','done')
    machine.handle_pay(cost,'1')

    assert machine.total_icecreams == 3

def test_case_five(machine):
    if machine.remaining_toppings <= 3:
        assert True
    else:
        assert False
