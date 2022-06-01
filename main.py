import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from pandas import DataFrame

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
"Dnt": "1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
}

def get_html(link):
    html_ver = requests.get(link, headers=headers)
    return html_ver.text

def get_list_of_animal_links(html_text):
   try:
    array_of_animals = []
    soup = BeautifulSoup(html_text, 'html.parser')
    for html_code in soup.find_all('li', 'list-item col-md-4 col-sm-6'):
        for links in html_code.find_all('a'):
            array_of_animals.append(links.get('href'))
    return array_of_animals
   except Exception as e:
       pass
def get_title_of_animal(link):
   try:
    soup = BeautifulSoup(get_html(link), 'html.parser')
    title = soup.find('div', 'col-12').h1.text
    return title
   except Exception as e:
       pass
def get_facts(link):
   try:
    soup = BeautifulSoup(get_html(link), 'html.parser')
    property = []
    description_of_property = []
    title_animal = get_title_of_animal(link)

    property.append("name")
    description_of_property.append(title_animal)

    info = soup.find('div', 'col-lg-8').dl
    for property_iterator in info.find_all('dt', 'col-sm-6 text-md-right'):
        property.append(property_iterator.text)

    for description_iterator in info.find_all('dd', 'col-sm-6'):
        description_of_property.append(description_iterator.text)

    od = OrderedDict()
    for prop in range(len(property)):
            od[property[prop]] = description_of_property[prop]
    return od
   except Exception as e:
       pass

dict_of_properties = {}
try:
    final_list_of_animals = []
    link = "https://a-z-animals.com/animals/"
    html_source_of_links = get_html(link)
    list_of_animal_links = get_list_of_animal_links(html_source_of_links)
except Exception as e:
    pass
for animal in list_of_animal_links:
    try:
        facts = get_facts(animal)
        for i,k in facts.items():
            dict_of_properties.setdefault(i)
        print(facts)
        final_list_of_animals.append(facts)
    except Exception as e:
        pass

finished_work = list(filter((None).__ne__, final_list_of_animals))
try:
    df = DataFrame(finished_work, columns=dict_of_properties.keys())
    df.to_csv('Animal.csv')
except Exception as e:
    pass

