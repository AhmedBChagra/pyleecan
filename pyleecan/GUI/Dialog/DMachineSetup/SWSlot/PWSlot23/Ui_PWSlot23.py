# -*- coding: utf-8 -*-

# File generated according to PWSlot23.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot23(object):
    def setupUi(self, PWSlot23):
        if not PWSlot23.objectName():
            PWSlot23.setObjectName(u"PWSlot23")
        PWSlot23.resize(848, 470)
        PWSlot23.setMinimumSize(QSize(630, 470))
        PWSlot23.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot23)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PWSlot23)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WSlot/SlotW23.png")
        )
        self.img_slot.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PWSlot23)
        self.txt_constraint.setObjectName(u"txt_constraint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy1)
        self.txt_constraint.setMaximumSize(QSize(16777215, 70))
        self.txt_constraint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_2.addWidget(self.txt_constraint)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.widget = QWidget(PWSlot23)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 0))
        self.widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.is_cst_tooth = QCheckBox(self.widget)
        self.is_cst_tooth.setObjectName(u"is_cst_tooth")

        self.verticalLayout.addWidget(self.is_cst_tooth)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_W0 = QLabel(self.widget)
        self.in_W0.setObjectName(u"in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.lf_W0 = FloatEdit(self.widget)
        self.lf_W0.setObjectName(u"lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.unit_W0 = QLabel(self.widget)
        self.unit_W0.setObjectName(u"unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)

        self.in_W1 = QLabel(self.widget)
        self.in_W1.setObjectName(u"in_W1")

        self.gridLayout.addWidget(self.in_W1, 1, 0, 1, 1)

        self.lf_W1 = FloatEdit(self.widget)
        self.lf_W1.setObjectName(u"lf_W1")

        self.gridLayout.addWidget(self.lf_W1, 1, 1, 1, 1)

        self.unit_W1 = QLabel(self.widget)
        self.unit_W1.setObjectName(u"unit_W1")

        self.gridLayout.addWidget(self.unit_W1, 1, 2, 1, 1)

        self.in_W2 = QLabel(self.widget)
        self.in_W2.setObjectName(u"in_W2")

        self.gridLayout.addWidget(self.in_W2, 2, 0, 1, 1)

        self.lf_W2 = FloatEdit(self.widget)
        self.lf_W2.setObjectName(u"lf_W2")

        self.gridLayout.addWidget(self.lf_W2, 2, 1, 1, 1)

        self.unit_W2 = QLabel(self.widget)
        self.unit_W2.setObjectName(u"unit_W2")

        self.gridLayout.addWidget(self.unit_W2, 2, 2, 1, 1)

        self.in_W3 = QLabel(self.widget)
        self.in_W3.setObjectName(u"in_W3")

        self.gridLayout.addWidget(self.in_W3, 3, 0, 1, 1)

        self.lf_W3 = FloatEdit(self.widget)
        self.lf_W3.setObjectName(u"lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 3, 1, 1, 1)

        self.unit_W3 = QLabel(self.widget)
        self.unit_W3.setObjectName(u"unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 3, 2, 1, 1)

        self.in_H0 = QLabel(self.widget)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 4, 0, 1, 1)

        self.lf_H0 = FloatEdit(self.widget)
        self.lf_H0.setObjectName(u"lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 4, 1, 1, 1)

        self.unit_H0 = QLabel(self.widget)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 4, 2, 1, 1)

        self.in_H1 = QLabel(self.widget)
        self.in_H1.setObjectName(u"in_H1")

        self.gridLayout.addWidget(self.in_H1, 5, 0, 1, 1)

        self.lf_H1 = FloatEdit(self.widget)
        self.lf_H1.setObjectName(u"lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 5, 1, 1, 1)

        self.in_H2 = QLabel(self.widget)
        self.in_H2.setObjectName(u"in_H2")

        self.gridLayout.addWidget(self.in_H2, 6, 0, 1, 1)

        self.lf_H2 = FloatEdit(self.widget)
        self.lf_H2.setObjectName(u"lf_H2")

        self.gridLayout.addWidget(self.lf_H2, 6, 1, 1, 1)

        self.unit_H2 = QLabel(self.widget)
        self.unit_H2.setObjectName(u"unit_H2")

        self.gridLayout.addWidget(self.unit_H2, 6, 2, 1, 1)

        self.unit_H1 = QLabel(self.widget)
        self.unit_H1.setObjectName(u"unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 5, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.widget)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.horizontalLayout.addWidget(self.widget)

        QWidget.setTabOrder(self.is_cst_tooth, self.lf_W0)
        QWidget.setTabOrder(self.lf_W0, self.lf_W1)
        QWidget.setTabOrder(self.lf_W1, self.lf_W2)
        QWidget.setTabOrder(self.lf_W2, self.lf_W3)
        QWidget.setTabOrder(self.lf_W3, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_H2)
        QWidget.setTabOrder(self.lf_H2, self.txt_constraint)

        self.retranslateUi(PWSlot23)

        QMetaObject.connectSlotsByName(PWSlot23)

    # setupUi

    def retranslateUi(self, PWSlot23):
        PWSlot23.setWindowTitle(QCoreApplication.translate("PWSlot23", u"Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PWSlot23",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">W0 &lt;= W1</span></p></body></html>',
                None,
            )
        )
        self.is_cst_tooth.setText(
            QCoreApplication.translate("PWSlot23", u"Constant Tooth Width", None)
        )
        self.in_W0.setText(QCoreApplication.translate("PWSlot23", u"W0", None))
        self.unit_W0.setText(QCoreApplication.translate("PWSlot23", u"m", None))
        self.in_W1.setText(QCoreApplication.translate("PWSlot23", u"W1", None))
        self.unit_W1.setText(QCoreApplication.translate("PWSlot23", u"m", None))
        self.in_W2.setText(QCoreApplication.translate("PWSlot23", u"W2", None))
        self.unit_W2.setText(QCoreApplication.translate("PWSlot23", u"m", None))
        self.in_W3.setText(QCoreApplication.translate("PWSlot23", u"W3", None))
        self.unit_W3.setText(QCoreApplication.translate("PWSlot23", u"m", None))
        self.in_H0.setText(QCoreApplication.translate("PWSlot23", u"H0", None))
        self.unit_H0.setText(QCoreApplication.translate("PWSlot23", u"m", None))
        self.in_H1.setText(QCoreApplication.translate("PWSlot23", u"H1", None))
        self.in_H2.setText(QCoreApplication.translate("PWSlot23", u"H2", None))
        self.unit_H2.setText(QCoreApplication.translate("PWSlot23", u"m", None))
        self.unit_H1.setText(QCoreApplication.translate("PWSlot23", u"m", None))

    # retranslateUi
