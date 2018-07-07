import pytest
from main import initializeGraph, getRouteCost, findShortestPath


def setup():
    return initializeGraph()


def test_route_cost_1():
    graph = setup()
    assert getRouteCost(graph, 'A-B-C') == 9

def test_route_cost_2():
    graph = setup()
    assert getRouteCost(graph, 'A-D') == 5

def test_route_cost_3():
    graph = setup()
    assert getRouteCost(graph, 'A-D-C') == 13

def test_route_cost_4():
    graph = setup()
    assert getRouteCost(graph, 'A-E-B-C-D') == 22

def test_route_cost_5():
    graph = setup()
    assert getRouteCost(graph, 'A-E-D') == 'NO SUCH ROUTE'

def test_shortest_path_1():
    graph = setup()
    assert findShortestPath(graph, 'A', 'C', visited=[], costs={}, lastVisited={}) == 9

    def test_shortest_path_1():
        graph = setup()
        assert findShortestPath(graph, 'B', 'B', visited=[], costs={}, lastVisited={})==0

