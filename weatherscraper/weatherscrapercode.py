import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
page = requests.get("http://city.imd.gov.in/citywx/citywxnew.php?id=43063")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
n = 35
for n in range(35,55,1):
	td2 = soup.find_all('td')[n].get_text()

#	a= td2.split('\n')
#	if len(a) == 4:
#		print(a[-2])
#	elif len(a) == 3:	
#		print(a[-1])
	print(td2)
