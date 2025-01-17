import requests
from bs4 import BeautifulSoup
from flask import Flask,request,render_template

app = Flask(__name__)


def slink(url,t):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        if t:
            title = soup.find_all('h2')[0]
            cname = soup.find_all('img')[0]['alt'].replace('logo','')
            loc = soup.find('div',class_='sort-by-time')
            return title.text,cname,loc.text    
        else:
            title = soup.find('h1')
            loc = soup.find('div',class_='location')
            cname = soup.find('span',class_='company-name')
            return title.text,cname.text.strip().replace('at',''),loc.text.strip()
    except Exception as e:
        print(e)
    
def scrape_job(postion,location,t):
    pos = postion.replace(" ","+")
    url = f"https://www.google.co.in/search?q=site%3Alever.co+%22{pos}%22+%26+%22{location}%22"
    url1 = f"https://www.google.co.in/search?q=site%3Agreenhouse.io+%22{pos}%22+%26+%22{location}%22"
    response = requests.get(url) if t else requests.get(url1)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div')
    checklink = 'https://jobs.lever.co' if t else 'https://boards.greenhouse.io'
    tr = '- Lever' if t else '- Greenhouse'
    jobdir = {}
    for result in results:
        title = result.find('h3').text if result.find('h3') is not None else ''
        link = result.find('a')['href'] if result.find('a') is not None else ''
        if checklink in link:
            jobdir[link[link.index(checklink):link.index('&')]] = title.replace(tr,'')
    finjlist = []
    for i in jobdir:
        try:
            details = slink(i,t)
            print(details)
            job = [i,details[0],f'{details[1]} [{details[2]}]']
            finjlist.append(job) if len(job)==3 else None
        except Exception as e:
            print(e)
    print('='*150)
    print('='*150)
    return finjlist if len(finjlist)>0 else ['/','Couldn\'t srape jobs this time!','-','Try Again']

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('some.html')
    elif request.method == 'POST':
        title = request.form["title"]
        location = request.form["loc"]
        jobs = scrape_job(title,location,t=True) + scrape_job(title,location,t=False) 
        return render_template('some.html',jobs=jobs)


if __name__ == '__main__':
    app.run(debug=True)
    #scrape_google(pos,location)
