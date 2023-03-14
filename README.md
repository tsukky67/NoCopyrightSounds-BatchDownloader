# NoCopyrightSounds-BatchDownloader
 
NCSの音楽を一括ダウンロードするためのPythonスクリプトです。/This is to download all musics of NCS.

# How to use

main.pyを実行するだけで同ディレクトリ内のmusicsフォルダに全曲がダウンロードされます。/Just run main.py and all songs will be downloaded to the musics folder in the same directory.

# Requirement

* Google Chrome 105.0.5195.127
* Python 3.10.7
* selenium 4.4.3
* chromedriver-binary 105.0.5195.52.0
(chromeのバージョンに合わせて適宜必要なchromedriverをインストールしてください/Install the necessary chromedriver according to your chrome version.)

# Installation

上述した二つのライブラリをインストールしてください。/Install the two libraries mentioned above.

```bash
pip install selenium
pip install chromedriver-binary
```

# Note

chromedriverのバージョンがインストールされているchromeのバージョンと一致しない場合動かない恐れがあるので一致するバージョンの利用を推奨します。/If the version of chromedriver does not match the installed version of chrome, it may not work, so please install the matching version.
