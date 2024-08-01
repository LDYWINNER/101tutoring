import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch"


def extract_indeed_pages():
    result = requests.get(URL)
    # print(result.text)

    soup = BeautifulSoup(result.text, "html.parser")
    # print(soup)

    pagination = soup.find("div", {"class": "pagination"})
    # print(pagination)

    links = pagination.find_all('a')
    # print(links)

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0 * LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("h2", {"class": "jobTitle"})
    # print(results)

    for h2 in results:
        spans = h2.find_all("span")
        for span in spans:
            if span.get("title") not in ["new", None]:
                print(span.get("title"))
                jobs.append(span.get("title"))

    return jobs
