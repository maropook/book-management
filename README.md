# DRFでAPIを作成し，楽天bookAPIから取得したデータを操作する書籍管理システムを作る
  __開発環境__

* OS: `macOS Big Sur v11.5.2`
* Python: `Python 3.0.6`
* Django: `3.2.5`

# 使い方


__環境構築__

python3系をインストール

pythonのインストールはYouTubeの動画で調べるのがおすすめ

***
__書籍管理システム使用に必要なモジュールをインストール__

```bash


#Django本体
$pip install django

#CORS対策モジュール
$pip install django-cors-headers

#RESTフレームワーク。
$pip install djangorestframework 

```
***

__書籍管理システム本体のインストール__

```bash

#このプロジェクトを自分のPCにインストール
$git clone https://github.com/maropook/BookManagement.git

#book_managementディレクトリに移動
$cd book_management

```

***
__Djangoの設定__



```bash



#migrationファイルを作る(model.pyファイルをもとに)
$python manage.py makemigrations

#migrationファイルからデータベースを作成
$python manage.py migrate


```

***

__書籍管理システムを起動__
```bash

# 開発サーバーを起動
$python manage.py runserver

```

http://localhost:8000/book/book

DRFが起動しているか確認


http://localhost:8000/rakuten

書籍管理システムの利用



# 作り方
## :horse: Djangoのプロジェクトを作成

  __API実装__

[Django REST Frameworkを使って爆速でAPIを実装する](https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)

__CORS設定__

DRFを使って、APIエンドポイントをフロントエンドから叩く場合にはCORSの設定が必要

[【drf】django-cors-headersを使ってCORS設定を行う](https://self-methods.com/drf-cors-headers/)


__動作確認__

```bash

# 開発サーバーを起動
$python manage.py runserver

```


http://localhost:8000/book/book

DRFが起動しているか確認




REST APIを作成するには最低限以下の3つを定義する必要があります。

 - Serializer
 - ViewSet
 - URL pattern

ざっくり言うと、Serializerは「Modelをどのようにシリアライズ(・デシリアライズ)するかを決めるためのもの」、ViewSetは「APIのクエリーをどう解釈するかを決めるためのもの」、そしてURL Patternは「DjangoにURLのパターンを教えるためのもの」です。これらをAPI化したいModelに対してそれぞれ定義していきます。

最低限のAPI実装をしたい時には結構手間に感じるかもしれませんが、このように分割することによって高い拡張性とコードの見通しのよさを実現しています。
