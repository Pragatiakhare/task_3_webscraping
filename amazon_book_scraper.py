import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=book&crid=M3PTG1FYB8XL&sprefix=book%2Caps%2C472&ref=nb_sb_noss_1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.amazon.com/',
    'DNT': '1'  # Do Not Track request header (optional)
}

response=requests.get(url,headers=headers)

soup = BeautifulSoup(response.text,"html.parser")

if response.status_code==200:
    print("ok")
else:
    print("not ok")    

book_name=soup.find_all('span',class_="a-size-medium a-color-base a-text-normal")
book_author=soup.find_all('a',class_="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style")
book_price=soup.find_all('span',class_="a-offscreen")



book_name_list=[]

for name,author,price in zip(book_name,book_author,book_price):

    b_name=name.get_text()
    b_author=author.get_text()
    b_price=price.get_text()

    book_name_list.append([b_name,b_author,b_price])



print("FOLLOWING BOOKS ARE AVAILABLE!!!!!!")

print(book_name_list)    




#CHECKING THE AVAILABILITY OF BOOk

def check_for_book(list):
    name_of_book = input("Enter name of book you want to search : ")
    for book in list:
        if book[0] == name_of_book:
            return name_of_book  + " " + "is available"
        
    else:
        return name_of_book  + " " + "is not available"

result1 = check_for_book(book_name_list)
print(result1)   


#Prints author and price of the book

def check_info_of_book(list):
    
    info_of_book = input("Enter name of book of which you want information :  ")
    for book in list:
     if info_of_book in book[0]:
        return "Author : " + book[1] + " and  " + "Price :" + book[2] 
    else:
       return "Book is not available"   
    
result2 = check_info_of_book(book_name_list)
print(result2)   




def extract_price(list):
   import re 
   list = [[int(re.search(r'\d+',x).group())if '₹' in x else x for x in sublist] for sublist in list]
   return list

result3 = extract_price(book_name_list)






def check_are_price_dec_or_inc(new_prices):
     global book_name_list
     for stored,new in zip(book_name_list,new_prices):
      
      if new[2]>stored[2]:
         return (f"Price increase : {stored[0]} ({stored[2]} -> {new[2]})")
      
      elif new[2]<stored[2]:
         return (f"Price decrease : {stored[0]} ({stored[2]} -> {new[2]})")
         
      else :
         return "Price are same as previous "   
      

new_prices=book_name_list
result4 = check_are_price_dec_or_inc(new_prices)
print(result4)     
   
           
