from rdflib import Graph
from rdflib.term import BNode, URIRef, Literal


def set_operating_power_range(graph: Graph, system_instance: URIRef, min_val: float, max_val: float, qudt_unit):
    temp_bnode = BNode()
    graph.add((temp_bnode, graph.namespaces()['SCHEMA'].minValue, Literal(min_val)))
    graph.add((temp_bnode, graph.namespaces()['SCHEMA'].maxValue, Literal(max_val)))
    graph.add((temp_bnode, graph.namespaces()['SCHEMA'].unitCode, qudt_unit))
    graph.add((system_instance, graph.namespaces()['SSN-SYSTEM'].OperatingPowerRange, temp_bnode))
