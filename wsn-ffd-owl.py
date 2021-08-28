from rdflib import Graph
from rdflib.term import URIRef, Literal
from rdflib.namespace import Namespace, RDF, RDFS
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

    SOSA: Namespace = Namespace('http://www.w3.org/ns/sosa/')
    wsd_ffd_owl.bind('sosa', SOSA)

    # owl:imports 'https://wsn-ffd-rdf.org/' --> in realtà metto il link alla ontologia sul repo gitlab
    my_ontology_uri = 'https://gitlab.com/paganelli.f/ws-project-paganelli-2021/-/raw/develop/wsd-ffd-pretty-xml.rdf'

    ontology = URIRef(value='wsn-mas-ontology', base=base_ontology)
    wsd_ffd_owl.add((ontology, RDF.type, OWL.Ontology))
    wsd_ffd_owl.add((ontology, OWL.versionInfo, Literal('1.0')))
    wsd_ffd_owl.add((ontology, OWL.imports, URIRef(value=my_ontology_uri)))

    ##############################
    # Class Definition
    ##############################
    router_node_1 = URIRef(value='RouterNode', base=base_ontology)
    wsd_ffd_owl.add((router_node_1, RDF.type, OWL.Class))
    wsd_ffd_owl.add((router_node_1, RDFS.comment, Literal('Router node of the wireless sensor network')))
    wsd_ffd_owl.add((router_node_1, RDFS.subClassOf, SOSA.Platform))

    # definire router e coordinator nodes
    # definire/estendere agenti

    ##############################
    # Property Definition
    ##############################

    # definire proprietà per nodo router e coordinator
    # definire altre proprietà per gli agenti
    # aggiungere proprietà alle classi rdf??
    # fare esempi di proprietà inverse di alcune proprietà definite nel precedente RDF owl:inverseOf

    ##############################
    # Instance Definition
    ##############################

    # definire alcune istanze di router, altre istanze di edgenode ed un coordinator
    # e alcune istanze di agenti/containerAgent, ...
    # costruendo la rete wsn-mas finale

    ##############################
    # RDF Serialization
    ##############################
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-xml-owl.rdf', format='xml')
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-pretty-xml-owl.rdf', format='pretty-xml')
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-turtle-owl.ttl', format='turtle')
