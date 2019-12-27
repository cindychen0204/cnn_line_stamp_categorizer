# CNNモデルを使ったLineスタンプ分類器

- Tensorflow-gpu == 1.8.0 <br>

- CUDA == 9.0 <br>
- Python == 3.5 <br>
- Keras == 2.1.5 <br>

## 各スクリプトの説明

- scrape-line-stamp.py →　ラインのスタンプを一括ダウンロードする
                        参考：[LINEスタンプをDeepLearningで自動生成してみる【Part 2】](https://qiita.com/enmaru/items/1d65307ca46264bf6259)
- rename.py : 分類するときに、ファイル名を重複しないように実行する
- convert2Numpy.py : 収集した画像を全てNumpy形式に変換して保存する
- cnn_model.py : 定義したcnnモデル（ training.py に呼び出される）
- training.py : 学習する
- predict.py : 学習結果を検証する

実行順： convert2Numpy.py  →　training.py → predict.py 

 <br>
 
## 参考

[ラーメンを本気で分類してみた](https://blog.aidemy.net/entry/2018/12/23/022554)
