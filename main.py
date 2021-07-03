import rdflib

if __name__ == '__main__':
    g = rdflib.Graph()
    g.load('http://dbpedia.org/resource/Semantic_Web')

    for s, p, o in g:
        print(s, p, o)
