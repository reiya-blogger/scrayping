# • スクレイピングに必要なライブラリ選定
# requests / BeautifulSoup を使用
# • colab 等で実行する sandbox 場所を作成 → GitHub上に作成
# • 取得したデータを置く場所を検討する(DBの調査/選定) → 置く場所は作らない（必要となる結果を返す）

# 問題
# 以下のページから25日分の記事のURLとタイトルを取得して表示してください。

# クローラー／Webスクレイピング Advent Calendar 2016 - Qiita
# http://qiita.com/advent-calendar/2016/crawler


# requests / BeautifulSoup のライブラリをインポート

import requests

from bs4 import BeautifulSoup

url = 'http://qiita.com/advent-calendar/2016/crawler'
res = requests.get(url)


# BeautifulSoupを利用して対象ページのHTML構造を解析

soup = BeautifulSoup(res.text, 'html.parser')

# カレンダー内のa要素のみを特定するため、該当divをまず特定

calendar = soup.find_all('div', attrs={'class': 'adventCalendarCalendar_comment'})


# 該当するaタグを解析データから全て見つけてhref属性の中身を表示
# for文でa要素内のhrefおよびテキストを抽出して表示

for element in calendar.find_all('a'):
    link = element.get('href')
    text = element.get_text()
    print(link)
    print(text)