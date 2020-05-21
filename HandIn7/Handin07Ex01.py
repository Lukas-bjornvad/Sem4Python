import bs4
import requests
import time
import re
#Opgave er fra free range chickens
req = requests.get('http://kultunaut.dk/perl/searchlist/type-nynaut?Genre=Familiefilm&Genre=Komedie%2FRomantik&Genre=Action%2FDrama&Genre=Science%20Fiction&Genre=Thriller%2FGyser&Genre=Tegnefilm%2FAnimation&Genre=Dokumentar&Genre=Andre%20Film&&Area=&periode=')
soup = bs4.BeautifulSoup(req.text, 'html.parser')
movies = soup.findAll("div", attrs={"style": "clear:both"})
links = soup.findAll('a', attrs={'href': re.compile("^http"),})
numbermovies = len(movies)
numberlinks = len(links)
#Opgave 1
print (f"Der er {numbermovies} film")
#Den skriver det hele ud men der mangler
#Opgave 2
for m in movies:
    print(m.getText())

print (f"Der er {numberlinks} links")