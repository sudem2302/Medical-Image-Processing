# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1315, 720)
        Widget.setMinimumSize(QSize(1312, 0))
        Widget.setSizeIncrement(QSize(0, 0))
        self.load_button = QPushButton(Widget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setGeometry(QRect(20, 30, 110, 30))
        self.original_label = QLabel(Widget)
        self.original_label.setObjectName(u"original_label")
        self.original_label.setGeometry(QRect(70, 90, 550, 410))
        self.processed_label = QLabel(Widget)
        self.processed_label.setObjectName(u"processed_label")
        self.processed_label.setGeometry(QRect(680, 90, 550, 410))
        self.edge_button = QPushButton(Widget)
        self.edge_button.setObjectName(u"edge_button")
        self.edge_button.setGeometry(QRect(730, 660, 100, 30))
        self.sharpen_button = QPushButton(Widget)
        self.sharpen_button.setObjectName(u"sharpen_button")
        self.sharpen_button.setGeometry(QRect(600, 660, 100, 30))
        self.brightness_slider = QSlider(Widget)
        self.brightness_slider.setObjectName(u"brightness_slider")
        self.brightness_slider.setGeometry(QRect(680, 560, 240, 20))
        self.brightness_slider.setMinimum(-100)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setOrientation(Qt.Orientation.Horizontal)
        self.contrast_slider = QSlider(Widget)
        self.contrast_slider.setObjectName(u"contrast_slider")
        self.contrast_slider.setGeometry(QRect(680, 600, 240, 20))
        self.contrast_slider.setMinimum(10)
        self.contrast_slider.setMaximum(300)
        self.contrast_slider.setValue(100)
        self.contrast_slider.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 560, 62, 20))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(600, 600, 62, 20))
        self.hist_button = QPushButton(Widget)
        self.hist_button.setObjectName(u"hist_button")
        self.hist_button.setGeometry(QRect(70, 560, 180, 30))
        self.auto_enhance_button = QPushButton(Widget)
        self.auto_enhance_button.setObjectName(u"auto_enhance_button")
        self.auto_enhance_button.setGeometry(QRect(70, 600, 180, 30))
        self.highlight_button = QPushButton(Widget)
        self.highlight_button.setObjectName(u"highlight_button")
        self.highlight_button.setGeometry(QRect(70, 640, 180, 30))
        self.canny_thresh1_spin = QSpinBox(Widget)
        self.canny_thresh1_spin.setObjectName(u"canny_thresh1_spin")
        self.canny_thresh1_spin.setGeometry(QRect(380, 560, 70, 30))
        self.canny_thresh1_spin.setMaximum(500)
        self.canny_thresh1_spin.setSingleStep(1)
        self.canny_thresh1_spin.setValue(100)
        self.canny_thresh2_spin = QSpinBox(Widget)
        self.canny_thresh2_spin.setObjectName(u"canny_thresh2_spin")
        self.canny_thresh2_spin.setGeometry(QRect(380, 600, 70, 30))
        self.canny_thresh2_spin.setMaximum(500)
        self.canny_thresh2_spin.setSingleStep(1)
        self.canny_thresh2_spin.setValue(150)
        self.area_threshold_spin = QSpinBox(Widget)
        self.area_threshold_spin.setObjectName(u"area_threshold_spin")
        self.area_threshold_spin.setGeometry(QRect(380, 670, 70, 30))
        self.area_threshold_spin.setMaximum(10000)
        self.area_threshold_spin.setSingleStep(1)
        self.area_threshold_spin.setValue(500)
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 520, 210, 20))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 560, 60, 20))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 600, 60, 20))
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 640, 100, 20))
        self.undo_button = QPushButton(Widget)
        self.undo_button.setObjectName(u"undo_button")
        self.undo_button.setGeometry(QRect(680, 30, 110, 30))
        self.redo_button = QPushButton(Widget)
        self.redo_button.setObjectName(u"redo_button")
        self.redo_button.setGeometry(QRect(810, 30, 110, 30))
        self.reset_button = QPushButton(Widget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(940, 30, 110, 30))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.load_button.setText(QCoreApplication.translate("Widget", u"G\u00f6rsel Y\u00fckle", None))
        self.original_label.setText(QCoreApplication.translate("Widget", u"Orijinal G\u00f6rsel", None))
        self.processed_label.setText(QCoreApplication.translate("Widget", u"\u0130\u015flenmi\u015f G\u00f6rsel", None))
        self.edge_button.setText(QCoreApplication.translate("Widget", u"Kenar Tespit", None))
        self.sharpen_button.setText(QCoreApplication.translate("Widget", u"Keskinle\u015ftir", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Parlakl\u0131k:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Kontrast:", None))
        self.hist_button.setText(QCoreApplication.translate("Widget", u"Histogram G\u00f6ster", None))
        self.auto_enhance_button.setText(QCoreApplication.translate("Widget", u"Otomatik \u0130yile\u015ftir", None))
        self.highlight_button.setText(QCoreApplication.translate("Widget", u"Anormal Alanlar\u0131 \u0130\u015faretle", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Kenar alg\u0131lamada hassasiyetin", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Min:", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Max:", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u00c7ember Alan\u0131:", None))
        self.undo_button.setText(QCoreApplication.translate("Widget", u"Geri", None))
        self.redo_button.setText(QCoreApplication.translate("Widget", u"\u0130leri", None))
        self.reset_button.setText(QCoreApplication.translate("Widget", u"S\u0131f\u0131rla", None))
    # retranslateUi

