from rdflib import Graph
from rdflib.container import Bag
from rdflib.term import BNode, URIRef, Literal
from rdflib.namespace import Namespace, RDFS, RDF
import os
import sys

if __name__ == '__main__':

    ##############################
    # Graph Definition
    ##############################
    wsd_ffd_rdf: Graph = Graph()
    base_ontology: str = 'https://wsn-ffd-rdf.org/'

    ##############################
    # Binding Namespaces
    ##############################
    SOSA: Namespace = Namespace('http://www.w3.org/ns/sosa/')
    wsd_ffd_rdf.bind('sosa', SOSA)

    SSN: Namespace = Namespace('http://www.w3.org/ns/ssn/')
    wsd_ffd_rdf.bind('ssn', SSN)

    SSN_SYSTEM: Namespace = Namespace('http://www.w3.org/ns/ssn/systems/')
    wsd_ffd_rdf.bind('ssn-system', SSN_SYSTEM)

    GEO: Namespace = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
    wsd_ffd_rdf.bind('geo', GEO)

    QUDT: Namespace = Namespace('http://qudt.org/1.1/schema/qudt#')
    wsd_ffd_rdf.bind('qudt-1-1', QUDT)

    QUDT_UNIT: Namespace = Namespace('http://qudt.org/1.1/vocab/unit#')
    wsd_ffd_rdf.bind('qudt-unit-1-1', QUDT_UNIT)

    SCHEMA: Namespace = Namespace('http://schema.org/')
    wsd_ffd_rdf.bind('schema', SCHEMA)

    ##############################
    # RDFS
    ##############################

    # Class definition
    # EdgeDevice
    edge_device = URIRef(value='EdgeDevice', base=base_ontology)
    wsd_ffd_rdf.add((edge_device, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((edge_device, RDFS.comment, Literal('Edge device node of the wireless sensor network')))
    wsd_ffd_rdf.add((edge_device, RDFS.subClassOf, SOSA.Platform))

    # DHT11
    dht11 = URIRef(value='DHT11', base=base_ontology)
    wsd_ffd_rdf.add((dht11, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((dht11, RDFS.comment, Literal('DHT11 sensor contains a humidity and a temperature sensor')))
    wsd_ffd_rdf.add((dht11, RDFS.seeAlso, URIRef(value='https://www.adafruit.com/product/386')))
    wsd_ffd_rdf.add((dht11, RDFS.subClassOf, SSN.Sensor))

    # MQ2
    mq2 = URIRef(value='MQ2', base=base_ontology)
    wsd_ffd_rdf.add((mq2, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((mq2, RDFS.comment, Literal('MQ2 Gas sensor for sensing LPG, Smoke, Alcohol, Propane, Hydrogen, Methane and Carbon Monoxide')))
    wsd_ffd_rdf.add((mq2, RDFS.seeAlso, URIRef(value='https://www.mouser.com/datasheet/2/321/605-00008-MQ-2-Datasheet-370464.pdf')))
    wsd_ffd_rdf.add((mq2, RDFS.subClassOf, SSN.Sensor))

    # KY026
    ky026 = URIRef(value='KY026', base=base_ontology)
    wsd_ffd_rdf.add((ky026, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((ky026, RDFS.comment, Literal('KY-026 Flame Sensor Module')))
    wsd_ffd_rdf.add((ky026, RDFS.seeAlso, URIRef(value='https://datasheetspdf.com/pdf/1402037/Joy-IT/KY-026/1')))
    wsd_ffd_rdf.add((ky026, RDFS.subClassOf, SSN.Sensor))

    # SFM27
    sfm27 = URIRef(value='SFM27', base=base_ontology)
    wsd_ffd_rdf.add((sfm27, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((sfm27, RDFS.comment, Literal('SFM-27 active buzzer')))
    wsd_ffd_rdf.add((sfm27, RDFS.seeAlso, URIRef(value='https://opencircuit.shop/resources/file/7379f0193d4549c771f0d61bd31d06b316cd4706466/SFM27-Datasheet.pdf')))
    wsd_ffd_rdf.add((sfm27, RDFS.subClassOf, SSN.Actuator))

    # Agent
    agent = URIRef(value='Agent', base=base_ontology)
    wsd_ffd_rdf.add((agent, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((agent, RDFS.comment, Literal('MAS Base Agent')))

    # AgentContainer
    agent_container = URIRef(value='AgentContainer', base=base_ontology)
    wsd_ffd_rdf.add((agent_container, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((agent, RDFS.comment, Literal('Agent Execution Environment')))

    # SensorAgent
    sensor_agent = URIRef(value='SensorAgent', base=base_ontology)
    wsd_ffd_rdf.add((sensor_agent, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((sensor_agent, RDFS.comment, Literal('MAS Sensor Agent')))
    wsd_ffd_rdf.add((sensor_agent, RDFS.seeAlso, URIRef(value='https://gitlab.com/paganelli.f/sd-project-paganelli-1920/-/blob/master/WSN/sensoragent.py')))
    wsd_ffd_rdf.add((sensor_agent, RDFS.subClassOf, agent))

    # TriggerAgent
    trigger_agent = URIRef(value='TriggerAgent', base=base_ontology)
    wsd_ffd_rdf.add((trigger_agent, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((trigger_agent, RDFS.comment, Literal('MAS Trigger Agent')))
    wsd_ffd_rdf.add((trigger_agent, RDFS.seeAlso, URIRef(value='https://gitlab.com/paganelli.f/sd-project-paganelli-1920/-/blob/master/processing/triggeragent.py')))
    wsd_ffd_rdf.add((trigger_agent, RDFS.subClassOf, agent))

    # Property Definition
    # WSN Properties
    is_routed_by = URIRef(value='isRoutedBy', base=base_ontology)
    wsd_ffd_rdf.add((is_routed_by, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((is_routed_by, RDFS.comment, Literal('Router node able to route information to this node')))
    wsd_ffd_rdf.add((is_routed_by, RDFS.domain, SSN.System))
    wsd_ffd_rdf.add((is_routed_by, RDFS.range, SOSA.Platform))

    device_serial_num = URIRef(value='SerialNum', base=base_ontology)
    wsd_ffd_rdf.add((device_serial_num, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((device_serial_num, RDFS.comment, Literal('Node Serial Number Identifier')))
    wsd_ffd_rdf.add((device_serial_num, RDFS.domain, SSN.System))
    wsd_ffd_rdf.add((device_serial_num, RDFS.range, RDFS.Literal))

    temp_condition = URIRef(value='TempCondition', base=base_ontology)
    wsd_ffd_rdf.add((temp_condition, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((temp_condition, RDFS.comment, Literal('Sensor/Actuator operating temperature condition')))
    wsd_ffd_rdf.add((temp_condition, RDFS.domain, SSN.System))
    wsd_ffd_rdf.add((temp_condition, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((temp_condition, RDFS.subPropertyOf, SSN_SYSTEM.Condition))

    hum_condition = URIRef(value='HumCondition', base=base_ontology)
    wsd_ffd_rdf.add((hum_condition, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((hum_condition, RDFS.comment, Literal('Sensor/Actuator operating humidity condition')))
    wsd_ffd_rdf.add((hum_condition, RDFS.domain, SSN.System))
    wsd_ffd_rdf.add((hum_condition, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((hum_condition, RDFS.subPropertyOf, SSN_SYSTEM.Condition))

    # mq2 properties
    gas_measurement = URIRef(value='GasMeasurement', base=base_ontology)
    wsd_ffd_rdf.add((gas_measurement, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((gas_measurement, RDFS.comment, Literal('Parts-per-million is the ratio of one gas to another')))
    wsd_ffd_rdf.add((gas_measurement, RDFS.domain, mq2))
    wsd_ffd_rdf.add((gas_measurement, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((gas_measurement, RDFS.subPropertyOf, SSN_SYSTEM.MeasurementRange))

    oxygen_condition = URIRef(value='OxygenCondition', base=base_ontology)
    wsd_ffd_rdf.add((oxygen_condition, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((oxygen_condition, RDFS.comment, Literal('Sensor/Actuator operating oxygen condition')))
    wsd_ffd_rdf.add((oxygen_condition, RDFS.domain, mq2))
    wsd_ffd_rdf.add((oxygen_condition, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((oxygen_condition, RDFS.subPropertyOf, SSN_SYSTEM.Condition))

    # dht11 properties
    temp_accuracy = URIRef(value='TempAccuracy', base=base_ontology)
    wsd_ffd_rdf.add((temp_accuracy, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((temp_accuracy, RDFS.comment, Literal('Temperature accuracy')))
    wsd_ffd_rdf.add((temp_accuracy, RDFS.domain, dht11))
    wsd_ffd_rdf.add((temp_accuracy, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((temp_accuracy, RDFS.subPropertyOf, SSN_SYSTEM.Accuracy))

    hum_accuracy = URIRef(value='HumAccuracy', base=base_ontology)
    wsd_ffd_rdf.add((hum_accuracy, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((hum_accuracy, RDFS.comment, Literal('Humidity accuracy')))
    wsd_ffd_rdf.add((hum_accuracy, RDFS.domain, dht11))
    wsd_ffd_rdf.add((hum_accuracy, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((hum_accuracy, RDFS.subPropertyOf, SSN_SYSTEM.Accuracy))

    # ky026 properties
    uv_measurement = URIRef(value='UVMeasurement', base=base_ontology)
    wsd_ffd_rdf.add((uv_measurement, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((uv_measurement, RDFS.comment, Literal('Infrared Wavelength Detection')))
    wsd_ffd_rdf.add((uv_measurement, RDFS.domain, ky026))
    wsd_ffd_rdf.add((uv_measurement, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((uv_measurement, RDFS.subPropertyOf, SSN_SYSTEM.MeasurementRange))

    angle_operating_range = URIRef(value='AngleOperatingRange', base=base_ontology)
    wsd_ffd_rdf.add((angle_operating_range, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((angle_operating_range, RDFS.comment, Literal('Sensor Detection Angle')))
    wsd_ffd_rdf.add((angle_operating_range, RDFS.domain, ky026))
    wsd_ffd_rdf.add((angle_operating_range, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((angle_operating_range, RDFS.subPropertyOf, SSN_SYSTEM.OperatingRange))

    # sfm27 properties
    sound_output = URIRef(value='SoundOutput', base=base_ontology)
    wsd_ffd_rdf.add((sound_output, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((sound_output, RDFS.comment, Literal('Sensor Sound Output')))
    wsd_ffd_rdf.add((sound_output, RDFS.domain, sfm27))
    wsd_ffd_rdf.add((sound_output, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((sound_output, RDFS.subPropertyOf, SOSA.ActuableProperty))

    # MAS Properties
    contains = URIRef(value='contains', base=base_ontology)
    wsd_ffd_rdf.add((contains, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((contains, RDFS.comment, Literal('List of agents contained by the container')))
    wsd_ffd_rdf.add((contains, RDFS.domain, agent_container))
    wsd_ffd_rdf.add((contains, RDFS.range, agent))

    hosts_agent_container = URIRef(value='hostsAgentContainer', base=base_ontology)
    wsd_ffd_rdf.add((hosts_agent_container, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((hosts_agent_container, RDFS.comment, Literal('Agent container hosted by a WSN Node')))
    wsd_ffd_rdf.add((hosts_agent_container, RDFS.domain, SOSA.Platform))
    wsd_ffd_rdf.add((hosts_agent_container, RDFS.range, agent_container))

    has_jid = URIRef(value='hasJID', base=base_ontology)
    wsd_ffd_rdf.add((has_jid, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((has_jid, RDFS.comment, Literal('Identifier of the agent in the form username@server')))
    wsd_ffd_rdf.add((has_jid, RDFS.domain, agent))
    wsd_ffd_rdf.add((has_jid, RDFS.range, RDFS.Literal))

    has_neighbour = URIRef(value='hasNeighbour', base=base_ontology)
    wsd_ffd_rdf.add((has_neighbour, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((has_neighbour, RDFS.comment, Literal('Neighbour Agent')))
    wsd_ffd_rdf.add((has_neighbour, RDFS.domain, agent))
    wsd_ffd_rdf.add((has_neighbour, RDFS.range, agent))

    is_alive = URIRef(value='isAlive', base=base_ontology)
    wsd_ffd_rdf.add((is_alive, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((is_alive, RDFS.comment, Literal('Indicates whether the agent is alive')))
    wsd_ffd_rdf.add((is_alive, RDFS.domain, agent))
    wsd_ffd_rdf.add((is_alive, RDFS.range, RDFS.Literal))

    ##############################
    # RDF
    ##############################
    # Instances definition
    edge_device_instance = URIRef(value='ED0000001', base=base_ontology)
    router_instance = URIRef(value='RN0000001', base=base_ontology)
    dht11_instance = URIRef(value='DHT110000001', base=base_ontology)
    ky026_instance = URIRef(value='KY0260000001', base=base_ontology)
    mq2_instance = URIRef(value='MQ20000001', base=base_ontology)
    sfm27_instance = URIRef(value='SFM270000001', base=base_ontology)

    # DHT11 instance
    wsd_ffd_rdf.add((dht11_instance, RDF.type, dht11))
    wsd_ffd_rdf.add((dht11_instance, SOSA.isHostedBy, edge_device_instance))

    dht11_power_range = BNode()
    wsd_ffd_rdf.add((dht11_power_range, SCHEMA.minValue, Literal(3)))
    wsd_ffd_rdf.add((dht11_power_range, SCHEMA.maxValue, Literal(5)))
    wsd_ffd_rdf.add((dht11_power_range, SCHEMA.unitCode, QUDT_UNIT.V))
    wsd_ffd_rdf.add((dht11_instance, SSN_SYSTEM.OperatingPowerRange, dht11_power_range))

    dht11_frequency = BNode()
    wsd_ffd_rdf.add((dht11_frequency, SCHEMA.value, Literal(1)))
    wsd_ffd_rdf.add((dht11_frequency, SCHEMA.unitCode, QUDT_UNIT.Second))
    wsd_ffd_rdf.add((dht11_instance, SSN_SYSTEM.Frequency, dht11_frequency))

    dht11_temp_acc = BNode()
    wsd_ffd_rdf.add((dht11_temp_acc, SCHEMA.minValue, Literal(2)))
    wsd_ffd_rdf.add((dht11_temp_acc, SCHEMA.maxValue, Literal(-2)))
    wsd_ffd_rdf.add((dht11_temp_acc, SCHEMA.unitCode, QUDT_UNIT.DegreeCelsius))
    wsd_ffd_rdf.add((dht11_instance, temp_accuracy, dht11_temp_acc))

    dht11_temp_cond = BNode()
    wsd_ffd_rdf.add((dht11_temp_cond, SCHEMA.minValue, Literal(0)))
    wsd_ffd_rdf.add((dht11_temp_cond, SCHEMA.maxValue, Literal(50)))
    wsd_ffd_rdf.add((dht11_temp_cond, SCHEMA.unitCode, QUDT_UNIT.DegreeCelsius))
    wsd_ffd_rdf.add((dht11_instance, temp_condition, dht11_temp_cond))

    dht11_hum_acc = BNode()
    wsd_ffd_rdf.add((dht11_hum_acc, SCHEMA.value, Literal(5)))
    wsd_ffd_rdf.add((dht11_hum_acc, SCHEMA.unitCode, QUDT_UNIT.Percent))
    wsd_ffd_rdf.add((dht11_instance, hum_accuracy, dht11_hum_acc))

    dht11_hum_cond = BNode()
    wsd_ffd_rdf.add((dht11_hum_cond, SCHEMA.minValue, Literal(20)))
    wsd_ffd_rdf.add((dht11_hum_cond, SCHEMA.maxValue, Literal(80)))
    wsd_ffd_rdf.add((dht11_hum_cond, SCHEMA.unitCode, QUDT_UNIT.Percent))
    wsd_ffd_rdf.add((dht11_instance, hum_condition, dht11_hum_cond))

    # MQ2 instance
    wsd_ffd_rdf.add((mq2_instance, RDF.type, mq2))
    wsd_ffd_rdf.add((mq2_instance, SOSA.isHostedBy, edge_device_instance))

    mq2_power_range = BNode()
    wsd_ffd_rdf.add((mq2_power_range, SCHEMA.minValue, Literal(5)))
    wsd_ffd_rdf.add((mq2_power_range, SCHEMA.maxValue, Literal(5)))
    wsd_ffd_rdf.add((mq2_power_range, SCHEMA.unitCode, QUDT_UNIT.V))
    wsd_ffd_rdf.add((mq2_instance, SSN_SYSTEM.OperatingPowerRange, mq2_power_range))

    mq2_frequency = BNode()
    wsd_ffd_rdf.add((mq2_frequency, SCHEMA.value, Literal(1)))
    wsd_ffd_rdf.add((mq2_frequency, SCHEMA.unitCode, QUDT_UNIT.Second))
    wsd_ffd_rdf.add((mq2_instance, SSN_SYSTEM.Frequency, mq2_frequency))

    mq2_gas_measurement = BNode()
    wsd_ffd_rdf.add((mq2_gas_measurement, SCHEMA.minValue, Literal(200)))
    wsd_ffd_rdf.add((mq2_gas_measurement, SCHEMA.maxValue, Literal(10000)))
    wsd_ffd_rdf.add((mq2_gas_measurement, SCHEMA.unitCode, QUDT_UNIT.PPM))
    wsd_ffd_rdf.add((mq2_instance, gas_measurement, mq2_gas_measurement))

    mq2_oxy_cond = BNode()
    wsd_ffd_rdf.add((mq2_oxy_cond, SCHEMA.value, Literal(21)))
    wsd_ffd_rdf.add((mq2_oxy_cond, SCHEMA.unitCode, QUDT_UNIT.Percent))
    wsd_ffd_rdf.add((mq2_instance, oxygen_condition, mq2_oxy_cond))

    mq2_temp_cond = BNode()
    wsd_ffd_rdf.add((mq2_temp_cond, SCHEMA.minValue, Literal(18)))
    wsd_ffd_rdf.add((mq2_temp_cond, SCHEMA.maxValue, Literal(22)))
    wsd_ffd_rdf.add((mq2_temp_cond, SCHEMA.unitCode, QUDT_UNIT.DegreeCelsius))
    wsd_ffd_rdf.add((mq2_instance, temp_condition, mq2_temp_cond))

    mq2_hum_cond = BNode()
    wsd_ffd_rdf.add((mq2_hum_cond, SCHEMA.minValue, Literal(60)))
    wsd_ffd_rdf.add((mq2_hum_cond, SCHEMA.maxValue, Literal(70)))
    wsd_ffd_rdf.add((mq2_hum_cond, SCHEMA.unitCode, QUDT_UNIT.Percent))
    wsd_ffd_rdf.add((mq2_instance, hum_condition, mq2_hum_cond))

    # KY026 instance
    wsd_ffd_rdf.add((ky026_instance, RDF.type, ky026))
    wsd_ffd_rdf.add((ky026_instance, SOSA.isHostedBy, edge_device_instance))

    ky026_power_range = BNode()
    wsd_ffd_rdf.add((ky026_power_range, SCHEMA.minValue, Literal(3)))
    wsd_ffd_rdf.add((ky026_power_range, SCHEMA.maxValue, Literal(5)))
    wsd_ffd_rdf.add((ky026_power_range, SCHEMA.unitCode, QUDT_UNIT.V))
    wsd_ffd_rdf.add((ky026_instance, SSN_SYSTEM.OperatingPowerRange, ky026_power_range))

    ky026_uv_meas = BNode()
    wsd_ffd_rdf.add((ky026_uv_meas, SCHEMA.minValue, Literal(760)))
    wsd_ffd_rdf.add((ky026_uv_meas, SCHEMA.maxValue, Literal(1100)))
    wsd_ffd_rdf.add((ky026_uv_meas, SCHEMA.unitCode, QUDT_UNIT.NanoM))
    wsd_ffd_rdf.add((ky026_instance, uv_measurement, ky026_uv_meas))

    ky026_angle_op_range = BNode()
    wsd_ffd_rdf.add((ky026_angle_op_range, SCHEMA.value, Literal(60)))
    wsd_ffd_rdf.add((ky026_angle_op_range, SCHEMA.unitCode, QUDT_UNIT.DEG))
    wsd_ffd_rdf.add((ky026_instance, angle_operating_range, ky026_angle_op_range))

    # SFM27 instance
    wsd_ffd_rdf.add((sfm27_instance, RDF.type, sfm27))
    wsd_ffd_rdf.add((sfm27_instance, SOSA.isHostedBy, edge_device_instance))

    sfm27_power_range = BNode()
    wsd_ffd_rdf.add((sfm27_power_range, SCHEMA.minValue, Literal(3)))
    wsd_ffd_rdf.add((sfm27_power_range, SCHEMA.maxValue, Literal(24)))
    wsd_ffd_rdf.add((sfm27_power_range, SCHEMA.unitCode, QUDT_UNIT.V))
    wsd_ffd_rdf.add((sfm27_instance, SSN_SYSTEM.OperatingPowerRange, sfm27_power_range))

    sfm27_sound_out = BNode()
    wsd_ffd_rdf.add((sfm27_sound_out, SCHEMA.greaterOrEqual, Literal(95)))
    wsd_ffd_rdf.add((sfm27_sound_out, SCHEMA.unitCode, QUDT_UNIT.DeciB))
    wsd_ffd_rdf.add((sfm27_instance, sound_output, sfm27_sound_out))

    # EdgeDevice instance
    wsd_ffd_rdf.add((edge_device_instance, RDF.type, edge_device))
    wsd_ffd_rdf.add((edge_device_instance, GEO.lat, Literal(55.701)))
    wsd_ffd_rdf.add((edge_device_instance, GEO.long, Literal(12.552)))

    wsd_ffd_rdf.add((edge_device_instance, SOSA.hosts,
                     Bag(wsd_ffd_rdf, BNode(),
                         [dht11_instance, mq2_instance, ky026_instance, sfm27_instance]).uri
                     ))
    wsd_ffd_rdf.add((edge_device_instance, is_routed_by,
                     Bag(wsd_ffd_rdf, BNode(), [router_instance]).uri
                     ))

    ##############################
    # RDF Serialization
    ##############################
    if len(sys.argv) > 1:
        wsd_ffd_rdf.serialize(destination=os.getcwd()+'/'+sys.argv[1]+'-xml.rdf', format='xml')
        wsd_ffd_rdf.serialize(destination=os.getcwd()+'/'+sys.argv[1]+'-pretty-xml.rdf', format='pretty-xml')
        wsd_ffd_rdf.serialize(destination=os.getcwd()+'/'+sys.argv[1]+'-turtle.ttl', format='turtle')
    else:
        wsd_ffd_rdf.serialize(destination=os.getcwd()+'/wsd-ffd-xml.rdf', format='xml')
        wsd_ffd_rdf.serialize(destination=os.getcwd()+'/wsd-ffd-pretty-xml.rdf', format='pretty-xml')
        wsd_ffd_rdf.serialize(destination=os.getcwd()+'/wsd-ffd-turtle.ttl', format='turtle')
