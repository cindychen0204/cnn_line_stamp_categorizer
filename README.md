(English)
# Line Sticker categorizer with CNN model

Settings:

- Tensorflow-gpu == 1.8.0 <br>  (only work with python 3.5)
- CUDA == 9.0 <br>
- Python == 3.5 <br>
- Keras == 2.1.5 <br>

labels = ['angry', 'excited', 'fear', 'Happy', 'sad', 'shock']

## Scripts Description

- scrape-line-stamp.py →　scrape line sitcker from [line sticker shop](https://store.line.me/stickershop/showcase/top_creators/) into "Pictures" floder
                        reference：[LINEスタンプをDeepLearningで自動生成してみる【Part 2】](https://qiita.com/enmaru/items/1d65307ca46264bf6259)
- rename.py : rename sticker to avoid duplicating (in "line_stamps" folder)
- convert2Numpy.py : convert image into Numpy formate
- cnn_model.py : defined cnn model. (called by  training.py)
- training.py : do training
- predict.py : check the result

実行順： scrape-line-stamp.py　→　(manually) categorize　→　rename.py →　convert2Numpy.py  →　training.py → predict.py 

 <br>


(日本語)
# CNNモデルを使ったLineスタンプ分類器

- Tensorflow-gpu == 1.8.0 <br> (環境は Python3.5 のみ)
- CUDA == 9.0 <br>
- Python == 3.5 <br>
- Keras == 2.1.5 <br>

ラベル設定labels = ['angry', 'excited', 'fear', 'happy', 'sad', 'shock']

<br>

## 各スクリプトの説明

- scrape-line-stamp.py →　ラインのスタンプを一括ダウンロードする (保存先はPicturesフォルダー)
                        参考：[LINEスタンプをDeepLearningで自動生成してみる【Part 2】](https://qiita.com/enmaru/items/1d65307ca46264bf6259)
- rename.py : 分類するときに、ファイル名を重複しないように実行する
- convert2Numpy.py : 収集した画像を全てNumpy形式に変換して保存する
- cnn_model.py : 定義したcnnモデル（ training.py に呼び出される）
- training.py : 学習する
- predict.py : 学習結果を検証する

実行順： scrape-line-stamp.py　→　(手動で)分類　→　rename.py →　convert2Numpy.py  →　training.py → predict.py 

 <br>
 
## 参考

[ラーメンを本気で分類してみた](https://blog.aidemy.net/entry/2018/12/23/022554)
