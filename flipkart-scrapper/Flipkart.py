import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_Url = 'https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
uClient = uReq(my_Url)
page_html = uClient.read()
print(page_html)
uClient.close()
page_soup = soup(page_html, "html.parser")
print(page_soup.p)

containers = page_soup.find_all("div", {"class": "_3O0U0u"})
filename = "products.csv"
f = open(filename, "w")
headers = "Product_Title, Ram_Size\n"

f.write(headers)
print(len(containers))
print(containers[0])
container = containers[0]
print(container.div)
for container in containers:
    title_container = container.find_all("div", {"class": "_3wU53n"})
    product_name = title_container[0].text

    print(product_name)

    f.write(product_name+ "\n")
f.close()