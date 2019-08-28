import requests
import MySQLdb
from bs4 import BeautifulSoup
import time

'''
database settings
'''
kHost = '127.0.0.1'
kUser = 'user'
kPassword = 'password'
kDatabase = 'HUAQI'
kTable = 'i_robot_news'


'''
clawler settings
'''
kGap = 600
kDelay = 1
kHeaders = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}


def crawl():
    while True:
        
        url = 'http://fund.jrj.com.cn/list/jjdt.shtml'

        for i in range(2, 12):
            response = requests.get(url, headers=kHeaders)
            soup = BeautifulSoup(response.text, 'html.parser')

            ul = soup.find('ul', {'class': 'jrj-l1'})
            
            for li in ul.find_all('li'):
                if li.get('class') == ['space']:
                    continue
                try:
                    date = li.i.text
                    href = li.a.get('href').replace('//', '')

                    select_sql = """
                        SELECT EXISTS(SELECT 1 FROM """+kTable+""" WHERE URL=%s);
                    """
                    cursor.execute(select_sql, (href,))
                    exist = cursor.fetchone()
                    if exist[0]:
                        continue
                    
                    response = requests.get('http://'+href, headers=kHeaders)
                    soup = BeautifulSoup(response.text, 'html.parser')

                    title = soup.h1.text.replace('\r', '').replace('\n', '')
                    date_time = soup.find('span', {'class': 'time'}).text.replace(
                        '\r', '').replace('\n', '')
                    source = soup.find('span', {'class': 'urladd'}).text.replace(
                        '来源：', '').replace('\n', '')
                    newspaper = soup.find('div', {'class': 'texttit_m1'})
                    
                    text = ''
                    for p in newspaper.find_all('p'):
                        image = p.find('img')
                        if image:
                            image_url = image.get('src')
                            if image_url.startswith('//'):
                                image_url = 'http:' + image_url
                            text += '<p class="image"><img src="'+image_url+'"></p>'
                        else:
                            text += '<p>'+p.text+'</p>'
                    
                    insert_sql = """
                        INSERT INTO """+kTable+"""(DATE,URL,TITLE,TIME,SOURCE,NEWSPAPER)
                        VALUES(%s,%s,%s,%s,%s,%s);
                    """
                    val = (date, href, title, date_time, source, text)
                    cursor.execute(insert_sql, val)
                    connect.commit()
                    time.sleep(kDelay)
                except:
                    print(li)

            url = 'http://fund.jrj.com.cn/list/jjdt-%s.shtml' % i
            time.sleep(kDelay)
        
        time.sleep(kGap)




if __name__ == "__main__":
    connect = MySQLdb.connect(kHost, kUser, kPassword,
                              kDatabase, charset='utf8', use_unicode=True)

    cursor = connect.cursor()
    crawl()
    connect.close()
