# web-scraping-challenge:    Mission to Mars
<img width="1050" alt="Screen Shot 2023-03-11 at 12 15 47 PM" src="https://user-images.githubusercontent.com/44728723/224502506-99587731-f543-4c0a-9b79-59979fe482b3.png">


### Built web application that scrapes various websites for data related to the Mission to Mars and displayed the information in a single HTML page.


## Approach

(1) Using Pandas and Juptyer Notebook, scraped the following websites for source data:
- https://redplanetscience.com for the most recent NASA news regarding the Mission to Mars
- https://spaceimages-mars.com for the URL of the featured Mars image
- https://galaxyfacts-mars.com for the Mars Facts HTML table
- https://marshemispheres.com for the images and names of the 4 hemispheres

(2) Use MongoDB with Flask templating, created a new HTML page that displays all of the information that was scraped from the URLs above.
- Converted Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of the scraping code from step 1 above and return one Python dictionary containing all of the scraped data.
- Created a route called /scrape that imports the scrape_mars.py script and call the scrape function.
- Stored the return value in Mongo as a Python dictionary.
- Created a root route / that queries the Mongo database and passes the mars data into an HTML template to display the data.
- Created a template HTML file called index.html that takes the mars data dictionary and displays all of the data in the appropriate HTML elements. 
 
## Example Website App

- To see the live version of the website application, download the source code and run the following in order:  scrape_mars.py / app.py / index.html
- Click on the "Scrape New Data" button to load updated information

<img width="700" alt="Screen Shot 2023-03-16 at 9 13 22 AM" src="https://user-images.githubusercontent.com/44728723/225627838-773faaeb-3f72-4c98-9088-e8c59674cb2d.png">



## Technology
- pandas
- beautifulsoup
- requests/splinter
- flask
- mongoDB
