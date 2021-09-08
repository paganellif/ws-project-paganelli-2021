from rdflib import Graph
from rdflib.term import URIRef, Literal, BNode
from rdflib.container import BNode
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

    SSN: Namespace = Namespace('http://www.w3.org/ns/ssn/')
    wsd_ffd_owl.bind('ssn', SSN)

    SCHEMA: Namespace = Namespace('http://schema.org/')
    wsd_ffd_owl.bind('schema', SCHEMA)

    QUDT_UNIT: Namespace = Namespace('http://qudt.org/1.1/vocab/unit#')
    wsd_ffd_owl.bind('qudt-unit-1-1', QUDT_UNIT)

    ontology = URIRef(value='wsn-mas-ontology', base=base_owl_ontology)
    wsd_ffd_owl.add((ontology, RDF.type, OWL.Ontology))
    wsd_ffd_owl.add((ontology, OWL.versionInfo, Literal('1.0')))
    wsd_ffd_owl.add((ontology, OWL.imports, URIRef(value=base_rdf_ontology_uri)))

    MY_RDF_ONTOLOGY: Namespace = Namespace(base_rdf_ontology_uri)
    wsd_ffd_owl.bind('wsn-ffd-rdf', MY_RDF_ONTOLOGY)

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

    # Sensor Procedure a.k.a. Agents Strategies
    strategy = URIRef(value='Strategy', base=base_owl_ontology)
    wsd_ffd_owl.add((strategy, RDFS.subClassOf, SOSA.Procedure))

    trigger_strategy = URIRef(value='TriggerStrategy', base=base_owl_ontology)
    wsd_ffd_owl.add((trigger_strategy, RDFS.subClassOf, strategy))
    trigger_strategy_output_restriction = BNode()
    wsd_ffd_owl.add((trigger_strategy_output_restriction, RDF.type, OWL.Restriction))
    wsd_ffd_owl.add((trigger_strategy_output_restriction, RDFS.comment,
                     Literal('Strategy implemented by a TriggerAgent to trigger a SensorAgent')))
    wsd_ffd_owl.add((trigger_strategy_output_restriction, SCHEMA.unitCode, QUDT_UNIT.Bit))
    wsd_ffd_owl.add((trigger_strategy_output_restriction, OWL.onProperty, SSN.hasOutput))
    wsd_ffd_owl.add((trigger_strategy, RDFS.subClassOf, trigger_strategy_output_restriction))

    ##############################
    # Property Definition
    ##############################

    triggers = URIRef(value='triggers', base=base_owl_ontology)
    wsd_ffd_owl.add((triggers, RDF.type, OWL.ObjectProperty))
    wsd_ffd_owl.add((triggers, RDFS.comment, Literal('SensorAgents that can be triggered by this TriggerAgent')))
    wsd_ffd_owl.add((triggers, RDFS.domain, URIRef(value='TriggerAgent', base=base_rdf_ontology)))
    wsd_ffd_owl.add((triggers, RDFS.range, URIRef(value='SensorAgent', base=base_rdf_ontology)))

    implements_strategy = URIRef(value='implementsStrategy', base=base_owl_ontology)
    wsd_ffd_owl.add((implements_strategy, RDF.type, OWL.ObjectProperty))
    wsd_ffd_owl.add((implements_strategy, RDFS.subPropertyOf, SSN.implements))
    wsd_ffd_owl.add((implements_strategy, RDFS.domain, strategy))
    wsd_ffd_owl.add((implements_strategy, RDFS.range, URIRef(value='Agent', base=base_rdf_ontology)))

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
    coordinator_node_instance = URIRef(value='CN0000001', base=base_owl_ontology)
    wsd_ffd_owl.add((coordinator_node_instance, RDF.type, OWL.CoordinatorNode))
    wsd_ffd_owl.add((coordinator_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT234GJ55500001')))

    router2_node_instance = URIRef(value='RN0000002', base=base_owl_ontology)
    wsd_ffd_owl.add((router2_node_instance, RDF.type, OWL.RouterNode))
    wsd_ffd_owl.add((router2_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT456UI67800001')))   

    router3_node_instance = URIRef(value='RN0000003', base=base_owl_ontology)
    wsd_ffd_owl.add((router3_node_instance, RDF.type, OWL.RouterNode))
    wsd_ffd_owl.add((router3_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT456UI67900001')))

    router4_node_instance = URIRef(value='RN0000004', base=base_owl_ontology)
    wsd_ffd_owl.add((router4_node_instance, RDF.type, OWL.RouterNode))
    wsd_ffd_owl.add((router4_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT456UI68000001')))

    edge2_node_instance = URIRef(value='ED0000002', base=base_rdf_ontology)
    wsd_ffd_owl.add((edge2_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge2_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1100001')))

    edge3_node_instance = URIRef(value='ED0000003', base=base_rdf_ontology)
    wsd_ffd_owl.add((edge3_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge3_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1200001')))

    edge4_node_instance = URIRef(value='ED0000004', base=base_rdf_ontology)
    wsd_ffd_owl.add((edge4_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge4_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1300001')))

    edge5_node_instance = URIRef(value='ED0000005', base=base_rdf_ontology)
    wsd_ffd_owl.add((edge5_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge5_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1400001')))

    edge6_node_instance = URIRef(value='ED0000006', base=base_rdf_ontology)
    wsd_ffd_owl.add((edge6_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge6_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1500001')))

    edge7_node_instance = URIRef(value='ED0000007', base=base_rdf_ontology)
    wsd_ffd_owl.add((edge7_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge7_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1600001')))

    # WSN TOPOLOGY
    wsd_ffd_owl.add((coordinator_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000002', base=base_owl_ontology)))
    wsd_ffd_owl.add((coordinator_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000003', base=base_owl_ontology)))

    wsd_ffd_owl.add((router2_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000003', base=base_owl_ontology)))
    wsd_ffd_owl.add((router2_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000004', base=base_owl_ontology)))
    wsd_ffd_owl.add((router2_node_instance, can_route, Bag(wsd_ffd_owl, BNode(),
                        [coordinator, router3_node_instance, edge2_node_instance, edge3_node_instance, edge4_node_instance]).uri
                    ))

    wsd_ffd_owl.add((router3_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000002', base=base_owl_ontology)))
    wsd_ffd_owl.add((router3_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000004', base=base_owl_ontology)))
    wsd_ffd_owl.add((router3_node_instance, can_route, Bag(wsd_ffd_owl, BNode(),
                        [coordinator, router3_node_instance, edge2_node_instance, edge3_node_instance, edge4_node_instance]).uri
                    ))

    wsd_ffd_owl.add((router4_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000002', base=base_owl_ontology)))
    wsd_ffd_owl.add((router4_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000003', base=base_owl_ontology)))

    wsd_ffd_owl.add((edge2_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000002', base=base_owl_ontology)))  

    wsd_ffd_owl.add((edge3_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000002', base=base_owl_ontology)))

    wsd_ffd_owl.add((edge4_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000002', base=base_owl_ontology)))
    wsd_ffd_owl.add((edge4_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000004', base=base_owl_ontology)))              

    wsd_ffd_owl.add((edge5_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000003', base=base_owl_ontology)))
    wsd_ffd_owl.add((edge5_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000004', base=base_owl_ontology)))

    wsd_ffd_owl.add((edge6_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000003', base=base_owl_ontology)))  

    wsd_ffd_owl.add((edge7_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000003', base=base_owl_ontology)))

    ##############################
    # RDF Serialization
    ##############################
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-xml-owl.rdf', format='xml')
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-pretty-xml-owl.rdf', format='pretty-xml')
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-turtle-owl.ttl', format='turtle')
