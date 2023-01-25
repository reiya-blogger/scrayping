# 2. [初級] みずほ銀行の外貨普通預金を取得する（表のスクレイピング）
# 金融機関のWebサイトにはいろいろな表が掲載されています。 毎日自動で取得したら、景気の変動と連動していることがわかるかもしれません。

# 問題
# 以下のページから外貨普通預金の通貨ごとの金利を取得して表示してください。

# みずほ銀行 : 外貨預金金利
# https://www.mizuhobank.co.jp/rate/interest.html


import requests
from bs4 import BeautifulSoup

url = 'https://www.mizuhobank.co.jp/rate_fee/rate_interest.html'
res = requests.get(url)

# BeautifulSoupを利用して対象ページのHTML構造を解析

soup = BeautifulSoup(res.content, 'html.parser')

# タイトル文のクラスを指定して抽出、テキストのみ表示

title = soup.find('th', attrs={'class': 'alnCenter'})
rate = soup.find('p', attrs={'class': 'alnRight mT0'})

print(title.get_text())
print(rate.get_text())

# htmlという変数に先ほどの1つ目のテーブルのコードを文字列で保存

html = '''
<tbody>

<tr>
<th headers="th1 th2" class="tbgGray02 noBorderL left">米ドル</th>
<td headers="th1 th2" class="alnRight">0.010</td>
</tr><tr>
<th headers="th1 th2" class="tbgGray02 noBorderL left">英ポンド</th>
<td headers="th1 th2" class="alnRight">0.001</td>
</tr><tr>
<th headers="th1 th2" class="tbgGray02 noBorderL left">ユーロ</th>
<td headers="th1 th2" class="alnRight">0.001</td>
</tr><tr>
<th headers="th1 th2" class="tbgGray02 noBorderL left">豪ドル</th>
<td headers="th1 th2" class="alnRight">0.001</td>
</tr><tr>
<th headers="th1 th2" class="tbgGray02 noBorderL left">ニュージーランドドル</th>
<td headers="th1 th2" class="alnRight">0.001</td>
</tr><tr>
<th headers="th1 th2" class="tbgGray02 noBorderL left">スイスフラン</th>
<td headers="th1 th2" class="alnRight">0.001</td>
</tr></tbody>
'''

rate_list = []

row = []

for element in soup.find_all('th', attrs={'class': 'tbgGray02 noBorderL left'})[:5]:
    th = element.get_text()
    print(th)

for element in soup.find_all('td', attrs={'class': 'alnRight'})[:5]:
    td = element.get_text()
    print(td)