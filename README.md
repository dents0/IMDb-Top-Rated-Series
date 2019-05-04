Scraping IMDb Top Rated TV Shows
================================
Licensing information: READ LICENCE
----
Project source can be downloaded from https://github.com/dents0/IMDb-Top-Rated-Series.git
----
Author
------
Deniss Tsokarev

Description
-----------
This script uses Python modules **Requests**, **Beautiful Soup 4** and **Pandas** to scrape [IMDb](https://www.imdb.com/) for it's top rated TV shows and saves the information in Excel-file.

The information includes show's **rank**, **title**, release **year**, **rating** and the number of **votes**.

Requirements
------------
Python 3.x 

Modules:

* [Requests](http://docs.python-requests.org/en/master/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/)

How to use
----------
1) Running **series_rating.py** will print out in a command-line interpreter 250 top rated TV shows according to IMDb:

![terminal](https://user-images.githubusercontent.com/28843507/56235191-39ea0400-6087-11e9-9b40-086189ef2458.PNG)

2) Excel-file **top_rated_series.xlsx** will be created in the same directory:

![files](https://user-images.githubusercontent.com/28843507/56235776-605c6f00-6088-11e9-9bb5-1960f2a91072.PNG)

3) The file will contain scraped information:

![excel](https://user-images.githubusercontent.com/28843507/56235868-9a2d7580-6088-11e9-8736-2101a9ea0724.PNG)
