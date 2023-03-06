# RENAME FILE as:  scrape_mars.py

# •	Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a 
    # function called scrape that will execute all of your scraping code from above and return one 
    # Python dictionary containing all of the scraped data.



# Import dependencies
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as soup
#from flask_pymongo import PyMongo
import pandas as pd
import time


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Create an empty dict to save info to Mongo
    # mars_data = {}
    print("starting to scrape")

    
###  1  ####################################################################
   
    ## MARS NEWS Scraping

    # URL of page to be scraped
    url = 'https://redplanetscience.com'

    # Call visit on our browser and pass the url we want to scrape
    browser.visit(url)

    # Let it sleep for 1 second
    time.sleep(1)

    # Return all the HTML on the page
    html = browser.html

    # Create Beautiful Soup object, pass in our html and parse with'html.parser'
    results = soup(html, "html.parser")

    # Collect the NEWS TITLE and PARAGRAPH TEXT 
    article = results.find_all('div', class_='content_title')[0].text
    text = results.find_all('div', class_='article_teaser_body')[0].text
       

###  2  ####################################################################
   
    ## FEATURED IMAGE Scraping

    # URL of page to be scraped
    url = 'https://spaceimages-mars.com'

    # Call visit on our browser and pass the url we want to scrape
    browser.visit(url)

    # Let it sleep for 1 second
    time.sleep(1)

    # BUTTON
    button_elem = browser.find_by_tag("button")[1]
    button_elem.click()

    # Return all the HTML on the page
    html = browser.html

    # Create Beautiful Soup object, pass in our html and parse with'html.parser
    results = soup(html, 'html.parser')

    # Collect the FEATURED IMAGE from the scraped data
    relative_image_path = results.find('img', class_='fancybox-image').get("src")
    featured_img_url = url + relative_image_path
        

###  3  ####################################################################
   
    ## MARS FACTS TABLE Scraping

    # URL of page to be scraped
    url = 'https://galaxyfacts-mars.com/'

    # Read the table with Pandas
    tables = pd.read_html(url)

    # Modify the table rows
    df = tables[0]
    df.columns = ['Feature', 'Mars', 'Earth']
    df = df.drop([df.index[0]])

    # Extract the code to the new table
    mars_facts_table = df.to_html


###  4  ####################################################################
   
    ## MARS HEMISPHERS Scraping

    # URL of page to be scraped
    url = 'https://marshemispheres.com/'

    # Call visit on our browser and pass the url we want to scrape
    browser.visit(url)

    # Let it sleep for 1 second
    time.sleep(1)

    # Return all the HTML on the page
    html = browser.html

    # Create Beautiful Soup object, pass in our html and parse with'html.parser
    results = soup(html, 'html.parser')

    # Click thru to high res image
    button_elem = browser.find_by_tag("thumb")[1]
    button_elem.click()

    button_elem = browser.find_by_tag("wide-image-toggle")[1]
    button_elem.click()

    # Return all the HTML on the page
    html = browser.html

    # Create Beautiful Soup object, pass in our html and parse with'html.parser
    results = soup(html, 'html.parser')

    # Build dictionary for FEATURED IMAGE from the scraped data
    hemis = results.find_all('div', class_='item')

<img class="thumb" src="images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png" alt="Cerberus Hemisphere Enhanced thumbnail">

<a id="wide-image-toggle" class="open-toggle" href="#open">Open</a>

<img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://marshemispheres.com/images/full.jpg" width="414" height="414">

    # Create an empty list to store the data
    hemisphere_image_urls = []

    for hemi in hemis:
        title = hemi.find('h3')
        img_url = hemi.find('img', class_='thumb')['src']
        hemisphere_image_urls.append({'title': title,'image_url': img_url})

#####################################################################

    # Save all info in the MARS DICTIONARY 
    mars_dict = {
        'article' : article,
        "text": text,
        "featured_image" : featured_img_url,
        "mars_facts_table": str(mars_facts_table),
        "hemisphere_images": hemisphere_image_urls
    }

    # Quit the browser
    browser.quit()

    # Return our dictionary
    return mars_dict
