from typing import Any, Union

from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON, N3


def getData():
    sparql = SPARQLWrapper('https://dbpedia.org/sparql')
    sparql.setQuery('''
                    PREFIX : <http://dbpedia.org/resource/>
                    SELECT ?name ?birth ?img ?description
                    WHERE {
                      #?person a dbo:Scientist .
                      ?person dbo:birthPlace :India .
                      ?person dbo:birthDate ?birth .
                      ?person foaf:name ?name .
                      ?person rdfs:comment ?description .
                      optional { ?person dbo:thumbnail ?img }
                      FILTER (LANG(?description) = 'en') . 
                      FILTER (LANG(?name) = 'en') . 
                      #FILTER (?birth > "1900-02-09"^^xsd:dateTime) .
                      FILTER (DAY(?birth)= DAY(NOW()))
                      FILTER (MONTH(?birth)= MONTH(NOW()))
                      #FILTER (DAY(?birth)= 9) .
                      #FILTER (MONTH(?birth)= 2) .
                      } 
                    ORDER BY ?name
                    ''')
    sparql.setReturnFormat(JSON)
    # sparql = SPARQLWrapper("https://dbpedia.org/sparql", agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11")
    qres = sparql.query().convert()
    return qres


