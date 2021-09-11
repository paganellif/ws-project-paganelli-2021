from rdflib import Graph
from rdflib.term import URIRef, Literal, BNode
from rdflib.container import Bag
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

    GEO: Namespace = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
    wsd_ffd_owl.bind('geo', GEO)

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
    coordinator_node_instance = URIRef(value='CN0000001', base=base_owl_ontology)

    router2_node_instance = URIRef(value='RN0000002', base=base_owl_ontology)
    router3_node_instance = URIRef(value='RN0000003', base=base_owl_ontology)
    router4_node_instance = URIRef(value='RN0000004', base=base_owl_ontology)

    edge2_node_instance = URIRef(value='ED0000002', base=base_owl_ontology)
    edge3_node_instance = URIRef(value='ED0000003', base=base_owl_ontology)
    edge4_node_instance = URIRef(value='ED0000004', base=base_owl_ontology)
    edge5_node_instance = URIRef(value='ED0000005', base=base_owl_ontology)
    edge6_node_instance = URIRef(value='ED0000006', base=base_owl_ontology)
    edge7_node_instance = URIRef(value='ED0000007', base=base_owl_ontology)

    agent_container_edge2 = URIRef(value='AC0000002', base=base_owl_ontology)
    wsd_ffd_owl.add((agent_container_edge2, RDF.type, URIRef(value="AgentContainer", base=base_rdf_ontology)))
    agent_container_edge3 = URIRef(value='AC0000003', base=base_owl_ontology)
    wsd_ffd_owl.add((agent_container_edge3, RDF.type, URIRef(value="AgentContainer", base=base_rdf_ontology)))
    agent_container_edge4 = URIRef(value='AC0000004', base=base_owl_ontology)
    wsd_ffd_owl.add((agent_container_edge4, RDF.type, URIRef(value="AgentContainer", base=base_rdf_ontology)))
    agent_container_edge5 = URIRef(value='AC0000005', base=base_owl_ontology)
    wsd_ffd_owl.add((agent_container_edge5, RDF.type, URIRef(value="AgentContainer", base=base_rdf_ontology)))
    agent_container_edge6 = URIRef(value='AC0000006', base=base_owl_ontology)
    wsd_ffd_owl.add((agent_container_edge6, RDF.type, URIRef(value="AgentContainer", base=base_rdf_ontology)))
    agent_container_edge7 = URIRef(value='AC0000007', base=base_owl_ontology)
    wsd_ffd_owl.add((agent_container_edge7, RDF.type, URIRef(value="AgentContainer", base=base_rdf_ontology)))

    sensor_agent_edge2 = URIRef(value='SA0000002', base=base_owl_ontology)
    wsd_ffd_owl.add((sensor_agent_edge2, RDF.type, URIRef(value="SensorAgent", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sensor_agent_edge2, MY_RDF_ONTOLOGY.hasJID, Literal("sensoragent.edge2@wsn-mas.org")))
    sensor_agent_edge3 = URIRef(value='SA0000003', base=base_owl_ontology)
    wsd_ffd_owl.add((sensor_agent_edge3, RDF.type, URIRef(value="SensorAgent", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sensor_agent_edge3, MY_RDF_ONTOLOGY.hasJID, Literal("sensoragent.edge3@wsn-mas.org")))
    sensor_agent_edge4 = URIRef(value='SA0000004', base=base_owl_ontology)
    wsd_ffd_owl.add((sensor_agent_edge4, RDF.type, URIRef(value="SensorAgent", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sensor_agent_edge4, MY_RDF_ONTOLOGY.hasJID, Literal("sensoragent.edge4@wsn-mas.org")))
    sensor_agent_edge5 = URIRef(value='SA0000005', base=base_owl_ontology)
    wsd_ffd_owl.add((sensor_agent_edge5, RDF.type, URIRef(value="SensorAgent", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sensor_agent_edge5, MY_RDF_ONTOLOGY.hasJID, Literal("sensoragent.edge5@wsn-mas.org")))
    sensor_agent_edge6 = URIRef(value='SA0000006', base=base_owl_ontology)
    wsd_ffd_owl.add((sensor_agent_edge6, RDF.type, URIRef(value="SensorAgent", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sensor_agent_edge6, MY_RDF_ONTOLOGY.hasJID, Literal("sensoragent.edge6@wsn-mas.org")))
    sensor_agent_edge7 = URIRef(value='SA0000007', base=base_owl_ontology)
    wsd_ffd_owl.add((sensor_agent_edge7, RDF.type, URIRef(value="SensorAgent", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sensor_agent_edge7, MY_RDF_ONTOLOGY.hasJID, Literal("sensoragent.edge7@wsn-mas.org")))

    trigger_agent_edge2 = URIRef(value='TA0000002', base=base_owl_ontology)
    wsd_ffd_owl.add((trigger_agent_edge2, RDF.type, URIRef(value="TriggerAgent", base=base_rdf_ontology)))
    trigger_agent_edge3 = URIRef(value='TA0000003', base=base_owl_ontology)
    wsd_ffd_owl.add((trigger_agent_edge3, RDF.type, URIRef(value="TriggerAgent", base=base_rdf_ontology)))
    trigger_agent_edge4 = URIRef(value='TA0000004', base=base_owl_ontology)
    wsd_ffd_owl.add((trigger_agent_edge4, RDF.type, URIRef(value="TriggerAgent", base=base_rdf_ontology)))
    trigger_agent_edge5 = URIRef(value='TA0000005', base=base_owl_ontology)
    wsd_ffd_owl.add((trigger_agent_edge5, RDF.type, URIRef(value="TriggerAgent", base=base_rdf_ontology)))
    trigger_agent_edge6 = URIRef(value='TA0000006', base=base_owl_ontology)
    wsd_ffd_owl.add((trigger_agent_edge6, RDF.type, URIRef(value="TriggerAgent", base=base_rdf_ontology)))
    trigger_agent_edge7 = URIRef(value='TA0000007', base=base_owl_ontology)
    wsd_ffd_owl.add((trigger_agent_edge7, RDF.type, URIRef(value="TriggerAgent", base=base_rdf_ontology)))

    dbmanager_agent_edge2 = URIRef(value='DBMA0000002', base=base_owl_ontology)
    wsd_ffd_owl.add((dbmanager_agent_edge2, RDF.type, URIRef(value="DBManagerAgent", base=base_owl_ontology)))
    dbmanager_agent_edge3 = URIRef(value='DBMA0000003', base=base_owl_ontology)
    wsd_ffd_owl.add((dbmanager_agent_edge3, RDF.type, URIRef(value="DBManagerAgent", base=base_owl_ontology)))
    dbmanager_agent_edge4 = URIRef(value='DBMA0000004', base=base_owl_ontology)
    wsd_ffd_owl.add((dbmanager_agent_edge4, RDF.type, URIRef(value="DBManagerAgent", base=base_owl_ontology)))
    dbmanager_agent_edge5 = URIRef(value='DBMA0000005', base=base_owl_ontology)
    wsd_ffd_owl.add((dbmanager_agent_edge5, RDF.type, URIRef(value="DBManagerAgent", base=base_owl_ontology)))
    dbmanager_agent_edge6 = URIRef(value='DBMA0000006', base=base_owl_ontology)
    wsd_ffd_owl.add((dbmanager_agent_edge6, RDF.type, URIRef(value="DBManagerAgent", base=base_owl_ontology)))
    dbmanager_agent_edge7 = URIRef(value='DBMA0000007', base=base_owl_ontology)
    wsd_ffd_owl.add((dbmanager_agent_edge7, RDF.type, URIRef(value="DBManagerAgent", base=base_owl_ontology)))

    wsd_ffd_owl.add((agent_container_edge2, MY_RDF_ONTOLOGY.contains,
                     Bag(wsd_ffd_owl, BNode(),
                         [sensor_agent_edge2, trigger_agent_edge2, dbmanager_agent_edge2]).uri
                     ))

    wsd_ffd_owl.add((agent_container_edge3, MY_RDF_ONTOLOGY.contains,
                     Bag(wsd_ffd_owl, BNode(),
                         [sensor_agent_edge3, trigger_agent_edge3, dbmanager_agent_edge3]).uri
                     ))

    wsd_ffd_owl.add((agent_container_edge4, MY_RDF_ONTOLOGY.contains,
                     Bag(wsd_ffd_owl, BNode(),
                         [sensor_agent_edge4, trigger_agent_edge4, dbmanager_agent_edge4]).uri
                     ))

    wsd_ffd_owl.add((agent_container_edge5, MY_RDF_ONTOLOGY.contains,
                     Bag(wsd_ffd_owl, BNode(),
                         [sensor_agent_edge5, trigger_agent_edge5, dbmanager_agent_edge5]).uri
                     ))

    wsd_ffd_owl.add((agent_container_edge6, MY_RDF_ONTOLOGY.contains,
                     Bag(wsd_ffd_owl, BNode(),
                         [sensor_agent_edge6, trigger_agent_edge6, dbmanager_agent_edge6]).uri
                     ))

    wsd_ffd_owl.add((agent_container_edge7, MY_RDF_ONTOLOGY.contains,
                     Bag(wsd_ffd_owl, BNode(),
                         [sensor_agent_edge7, trigger_agent_edge7, dbmanager_agent_edge7]).uri
                     ))

    wsd_ffd_owl.add((edge2_node_instance, MY_RDF_ONTOLOGY.hostsAgentContainer, agent_container_edge2))
    wsd_ffd_owl.add((edge3_node_instance, MY_RDF_ONTOLOGY.hostsAgentContainer, agent_container_edge3))
    wsd_ffd_owl.add((edge4_node_instance, MY_RDF_ONTOLOGY.hostsAgentContainer, agent_container_edge4))
    wsd_ffd_owl.add((edge5_node_instance, MY_RDF_ONTOLOGY.hostsAgentContainer, agent_container_edge5))
    wsd_ffd_owl.add((edge6_node_instance, MY_RDF_ONTOLOGY.hostsAgentContainer, agent_container_edge6))
    wsd_ffd_owl.add((edge7_node_instance, MY_RDF_ONTOLOGY.hostsAgentContainer, agent_container_edge7))

    # Sensors edge2
    dht11_edge2 = URIRef(value='DHT110000002', base=base_owl_ontology)
    ky026_edge2 = URIRef(value='KY0260000002', base=base_owl_ontology)
    mq2_edge2 = URIRef(value='MQ20000002', base=base_owl_ontology)
    sfm27_edge2 = URIRef(value='SFM270000002', base=base_owl_ontology)

    # Sensors edge3
    dht11_edge3 = URIRef(value='DHT110000003', base=base_owl_ontology)
    ky026_edge3 = URIRef(value='KY0260000003', base=base_owl_ontology)
    mq2_edge3 = URIRef(value='MQ20000003', base=base_owl_ontology)
    sfm27_edge3 = URIRef(value='SFM270000003', base=base_owl_ontology)

    # Sensors edge4
    dht11_edge4 = URIRef(value='DHT110000004', base=base_owl_ontology)
    ky026_edge4 = URIRef(value='KY0260000004', base=base_owl_ontology)
    mq2_edge4 = URIRef(value='MQ20000004', base=base_owl_ontology)
    sfm27_edge4 = URIRef(value='SFM270000004', base=base_owl_ontology)

    # Sensors edge5
    dht11_edge5 = URIRef(value='DHT110000005', base=base_owl_ontology)
    ky026_edge5 = URIRef(value='KY0260000002', base=base_owl_ontology)
    mq2_edge5 = URIRef(value='MQ20000005', base=base_owl_ontology)
    sfm27_edge5 = URIRef(value='SFM270000005', base=base_owl_ontology)

    # Sensors edge6
    dht11_edge6 = URIRef(value='DHT110000006', base=base_owl_ontology)
    ky026_edge6 = URIRef(value='KY0260000006', base=base_owl_ontology)
    mq2_edge6 = URIRef(value='MQ20000006', base=base_owl_ontology)
    sfm27_edge6 = URIRef(value='SFM270000006', base=base_owl_ontology)

    # Sensors edge7
    dht11_edge7 = URIRef(value='DHT110000007', base=base_owl_ontology)
    ky026_edge7 = URIRef(value='KY0260000007', base=base_owl_ontology)
    mq2_edge7 = URIRef(value='MQ20000007', base=base_owl_ontology)
    sfm27_edge7 = URIRef(value='SFM270000007', base=base_owl_ontology)

    wsd_ffd_owl.add((dht11_edge2, RDF.type, URIRef(value="DHT11", base=base_rdf_ontology)))
    wsd_ffd_owl.add((dht11_edge2, SOSA.isHostedBy, edge2_node_instance))

    wsd_ffd_owl.add((dht11_edge3, RDF.type, URIRef(value="DHT11", base=base_rdf_ontology)))
    wsd_ffd_owl.add((dht11_edge3, SOSA.isHostedBy, edge3_node_instance))

    wsd_ffd_owl.add((dht11_edge4, RDF.type, URIRef(value="DHT11", base=base_rdf_ontology)))
    wsd_ffd_owl.add((dht11_edge4, SOSA.isHostedBy, edge4_node_instance))

    wsd_ffd_owl.add((dht11_edge5, RDF.type, URIRef(value="DHT11", base=base_rdf_ontology)))
    wsd_ffd_owl.add((dht11_edge5, SOSA.isHostedBy, edge5_node_instance))

    wsd_ffd_owl.add((dht11_edge6, RDF.type, URIRef(value="DHT11", base=base_rdf_ontology)))
    wsd_ffd_owl.add((dht11_edge6, SOSA.isHostedBy, edge6_node_instance))

    wsd_ffd_owl.add((dht11_edge7, RDF.type, URIRef(value="DHT11", base=base_rdf_ontology)))
    wsd_ffd_owl.add((dht11_edge7, SOSA.isHostedBy, edge7_node_instance))


    wsd_ffd_owl.add((ky026_edge2, RDF.type, URIRef(value="KY026", base=base_rdf_ontology)))
    wsd_ffd_owl.add((ky026_edge2, SOSA.isHostedBy, edge2_node_instance))

    wsd_ffd_owl.add((ky026_edge3, RDF.type, URIRef(value="KY026", base=base_rdf_ontology)))
    wsd_ffd_owl.add((ky026_edge3, SOSA.isHostedBy, edge3_node_instance))

    wsd_ffd_owl.add((ky026_edge4, RDF.type, URIRef(value="KY026", base=base_rdf_ontology)))
    wsd_ffd_owl.add((ky026_edge4, SOSA.isHostedBy, edge4_node_instance))

    wsd_ffd_owl.add((ky026_edge5, RDF.type, URIRef(value="KY026", base=base_rdf_ontology)))
    wsd_ffd_owl.add((ky026_edge5, SOSA.isHostedBy, edge5_node_instance))

    wsd_ffd_owl.add((ky026_edge6, RDF.type, URIRef(value="KY026", base=base_rdf_ontology)))
    wsd_ffd_owl.add((ky026_edge6, SOSA.isHostedBy, edge6_node_instance))

    wsd_ffd_owl.add((ky026_edge7, RDF.type, URIRef(value="KY026", base=base_rdf_ontology)))
    wsd_ffd_owl.add((ky026_edge7, SOSA.isHostedBy, edge7_node_instance))


    wsd_ffd_owl.add((sfm27_edge2, RDF.type, URIRef(value="SFM27", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sfm27_edge2, SOSA.isHostedBy, edge2_node_instance))

    wsd_ffd_owl.add((sfm27_edge3, RDF.type, URIRef(value="SFM27", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sfm27_edge3, SOSA.isHostedBy, edge3_node_instance))

    wsd_ffd_owl.add((sfm27_edge4, RDF.type, URIRef(value="SFM27", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sfm27_edge4, SOSA.isHostedBy, edge4_node_instance))

    wsd_ffd_owl.add((sfm27_edge5, RDF.type, URIRef(value="SFM27", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sfm27_edge5, SOSA.isHostedBy, edge5_node_instance))

    wsd_ffd_owl.add((sfm27_edge6, RDF.type, URIRef(value="SFM27", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sfm27_edge6, SOSA.isHostedBy, edge6_node_instance))

    wsd_ffd_owl.add((sfm27_edge7, RDF.type, URIRef(value="SFM27", base=base_rdf_ontology)))
    wsd_ffd_owl.add((sfm27_edge7, SOSA.isHostedBy, edge7_node_instance))


    wsd_ffd_owl.add((mq2_edge2, RDF.type, URIRef(value="MQ2", base=base_rdf_ontology)))
    wsd_ffd_owl.add((mq2_edge2, SOSA.isHostedBy, edge2_node_instance))

    wsd_ffd_owl.add((mq2_edge3, RDF.type, URIRef(value="MQ2", base=base_rdf_ontology)))
    wsd_ffd_owl.add((mq2_edge3, SOSA.isHostedBy, edge3_node_instance))

    wsd_ffd_owl.add((mq2_edge4, RDF.type, URIRef(value="MQ2", base=base_rdf_ontology)))
    wsd_ffd_owl.add((mq2_edge4, SOSA.isHostedBy, edge4_node_instance))

    wsd_ffd_owl.add((mq2_edge5, RDF.type, URIRef(value="MQ2", base=base_rdf_ontology)))
    wsd_ffd_owl.add((mq2_edge5, SOSA.isHostedBy, edge5_node_instance))

    wsd_ffd_owl.add((mq2_edge6, RDF.type, URIRef(value="MQ2", base=base_rdf_ontology)))
    wsd_ffd_owl.add((mq2_edge6, SOSA.isHostedBy, edge6_node_instance))

    wsd_ffd_owl.add((mq2_edge7, RDF.type, URIRef(value="MQ2", base=base_rdf_ontology)))
    wsd_ffd_owl.add((mq2_edge7, SOSA.isHostedBy, edge7_node_instance))

    wsd_ffd_owl.add((coordinator_node_instance, RDF.type, OWL.CoordinatorNode))
    wsd_ffd_owl.add((coordinator_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT234GJ55500001')))
    wsd_ffd_owl.add((coordinator_node_instance, GEO.lat, Literal(55.701)))
    wsd_ffd_owl.add((coordinator_node_instance, GEO.long, Literal(12.552)))

    wsd_ffd_owl.add((router2_node_instance, RDF.type, OWL.RouterNode))
    wsd_ffd_owl.add((router2_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT456UI67800001')))
    wsd_ffd_owl.add((router2_node_instance, GEO.lat, Literal(55.895)))
    wsd_ffd_owl.add((router2_node_instance, GEO.long, Literal(12.437)))

    wsd_ffd_owl.add((router3_node_instance, RDF.type, OWL.RouterNode))
    wsd_ffd_owl.add((router3_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT456UI67900001')))
    wsd_ffd_owl.add((router3_node_instance, GEO.lat, Literal(55.634)))
    wsd_ffd_owl.add((router3_node_instance, GEO.long, Literal(12.606)))

    wsd_ffd_owl.add((router4_node_instance, RDF.type, OWL.RouterNode))
    wsd_ffd_owl.add((router4_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT456UI68000001')))
    wsd_ffd_owl.add((router4_node_instance, GEO.lat, Literal(56.030)))
    wsd_ffd_owl.add((router4_node_instance, GEO.long, Literal(12.112)))

    wsd_ffd_owl.add((edge2_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge2_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1100001')))
    wsd_ffd_owl.add((edge2_node_instance, GEO.lat, Literal(56.120)))
    wsd_ffd_owl.add((edge2_node_instance, GEO.long, Literal(11.969)))
    wsd_ffd_owl.add((edge2_node_instance, SOSA.hosts,
                     Bag(wsd_ffd_owl, BNode(),
                         [dht11_edge2, mq2_edge2, ky026_edge2, sfm27_edge2]).uri
                     ))

    wsd_ffd_owl.add((edge3_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge3_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1200001')))
    wsd_ffd_owl.add((edge3_node_instance, GEO.lat, Literal(56.330)))
    wsd_ffd_owl.add((edge3_node_instance, GEO.long, Literal(11.969)))
    wsd_ffd_owl.add((edge3_node_instance, SOSA.hosts,
                     Bag(wsd_ffd_owl, BNode(),
                         [dht11_edge3, mq2_edge3, ky026_edge3, sfm27_edge3]).uri
                     ))

    wsd_ffd_owl.add((edge4_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge4_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1300001')))
    wsd_ffd_owl.add((edge4_node_instance, GEO.lat, Literal(56.444)))
    wsd_ffd_owl.add((edge4_node_instance, GEO.long, Literal(11.969)))
    wsd_ffd_owl.add((edge4_node_instance, SOSA.hosts,
                     Bag(wsd_ffd_owl, BNode(),
                         [dht11_edge4, mq2_edge4, ky026_edge4, sfm27_edge4]).uri
                     ))

    wsd_ffd_owl.add((edge5_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge5_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1400001')))
    wsd_ffd_owl.add((edge5_node_instance, GEO.lat, Literal(56.454)))
    wsd_ffd_owl.add((edge5_node_instance, GEO.long, Literal(11.888)))
    wsd_ffd_owl.add((edge5_node_instance, SOSA.hosts,
                     Bag(wsd_ffd_owl, BNode(),
                         [dht11_edge5, mq2_edge5, ky026_edge5, sfm27_edge5]).uri
                     ))

    wsd_ffd_owl.add((edge6_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge6_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1500001')))
    wsd_ffd_owl.add((edge6_node_instance, GEO.lat, Literal(56.342)))
    wsd_ffd_owl.add((edge6_node_instance, GEO.long, Literal(11.765)))
    wsd_ffd_owl.add((edge6_node_instance, SOSA.hosts,
                     Bag(wsd_ffd_owl, BNode(),
                         [dht11_edge6, mq2_edge6, ky026_edge6, sfm27_edge6]).uri
                     ))

    wsd_ffd_owl.add((edge7_node_instance, RDF.type, OWL.EdgeDevice))
    wsd_ffd_owl.add((edge7_node_instance, MY_RDF_ONTOLOGY.SerialNum, Literal('IT833ZK1600001')))
    wsd_ffd_owl.add((edge7_node_instance, GEO.lat, Literal(56.323)))
    wsd_ffd_owl.add((edge7_node_instance, GEO.long, Literal(11.721)))
    wsd_ffd_owl.add((edge7_node_instance, SOSA.hosts,
                     Bag(wsd_ffd_owl, BNode(),
                         [dht11_edge7, mq2_edge7, ky026_edge7, sfm27_edge7]).uri
                     ))

    # WSN TOPOLOGY
    wsd_ffd_owl.add((coordinator_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000002', base=base_owl_ontology)))
    wsd_ffd_owl.add((coordinator_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000003', base=base_owl_ontology)))
    wsd_ffd_owl.add((coordinator_node_instance, can_route, Bag(wsd_ffd_owl, BNode(),
                        [router2_node_instance, router3_node_instance]).uri))

    wsd_ffd_owl.add((router2_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#CN0000001', base=base_owl_ontology)))
    wsd_ffd_owl.add((router2_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000004', base=base_owl_ontology)))
    wsd_ffd_owl.add((router2_node_instance, can_route, Bag(wsd_ffd_owl, BNode(),
                        [coordinator_node_instance, router4_node_instance,
                         edge2_node_instance, edge3_node_instance]).uri))

    wsd_ffd_owl.add((router3_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#CN0000001', base=base_owl_ontology)))
    wsd_ffd_owl.add((router3_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000004', base=base_owl_ontology)))
    wsd_ffd_owl.add((router3_node_instance, can_route, Bag(wsd_ffd_owl, BNode(),
                        [coordinator_node_instance, router4_node_instance,
                         edge6_node_instance, edge7_node_instance]).uri))

    wsd_ffd_owl.add((router4_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000002', base=base_owl_ontology)))
    wsd_ffd_owl.add((router4_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000003', base=base_owl_ontology)))
    wsd_ffd_owl.add((router4_node_instance, can_route, Bag(wsd_ffd_owl, BNode(),
                        [router2_node_instance, router3_node_instance,
                         edge3_node_instance, edge4_node_instance,
                         edge5_node_instance, edge6_node_instance]).uri))

    wsd_ffd_owl.add((edge2_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000002', base=base_owl_ontology)))  

    wsd_ffd_owl.add((edge3_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000002', base=base_owl_ontology)))
    wsd_ffd_owl.add((edge3_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000004', base=base_owl_ontology)))

    wsd_ffd_owl.add((edge4_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000004', base=base_owl_ontology)))

    wsd_ffd_owl.add((edge5_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000004', base=base_owl_ontology)))

    wsd_ffd_owl.add((edge6_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000003', base=base_owl_ontology)))
    wsd_ffd_owl.add((edge6_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000004', base=base_owl_ontology)))

    wsd_ffd_owl.add((edge7_node_instance, MY_RDF_ONTOLOGY.isRoutedBy,
                     URIRef(value='#RN0000003', base=base_owl_ontology)))

    ##############################
    # RDF Serialization
    ##############################
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-xml-owl.rdf', format='xml')
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-pretty-xml-owl.rdf', format='pretty-xml')
    wsd_ffd_owl.serialize(destination=os.getcwd()+'/wsd-ffd-turtle-owl.ttl', format='turtle')
