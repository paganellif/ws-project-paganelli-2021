from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery
from rdflib.term import URIRef, Literal, BNode
from rdflib.container import Bag
from rdflib.namespace import Namespace, RDF, RDFS
import os

if __name__ == '__main__':
    g = Graph()
    g.load(os.getcwd()+'/wsd-ffd-xml-owl.rdf')

    # Loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        # Check if there is at least one triple in the Graph
        if (subj, pred, obj) not in g:
            raise Exception("It better be!")
        # Print triple
        print(f"[sub]{subj} - [pred]{pred} - [obj]{obj}")

    # Print the number of "triples" in the Graph
    print(f"Graph g has {len(g)} statements.")

    query = prepareQuery("""
    prefix sosa: <http://www.w3.org/ns/sosa/>
    prefix ssn: <http://www.w3.org/ns/ssn/>
    prefix ssn-system: <http://www.w3.org/ns/ssn/systems/>
    prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
    prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#>
    prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#>
    prefix schema: <http://schema.org/>
    prefix wsn-ffd-rdf: <https://gitlab.com/paganelli.f/ws-project-paganelli-1920/-/raw/develop/wsd-ffd-pretty-xml.rdf>
    
    select *
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

    print("------WSN nodes position------")
    for row in g.query(query):
        print(f"[node]{row.n}\t-\t[serial num]{row.serial_num}\t-\t[lat]{row.lat}\t-\t[long]{row.long}")
