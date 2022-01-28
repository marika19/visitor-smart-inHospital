# 環境構築方法

## 仮想環境の作成

```
python3 -m venv env
```

## 仮想環境に入る
### Windowsの場合
```
.\env\Scripts\activate
```

### Macの場合
```
source env/bin/activate
```

## 仮想環境から抜ける
```
deactivate
```

## 必要なパッケージのインストール
```
pip install -r requirment.txt
```

## シークレットキーの生成

[1] local_settings.py(シークレットキーが書かれているファイル)の作成
```
touch django_app/local_settings.py
```
[2] シークレットキーを生成
```
python django_app/generate_secretkey_setting.py
```
[3] local_settings.pyにコピー

## サーバーを起動
```
python manage.py runserver
```