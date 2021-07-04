import rdflib
from rdflib import URIRef, RDF, FOAF, Literal, XSD

if __name__ == '__main__':
    '''
    # create a Graph
    g = rdflib.Graph()

    # parse in an RDF file hosted on the Internet
    result = g.parse("http://www.w3.org/People/Berners-Lee/card")

    # loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        # check if there is at least one triple in the Graph
        if (subj, pred, obj) not in g:
            raise Exception("It better be!")

    # print the number of "triples" in the Graph
    print("graph has {} statements.".format(len(g)))
    # prints graph has 86 statements.

    # print out the entire Graph in the RDF Turtle format
    print(g.serialize(format="turtle").decode("utf-8"))
    '''
    # create a Graph
    g = rdflib.Graph()

    # Create an RDF URI node to use as the subject for multiple triples
    donna = URIRef("http://example.org/donna")

    # Add triples using store's add() method.
    g.add((donna, RDF.type, FOAF.Person))
    g.add((donna, FOAF.nick, Literal("donna", lang="ed")))
    g.add((donna, FOAF.name, Literal("Donna Fales")))
    g.add((donna, FOAF.mbox, URIRef("mailto:donna@example.org")))

    # Add another person
    ed = URIRef("http://example.org/edward")

    # Add triples using store's add() method.
    g.add((ed, RDF.type, FOAF.Person))
    g.add((ed, FOAF.nick, Literal("ed", datatype=XSD.string)))
    g.add((ed, FOAF.name, Literal("Edward Scissorhands")))
    g.add((ed, FOAF.mbox, URIRef("mailto:e.scissorhands@example.org")))

    # Iterate over triples in store and print them out.
    print("--- printing raw triples ---")
    for s, p, o in g:
        print((s, p, o))

    # For each foaf:Person in the store, print out their mbox property's value.
    print("--- printing mboxes ---")
    for person in g.subjects(RDF.type, FOAF.Person):
        for mbox in g.objects(person, FOAF.mbox):
            print(mbox)

    # Bind the FOAF namespace to a prefix for more readable output
    g.bind("foaf", FOAF)

    # print all the data in the Notation3 format
    print("--- printing mboxes ---")
    print(g.serialize(format='n3').decode("utf-8"))
