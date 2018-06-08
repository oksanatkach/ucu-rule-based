from SPARQLWrapper import SPARQLWrapper, JSON

def get_country_description():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    sparql.setQuery(
        # TASK: Write your query here
                    )

    return sparql.query().convert()

jsn = get_country_description()['results']['bindings']
cities = [el['citylabel']['value'].split(', ')[0] for el in jsn]
cities.sort()
with open('cities.lst', 'w') as f:
    for el in cities:
        f.write(el.encode('utf-8') + '\n')
