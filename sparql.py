from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setReturnFormat(JSON)


def get_country_description():

    sparql.setQuery(
        "PREFIX  dbpedia-owl:  <http://dbpedia.org/ontology/>"
        "SELECT DISTINCT ?citylabel ?pop"
        "WHERE {"
            "?city rdf:type dbpedia-owl:City." # get city data from the City page
            "?city rdfs:label ?citylabel." # language labels
            "?city dbpedia-owl:populationTotal ?pop ." # get population data from the populationTotal page
            "FILTER (lang(?citylabel) = 'en' and ?pop>10000)" # only english names of cities with population over 10000
        "}"
                    )

    return sparql.query().convert()


if __name__ == "__main__":
    jsn = get_country_description()['results']['bindings']
    cities = [el['citylabel']['value'].split(', ')[0] for el in jsn]
    cities.sort()

    with open('gazetteers.lst', 'w', encoding='utf-8') as f:
        f.write('\n'.join(cities))
