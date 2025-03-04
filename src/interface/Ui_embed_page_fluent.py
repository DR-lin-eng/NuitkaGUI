# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'embed_page_fluent.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
)
from PySide6.QtGui import (
    QColor,
    QIcon,
)
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from qfluentwidgets import (
    BodyLabel,
    ElevatedCardWidget,
    IconWidget,
    PrimaryPushButton,
    ScrollArea,
    TitleLabel,
)
from src.component.embed_file_tree import EmbedFileTree
from src.resource import rc_res

rc_res = rc_res  # 防止格式化的时候资源文件被删除


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(870, 584)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea = ScrollArea(Form)
        self.ScrollArea.setObjectName("ScrollArea")
        self.ScrollArea.setFrameShape(QFrame.NoFrame)
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 870, 584))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 10, 30, 30)
        self.ElevatedCardWidget = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget.setObjectName("ElevatedCardWidget")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ElevatedCardWidget.sizePolicy().hasHeightForWidth()
        )
        self.ElevatedCardWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.ElevatedCardWidget)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.IconWidget = IconWidget(self.ElevatedCardWidget)
        self.IconWidget.setObjectName("IconWidget")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy1)
        self.IconWidget.setMinimumSize(QSize(64, 64))
        self.IconWidget.setMaximumSize(QSize(64, 64))
        self.IconWidget.setStyleSheet("")
        icon = QIcon()
        icon.addFile(
            ":/Icons/materialIcons/icons8_archive.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.IconWidget.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.IconWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitleLabel = TitleLabel(self.ElevatedCardWidget)
        self.TitleLabel.setObjectName("TitleLabel")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy2)
        self.TitleLabel.setStyleSheet("")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.BodyLabel = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel.setObjectName("BodyLabel")
        sizePolicy2.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy2)
        self.BodyLabel.setWordWrap(False)
        self.BodyLabel.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_2.addWidget(self.BodyLabel)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.addWidget(self.ElevatedCardWidget)

        self.treeWidget = EmbedFileTree(self.scrollAreaWidgetContents)
        self.treeWidget.setObjectName("treeWidget")

        self.verticalLayout_3.addWidget(self.treeWidget)

        self.BTNFlushDir = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.BTNFlushDir.setObjectName("BTNFlushDir")
        icon1 = QIcon()
        icon1.addFile(
            ":/Icons/materialIcons/icons8_double_down.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.BTNFlushDir.setIcon(icon1)
        self.BTNFlushDir.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.BTNFlushDir)

        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.ScrollArea)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.TitleLabel.setText(
            QCoreApplication.translate("Form", "\u5d4c\u5165\u6587\u4ef6", None)
        )
        self.BodyLabel.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>\u5728\u4e0b\u9762\u9009\u4e2d\u4f60\u9700\u8981\u5d4c\u5165\u7684\u6587\u4ef6\uff0c\u8fd9\u4e9b\u5185\u5bb9\u6700\u7ec8\u4f1a\u4f1a\u88ab\u7f16\u8bd1\u5230exe\u5f53\u4e2d(\u5982\u679c\u4f7f\u7528\u5355\u6587\u4ef6\u6253\u5305)<br/>\u5176\u4e2d\u7684\u8def\u5f84\u5219\u662f\u91c7\u7528\u76f8\u5bf9\u6253\u5305\u6587\u4ef6\u7684\u8def\u5f84</p></body></html>",
                None,
            )
        )
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(
            3, QCoreApplication.translate("Form", "\u6587\u4ef6\u7c7b\u578b", None)
        )
        ___qtreewidgetitem.setText(
            2, QCoreApplication.translate("Form", "\u76f8\u5bf9\u8def\u5f84", None)
        )
        ___qtreewidgetitem.setText(
            1, QCoreApplication.translate("Form", "\u7edd\u5bf9\u8def\u5f84", None)
        )
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("Form", "\u540d\u79f0", None)
        )
        # if QT_CONFIG(tooltip)
        self.BTNFlushDir.setToolTip(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>\u8b66\u544a:\u5c3d\u53ef\u80fd\u4e0d\u8981\u4f7f\u7528\u9664\u4e86\u9879\u76ee\u8def\u5f84\u5916\u7684\u5176\u4ed6\u8def\u5f84\uff0c\u53ef\u80fd\u4f1a\u5bfc\u81f4\u610f\u6599\u4e4b\u5916\u7684\u9519\u8bef</p><p>\u7a0b\u5e8f\u5bfb\u627e\u8fd9\u4e9b\u989d\u5916\u7684\u6587\u4ef6\u662f\u4f7f\u7528\u76f8\u5bf9\u8def\u5f84\u8fdb\u884c\u5bfb\u627e</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.BTNFlushDir.setStatusTip(
            QCoreApplication.translate(
                "Form",
                "\u8b66\u544a:\u5c3d\u53ef\u80fd\u4e0d\u8981\u4f7f\u7528\u9664\u4e86\u9879\u76ee\u8def\u5f84\u5916\u7684\u5176\u4ed6\u8def\u5f84\uff0c\u53ef\u80fd\u4f1a\u5bfc\u81f4\u610f\u6599\u4e4b\u5916\u7684\u9519\u8bef \u7a0b\u5e8f\u5bfb\u627e\u8fd9\u4e9b\u989d\u5916\u7684\u6587\u4ef6\u662f\u4f7f\u7528\u76f8\u5bf9\u8def\u5f84\u8fdb\u884c\u5bfb\u627e",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.BTNFlushDir.setWhatsThis(
            QCoreApplication.translate(
                "Form",
                "\u8b66\u544a:\u5c3d\u53ef\u80fd\u4e0d\u8981\u4f7f\u7528\u9664\u4e86\u9879\u76ee\u8def\u5f84\u5916\u7684\u5176\u4ed6\u8def\u5f84\uff0c\u53ef\u80fd\u4f1a\u5bfc\u81f4\u610f\u6599\u4e4b\u5916\u7684\u9519\u8bef \u7a0b\u5e8f\u5bfb\u627e\u8fd9\u4e9b\u989d\u5916\u7684\u6587\u4ef6\u662f\u4f7f\u7528\u76f8\u5bf9\u8def\u5f84\u8fdb\u884c\u5bfb\u627e",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.BTNFlushDir.setText(
            QCoreApplication.translate("Form", "\u8f7d\u5165", None)
        )

    # retranslateUi
