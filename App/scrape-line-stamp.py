#かわいいスタンプのランキング上位から順番に保存する
import requests
import os
from bs4 import BeautifulSoup

#htmlのソースから画像リンクを抽出するための関数
def rem(string):
    print(string)
    str0 = str(string).split("(")[1]
    return str0.split(";")[0]

#スタンプセットのNo.(指定した番号から始まり、セットごとにフォルダが生成される)
setname = 467
chara = "&character=" + str(10) #　10: ネコ, 11:ウサギ, 12:イヌ, 13:クマ, 14:鳥, 19:パンダ, 20:アザラシ
#キャラクター指定せずにすべてを対象とする場合
chara = ""

#「カワイイ・キュート」ジャンルのスタンプを昇順に並べ、ページごとにデータを取得する
for page in range(14,20):
    ranking_url = 'https://store.line.me/stickershop/showcase/top_creators/ja?taste=1'+ str(chara) + '&page=' + str(page)
    print("download from " + ranking_url)
    ran = requests.get(ranking_url)         #requestsを使って、webから取得
    soup0 = BeautifulSoup(ran.text, 'lxml') #要素を抽出
    stamp_list = soup0.find_all(class_="mdCMN02Li") #ソースの中でスタンプ一覧の箇所を探してリストに格納
    for i in stamp_list:
        target_url = "https://store.line.me" + i.a.get("href") #スタンプセットに含まれる画像を表示させるページのリンク
        #target_url = 'https://store.line.me/stickershop/product/3882252/ja'
        r = requests.get(target_url)         #requestsを使って、webから取得
        setname += 1
        new_dir_path = "../pictures/"+ str(setname) #スタンプセットのNo.に対応するフォルダを作成する
        os.makedirs(new_dir_path, exist_ok=True) #フォルダが存在しない場合作成する
        soup = BeautifulSoup(r.text, 'lxml') #要素を抽出
        span_list = soup.findAll("span",{"class":"mdCMN09Image"}) #スタンプセットに含まれる画像の情報をリストに格納

        fname = 0 #ダウンロードする画像データの名称
        for i in span_list:
            if i.get("style") is not None:
                fname += 1
                imgsrc = rem(i.get("style")) #画像データのURLを取得
                req = requests.get(imgsrc)

                if r.status_code == 200:
                    f = open( "../pictures/"+ str(setname) + "/" + str(fname) + ".png", 'wb')
                    f.write(req.content)
                    f.close()

    print ("finished downloading page: " + str(page) + " , set: ~" + str(setname)  )
