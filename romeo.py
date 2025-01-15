import PyPDF2
from PyPDF2 import PdfReader
from collections import Counter
import re

def word_calc(search: str):

    #Grab the file and assign to our variable of choice 
    Shakespeare = PyPDF2.PdfReader("Romeo.pdf")

    #Set the range of the number of pages read//numbers of items in the range 'Shakespeare'
    Pages = len(Shakespeare.pages)             
    
    #Initializing an array
    Ranker = []

    #Setting the total equal to 0
    total = 0  

    #for loop that will loop through the text
    for i in range(Pages):
        current_page = Shakespeare.pages[i]
        text = current_page.extract_text()

        #if Statement, that is searching text for our case//re.IGNORCASE creates a case-insensitivity where a = A or a
        if text and re.findall(search, text, re.IGNORECASE):

            count_page = len(re.findall(search, text, re.IGNORECASE))
            Ranker.append((count_page, i))
            total += count_page
    #if statement that returns the count and number of occurrences        
    if Ranker:
        for count, page_num in Ranker:
            print(f"Found {count} occurrences of '{search}' on page {page_num + 1}")
           
    else:
        print(f"No occurrences of '{search}' found in the document.")
    
    print(f"Total occurences of '{search}': {total}")

#Calling our function
word_calc("Love")  # Replace 'love' with the word you're searching for


    
   
   





















'''reader = PdfReader("romeo-and-juliet_PDF_FolgerShakespeare.pdf")
page = reader.pages[]
print(page.extract_text())
#print(page.)'''
















#print(PyPDF2.__version__)

