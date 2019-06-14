#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pytest
# from petri_dish import *
from petri_dish_solution import *
from petri_dish_solution import reset_all_cell_counts as RA


def test_activity1_task1a():
    petri_dish = activity1_task1a()
    assert petri_dish.SIZE == 5


def test_activity1_task1b():
    petri_dish = activity1_task1b()
    assert petri_dish.SIZE == 10


def test_activity1_task1c():
    petri_dish = activity1_task1c()
    assert petri_dish.SIZE == 20


def test_activity1_task1d():
    petri_dish = activity1_task1d()
    assert petri_dish.SIZE == 30


def test_activity1_task2a():
    petri_dish = activity1_task2a()
    assert petri_dish.SIZE == 30
    assert petri_dish.all_cells[-1].symbol == 'c'
    assert petri_dish.all_cells[-1].x == 0
    assert petri_dish.all_cells[-1].y == 0
    with open('activity1_task2a.txt', 'r') as f:
        assert f.read() == str(petri_dish)


def test_activity1_task2b():
    petri_dish = activity1_task2b()
    with open('activity1_task2b.txt', 'r') as f:
        assert f.read() == str(petri_dish)


def test_activity1_task2c():
    petri_dish = activity1_task2c()
    with open('activity1_task2c.txt', 'r') as f:
        assert f.read() == str(petri_dish)


def test_activity1_task3():
    petri_dish = activity1_task3()
    with open('activity1_task3.txt', 'r') as f:
        assert f.read() == str(petri_dish)



def test_activity2_task1():
    petri_dish = activity2_task1()
    with open('activity2_task1.txt', 'r') as f:
        assert f.read() == str(petri_dish)


def test_activity2_task2():
    petri_dish = activity2_task2()
    with open('activity2_task2.txt', 'r') as f:
        assert f.read() == str(petri_dish)


def test_activity2_task3():
    petri_dish = activity2_task3()
    with open('activity2_task3.txt', 'r') as f:
        assert f.read() == str(petri_dish)


def test_activity2_task4():
    petri_dish = activity2_task4()
    with open('activity2_task4.txt', 'r') as f:
        assert f.read() == str(petri_dish)


def test_activity2_task5():
    petri_dish = activity2_task5()
    with open('activity2_task5.txt', 'r') as f:
        assert f.read() == str(petri_dish)



def test_activity3_task1():
    RA()
    result = list(activity3_task1())
    assert result == [60,10,20,0,30]


def test_activity3_task2a():
    RA()
    result = list(activity3_task2a())
    assert result == [120,20, 40, 0, 60]


def test_activity3_task2b():
    RA()
    result = list(activity3_task2b())
    assert result == [60,10,20,0,30]


def test_activity3_task3():
    RA()
    result = list(activity3_task3())
    assert result == [50, 5, 15, 0, 30]


def test_activity3_task4():
    RA()
    petri_dish, list_of_cells = activity3_task4()
    with open('activity3_task4.txt', 'r') as f:
        assert f.read() == str(petri_dish)
    assert list_of_cells == [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 6, 6, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349, 349]


def test_activity3_task5():
    RA()
    petri_dish = activity3_task5()
    with open('activity3_task5.txt', 'r') as f:
        assert f.read() == str(petri_dish)

