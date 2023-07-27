# 実践ソフトウェア開発 サンプルソース

# はじめに

本サンプルソースは、講義：実践ソフトウェア開発で課題となる開発のベースになるソースです。

Frontend担当者とBackend担当者に分割して開発する前提で、PythonとJavaScriptを用いて開発を行います。

--------------------------------------------------------------------------------
# ソフトウェアのインストール

winget install Node.js
winget install Python
winget install git
winget install vscode

--------------------------------------------------------------------------------
# テンプレートプロジェクトの取得

git clone https://github.com/tt-hasegawa/ppp-sample01.git

ペアの人と同じリポジトリを利用してください。


--------------------------------------------------------------------------------

# サーバサイド開発
Python + Flaskを用いて開発します。
リクエストされたURLに応じて、必要なリソースを返したり、
リソースへの登録／更新を行う部分を担当します。

python3をインストールします。
python -m venv .venv
.venv\Scripts\activate
pip install flask flask-cors pickledb

## 実行方法
python server.py

http://localhost:5000/

にアクセスしてみましょう。

--------------------------------------------------------------------------------

# クライアントサイド開発
SvelteKitと呼ばれるフレームワークを用いて、
JavaScript+HTML、CSSでWeb画面を作成します。

https://svelte.jp/

- ※いちから作りたい人は以下を実行
npm create svelte@latest frontend

## 実行方法
cd frontend 
npm i
npm run dev

--------------------------------------------------------------------------------

# 開発の進め方

- やりたいことをきめる

- 画面要素を考える

- やりとりするデータを決める

- 画面構成を考える

- APIとデータに格納する部分を作る

