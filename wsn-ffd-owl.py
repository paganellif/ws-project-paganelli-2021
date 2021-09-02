from rdflib import Graph
from rdflib.term import URIRef, Literal, BNode
from rdflib.namespace import Namespace, RDF, RDFS
import os

if __name__ == '__main__':

    ##############################
    # Graph Definition
    ##############################
    wsd_ffd_owl: Graph = Graph()
    gitlab_repo_base_uri: str = 'https://gitlab.com/paganelli.f/sd-project-paganelli-1920/-/'
    # owl:imports 'https://wsn-ffd-rdf.org/' --> in realtà metto il link alla ontologia sul repo gitlab
    base_rdf_ontology_uri: str = gitlab_repo_base_uri + 'raw/develop/wsd-ffd-pretty-xml.rdf'
    base_rdf_ontology: str = 'https://wsn-ffd-rdf.org/'
    base_owl_ontology: str = 'https://wsn-ffd-owl.org/'

    ##############################
    # Binding/Import Namespaces
    ##############################
    OWL: Namespace = Namespace('http://www.w3.org/2002/07/owl#')
    wsd_ffd_owl.bind('owl', OWL)

    SOSA: Namespace = Namespace('http://www.w3.org/ns/sosa/')
    wsd_ffd_owl.bind('sosa', SOSA)

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
    wsd_ffd_owl.add((router_node, OWL.disjointWith, URIRef(value='EdgeDevice', base=base_rdf_ontology)))
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
    wsd_ffd_owl.add((statistics_agent, OWL.disjointWith, URIRef(value='DBManagerAgent', base=base_owl_ontology)))
    wsd_ffd_owl.add((statistics_agent, OWL.disjointWith, URIRef(value='FrontEndAgent', base=base_owl_ontology)))
    wsd_ffd_owl.add((statistics_agent, OWL.disjointWith, URIRef(value='SensorAgent', base=base_rdf_ontology)))
    wsd_ffd_owl.add((statistics_agent, RDFS.seeAlso,
                     URIRef(value=gitlab_repo_base_uri+'blob/master/processing/statisticsagent.py'))
                    )
    wsd_ffd_owl.add((statistics_agent, RDFS.subClassOf, URIRef(value='Agent', base=base_rdf_ontology)))

    dbmanager_agent = URIRef(value='DBManagerAgent', base=base_owl_ontology)
    wsd_ffd_owl.add((dbmanager_agent, RDF.type, OWL.Class))
    wsd_ffd_owl.add((dbmanager_agent, RDFS.comment, Literal('MAS DBManager Agent')))
    wsd_ffd_owl.add((dbmanager_agent, OWL.disjointWith, URIRef(value='FrontEndAgent', base=base_owl_ontology)))
    wsd_ffd_owl.add((dbmanager_agent, OWL.disjointWith, URIRef(value='StatisticsAgent', base=base_owl_ontology)))
    wsd_ffd_owl.add((dbmanager_agent, OWL.disjointWith, URIRef(value='SensorAgent', base=base_rdf_ontology)))
    wsd_ffd_owl.add((dbmanager_agent, RDFS.seeAlso,
                     URIRef(value=gitlab_repo_base_uri+'blob/master/processing/dbmanageragent.py'))
                    )
    wsd_ffd_owl.add((dbmanager_agent, RDFS.subClassOf, URIRef(value='Agent', base=base_rdf_ontology)))

    frontend_agent = URIRef(value='FrontEndAgent', base=base_owl_ontology)
    wsd_ffd_owl.add((frontend_agent, RDF.type, OWL.Class))
    wsd_ffd_owl.add((frontend_agent, RDFS.comment, Literal('MAS FrontEnd Agent')))
    wsd_ffd_owl.add((frontend_agent, OWL.disjointWith, URIRef(value='DBManagerAgent', base=base_owl_ontology)))
    wsd_ffd_owl.add((frontend_agent, OWL.disjointWith, URIRef(value='StatisticsAgent', base=base_owl_ontology)))
    wsd_ffd_owl.add((frontend_agent, OWL.disjointWith, URIRef(value='SensorAgent', base=base_rdf_ontology)))
    wsd_ffd_owl.add((frontend_agent, RDFS.seeAlso,
                     URIRef(value=gitlab_repo_base_uri+'blob/master/processing/frontendagent.py'))
                    )
    wsd_ffd_owl.add((frontend_agent, RDFS.subClassOf, URIRef(value='Agent', base=base_rdf_ontology)))

    ##############################
    # Property Definition
    ##############################

    # definire proprietà per nodo router e coordinator
    # definire altre proprietà per gli agenti
    # aggiungere proprietà alle classi rdf??

    can_route = URIRef(value='canRoute', base=base_owl_ontology)
    wsd_ffd_owl.add((can_route, RDF.type, OWL.ObjectProperty))
    wsd_ffd_owl.add((can_route, RDFS.comment, Literal('List of nodes to which this node is able to route information')))
    wsd_ffd_owl.add((can_route, OWL.inverseOf, URIRef(value='isRoutedBy', base=base_rdf_ontology)))
    wsd_ffd_owl.add((can_route, RDFS.domain, router_node))
    wsd_ffd_owl.add((can_route, RDFS.range, SOSA.Platform))

    is_hosted_by = URIRef(value='isHostedBy', base=base_owl_ontology)
    wsd_ffd_owl.add((is_hosted_by, RDF.type, OWL.ObjectProperty))
    wsd_ffd_owl.add((is_hosted_by, RDFS.comment, Literal('WSN Node that hosts this Agent Container')))
    wsd_ffd_owl.add((is_hosted_by, OWL.inverseOf, URIRef(value='hostsAgentContainer', base=base_rdf_ontology)))
    wsd_ffd_owl.add((is_hosted_by, RDFS.domain, URIRef(value='AgentContainer', base=base_rdf_ontology)))
    wsd_ffd_owl.add((is_hosted_by, RDFS.range, SOSA.Platform))

    collect_metrics_from = URIRef(value='collectMetricsFrom', base=base_owl_ontology)
    wsd_ffd_owl.add((collect_metrics_from, RDF.type, OWL.ObjectProperty))
    wsd_ffd_owl.add((collect_metrics_from, RDFS.comment,
                     Literal('Sensor Agents from which the DBManager Agent collects the detected data')))
    wsd_ffd_owl.add((collect_metrics_from, RDFS.domain, dbmanager_agent))
    wsd_ffd_owl.add((collect_metrics_from, RDFS.range, URIRef(value='#SensorAgent', base=base_rdf_ontology)))

    metrics_collected_by = URIRef(value='metricsCollectedBy', base=base_owl_ontology)
    wsd_ffd_owl.add((metrics_collected_by, RDF.type, OWL.ObjectProperty))
    wsd_ffd_owl.add((metrics_collected_by, RDFS.comment,
                     Literal('DBManager Agent that collects the data detected from this Sensor Agent')))
    wsd_ffd_owl.add((metrics_collected_by, RDFS.domain, URIRef(value='#SensorAgent', base=base_rdf_ontology)))
    wsd_ffd_owl.add((metrics_collected_by, RDFS.range, dbmanager_agent))
    wsd_ffd_owl.add((metrics_collected_by, OWL.inverseOf, URIRef(value='#collectMetricsFrom', base=base_owl_ontology)))

    max_cardinality_restriction = BNode()
    wsd_ffd_owl.add((max_cardinality_restriction, RDF.type, OWL.Restriction))
    wsd_ffd_owl.add((max_cardinality_restriction, OWL.maxCardinality, Literal(1)))
    wsd_ffd_owl.add((max_cardinality_restriction, OWL.onProperty,
                     URIRef(value='#metricsCollectedBy', base=base_owl_ontology)))

    wsd_ffd_owl.add((URIRef(value='SensorAgent', base=base_rdf_ontology), RDFS.subClassOf, max_cardinality_restriction))

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
