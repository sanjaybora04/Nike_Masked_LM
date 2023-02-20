import csv

reviews=[]

with open("web_scraped.csv", 'r') as file:
  csvreader = csv.reader(file)

  for row in csvreader:
    if len(row[0])>5:
        reviews.append(row[0])

print("hello")

with open('web_scraped.csv', 'w+', newline='') as file:
    writer = csv.writer(file)
    
    for review in reviews:
        writer.writerow([review])