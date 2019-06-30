Catchfire
====
Ver1.0
- - -
Table of contents
----
* [Overview](#chap1)
* [Environment](#chap2)
* [Usage](#chap3)
* [Details](#chap4)
* [Remarks](#chap5)


<a id="chap1"></a>
<a href="#chap1"></a>
- - -
Overview
----
This Python script displays the temperature of Linux. Use in an environment where lm-sensors can not be installed.


<a id="chap2"></a>
<a href="#chap2"></a>
- - -
Environment
----
- CentOS 7.x
- Python 2.7.10 or later
- Intel CPU


<a id="chap3"></a>
<a href="#chap3"></a>
- - -
Usage
----
1. The temperature is displayed simply by executing the script placed in the directory.<br>
`cd <script directory>`<br><br>
Launch the script "Catchfire".<br>
`python catchfire.py`<br>

1. The temperature will be displayed on the screen.


<a id="chap4"></a>
<a href="#chap4"></a>
- - -
Details
----
1. This script only supports Interl CPU. It does not work with AMD's Ryzen series or ARM CPUs.

1. The CPU temperature is displayed in the following color.<br>
Green:Under 45℃
Yellow:46℃ to 64℃
Red:Upper 65℃


<a id="chap5"></a>
<a href="#chap5"></a>
- - -
Remarks
----
- This script will be compatible with AMD's Ryzen in the future.
- If you find a bug, please report it. I also accept requests for improvements and new ideas. [issue](https://github.com/Yuki-Matsumura/catchfire/issues)
- The movie "Catchfire" gave me some ideas on creating this script. But I have never seen this movie. Jody Foster is beautiful.
