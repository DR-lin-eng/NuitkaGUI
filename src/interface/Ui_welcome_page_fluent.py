# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_page_fluent.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QColor,
)
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLayout,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)

from qfluentwidgets import (
    BodyLabel,
    CardWidget,
    DisplayLabel,
    HyperlinkButton,
    PrimaryPushButton,
    ProgressBar,
    PushButton,
    TitleLabel,
)
from src.resource import rc_res

rc_res = rc_res  # 防止格式化的时候资源文件被删除


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1000, 650)
        Form.setMinimumSize(QSize(1000, 650))
        Form.setMaximumSize(QSize(1000, 650))
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.DisplayLabel = DisplayLabel(Form)
        self.DisplayLabel.setObjectName("DisplayLabel")
        self.DisplayLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.DisplayLabel)

        self.BodyLabel = BodyLabel(Form)
        self.BodyLabel.setObjectName("BodyLabel")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy)
        self.BodyLabel.setAlignment(Qt.AlignCenter)
        self.BodyLabel.setWordWrap(True)
        self.BodyLabel.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_4.addWidget(self.BodyLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(45)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 10, 30, 10)
        self.CardWidget_3 = CardWidget(Form)
        self.CardWidget_3.setObjectName("CardWidget_3")
        self.CardWidget_3.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.CardWidget_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.TitleLabel_3 = TitleLabel(self.CardWidget_3)
        self.TitleLabel_3.setObjectName("TitleLabel_3")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.TitleLabel_3.sizePolicy().hasHeightForWidth()
        )
        self.TitleLabel_3.setSizePolicy(sizePolicy1)
        self.TitleLabel_3.setMinimumSize(QSize(0, 0))
        self.TitleLabel_3.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.TitleLabel_3.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.TitleLabel_3)

        self.BodyLabel_4 = BodyLabel(self.CardWidget_3)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        sizePolicy.setHeightForWidth(self.BodyLabel_4.sizePolicy().hasHeightForWidth())
        self.BodyLabel_4.setSizePolicy(sizePolicy)
        self.BodyLabel_4.setAlignment(Qt.AlignCenter)
        self.BodyLabel_4.setWordWrap(True)
        self.BodyLabel_4.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_3.addWidget(self.BodyLabel_4)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.PushButton_3 = PushButton(self.CardWidget_3)
        self.PushButton_3.setObjectName("PushButton_3")

        self.verticalLayout_3.addWidget(self.PushButton_3)

        self.PrimaryPushButton_3 = PrimaryPushButton(self.CardWidget_3)
        self.PrimaryPushButton_3.setObjectName("PrimaryPushButton_3")

        self.verticalLayout_3.addWidget(self.PrimaryPushButton_3)

        self.horizontalLayout.addWidget(self.CardWidget_3)

        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName("CardWidget")
        sizePolicy.setHeightForWidth(self.CardWidget.sizePolicy().hasHeightForWidth())
        self.CardWidget.setSizePolicy(sizePolicy)
        self.CardWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.CardWidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.CardWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.TitleLabel = TitleLabel(self.CardWidget)
        self.TitleLabel.setObjectName("TitleLabel")
        sizePolicy1.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy1)
        self.TitleLabel.setMinimumSize(QSize(0, 0))
        self.TitleLabel.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.TitleLabel.setWordWrap(False)

        self.verticalLayout.addWidget(self.TitleLabel)

        self.BodyLabel_2 = BodyLabel(self.CardWidget)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        sizePolicy.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy)
        self.BodyLabel_2.setAlignment(Qt.AlignCenter)
        self.BodyLabel_2.setWordWrap(True)
        self.BodyLabel_2.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout.addWidget(self.BodyLabel_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.PushButton = PushButton(self.CardWidget)
        self.PushButton.setObjectName("PushButton")

        self.verticalLayout.addWidget(self.PushButton)

        self.PrimaryPushButton = PrimaryPushButton(self.CardWidget)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")

        self.verticalLayout.addWidget(self.PrimaryPushButton)

        self.horizontalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(Form)
        self.CardWidget_2.setObjectName("CardWidget_2")
        self.CardWidget_2.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.CardWidget_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.TitleLabel_2 = TitleLabel(self.CardWidget_2)
        self.TitleLabel_2.setObjectName("TitleLabel_2")
        sizePolicy1.setHeightForWidth(
            self.TitleLabel_2.sizePolicy().hasHeightForWidth()
        )
        self.TitleLabel_2.setSizePolicy(sizePolicy1)
        self.TitleLabel_2.setMinimumSize(QSize(0, 0))
        self.TitleLabel_2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.TitleLabel_2.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.TitleLabel_2)

        self.BodyLabel_3 = BodyLabel(self.CardWidget_2)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        sizePolicy.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy)
        self.BodyLabel_3.setAlignment(Qt.AlignCenter)
        self.BodyLabel_3.setWordWrap(True)
        self.BodyLabel_3.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_2.addWidget(self.BodyLabel_3)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.PushButton_2 = PushButton(self.CardWidget_2)
        self.PushButton_2.setObjectName("PushButton_2")

        self.verticalLayout_2.addWidget(self.PushButton_2)

        self.PrimaryPushButton_2 = PrimaryPushButton(self.CardWidget_2)
        self.PrimaryPushButton_2.setObjectName("PrimaryPushButton_2")

        self.verticalLayout_2.addWidget(self.PrimaryPushButton_2)

        self.horizontalLayout.addWidget(self.CardWidget_2)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.finishedBtn = PushButton(Form)
        self.finishedBtn.setObjectName("finishedBtn")
        self.finishedBtn.setEnabled(False)
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.finishedBtn.sizePolicy().hasHeightForWidth())
        self.finishedBtn.setSizePolicy(sizePolicy2)
        self.finishedBtn.setSizeIncrement(QSize(0, 0))
        self.finishedBtn.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.finishedBtn)

        self.HyperlinkButton = HyperlinkButton(Form)
        self.HyperlinkButton.setObjectName("HyperlinkButton")

        self.verticalLayout_4.addWidget(self.HyperlinkButton)

        self.ProgressBar = ProgressBar(Form)
        self.ProgressBar.setObjectName("ProgressBar")
        self.ProgressBar.setMaximum(3)
        self.ProgressBar.setValue(0)

        self.verticalLayout_4.addWidget(self.ProgressBar)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate(
                "Form", "\u9996\u6b21\u8bbe\u7f6e\u9875\u9762", None
            )
        )
        self.DisplayLabel.setText(
            QCoreApplication.translate(
                "Form", "\u6b22\u8fce\u4f7f\u7528NuitkaGUI", None
            )
        )
        self.BodyLabel.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>\u5f53\u524d\u7a97\u4f53\u4ec5\u4f1a\u51fa\u73b0\u4e00\u6b21\uff0c\u60a8\u9700\u8981\u5b8c\u6210\u4e0b\u9762\u7684\u914d\u7f6e\u9879</p><p>\u60a8\u4e5f\u53ef\u4ee5\u7a0d\u540e\u5728\u8bbe\u7f6e\u4e2d\u4fee\u6539</p></body></html>",
                None,
            )
        )
        self.TitleLabel_3.setText(
            QCoreApplication.translate("Form", "\u8bbe\u7f6e\u955c\u50cf\u6e90", None)
        )
        self.BodyLabel_4.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>\u9009\u62e9\u4e00\u4e2a\u6700\u5feb\u7684 pip \u4e0b\u8f7d\u955c\u50cf\u6e90</p><p>\u70b9\u51fb\u4e0b\u65b9\u6309\u94ae\u81ea\u52a8\u4ece\u5185\u7f6e\u76845\u4e2a\u955c\u50cf\u6e90\u4e2d\u9009\u62e9\u6700\u5feb\u7684\u4e00\u4e2a\u4e3a\u9ed8\u8ba4\u955c\u50cf\u6e90</p></body></html>",
                None,
            )
        )
        self.PushButton_3.setText(
            QCoreApplication.translate("Form", "\u4f7f\u7528\u5b98\u65b9pypi", None)
        )
        self.PrimaryPushButton_3.setText(
            QCoreApplication.translate("Form", "\u81ea\u52a8\u68c0\u6d4b", None)
        )
        self.TitleLabel.setText(
            QCoreApplication.translate("Form", "Python.exe\u8def\u5f84", None)
        )
        self.BodyLabel_2.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>\u8bf7\u9009\u62e9\u4e00\u4e2a\u53ef\u7528\u7684 Python.exe \u8def\u5f84</p><p>\u9009\u62e9\u5b8c\u6bd5\u4f1a\u7acb\u5373\u4e0b\u8f7d\u4e00\u4e9b\u7b2c\u4e09\u65b9\u5e93<br/></p></body></html>",
                None,
            )
        )
        self.PushButton.setText(
            QCoreApplication.translate("Form", "\u624b\u52a8\u641c\u7d22", None)
        )
        self.PrimaryPushButton.setText(
            QCoreApplication.translate("Form", "\u81ea\u52a8\u641c\u7d22", None)
        )
        self.TitleLabel_2.setText(
            QCoreApplication.translate("Form", "\u4f9d\u8d56\u5b89\u88c5", None)
        )
        self.BodyLabel_3.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>Nuitka\u9700\u8981\u5404\u79cd\u4f9d\u8d56</p><p>\u60a8\u53ef\u4ee5\u76f4\u63a5\u901a\u8fc7NuitkaGUI\u5feb\u901f\u89e3\u538b\u5230\u73af\u5883\u53d8\u91cf\u4e2d\uff0c\u4e3a\u60a8\u8282\u7701\u5927\u91cf\u4e0b\u8f7d\u65f6\u95f4</p></body></html>",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.PushButton_2.setToolTip(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>\u4f9d\u8d56\u4ec5\u5728\u8fd0\u884cNuitkaGUI\u65f6\u751f\u6548\uff0c\u9000\u51fa\u65f6\u81ea\u52a8\u6e05\u7a7a\u73af\u5883\u53d8\u91cf</p><p>\u4f7f\u7528\u8be5\u65b9\u6cd5\u80fd\u591f\u4e0d\u6c61\u67d3\u7cfb\u7edf\u73af\u5883\u53d8\u91cf</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.PushButton_2.setText(
            QCoreApplication.translate("Form", "\u4ec5\u5728\u8fd0\u884c\u65f6", None)
        )
        # if QT_CONFIG(tooltip)
        self.PrimaryPushButton_2.setToolTip(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>\u5b89\u88c5\u4e4b\u540e\u60a8\u53ef\u4ee5\u5728\u5176\u4ed6\u4efb\u4f55\u5730\u65b9\u4f7f\u7528\u5df2\u6709\u7684\u4f9d\u8d56,\u4f46\u662f\u4f1a\u4fee\u6539\u60a8\u7cfb\u7edf\u7684\u73af\u5883\u53d8\u91cf</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.PrimaryPushButton_2.setText(
            QCoreApplication.translate(
                "Form", "\u6dfb\u52a0\u7cfb\u7edf\u73af\u5883\u53d8\u91cf", None
            )
        )
        self.finishedBtn.setText(
            QCoreApplication.translate(
                "Form", "\u60a8\u9700\u8981\u5148\u5b8c\u6210\u8bbe\u7f6e", None
            )
        )
        self.HyperlinkButton.setText(
            QCoreApplication.translate(
                "Form",
                "\u76f4\u63a5\u8df3\u8fc7\uff0c\u6211\u7a0d\u540e\u81ea\u884c\u8bbe\u7f6e",
                None,
            )
        )

    # retranslateUi
