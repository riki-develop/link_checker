#! Python3
# 機能
#  ページのリンク切れをチェックする
# 使い方
#  Pythonを実行する
# 実行コマンド
#  python3 link_checker.py <チェック対象のサイトURL>

import re
import sys
import bs4
import requests
from urllib.parse import urljoin

# ページ内のリンクを取得する関数
def get_link(url):
    # ページ取得
    res = requests.get(url)
    res.raise_for_status()

    # リンク取得
    soup = bs4.BeautifulSoup(res.text, "lxml")
    links = soup.select("a")

    keys = set()
    results = []
    for link in links:
        # リンクURL取得
        link_url = link.get("href")
        if not link_url:
            continue

        # URL補完
        if not link_url.startswith("http"):
            link_url = urljoin(url, link_url)

        # リンクテキスト取得
        link_text = link.text
        if not link_text:
            link_text = ""
        link_text = link_text.strip()
        link_text = re.sub(r"\n", " ", link_text)

        # 重複削除
        key = link_url + link_text
        if key in keys:
            continue
        keys.add(key)

        results.append({"url": link_url, "text": link_text})

    return results


def check_link(url):
    # リンク取得
    results = get_link(url)

    for result in results:
        try:
            # リンクアクセス
            res = requests.get(result["url"])
            # 200番台のステータスコードを全て成功とみなす
            if 200 <= res.status_code < 300:
                print(f"OK URL -> {result['url']} (Status Code: {res.status_code})")
            else:
                print(f"NG URL -> {result['url']} (Status Code: {res.status_code})")
        except:
            print("ERROR URL -> ", result["url"])


if len(sys.argv) != 2:
    sys.exit("使い方：python link_checker.py URL")

check_link(sys.argv[1])
