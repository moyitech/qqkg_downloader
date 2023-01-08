# -*- coding = utf-8 -*-
# @Time: 2023/01/05
# @Author:MoyiTech
# @Software: PyCharm
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QByteArray
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QDesktopWidget, \
    QLineEdit, QLabel, QTextEdit, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QImage
import time
import core


img_data = 'AAABAAEAGBgAAAEAIACICQAAFgAAACgAAAAYAAAAMAAAAAEAIAAAAAAAAAkAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAgH/AAIB/wAAAv8AQw7+AIs1+QCKNPwAnjr8Apc5+z2ZOvyKnDn7v5s6+9+XOfvvkzf72o42+7KKNvx6gjL9KnYu/ABfJv0AUSDBAAAAAAB2CUELiQdfC////wD///8AAQD/AAEA/wAAAP8AQw3/AIgz+QCQNvsxozv7xqE8+v+cOfr/ljf7/480+/+LNPv/iTP7/4g0+/+HNfr/hjX7/n8z+59nKfwZWCDNACwCExWHC0vniwxTu////wD///8AAAD/AAAA/wAAAP8ANQD/AJ88+oKhOvr5mjn6/5M0+/+MM/v/iDH7/4Iw+/9+Lvz/ey78/3kt+/93Lfz/dy77/3sw+/97MPvxeSjkWaMFRbuQDU//lwhKsv///wD///8AAAu/AAALvwAAB8UAdSr4iaU7+/+XN/v/jTP7/4cw+/+BLvz/fCz8/3cr/P9yKfz/cCf8/24o/P9rJ/3/ayj8/2sp/f9vK/3/di72/4kYgP6QBzr9fgRWOv///wD///8AZCfhAGEm4QB3LuNfpz33+480+/+KMfv/gjD8/30u/P92Kfz/cSn8/24m/P9oJvz/ZiT8/2Ik/P9hI/v/XSP//1Un//9WKf//YCn//2ou//+IEWOzVQpGAP///wD///8AXhv/AGMe/winOf/ykTb8/4cx+/+ALvz/eSv8/3In/P9sJvz/aCT8/2Qi/v9eIv7/XCD+/1kg/v9XHf//Uh///3YWm/93Fpn/XCH2/1co//9mJ/2/ayT2AP///wD///8AaCb7AH8w/IWVN/v/hjD7/30s/P92Kfz/byf8/2kk/v9kIv7/XiD+/1ke/v9WHv7/VBz+/1Ec/v9MG///eROF/5UFKP+UBCz/hQ5g/2Ed4P9bJf/9UyX/S////wD///8AhTX6AJk5+/eFMfv/fSz8/3Qr/P9uKPz/ZiT+/2Ag/f9aHv7/Vh7+/1Qc/v9PGf7/TBn//0oZ/v9GGf//lAcx/4sNUP+NC07/kwc2/3AWp/9UHv7/VB7+ov///wD///8AhjH8QIgz+/9+Lvv/dSv8/2wo/P9mJP7/XiL8/1ge/v9UHP7/TRT+/zoA/P8sAPv/NgD9/0UW//8+Fv//exJ+/5kGKP+XBjD/kgg9/1sU1/9OGf7/UBz+2P///wD///8AiDT7cYAw+/92K/z/bij8/2Uk/P9eIP7/WB7+/1Qe/v87APz/LQD7/1g2/v9tVf//YUb//0IR//9AFv//Pxb//28Ul/93E4T/XRbE/z8Y//9IF/7/Thz++v///wD///8AgjH7jnou/P9wKfz/ZyT8/14i/v9YHv7/Uhz+/zoA/P9XNv//wrn///j4////////tqz//z0O/vpAFP6IPRP/5ikl//8vJ///LCr//zwl//9AIv7/RiD+/////wD///8AfTD8jnQr/P9qJ/3/YSL+/1kg/v9SHP7/SxT+/1Uz/v/u6///////////////////koP//0AU/sVCFP4APhf/AEEo/6o3Nv//Nzf9/zk1/f88K/3/QSb9/////wD///8Adi35cW8r/P9lJvz/XSD9/1Ue/f9OHP7/SyD+/720////////////////////////mo3//0EN/49BHv4ANyL/KkoZ/ys4P/3TNUL9/zY//f85Nf3/PSj9+f///wD///8AbSn/QGwp/f9gJPz/WCD8/1Ae/f9KGf7/UzH+//j3////////////////////////4Nz//xkA++w9JP/aOzD+/zku/qI1MP03Mk78/zZD/f84Of3/Oyv92P///wD///8ASB3iAGco+vdeIvz/VR79/04c/f9IGf7/WD7//////////////////////////////////4d+//8FAPv/Mi/+/zZD/ts2Nf0DNE781jZG/P83O/3/PC3+ov///wD///8AWSLsAGkq/4NfJP7/VB79/0sc/f9GHP7/VTr//////////////////9DK//+Qgf//6uf///v7//+Hiv//HCf7/zBH/Ow4Q/sYMkL9gjJL/P8zRvz9Pjv8Sf///wD///8AThj3AEgU8AhXIvnwVB7+/0sc/f9GHP7/SSv+/+Lg/////////////3Vg//8AAPj/wLj/////////////5eT//0Bh/egvTP0YMFH8Xy9b+/8tQ/3NRCH7AP///wD///8ARwzzAEcM8wBVG/qDVR7+/0we/v9FG///QBr+/5CF///+/v///////+7s//+7tP//9/b/////////////6+///x9i+8wtUP0DMVz+cCFk+/+GDf8YhwD/AP///wD///8AaCf/AGgn/wBhJvyKVSL+/0si/v9EJP7/PyT//ykA/f+opf/////////////////////////////T3f//Kmj8/0BQ/HxQSf0ANm78pD0+/VZoAP8AZwD/AP///wD///8AVy/7AFcv+wBbMvuNVTD8/0k0/P9ANv3/Ozj9/zA0/f8LAfv/aHH//6yy///GzP//u8X//4Of//8VYPv/EWn82ExD/wB1HP8AS07+JEUt/QBQAP8AUAD/AP///wD///8AUj/9AFI//QBZQPxzWEf+/0ZM+/49U/z9NFj8/y9a+/8sW/r/ADn6/wAw+v8EQPv/AEf5/wBS+f8ZbvvIK2D8FR9b/wB4Dv8AUTz/AEIz/QBVAP8AVQD/AP///wD///8AUkX5AFJF+QBXRvo9UUryc0FV/iQ7X/wbM2L8Mi1u+1sqcvySKXX8xClw++MmbvvhJHL8tjJr/mEtZPsHK177ACpX/wB2GP8ATkP/AEIz/QBVAP8AVQD/AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A/gB5APwAEQD4AAEA8AABAOAAAwDAAAMAwAABAMAAAQCAAAEAgAABAIAAAQCAAYEAgAEBAIAAAQDAAAEAwAABAMAAAwDgAAMA4AAnAOAAbwDgAH8A4AD/AP///wA='


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.run_btn = None
        self.output_url = None
        self.song_url_input = None
        self.central_widget = None
        self.init_gui()

    def init_gui(self):
        self.resize(700, 500)
        self.setWindowTitle('全民K歌解析工具 Downloader')

        # 配置base64 to icon
        image = QImage()
        image.loadFromData(QByteArray().fromBase64(img_data.encode()), 'ico')
        pix = QPixmap.fromImage(image)
        self.setWindowIcon(QIcon(pix))

        # 配置central widget(因为是QMainWindow)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 配置栅格(grid)布局
        grid = QGridLayout()
        grid.setSpacing(15)
        self.central_widget.setLayout(grid)

        # 配置组件
        song_url_label = QLabel("请输入歌曲链接：")
        self.song_url_input = QLineEdit()
        self.output_url = QTextEdit()
        self.run_btn = QPushButton("解析")

        # 配置状态栏
        self.statusBar().showMessage("等待解析")

        # 绑定事件
        self.run_btn.clicked.connect(self.button_clicked)

        # 栅格布局
        grid.addWidget(song_url_label, 0, 0, 1, 1)
        grid.addWidget(self.song_url_input, 0, 1, 1, 4)
        grid.addWidget(self.output_url, 1, 1, 2, 4)
        grid.addWidget(self.run_btn, 3, 4, 1, 1)

        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key_Escape:
            self.close()

    def button_clicked(self):
        sender = self.sender()
        # if sender.text() == '解析':
        if sender == self.run_btn:
            self.statusBar().showMessage("解析中，请稍后")
            # resp = core.get_url(self.song_url_input.text())
            resp = core.get_url(self.song_url_input.text())
            self.output_url.setText(resp)
            print('解析完成：', resp)
            self.statusBar().showMessage("解析完成")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
