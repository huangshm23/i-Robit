# Crawler
爬虫

## 功能
爬取新闻和网页

## checkpoint
- 8/15 建立文件夹，完成[金融界](http://fund.jrj.com.cn/list/jjdt.shtml)爬取
- 8/18 fix some bug

## Run
- pip install -r requirements.txt 
- python crawler.py > log.txt &
  
## Notice
- crawl website http://fund.jrj.com.cn/list/jjdt.shtml
- start crawling every *kGap* seconds
- delay *kDelay* seconds every url
- database mysql
  
  ```
  -------------------------------------------------------------------------------------------------------------
  | date DATE | url VARCHAR(2083) | title VARCHAR(255) | TIME DATATIME | source VARCHAR(255) | newspaper TEXT |
  -------------------------------------------------------------------------------------------------------------
  ```
- newspaper
  ```html
  <p>
    ljfsdlfjksdflsdf
  </p>
  <p class='image'>
    <img src="http://lfsdjfdskjf">
  </p>
  <p>
    fdlsjfdslfjdsdfsdf
  </p>
  ...
  ```  