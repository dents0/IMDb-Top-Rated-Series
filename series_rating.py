import requests
from bs4 import BeautifulSoup
import pandas

data = requests.get("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250",
                    headers={"Accept-language": "en-US"})
soup = BeautifulSoup(data.text, "html.parser")

tbl = soup.find("table", {"class": "chart full-width"})
tbody = tbl.find("tbody")

ranks = [tr.select(".titleColumn")[0].get_text().split("\n")[1].strip()
         for tr in tbody.find_all("tr")]
titles = [tr.select(".titleColumn a")[0].get_text() for tr in tbody.find_all("tr")]
released = [tr.select(".titleColumn .secondaryInfo")[0].get_text().strip("()")
            for tr in tbody.find_all("tr")]
ratings = [tr.select(".ratingColumn strong")[0].get_text() for tr in tbody.find_all("tr")]
votes = [tr.find("td", {"class": "ratingColumn"}).strong.get("title").split()[3]
         for tr in tbody.find_all("tr")]

series = pandas.DataFrame({
    "Rank": ranks,
    "Title": titles,
    "Year": released,
    "Rating": ratings,
    "Votes": votes
}, index=ranks)

print("\n", series)
series.to_excel("top_rated_series.xlsx", index=False)
