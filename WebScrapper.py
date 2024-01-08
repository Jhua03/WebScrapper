import requests
import pandas as pd
from bs4 import BeautifulSoup


URL = "https://pythonjobs.github.io"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("section", class_="job_list")
job_elements = results.find_all("div", class_="job")
pair_list = []
weblist = []
for job_element in job_elements:
    pair_list = []
    links = job_element.find_all("a")
    title_element = links[1]
    company_element = job_element.find("i", class_= "i-company")
    location_element = job_element.find("i", class_= "i-globe")
    link_url = links[1]["href"]
    pair_list.append(title_element.text.strip())
    pair_list.append(company_element.parent.text.strip())
    pair_list.append(location_element.parent.text.strip())
    pair_list.append(f"Apply here: {link_url}\n")
    weblist.append(pair_list)
    # print(title_element.text.strip())
    # print(company_element.parent.text.strip())
    # print(location_element.parent.text.strip())
    # print(f"Apply here: {link_url}\n")
    # print()
# for pair in weblist:
    # print(pair[0])
    # print(pair[1])
    # print(pair[2])
    # print(pair[3])
    # print()
df = pd.DataFrame(weblist, columns=['Title', 'Company', 'Location','URL'])
df.to_csv('FirstWS.csv')

## Filtering specific keyword
# python_jobs = results.find_all(
#     "h2", string=lambda text: "python" in text.lower()
# 
# python_job_elements = [
#     h2_element.parent.parent.parent for h2_element in python_jobs
