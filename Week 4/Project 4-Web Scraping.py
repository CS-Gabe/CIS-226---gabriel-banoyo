
from bs4 import BeautifulSoup # Importing library tools for web scraping.
import requests # Importing the requests library to handle HTTP requests.
from csv import writer # Importing the writer module from the csv library to write data to a CSV file.

url_input = input("Enter a website URL: ") # Input function from user for URL parsing requests.

web_data = requests.get(url_input) # activating the requests library using GET method to fetch the data and convert it to text.
soup = BeautifulSoup(web_data.content, 'lxml') # Creating a BeautifulSoup object and specifying the parser.
profile_personal_info = soup.get_text().split('\n') # get the name of the other information using the <br> tag from developer tools.

with open("Project_4_CIS226.csv", "w", newline='', encoding = 'utf8') as f: #Creating a new CSV file for every URL input to save the data
   thewriter = writer(f) # Creating a writer object to write data to the CSV file.
   cleaned_info = [info.strip() for info in profile_personal_info if info.strip()] # Using list comprehension to clean the data by 
   # removing any leading/trailing whitespace characters and empty strings.
   for info in cleaned_info: # Looping through the cleaned data.
       thewriter.writerow([info]) # Writing each piece of information to a new row in the CSV file.
    
print("Web scraping is executed, CSV filed created for the URL input.") # File creation and web scraping execution indicator.




