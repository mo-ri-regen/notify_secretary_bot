## 準備

https://discord.com/developers
にアクセスする

OAuth2 > URL Generator で bot にチェック
→GENERATED URL にアクセス
→Discord のアクセスを許可する

Bot > Privileged Gateway Intents の権限をオンにする

## セットアップ

### Docker イメージの作成

docker-compose.yml があるディレクトリで下記コマンドを実行します。
すると、Docker Image が作成されます。
ソースを変更したときはビルドしてください。

```bash
docker-compose build
```

依存パッケージをインストールします

```bash
docker-compose run --entrypoint "poetry init" notice-secretary-bot
```

```bash
docker-compose run --entrypoint "poetry install" notice-secretary-bot
```

```bash
docker-compose run --entrypoint "poetry add discord.py" notice-secretary-bot
```

```bash
docker-compose run --entrypoint "poetry add discordwebhook" notice-secretary-bot
```

```bash
docker-compose run --entrypoint "poetry add python-dotenv" notice-secretary-bot
```

```bash
docker-compose run --entrypoint "poetry add schedule" notice-secretary-bot
```

新しい Python パッケージを追加した場合は下記コマンドで再ビルドをします

```bash
docker-compose build --no-cache
```

### 実行

```bash
docker-compose run --entrypoint "poetry run python3 bot/main.py" notice-secretary-bot
```

## Heroku

heroku で poetry を利用する場合、requirements.txt と Procfile が必要
requirements.txt:サーバに何のパッケージがインストールされている必要があるかを Heroku に教えるためのファイル
下記コマンドで requirements.txt が生成される

```bash
docker-compose run --entrypoint "poetry export -f requirements.txt -o requirements.txt" notice-secretary-bot
```

https://minerva.mamansoft.net/Notes/Poetry%E3%81%A7requirements.txt%E3%82%92%E4%BD%9C%E6%88%90

### Procfile

Heroku にデプロイしたときに自動的に実行されるコマンドを記述

https://devcenter.heroku.com/ja/articles/release-phase
