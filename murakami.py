import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt




class MyCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 500, 500) # 위치와 크기 설정/ 파리미터 변경
        self.setWindowTitle('My_heart_Canvas') #  gui이름 정하기
        self.show() # 출력

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # 팔레트 색상을 만들기
        pink = QPen(QColor(255, 167, 167), 10, Qt.SolidLine) # HSV Color Format ( 0~255 ) , size(10)
        yellow = QPen(QColor(250, 224, 140), 10, Qt.SolidLine)
        green = QPen(QColor(206, 242, 121), 10, Qt.SolidLine)
        lightpink = QPen(QColor(255, 193, 158), 10, Qt.SolidLine)
        darkgray = QPen(QColor(72, 72, 72), 10, Qt.SolidLine)
        
        #Decision
        painter.setPen(pink)
        #drawing_point
        painter.setPen(darkgray)
        
        
        painter.drawPoint(10, 10), painter.drawPoint(10, 20), painter.drawPoint(10, 30)
        painter.drawPoint(10, 40), painter.drawPoint(10, 50), painter.drawPoint(10, 60)
        painter.drawPoint(10, 70), painter.drawPoint(10, 80), painter.drawPoint(10, 90)
        painter.drawPoint(10, 100), painter.drawPoint(10, 110), painter.drawPoint(10, 120)
        painter.drawPoint(10, 130), painter.drawPoint(10, 140), painter.drawPoint(10, 150)
        painter.drawPoint(10, 160), painter.drawPoint(10, 170), painter.drawPoint(10, 180)
        painter.drawPoint(10, 190), painter.drawPoint(10, 200), painter.drawPoint(10, 210)
        painter.drawPoint(10, 220), painter.drawPoint(10, 230), painter.drawPoint(10, 240)
        painter.drawPoint(10, 250), painter.drawPoint(10, 260), painter.drawPoint(10, 270)
        painter.drawPoint(10, 280), painter.drawPoint(10, 290), painter.drawPoint(10, 300)
        painter.drawPoint(10, 310), painter.drawPoint(10, 320), painter.drawPoint(10, 330)
        painter.drawPoint(10, 340), painter.drawPoint(10, 350), painter.drawPoint(10, 360)
        painter.drawPoint(10, 370), painter.drawPoint(10, 380), painter.drawPoint(10, 390)
        painter.drawPoint(10, 400), painter.drawPoint(10, 410), painter.drawPoint(10, 420)
        painter.drawPoint(10, 430), painter.drawPoint(10, 440), painter.drawPoint(10, 450)
        painter.drawPoint(10, 460), painter.drawPoint(10, 470), painter.drawPoint(10, 480)
        painter.drawPoint(10, 490), painter.drawPoint(10, 500)
        #######################################################################################10
        painter.drawPoint(20, 10), painter.drawPoint(20, 20), painter.drawPoint(20, 30)
        painter.drawPoint(20, 40), painter.drawPoint(20, 50), painter.drawPoint(20, 60)
        painter.drawPoint(20, 70), painter.drawPoint(20, 80), painter.drawPoint(20, 90)
        painter.drawPoint(20, 100), painter.drawPoint(20, 110), painter.drawPoint(20, 120)
        painter.drawPoint(20, 130), painter.drawPoint(20, 140), painter.drawPoint(20, 150)
        painter.drawPoint(20, 160), painter.drawPoint(20, 170), painter.drawPoint(20, 180)
        painter.drawPoint(20, 190), painter.drawPoint(20, 200), painter.drawPoint(20, 210)
        painter.drawPoint(20, 220), painter.drawPoint(20, 230), painter.drawPoint(20, 240)
        painter.drawPoint(20, 250), painter.drawPoint(20, 260), painter.drawPoint(20, 270)
        painter.drawPoint(20, 280), painter.drawPoint(20, 290), painter.drawPoint(20, 300)
        painter.drawPoint(20, 310), painter.drawPoint(20, 320), painter.drawPoint(20, 330)
        painter.drawPoint(20, 340), painter.drawPoint(20, 350), painter.drawPoint(20, 360)
        painter.drawPoint(20, 370), painter.drawPoint(20, 380), painter.drawPoint(20, 390)
        painter.drawPoint(20, 400), painter.drawPoint(20, 410), painter.drawPoint(20, 420)
        painter.drawPoint(20, 430), painter.drawPoint(20, 440), painter.drawPoint(20, 450)
        painter.drawPoint(20, 460), painter.drawPoint(20, 470), painter.drawPoint(20, 480)
        painter.drawPoint(20, 490), painter.drawPoint(20, 500)
        #######################################################################################20
        painter.drawPoint(30, 10), painter.drawPoint(30, 20), painter.drawPoint(30, 30)
        painter.drawPoint(30, 40), painter.drawPoint(30, 50), painter.drawPoint(30, 60)
        painter.drawPoint(30, 70), painter.drawPoint(30, 80), painter.drawPoint(30, 90)
        painter.drawPoint(30, 100), painter.drawPoint(30, 110), painter.drawPoint(30, 120)
        painter.drawPoint(30, 130), painter.drawPoint(30, 140), painter.drawPoint(30, 150)
        painter.drawPoint(30, 160), painter.drawPoint(30, 170), painter.drawPoint(30, 180)
        painter.drawPoint(30, 190), painter.drawPoint(30, 200), painter.drawPoint(30, 210)
        painter.drawPoint(30, 220), painter.drawPoint(30, 230), painter.drawPoint(30, 240)
        painter.drawPoint(30, 250), painter.drawPoint(30, 260), painter.drawPoint(30, 270)
        painter.drawPoint(30, 280), painter.drawPoint(30, 290), painter.drawPoint(30, 300)
        painter.drawPoint(30, 310), painter.drawPoint(30, 320), painter.drawPoint(30, 330)
        painter.drawPoint(30, 340), painter.drawPoint(30, 350), painter.drawPoint(30, 360)
        painter.drawPoint(30, 370), painter.drawPoint(30, 380), painter.drawPoint(30, 390)
        painter.drawPoint(30, 400), painter.drawPoint(30, 410), painter.drawPoint(30, 420)
        painter.drawPoint(30, 430), painter.drawPoint(30, 440), painter.drawPoint(30, 450)
        painter.drawPoint(30, 460), painter.drawPoint(30, 470), painter.drawPoint(30, 480)
        painter.drawPoint(30, 490), painter.drawPoint(30, 500)
        #############################################################30
        painter.drawPoint(40, 10), painter.drawPoint(40, 20), painter.drawPoint(40, 30)
        painter.drawPoint(40, 40), painter.drawPoint(40, 50), painter.drawPoint(40, 60)
        painter.drawPoint(40, 70), painter.drawPoint(40, 80), painter.drawPoint(40, 90)
        painter.drawPoint(40, 100), painter.drawPoint(40, 110), painter.drawPoint(40, 120)
        painter.drawPoint(40, 130), painter.drawPoint(40, 140), painter.drawPoint(40, 150)
        painter.drawPoint(40, 160), painter.drawPoint(40, 170), painter.drawPoint(40, 180)
        painter.drawPoint(40, 190), painter.drawPoint(40, 200), painter.drawPoint(40, 210)
        painter.drawPoint(40, 220), painter.drawPoint(40, 230), painter.drawPoint(40, 240)
        painter.drawPoint(40, 250), painter.drawPoint(40, 260), painter.drawPoint(40, 270)
        painter.drawPoint(40, 280), painter.drawPoint(40, 290), painter.drawPoint(40, 300)
        painter.drawPoint(40, 310), painter.drawPoint(40, 320), painter.drawPoint(40, 330)
        painter.drawPoint(40, 340), painter.drawPoint(40, 350), painter.drawPoint(40, 360)
        painter.drawPoint(40, 370), painter.drawPoint(40, 380), painter.drawPoint(40, 390)
        painter.drawPoint(40, 400), painter.drawPoint(40, 410), painter.drawPoint(40, 420)
        painter.drawPoint(40, 430), painter.drawPoint(40, 440), painter.drawPoint(40, 450)
        painter.drawPoint(40, 460), painter.drawPoint(40, 470), painter.drawPoint(40, 480)
        painter.drawPoint(40, 490), painter.drawPoint(40, 500)
        ###########################################################40
        painter.drawPoint(50, 10), painter.drawPoint(50, 20), painter.drawPoint(50, 30)
        painter.drawPoint(50, 40), painter.drawPoint(50, 50), painter.drawPoint(50, 60)
        painter.drawPoint(50, 70), painter.drawPoint(50, 80), painter.drawPoint(50, 90)
        painter.drawPoint(50, 100), painter.drawPoint(50, 110), painter.drawPoint(50, 120)
        painter.drawPoint(50, 130), painter.drawPoint(50, 140), painter.drawPoint(50, 150)
        painter.drawPoint(50, 160), painter.drawPoint(50, 170), painter.drawPoint(50, 180)
        painter.drawPoint(50, 190), painter.drawPoint(50, 200), painter.drawPoint(50, 210)
        painter.drawPoint(50, 220), painter.drawPoint(50, 230), painter.drawPoint(50, 240)
        painter.drawPoint(50, 250), painter.drawPoint(50, 260), painter.drawPoint(50, 270)
        painter.drawPoint(50, 280), painter.drawPoint(50, 290), painter.drawPoint(50, 300)
        painter.drawPoint(50, 310), painter.drawPoint(50, 320), painter.drawPoint(50, 330)
        painter.drawPoint(50, 340), painter.drawPoint(50, 350), painter.drawPoint(50, 360)
        painter.drawPoint(50, 370), painter.drawPoint(50, 380), painter.drawPoint(50, 390)
        painter.drawPoint(50, 400), painter.drawPoint(50, 410), painter.drawPoint(50, 420)
        painter.drawPoint(50, 430), painter.drawPoint(50, 440), painter.drawPoint(50, 450)
        painter.drawPoint(50, 460), painter.drawPoint(50, 470), painter.drawPoint(50, 480)
        painter.drawPoint(50, 490), painter.drawPoint(50, 500)
        ############################################################50
        painter.drawPoint(60, 10), painter.drawPoint(60, 20), painter.drawPoint(60, 30)
        painter.drawPoint(60, 40), painter.drawPoint(60, 50), painter.drawPoint(60, 60)
        painter.drawPoint(60, 70)
        ###############################60
        painter.drawPoint(70, 10), painter.drawPoint(70, 20), painter.drawPoint(70, 30)
        painter.drawPoint(70, 40), painter.drawPoint(70, 50), painter.drawPoint(70, 60)
        #######################################################################################70
        painter.drawPoint(80, 10), painter.drawPoint(80, 20), painter.drawPoint(80, 30)
        painter.drawPoint(80, 40), painter.drawPoint(80, 50)
        #######################################################80
        painter.drawPoint(90, 10), painter.drawPoint(90, 20), painter.drawPoint(90, 30)
        painter.drawPoint(90, 40)
        ##############################90
        painter.drawPoint(100, 10), painter.drawPoint(100, 20), painter.drawPoint(100, 30)
        painter.drawPoint(110, 10), painter.drawPoint(110, 20), painter.drawPoint(110, 30)
        ###################################################################################100~110
        painter.drawPoint(120, 10), painter.drawPoint(120, 20)
        painter.drawPoint(130, 10), painter.drawPoint(130, 20)
        painter.drawPoint(140, 10), painter.drawPoint(140, 20)
        painter.drawPoint(150, 10), painter.drawPoint(150, 20)
        painter.drawPoint(160, 10), painter.drawPoint(160, 20)
        painter.drawPoint(170, 10), painter.drawPoint(170, 20)
        painter.drawPoint(180, 10), painter.drawPoint(180, 20)
        painter.drawPoint(190, 10), painter.drawPoint(190, 20)
        painter.drawPoint(200, 10), painter.drawPoint(200, 20)
        painter.drawPoint(210, 10), painter.drawPoint(210, 20)
        painter.drawPoint(220, 10), painter.drawPoint(220, 20)
        painter.drawPoint(230, 10), painter.drawPoint(230, 20)
        painter.drawPoint(240, 10), painter.drawPoint(240, 20)
        painter.drawPoint(250, 10), painter.drawPoint(250, 20)
        painter.drawPoint(260, 10), painter.drawPoint(260, 20)
        painter.drawPoint(270, 10), painter.drawPoint(270, 20)
        painter.drawPoint(280, 10), painter.drawPoint(280, 20)
        painter.drawPoint(290, 10), painter.drawPoint(290, 20)
        painter.drawPoint(300, 10), painter.drawPoint(300, 20)
        painter.drawPoint(310, 10), painter.drawPoint(310, 20)
        painter.drawPoint(320, 10), painter.drawPoint(320, 20)
        painter.drawPoint(330, 10), painter.drawPoint(330, 20)
        painter.drawPoint(340, 10), painter.drawPoint(340, 20)
        painter.drawPoint(350, 10), painter.drawPoint(350, 20)
        painter.drawPoint(360, 10), painter.drawPoint(360, 20)
        painter.drawPoint(370, 10), painter.drawPoint(370, 20)
        painter.drawPoint(380, 10), painter.drawPoint(380, 20)
        painter.drawPoint(390, 10), painter.drawPoint(390, 20)
        painter.drawPoint(400, 10), painter.drawPoint(400, 20)
        painter.drawPoint(410, 10), painter.drawPoint(410, 20)
        painter.drawPoint(420, 10), painter.drawPoint(420, 20)
        painter.drawPoint(430, 10), painter.drawPoint(430, 20)
        painter.drawPoint(440, 10), painter.drawPoint(440, 20)
        painter.drawPoint(450, 10), painter.drawPoint(450, 20)
        painter.drawPoint(460, 10), painter.drawPoint(460, 20)
        painter.drawPoint(470, 10), painter.drawPoint(470, 20)
        painter.drawPoint(480, 10), painter.drawPoint(480, 20)
        painter.drawPoint(490, 10), painter.drawPoint(490, 20)
        painter.drawPoint(500, 10), painter.drawPoint(500, 20)
        ###########################################################120~500
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyCanvas()
    sys.exit(app.exec_())
    
