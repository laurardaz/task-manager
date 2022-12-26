# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 674)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color:#fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color: #3F8FD2;\n"
"}\n"
"#leftMenuSubContainer{\n"
"    background-color: #043C6B;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"    text-align: left;\n"
"    padding: 8px 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"    background-color: #25547B;\n"
"}\n"
"#profileSubContainer{\n"
"    background-color: #25547B;\n"
"    border-radius: 10px;\n"
"}\n"
"#frame_7, #popupNotificationSubContainer{\n"
"    background-color:#043C6B;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuContainer = QtWidgets.QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leftMenuSubContainer = QtWidgets.QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuBtn = QtWidgets.QPushButton(self.frame)
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/feather/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_2.addWidget(self.menuBtn)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.homeBtn = QtWidgets.QPushButton(self.frame_3)
        self.homeBtn.setStyleSheet("background-color: #25547B;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/feather/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(24, 24))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_3.addWidget(self.homeBtn)
        self.projectsBtn = QtWidgets.QPushButton(self.frame_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/feather/layers.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.projectsBtn.setIcon(icon2)
        self.projectsBtn.setIconSize(QtCore.QSize(24, 24))
        self.projectsBtn.setObjectName("projectsBtn")
        self.verticalLayout_3.addWidget(self.projectsBtn)
        self.tasksBtn = QtWidgets.QPushButton(self.frame_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/feather/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tasksBtn.setIcon(icon3)
        self.tasksBtn.setIconSize(QtCore.QSize(24, 24))
        self.tasksBtn.setObjectName("tasksBtn")
        self.verticalLayout_3.addWidget(self.tasksBtn)
        self.statisticsBtn = QtWidgets.QPushButton(self.frame_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/feather/activity.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statisticsBtn.setIcon(icon4)
        self.statisticsBtn.setIconSize(QtCore.QSize(24, 24))
        self.statisticsBtn.setObjectName("statisticsBtn")
        self.verticalLayout_3.addWidget(self.statisticsBtn)
        self.calendarBtn = QtWidgets.QPushButton(self.frame_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/feather/calendar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calendarBtn.setIcon(icon5)
        self.calendarBtn.setIconSize(QtCore.QSize(24, 24))
        self.calendarBtn.setObjectName("calendarBtn")
        self.verticalLayout_3.addWidget(self.calendarBtn)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_4 = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.settingsBtn = QtWidgets.QPushButton(self.frame_4)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/feather/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon6)
        self.settingsBtn.setIconSize(QtCore.QSize(24, 24))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_4.addWidget(self.settingsBtn)
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, QtCore.Qt.AlignLeft)
        self.mainBodyContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet("")
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.headerContainer = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy)
        self.headerContainer.setObjectName("headerContainer")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.headerContainer)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_5.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/feather/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.horizontalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignRight)
        self.frame_5 = QtWidgets.QFrame(self.headerContainer)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_6.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/feather/feather.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/feather/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon9)
        self.pushButton_4.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.horizontalLayout_4.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(self.headerContainer)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minimizeBtn = QtWidgets.QPushButton(self.frame_2)
        self.minimizeBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/feather/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeBtn.setIcon(icon10)
        self.minimizeBtn.setIconSize(QtCore.QSize(24, 24))
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_3.addWidget(self.minimizeBtn)
        self.restoreBtn = QtWidgets.QPushButton(self.frame_2)
        self.restoreBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/feather/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreBtn.setIcon(icon11)
        self.restoreBtn.setIconSize(QtCore.QSize(24, 24))
        self.restoreBtn.setObjectName("restoreBtn")
        self.horizontalLayout_3.addWidget(self.restoreBtn)
        self.closeBtn = QtWidgets.QPushButton(self.frame_2)
        self.closeBtn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/feather/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon12)
        self.closeBtn.setIconSize(QtCore.QSize(24, 24))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_3.addWidget(self.closeBtn)
        self.horizontalLayout_4.addWidget(self.frame_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.headerContainer, 0, QtCore.Qt.AlignTop)
        self.mainBodyContent = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.mainBodyContent.setMinimumSize(QtCore.QSize(0, 0))
        self.mainBodyContent.setObjectName("mainBodyContent")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.mainContentsContainer = QtWidgets.QWidget(self.mainBodyContent)
        self.mainContentsContainer.setMinimumSize(QtCore.QSize(0, 0))
        self.mainContentsContainer.setObjectName("mainContentsContainer")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainContentsContainer)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_5 = QtWidgets.QLabel(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_14.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.page_5)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_9.addWidget(self.stackedWidget)
        self.horizontalLayout_7.addWidget(self.mainContentsContainer)
        self.profileContainer = QtWidgets.QWidget(self.mainBodyContent)
        self.profileContainer.setMinimumSize(QtCore.QSize(230, 0))
        self.profileContainer.setObjectName("profileContainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.profileContainer)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.profileSubContainer = QtWidgets.QWidget(self.profileContainer)
        self.profileSubContainer.setMinimumSize(QtCore.QSize(230, 0))
        self.profileSubContainer.setObjectName("profileSubContainer")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.profileSubContainer)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.profileSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_7.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/feather/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon13)
        self.pushButton_7.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_8.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.widget = QtWidgets.QWidget(self.profileSubContainer)
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.verticalLayout_7.addWidget(self.widget)
        self.verticalLayout_6.addWidget(self.profileSubContainer, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_7.addWidget(self.profileContainer, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.mainBodyContent)
        self.popupNotificationContainer = QtWidgets.QWidget(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName("popupNotificationContainer")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.popupNotificationSubContainer = QtWidgets.QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName("popupNotificationSubContainer")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.popupNotificationSubContainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_16.addWidget(self.label_9)
        self.frame_8 = QtWidgets.QFrame(self.popupNotificationSubContainer)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_8.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/feather/x-octagon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon14)
        self.pushButton_8.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_9.addWidget(self.pushButton_8, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_16.addWidget(self.frame_8)
        self.verticalLayout_15.addWidget(self.popupNotificationSubContainer)
        self.verticalLayout_5.addWidget(self.popupNotificationContainer)
        self.footerContainer = QtWidgets.QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName("footerContainer")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_9 = QtWidgets.QFrame(self.footerContainer)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.frame_9)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.horizontalLayout_11.addWidget(self.frame_9)
        self.sizeGrip = QtWidgets.QFrame(self.footerContainer)
        self.sizeGrip.setMinimumSize(QtCore.QSize(30, 30))
        self.sizeGrip.setMaximumSize(QtCore.QSize(30, 30))
        self.sizeGrip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sizeGrip.setObjectName("sizeGrip")
        self.label_11 = QtWidgets.QLabel(self.sizeGrip)
        self.label_11.setGeometry(QtCore.QRect(20, 0, 58, 18))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.sizeGrip)
        self.verticalLayout_5.addWidget(self.footerContainer)
        self.horizontalLayout.addWidget(self.mainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 948, 30))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task-tracker"))
        self.menuBtn.setToolTip(_translate("MainWindow", "Menu"))
        self.homeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.homeBtn.setText(_translate("MainWindow", "Главное меню"))
        self.projectsBtn.setToolTip(_translate("MainWindow", "Projects"))
        self.projectsBtn.setText(_translate("MainWindow", "Проекты"))
        self.tasksBtn.setToolTip(_translate("MainWindow", "Tasks"))
        self.tasksBtn.setText(_translate("MainWindow", "Задачи"))
        self.statisticsBtn.setToolTip(_translate("MainWindow", "Statistics"))
        self.statisticsBtn.setText(_translate("MainWindow", "Статистика"))
        self.calendarBtn.setToolTip(_translate("MainWindow", "Calendar"))
        self.calendarBtn.setText(_translate("MainWindow", "Календарь"))
        self.settingsBtn.setToolTip(_translate("MainWindow", "Settings"))
        self.settingsBtn.setText(_translate("MainWindow", "Настройки"))
        self.pushButton_5.setToolTip(_translate("MainWindow", "Search"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "Notification"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "Profile"))
        self.minimizeBtn.setToolTip(_translate("MainWindow", "Minimise Window"))
        self.restoreBtn.setToolTip(_translate("MainWindow", "Restore Window"))
        self.closeBtn.setToolTip(_translate("MainWindow", "Close Window"))
        self.label_3.setText(_translate("MainWindow", "Главное меню"))
        self.label_5.setText(_translate("MainWindow", "Проекты"))
        self.label_6.setText(_translate("MainWindow", "Задачи"))
        self.label_4.setText(_translate("MainWindow", "Статистика"))
        self.label_7.setText(_translate("MainWindow", "Календарь"))
        self.label.setText(_translate("MainWindow", "Пользователь"))
        self.pushButton_7.setToolTip(_translate("MainWindow", "Close User"))
        self.label_2.setText(_translate("MainWindow", "User"))
        self.popupNotificationSubContainer.setToolTip(_translate("MainWindow", "Notification Message"))
        self.label_9.setText(_translate("MainWindow", "Notification"))
        self.label_8.setText(_translate("MainWindow", "Notification Message"))
        self.pushButton_8.setToolTip(_translate("MainWindow", "Close Notification"))
        self.label_10.setText(_translate("MainWindow", "Copyright"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))