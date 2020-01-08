#reference : https://qiita.com/enmaru/items/1d65307ca46264bf6259
import requests
import os
from bs4 import BeautifulSoup


setNumber = 0
chara = "&character=" + str(10)

for page in range(14, 20):
    ranking_url = 'https://store.line.me/stickershop/showcase/top_creators/ja?taste=1' + str(chara) + '&page=' + str(page)
    print("download from " + ranking_url)
    ran = requests.get(ranking_url)
    soup0 = BeautifulSoup(ran.text, 'lxml')
    stamp_list = soup0.find_all(class_="mdCMN02Li")  # find stamp list
    for i in stamp_list:
        target_url = "https://store.line.me" + i.a.get("href")
        r = requests.get(target_url)
        setNumber += 1
        new_dir_path = "../pictures/" + str(setNumber)
        os.makedirs(new_dir_path, exist_ok=True)  # create picture folder if does not exit
        soup = BeautifulSoup(r.text, 'lxml')  # extract element
        span_list = soup.findAll("span", {"class": "mdCMN09Image"})

        fileName = 0  # stamp name
        for j in span_list:
            if j.get("style") is not None:
                fileName += 1
                img_src = rem(j.get("style"))  # get stamp url
                req = requests.get(img_src)

                if r.status_code == 200:
                    f = open("../pictures/" + str(setNumber) + "/" + str(fileName) + ".png", 'wb')
                    f.write(req.content)
                    f.close()

    print("finished downloading page: " + str(page) + " , set: ~" + str(setNumber))
