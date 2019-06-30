ハートに火をつけて
====
ver1.0
- - -
目次
----
* [概要](#chap1)
* [環境](#chap2)
* [使い方](#chap3)
* [詳細](#chap4)
* [備考](#chap5)


<a id="chap1"></a>
<a href="#chap1"></a>
- - -
概要
----
このPythonスクリプトはLinuxの温度を表示するものです。lm-sensorsがインストールできない環境で使ってください。


<a id="chap2"></a>
<a href="#chap2"></a>
- - -
環境
----
- CentOS 7.x
- Python 2.7.10以降
- Intel CPU


<a id="chap3"></a>
<a href="#chap3"></a>
- - -
使い方
----
1. ディレクトリに配置したスクリプトを実行するだけで温度が表示されます。<br>
`cd <スクリプト配置ディレクトリ>`<br><br>
スクリプト"ハートに火をつけて"を起動します。<br>
`python catchfire.py`<br>

1. 画面に温度が表示されます。


<a id="chap4"></a>
<a href="#chap4"></a>
- - -
詳細
----
1. このスクリプトはInterl CPUのみ対応しています。AMDのRyzenシリーズやARMのCPUでは動作しません。

1. CPUの温度は下記の色で表示されます。<br>
緑:45度以下<br>
黄:46度以上〜64度以下<br>
赤:65度以上<br>


<a id="chap5"></a>
<a href="#chap5"></a>
- - -
備考
----
- このスクリプトは将来AMDのRyzenに対応する予定です。
- バグを発見した場合は報告をお願いします。改善の要望や新しいアイディアも記載してください。[issue](https://github.com/Yuki-Matsumura/catchfire/issues)
- 映画"ハートに火をつけて"がこのスクリプトを作成するにあたってアイディアをくれました。ですが、私はこの映画を見たことがありません。ジョディー・フォスターは美しいです。
