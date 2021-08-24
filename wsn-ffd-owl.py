from rdflib import Graph
from rdflib.container import Bag
from rdflib.term import BNode, URIRef, Literal
from rdflib.namespace import Namespace, RDFS, RDF, OWL
import os

if __name__ == '__main__':

    ##############################
    # Graph Definition
    ##############################
    wsd_ffd_owl: Graph = Graph()
    base_ontology: str = 'https://wsn-ffd-owl.org/'

    # owl:imports 'https://wsn-ffd-rdf.org/' --> in realtà metto il link alla ontologia sul repo gitlab
    # che magari la scarica davvero
    # https://gitlab.com/paganelli.f/ws-project-paganelli-2021/-/raw/develop/wsd-ffd-pretty-xml.rdf

    # fare esempi di proprietà inverse di alcune proprietà definite nel precedente RDF
    # owl:inverseOf


