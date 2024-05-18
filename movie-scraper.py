import requests
import os
from bs4 import BeautifulSoup

getMovieTitle = input("Type the movie title: ")

movieUrl = 'https://yts.mx/browse-movies/example/all/all/0/latest/0/all'
movieUrl = movieUrl.replace("example", getMovieTitle)

print("Please wait....\n")
#request data from given url
requestData = requests.get(movieUrl)

#soup parser
soup = BeautifulSoup(requestData.content,'html.parser')

def movieInfo():
  option1 = input("\nPaste the movie url: ")
  print("Please wait patiently....")
  #reuest the html data of the movie url
  option1 = requests.get(option1)
  #parse url data
  soup = BeautifulSoup(option1.content,'html.parser')
  #finding the movie plot with the elemnt 'synopsis'
  synopsis = soup.find('div',id='synopsis')
  moviePlot = synopsis.find('p').text.strip()
  #clears the previous text on screen
  os.system("clear")
  
  print("\n",moviePlot)
  
def movieFinder():
  result = ""
  #scanning the data for urls
  scanUrl = soup.find_all('div', class_='browse-movie-wrap')
  
  #filtering movie url
  for url in scanUrl:
    links = url.find('a')['href']
    print(links)
    result += "found"
  #printing error message when movie title is not found
  if result == "":
    print("\nMovie not found try, something else")
  
  #this statement works, if movie url's are found  
  if result != "":
    movieInfo()
    
movieFinder()

 
