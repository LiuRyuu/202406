import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_website(keyword):
    if keyword == '國文':
        url = 'https://stv.naer.edu.tw/learning/junior.jsp?cat=48'
    elif keyword == '英文':
        url = 'https://stv.naer.edu.tw/learning/junior.jsp?cat=49'
    elif keyword == '數學':
        url = 'https://stv.naer.edu.tw/learning/junior.jsp?cat=12'
    elif keyword == '歷史':
        url = 'https://stv.naer.edu.tw/learning/junior.jsp?cat=51'
    elif keyword == '地理':
        url = 'https://stv.naer.edu.tw/learning/junior.jsp?cat=52'
    elif keyword == '公民':
        url = 'https://stv.naer.edu.tw/learning/junior.jsp?cat=53'
    elif keyword == '生物':
        url = 'https://stv.naer.edu.tw/learning/junior.jsp?cat=54'
    elif keyword == '理化':
        url = 'https://stv.naer.edu.tw/learning/junior.jsp?cat=55'
    elif keyword == '地球科學':
        url = 'https://stv.naer.edu.tw/learning/junior.jsp?cat=56'
    else:
        return '沒有這個科目'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    tab_content = soup.find('div', class_='tab-content')
    try:
      if tab_content:
          links = tab_content.find_all('a', href=True)
          for link in links:
              title = link.find_previous('p', class_='resource-title')
              if title:
                  title_text = title.text.strip()
                  href = urljoin(url, link['href'])
                  print(f' [{title_text}] -> ')
                  print(f'  {href}')
      return f'以上是科目: {keyword} 的相關教材影片'           
    except:
      return '沒有這個科目關教材影片'
