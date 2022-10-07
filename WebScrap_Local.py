***

Scrapping a HTML file stored at local machine
'../Main.html'

***

# importing beautifulsoup library
from bs4 import BeautifulSoup

# accessing the path of the file
with open('../Main.html', 'r') as html_file:
  content = html_file.read()
  
  soup = BeautifulSoup(content, 'lxml')
  # print(soup.prettify())
  
  # grabbing the info - course tags
  # course_tags = soup.find('h5')  # finds only the first h5 tag
  course_tags = soup.find_all('h5')  # finds all the h5 tags
  # print(tags)
  
  for courses in course_tags:
    print(course.text)

  # grabbing the info - course name and price
  course_cards = soup.find_all(div, class_='card')
  for cards in course_cards:
    #print(cards)
    course_name = course.h5.text
    course_price = course.a.text.split()[-1]
    
    print(course_name)
    print(course_price)
    print(f'{course_name} costs {course_price}')
    
