import csv
# import module
import requests
from bs4 import BeautifulSoup
  
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
  
# user define function
# Scrape the data
def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text
  
  
def html_code(url):
  
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
  
    # display html code
    return (soup)

  
def cus_data(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    cus_list = []
  
    for item in soup.find_all("span",class_="review-text"):
        data_str = data_str + item.get_text()
        cus_list.append(data_str)
        data_str = ""
    return cus_list
  


urls = ["https://www.amazon.in/Nike-Mens-Revolution-Running-Shoe/product-reviews/B0BPMRTPLD/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&filterByStar=five_star&pageNumber=1",
"https://www.amazon.in/Nike-Mens-Lebron-Running-Shoe/product-reviews/B0B5Z9SJZ8/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&filterByStar=five_star&pageNumber=1",
"https://www.amazon.in/Nike-Men-Runallday-Running-Shoes/product-reviews/B0BW43FTVD/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
"https://www.amazon.in/Nike-Men-Runallday-Running-Shoes/product-reviews/B0BW43FTVD/ref=cm_cr_getr_d_paging_btm_next_5?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=five_star",
"https://www.amazon.in/Nike-Men-Runallday-Running-Shoes/product-reviews/B0BW43FTVD/ref=cm_cr_getr_d_paging_btm_next_5?ie=UTF8&reviewerType=all_reviews&pageNumber=2&filterByStar=five_star",
"https://www.amazon.in/Nike-Men-Runallday-Running-Shoes/product-reviews/B0BW43FTVD/ref=cm_cr_getr_d_paging_btm_next_5?ie=UTF8&reviewerType=all_reviews&pageNumber=3&filterByStar=five_star",
"https://www.amazon.in/Nike-Men-Runallday-Running-Shoes/product-reviews/B0BW43FTVD/ref=cm_cr_getr_d_paging_btm_next_5?ie=UTF8&reviewerType=all_reviews&pageNumber=4&filterByStar=five_star",
"https://www.amazon.in/Nike-Men-Runallday-Running-Shoes/product-reviews/B0BW43FTVD/ref=cm_cr_getr_d_paging_btm_next_5?ie=UTF8&reviewerType=all_reviews&pageNumber=5&filterByStar=five_star",
"https://www.amazon.in/Nike-Men-Runallday-Running-Shoes/product-reviews/B0BW43FTVD/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&filterByStar=five_star&pageNumber=1",
"https://www.amazon.in/Nike-Men-Runallday-Running-Shoes/product-reviews/B0BW43FTVD/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&filterByStar=five_star&pageNumber=2",
]

reviews = ["Content"]
for url in urls:    
    cus_res = []
    
    while len(cus_res)==0:
        soup=html_code(url)
        cus_res = cus_data(soup)
    print(cus_res)
    reviews.extend(cus_res)

for review in reviews:
    print(review)


with open('web_scraped.csv', 'w+', newline='') as file:
    writer = csv.writer(file)
    
    for review in reviews:
        writer.writerow([review])