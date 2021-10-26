from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery
import os
import sys

if __name__ == '__main__':
    g = Graph()
    f = Graph()
    g.parse(sys.argv[1] if len(sys.argv) > 1 else os.getcwd()+'/'+'wsd-ffd-turtle-owl.ttl')

    if len(sys.argv) > 1:
        f.parse(sys.argv[2])

    # Print the number of "triples" in the Graph
    print(f"Graph {sys.argv[1]} has {len(g)} statements.")

    if len(sys.argv) > 1:
        print(f"Graph {sys.argv[2]}  has {len(g)} statements.")
        if len(g) != len(f):
            exit(1)

    prefix = """
    prefix sosa: <http://www.w3.org/ns/sosa/>
    prefix ssn: <http://www.w3.org/ns/ssn/>
    prefix ssn-system: <http://www.w3.org/ns/ssn/systems/>
    prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
    prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#>
    prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#>
    prefix schema: <http://schema.org/>
    prefix wsn-ffd-rdf: <https://gitlab.com/paganelli.f/ws-project-paganelli-1920/-/raw/develop/wsd-ffd-pretty-xml.rdf>
    
    """

    query = prepareQuery(prefix+"""
    select ?n ?serial_num ?lat ?long
    where {
        { ?n rdf:type <http://www.w3.org/2002/07/owl#EdgeDevice>} 
            union { ?n rdf:type <http://wsn-ffd.org/EdgeDevice>} 
            union { ?n rdf:type <http://www.w3.org/2002/07/owl#RouterNode>}
            union { ?n rdf:type <http://www.w3.org/2002/07/owl#CoordinatorNode>} .
        ?n geo:lat ?lat .
        ?n geo:long ?long .
        ?n wsn-ffd-rdf:SerialNum ?serial_num .
    }
    order by asc(?serial_num)
    """)

    print("------WSN nodes spatial position------")
    for row in g.query(query):
        print(f"[node]{row.n}\t-\t[serial num]{row.serial_num}\t-\t[lat]{row.lat}\t-\t[long]{row.long}")

    if len(sys.argv) > 1:
        if len(g.query(query)) != len(f.query(query)):
            exit(1)

    query = prepareQuery(prefix+"""
    select ?n ?is_routed_by ?serial_num
    where {
        ?n wsn-ffd-rdf:isRoutedBy ?is_routed_by .
        ?n wsn-ffd-rdf:SerialNum ?serial_num .
        filter (?serial_num != 'IT234GJ55500001') .
    }
    """)

    print("\n------WSN nodes routing table------")
    for row in g.query(query):
        print(f"[node]{row.n}\t-\t[is routed by]{row.is_routed_by}")

    if len(sys.argv) > 1:
        if len(g.query(query)) != len(f.query(query)):
            exit(1)