# mypkgパッケージ
![test](https://github.com/SomaKobayashi/mypkg/actions/workflows/test.yml/badge.svg)

* mkpkgはROS2のパッケージです.

* mypkgの中にtalker.py,listener.py,talk_listen.launch.pyという3つのコマンドがあります.

## トピックの名前

* /countup

## コマンドの使用方法

* talker.py
```
端末1
ros2 run mypkg talker

端末2
ros2 topic echo /countup
```
数字をカウントし始める.

* listener.py
```
端末1
ros2 run mypkg talker

端末2
ros2 run mypkg listener
```
talker.pyがカウントした数字を受けとり、出力し始める.

* talk_listen.launch.py
```
端末1
ros2 launch mypkg talk_listen.launch.py
```
talkerがカウントした数字をlistenerが受け取り、その結果を出力する.

## 実行環境

* Ubuntu 22.04.1 LTS

## 必要なソフトウェア

* Python (バージョン…3.10.6)
* ROS (バージョン…ROS2)


## ライセンス

* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.

© 2022 Soma Kobayashi
