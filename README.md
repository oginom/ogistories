# ogistories

## about

みんなで文を書いていって物語を作るアプリ。
のつもりだったが短歌を作るアプリになりそう。

## env

docker-compose

### frontend

nginx + Vue.js + Bootstrap

### backend

gunicorn + Flask

### database

MySQL

## run

```[bash]
docker-compose up -d
```

作り中なので今は動かない。

### フロントだけ動かす

```[bash]
cd front
npm install
npm run build
npm run dev
```

### バックだけ動かす

```[bash]
cd back
python run.py
```

## TODO

マイグレーション周り書く
