from rdflib import Namespace, Graph, URIRef, RDF, RDFS, Literal
import os

if __name__ == '__main__':

    ##############################
    # Graph Definition
    ##############################
    wsd_ffd_rdf: Graph = Graph()
    base_ontology: str = 'http://wsn-ffd.org/'

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
    wsd_ffd_rdf.add((dht11, RDFS.seeAlso, Literal('https://www.adafruit.com/product/386')))
    wsd_ffd_rdf.add((dht11, RDFS.subClassOf, SSN.Sensor))

    # MQ2
    mq2 = URIRef(value='MQ2', base=base_ontology)
    wsd_ffd_rdf.add((mq2, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((mq2, RDFS.comment, Literal('MQ2 Gas sensor for sensing LPG, Smoke, Alcohol, Propane, Hydrogen, Methane and Carbon Monoxide')))
    wsd_ffd_rdf.add((mq2, RDFS.seeAlso, Literal('https://www.mouser.com/datasheet/2/321/605-00008-MQ-2-Datasheet-370464.pdf')))
    wsd_ffd_rdf.add((mq2, RDFS.subClassOf, SSN.Sensor))

    # KY026
    ky026 = URIRef(value='KY026', base=base_ontology)
    wsd_ffd_rdf.add((ky026, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((ky026, RDFS.comment, Literal('KY-026 Flame Sensor Module')))
    wsd_ffd_rdf.add((ky026, RDFS.seeAlso, Literal('https://datasheetspdf.com/pdf/1402037/Joy-IT/KY-026/1')))
    wsd_ffd_rdf.add((ky026, RDFS.subClassOf, SSN.Sensor))

    # SFM27
    sfm27 = URIRef(value='SFM27', base=base_ontology)
    wsd_ffd_rdf.add((sfm27, RDF.type, RDFS.Class))
    wsd_ffd_rdf.add((sfm27, RDFS.comment, Literal('SFM-27 active buzzer')))
    wsd_ffd_rdf.add((sfm27, RDFS.seeAlso, Literal('https://opencircuit.shop/resources/file/7379f0193d4549c771f0d61bd31d06b316cd4706466/SFM27-Datasheet.pdf')))
    wsd_ffd_rdf.add((sfm27, RDFS.subClassOf, SSN.Actuator))

    # Property Definition
    is_routed_by = URIRef(value='isRoutedBy', base=base_ontology)
    wsd_ffd_rdf.add((is_routed_by, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((is_routed_by, RDFS.comment, Literal('Router node that can route data to another node')))
    wsd_ffd_rdf.add((is_routed_by, RDFS.domain, SSN.System))
    wsd_ffd_rdf.add((is_routed_by, RDFS.range, SOSA.Platform))

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

    gas_measurement = URIRef(value='GasMeasurement', base=base_ontology)
    wsd_ffd_rdf.add((gas_measurement, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((gas_measurement, RDFS.comment, Literal('Sensor/Actuator operating humidity condition')))
    wsd_ffd_rdf.add((gas_measurement, RDFS.domain, SSN.System))
    wsd_ffd_rdf.add((gas_measurement, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((gas_measurement, RDFS.subPropertyOf, SSN_SYSTEM.MeasurementRange))

    dht11_temp_accuracy = URIRef(value='DHT11TempAccuracy', base=base_ontology)
    wsd_ffd_rdf.add((dht11_temp_accuracy, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((dht11_temp_accuracy, RDFS.comment, Literal('DHT11 temperature accuracy')))
    wsd_ffd_rdf.add((dht11_temp_accuracy, RDFS.domain, dht11))
    wsd_ffd_rdf.add((dht11_temp_accuracy, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((dht11_temp_accuracy, RDFS.subPropertyOf, SSN_SYSTEM.Accuracy))

    dht11_hum_accuracy = URIRef(value='DHT11HumAccuracy', base=base_ontology)
    wsd_ffd_rdf.add((dht11_hum_accuracy, RDF.type, RDF.Property))
    wsd_ffd_rdf.add((dht11_hum_accuracy, RDFS.comment, Literal('DHT11 humidity accuracy')))
    wsd_ffd_rdf.add((dht11_hum_accuracy, RDFS.domain, dht11))
    wsd_ffd_rdf.add((dht11_hum_accuracy, RDFS.range, RDFS.Literal))
    wsd_ffd_rdf.add((dht11_hum_accuracy, RDFS.subPropertyOf, SSN_SYSTEM.Accuracy))


    ##############################
    # RDF Serialization
    ##############################
    wsd_ffd_rdf.serialize(destination=os.getcwd()+'/wsd-ffd-xml.rdf', format='xml')
    wsd_ffd_rdf.serialize(destination=os.getcwd()+'/wsd-ffd-pretty-xml.rdf', format='pretty-xml')
    wsd_ffd_rdf.serialize(destination=os.getcwd()+'/wsd-ffd-turtle.ttl', format='turtle')
