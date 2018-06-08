## Set up

```
git clone https://github.com/oksanatkach/ucu-rule-based.git
virtualenv ucu-rule-based
source ucu-rule-based/bin/activate
pip install -r requirements.txt
```

Start working in an IDE of your choice. Run in terminal to test your progress.

## Practical Tasks

# Task 1: sparql.py
Write a query to dbpedia to download city names with the population of at least 10000 people.
You can also use the browser: https://dbpedia.org/sparql

#Task 2: date_regex.py
Write a set of regex to recognize various date expressions, such as:
	```01/12/1995
	August 23d, 2005
	31st of May 2017```

Once the date is found, parse it into the ```'%B %d, %Y’``` format (June 5th, 2018).

# Task 3: preprocessing.py
Complete the function to preprocess raw text.

# Task 4: NER.py
Upload the gazetteer.
Using heuristic knowledge, devise 3-4 rules for what constitutes a location.

Hints:
Check if it’s in the gazetteer.
Check if the POS-tag is for proper noun.
Check if there is a preposition POS-tag (‘IN’ or ‘TO’) before the candidate location.

# Task 5: greeting in chatbot_main.py
Write a simple greeting function. Return a randomly picked greeting from your list of greetings.

# Task 6: chatbot_flight.py
Write a function that parses a flight booking request for departure, destination and date.
