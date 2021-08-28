from rdflib import Graph
from rdflib.term import URIRef, Literal
from rdflib.namespace import Namespace, RDF, RDFS
import os

if __name__ == '__main__':

    ##############################
    # Graph Definition
    ##############################
    wsd_ffd_owl: Graph = Graph()
    base_rdf_ontology: str = 'https://wsn-ffd-rdf.org/'
    base_owl_ontology: str = 'https://wsn-ffd-owl.org/'

    ##############################
    # Binding/Import Namespaces
    ##############################
    OWL: Namespace = Namespace('http://www.w3.org/2002/07/owl#')
    wsd_ffd_owl.bind('owl', OWL)

    SOSA: Namespace = Namespace('http://www.w3.org/ns/sosa/')
    wsd_ffd_owl.bind('sosa', SOSA)

    # owl:imports 'https://wsn-ffd-rdf.org/' --> in realtà metto il link alla ontologia sul repo gitlab
    base_rdf_ontology_uri = 'https://gitlab.com/paganelli.f/ws-project-paganelli-2021/-/raw/develop/wsd-ffd-pretty-xml.rdf'

    ontology = URIRef(value='wsn-mas-ontology', base=base_owl_ontology)
    wsd_ffd_owl.add((ontology, RDF.type, OWL.Ontology))
    wsd_ffd_owl.add((ontology, OWL.versionInfo, Literal('1.0')))
    wsd_ffd_owl.add((ontology, OWL.imports, URIRef(value=base_rdf_ontology_uri)))

    ##############################
    # Class Definition
    ##############################
    # WSN
    router_node = URIRef(value='RouterNode', base=base_owl_ontology)
    wsd_ffd_owl.add((router_node, RDF.type, OWL.Class))
    wsd_ffd_owl.add((router_node, RDFS.comment, Literal('Router node of the wireless sensor network')))
    wsd_ffd_owl.add((router_node, RDFS.subClassOf, SOSA.Platform))

    coordinator_node = URIRef(value='CoordinatorNode', base=base_owl_ontology)
    wsd_ffd_owl.add((coordinator_node, RDF.type, OWL.Class))
    wsd_ffd_owl.add((coordinator_node, RDFS.comment,
                     Literal('Coordinator/Gateway node of the wireless sensor network'))
                    )
    wsd_ffd_owl.add((coordinator_node, RDFS.subClassOf, router_node))

    # MAS
    statistics_agent = URIRef(value='StatisticsAgent', base=base_owl_ontology)
    wsd_ffd_owl.add((statistics_agent, RDF.type, OWL.Class))
    wsd_ffd_owl.add((statistics_agent, RDFS.comment, Literal('MAS Statistics Agent')))
    wsd_ffd_owl.add((statistics_agent, RDFS.seeAlso, URIRef(value='https://gitlab.com/paganelli.f/sd-project-paganelli-1920/-/blob/master/processing/statisticsagent.py')))
    wsd_ffd_owl.add((statistics_agent, RDFS.subClassOf, URIRef(value='Agent', base=base_rdf_ontology)))

    dbmanager_agent = URIRef(value='DBManagerAgent', base=base_owl_ontology)
    wsd_ffd_owl.add((dbmanager_agent, RDF.type, OWL.Class))
    wsd_ffd_owl.add((dbmanager_agent, RDFS.comment, Literal('MAS DBManager Agent')))
    wsd_ffd_owl.add((dbmanager_agent, RDFS.seeAlso, URIRef(value='https://gitlab.com/paganelli.f/sd-project-paganelli-1920/-/blob/master/processing/dbmanageragent.py')))
    wsd_ffd_owl.add((dbmanager_agent, RDFS.subClassOf, URIRef(value='Agent', base=base_rdf_ontology)))

    frontend_agent = URIRef(value='FrontEndAgent', base=base_owl_ontology)
    wsd_ffd_owl.add((frontend_agent, RDF.type, OWL.Class))
    wsd_ffd_owl.add((frontend_agent, RDFS.comment, Literal('MAS FrontEnd Agent')))
    wsd_ffd_owl.add((frontend_agent, RDFS.seeAlso, URIRef(
        value='https://gitlab.com/paganelli.f/sd-project-paganelli-1920/-/blob/master/processing/dbmanageragent.py')))
    wsd_ffd_owl.add((frontend_agent, RDFS.subClassOf, URIRef(value='Agent', base=base_rdf_ontology)))



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
