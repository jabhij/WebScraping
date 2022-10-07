# importing beautifulsoup library
from bs4 import BeautifulSoup

# accessing the path of the file
with open('../Main.html', 'r') as html_file:
  content = html_file.read()
  
  soup = BeautifulSoup(content, 'lxml')
  # print(soup.prettify())
  
  # grabbing the info
  tags = soup.find('h5')
  #print (tags)
