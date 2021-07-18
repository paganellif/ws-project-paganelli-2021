from rdflib import Namespace, Graph, URIRef, RDF


def print_graph(graph: Graph):
    for subj, pred, obj in graph:
        # check if there is at least one triple in the Graph
        if (subj, pred, obj) not in graph:
            raise Exception("No triple in the graph!")
        else:
            print("Subject: "+subj+" Predicate: "+pred+" Object: "+obj)


if __name__ == '__main__':

    # Create Forest Fire Detection Graph
    ffd_graph: Graph = Graph()

    SOSA: Namespace = Namespace(' http://www.w3.org/ns/sosa/')

    ffd_graph.namespace_manager.bind('sosa', SOSA)

    thermistor_a = URIRef("http://example.org/thermistor_a")
    ffd_graph.add((thermistor_a, RDF.type, SOSA.Sensor))

    temperature = URIRef("http://example.org/temperature")
    ffd_graph.add((temperature, RDF.type, SOSA.ObservableProperty))

    ffd_graph.add((thermistor_a, SOSA.observes, temperature))
    ffd_graph.add((temperature, SOSA.isObservedBy, thermistor_a))

    # Print graph
    print_graph(ffd_graph)
