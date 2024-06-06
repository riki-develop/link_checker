# 概要

ページのリンク切れをチェックするプログラム  
1. 対象のサイトをスクレイピング  
2. ページ内のリンクを取得し順にアクセス  
3. 実行結果をコンソールに出力  
※HTTPステータスコードが200~以外であればNG (ERROR)  
  
## 実装環境（必要なパッケージ）

* MacBookPro M2 Apple silicon  
* Python3系（3.9.6で検証済）  
  * beautifulsoup4  
  * requests  
  
## 使い方

```
## このリポジトリをクローン
git clone https://github.com/chikara-karasawa/link_checker.git

## リポジトリへ移動
cd link_checker

## プログラム実行
python3 link_checker.py <チェック対象のサイトURL>
```
  
