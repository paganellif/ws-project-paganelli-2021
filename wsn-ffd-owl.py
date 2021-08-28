from rdflib import Graph
from rdflib.term import URIRef, Literal, BNode
from rdflib.namespace import Namespace, RDF
import os

if __name__ == '__main__':

    ##############################
    # Graph Definition
    ##############################
    wsd_ffd_owl: Graph = Graph()
    base_ontology: str = 'https://wsn-ffd-owl.org/'

    ##############################
    # Binding/Import Namespaces
    ##############################
    OWL: Namespace = Namespace('http://www.w3.org/2002/07/owl#')
    wsd_ffd_owl.bind('owl', OWL)

    # owl:imports 'https://wsn-ffd-rdf.org/' --> in realtà metto il link alla ontologia sul repo gitlab
    my_ontology_uri = 'https://gitlab.com/paganelli.f/ws-project-paganelli-2021/-/raw/develop/wsd-ffd-pretty-xml.rdf'

    ontology = URIRef(value='wsn-mas-ontology', base=base_ontology)
    wsd_ffd_owl.add((ontology, RDF.type, OWL.Ontology))
    wsd_ffd_owl.add((ontology, OWL.versionInfo, Literal('1.0')))
    wsd_ffd_owl.add((ontology, OWL.imports, URIRef(value=my_ontology_uri)))


    # fare esempi di proprietà inverse di alcune proprietà definite nel precedente RDF
    # owl:inverseOf


    ##############################
    # RDF Serialization
    ##############################
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-xml-owl.rdf', format='xml')
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-pretty-xml-owl.rdf', format='pretty-xml')
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-turtle-owl.ttl', format='turtle')
