# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Windows_Principal1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl  # rajouté !!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets  # Attention Qwebview remplacé par webEngineView !!!
from PyQt5.QtCore import Qt
import socket
import os
import webbrowser
import back1_hyperion
import Back2_dns
import pdfkit  # pip3 install pdfkit , sudo apt-get install wkhtmltopdf
import subprocess
import shutil

import nmap3
import json
import dns_error_qrc
from colorama import init
from termcolor import colored       #pip3 install colorama termcolor
from tkinter import ttk             #sudo apt-get install python3-tk
from tkinter import *
import time
import validators                  #pip3 install validators
import dns.resolver                #sudo pip3 install dnspython
from tabulate import tabulate      #pip3 install tabulate
import matplotlib.image as mpimg   #pip3 install matplotlib
import networkx as nx              #pip3 install networkx
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
import folium                      #pip3 install folium
import dns.name
import dns.resolver
from ip2geotools.databases.noncommercial import DbIpCity #pip install ip2geotools

import pandas as pd #pip3 install panda


import Picture_Background

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 379)
        MainWindow.setFixedSize(744, 379)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(204, 0, 0);\n"
"\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 75  16pt \"Uroob\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 130, 731, 131))
        self.label.setStyleSheet("image: url(:/newPrefix/Hyperion_red.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(16, 0, 711, 341))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 30))
        self.menubar.setObjectName("menubar")
        self.menuRecovery = QtWidgets.QMenu(self.menubar)
        self.menuRecovery.setObjectName("menuRecovery")
        self.menuWeb_server = QtWidgets.QMenu(self.menubar)
        self.menuWeb_server .setObjectName("menuWeb_server ")
        self.menuMail_Server= QtWidgets.QMenu(self.menubar)
        self.menuMail_Server.setObjectName("menuMail_Server")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        self.menuVulnerability = QtWidgets.QMenu(self.menubar)
        self.menuVulnerability.setObjectName("menuVulnerability")
        self.menuFirewall = QtWidgets.QMenu(self.menubar)
        self.menuFirewall.setObjectName("menuFirewall")
        self.menuAdmin_Panel = QtWidgets.QMenu(self.menubar)
        self.menuAdmin_Panel.setObjectName("menuAdmin_Panel")
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionmenu1 = QtWidgets.QAction(MainWindow)
        self.actionmenu1.setObjectName("actionmenu1")
        self.menubar.addAction(self.menuRecovery.menuAction())
        self.menubar.addAction(self.menuMail_Server.menuAction())
        self.menubar.addAction(self.menuWeb_server.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuVulnerability.menuAction())
        self.menubar.addAction(self.menuFirewall.menuAction())
        self.menubar.addAction(self.menuAdmin_Panel.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionInfos_DNS = QtWidgets.QAction(MainWindow)
        self.actionInfos_DNS.setObjectName("actionInfos_DNS")
        self.actionDNS_Champs_MX = QtWidgets.QAction(MainWindow)
        self.actionDNS_Champs_MX.setObjectName("actionDNS_Champs_MX")
        self.actionHote_IP = QtWidgets.QAction(MainWindow)
        self.actionHote_IP.setObjectName("actionHote_IP")
        self.actionRoute_Tcp = QtWidgets.QAction(MainWindow)
        self.actionRoute_Tcp.setObjectName("actionRoute_Tcp")
        self.actiondeep = QtWidgets.QAction(MainWindow)
        self.actiondeep.setObjectName("actiondeep")
        self.actionerr_http = QtWidgets.QAction(MainWindow)
        self.actionerr_http.setObjectName("actionerr_http")
        self.actionExif = QtWidgets.QAction(MainWindow)
        self.actionExif.setObjectName("actionExif")
        self.actionInfos_SearchEngins = QtWidgets.QAction(MainWindow)
        self.actionInfos_SearchEngins.setObjectName("actionInfos_SearchEngins")
        self.actionScraping_email = QtWidgets.QAction(MainWindow)
        self.actionScraping_email.setObjectName("actionScraping_email")
        self.actionDiscovering_interesting = QtWidgets.QAction(MainWindow)
        self.actionDiscovering_interesting.setObjectName("actionDiscovering_interesting")
        self.actionmod_userdir = QtWidgets.QAction(MainWindow)
        self.actionmod_userdir.setObjectName("actionmod_userdir")
        self.actionDetecting_SMTP = QtWidgets.QAction(MainWindow)
        self.actionDetecting_SMTP.setObjectName("actionDetecting_SMTP ")
        self.actionEnumerating_SMTP = QtWidgets.QAction(MainWindow)
        self.actionEnumerating_SMTP.setObjectName("actionEnumerating_SMTP")
        self.actionIMAP = QtWidgets.QAction(MainWindow)
        self.actionIMAP.setObjectName("actionIMAP")
        self.actionPOP3 = QtWidgets.QAction(MainWindow)
        self.actionPOP3.setObjectName("actionPOP3")
        self.actionNTLM_SMTP = QtWidgets.QAction(MainWindow)
        self.actionNTLM_SMTP.setObjectName("actionNTLM_SMTP")
        self.actioncve_scanner = QtWidgets.QAction(MainWindow)
        self.actioncve_scanner.setObjectName("actioncve_scanner")
        self.actionXSS_scanner = QtWidgets.QAction(MainWindow)
        self.actionXSS_scanner.setObjectName("actionXSS_scanner")
        self.actionSQL_scanner = QtWidgets.QAction(MainWindow)
        self.actionSQL_scanner.setObjectName("actionSQL_scanner")
        self.actionweb_applications = QtWidgets.QAction(MainWindow)
        self.actionweb_applications.setObjectName("actionweb_applications")
        self.actionShellshock = QtWidgets.QAction(MainWindow)
        self.actionShellshock.setObjectName("actionShellshock")
        self.actioninsecure_crossdomain = QtWidgets.QAction(MainWindow)
        self.actioninsecure_crossdomain.setObjectName("actioninsecure_crossdomain")
        self.actionsourcecode_control = QtWidgets.QAction(MainWindow)
        self.actionsourcecode_control.setObjectName("actionsourcecode_control")
        self.actionInsecureCipherSSL = QtWidgets.QAction(MainWindow)
        self.actionInsecureCipherSSL.setObjectName("actionInsecureCipherSSL")
        self.actionCSRF = QtWidgets.QAction(MainWindow)
        self.actionCSRF.setObjectName("actionCSRF")
        self.actionRFI = QtWidgets.QAction(MainWindow)
        self.actionRFI.setObjectName("actionRFI")
        self.actionSSL_inject = QtWidgets.QAction(MainWindow)
        self.actionSSL_inject.setObjectName("actionSSL_inject")
        self.actionscan_DB = QtWidgets.QAction(MainWindow)
        self.actionscan_DB.setObjectName("actionscan_DB")
        self.actionempty_MYSQL = QtWidgets.QAction(MainWindow)
        self.actionempty_MYSQL.setObjectName("actionempty_MYSQL")
        self.actionlistall_MYSQL = QtWidgets.QAction(MainWindow)
        self.actionlistall_MYSQL.setObjectName("actionlistall_MYSQL")
        self.actioninfo_msssql = QtWidgets.QAction(MainWindow)
        self.actioninfo_msssql.setObjectName("actioninfo_msssql")
        self.actioninfo_mongodb = QtWidgets.QAction(MainWindow)
        self.actioninfo_mongodb.setObjectName("actioninfo_mongodb")
        self.actionDetecting_MongoDB = QtWidgets.QAction(MainWindow)
        self.actionDetecting_MongoDB.setObjectName("Detecting_MongoDB")
        self.actionList_CoucheDB = QtWidgets.QAction(MainWindow)
        self.actionList_CoucheDB.setObjectName("actionList_CoucheDB")
        self.actionstatic_CoucheDB = QtWidgets.QAction(MainWindow)
        self.actionstatic_CoucheDB.setObjectName("static_CoucheDB")
        self.actionWafw00f = QtWidgets.QAction(MainWindow)
        self.actionWafw00f.setObjectName("actionWafw00f")
        self.actionwaf_http = QtWidgets.QAction(MainWindow)
        self.actionwaf_http.setObjectName("actionwaf_http")
        self.actionwaf_detect = QtWidgets.QAction(MainWindow)
        self.actionwaf_detect.setObjectName("actionwaf_detect")
        self.actionwaf_fingerprint = QtWidgets.QAction(MainWindow)
        self.actionwaf_fingerprint.setObjectName("actionwaf_fingerprint")
        self.actionadmin_finder = QtWidgets.QAction(MainWindow)
        self.actionadmin_finder.setObjectName("actionadmin_finder")
        self.actionmenulogin = QtWidgets.QAction(MainWindow)
        self.actionmenulogin.setObjectName("actionmenulogin")
        self.actionLogin_php = QtWidgets.QAction(MainWindow)
        self.actionLogin_php.setObjectName("actionLogin_php")
        self.menubar.addAction(self.menuRecovery.menuAction())
        self.menuRecovery.addAction(self.actionInfos_DNS)
        self.menuRecovery.addAction(self.actionDNS_Champs_MX)
        self.menuRecovery.addAction(self.actionHote_IP)
        self.menubar.addAction(self.menuWeb_server.menuAction())
        self.menuWeb_server.addAction(self.actionRoute_Tcp)
        self.menuWeb_server.addAction(self.actiondeep)
        self.menuWeb_server.addAction(self.actionerr_http)
        self.menuWeb_server.addAction(self.actionExif)
        self.menuWeb_server.addAction(self.actionInfos_SearchEngins)
        self.menuWeb_server.addAction(self.actionScraping_email)
        self.menuWeb_server.addAction(self.actionDiscovering_interesting)
        self.menuWeb_server.addAction(self.actionmod_userdir)
        self.menuMail_Server.addAction(self.actionDetecting_SMTP)
        self.menuMail_Server.addAction(self.actionEnumerating_SMTP)
        self.menuMail_Server.addAction(self.actionIMAP)
        self.menuMail_Server.addAction(self.actionPOP3)
        self.menuMail_Server.addAction(self.actionNTLM_SMTP)
        self.menubar.addAction(self.menuMail_Server.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menuDatabase.addAction(self.actionscan_DB)
        self.menuDatabase.addAction(self.actionempty_MYSQL)
        self.menuDatabase.addAction(self.actionlistall_MYSQL)
        self.menuDatabase.addAction(self.actioninfo_msssql)
        self.menuDatabase.addAction(self.actioninfo_mongodb)
        self.menuDatabase.addAction(self.actionDetecting_MongoDB)
        self.menuDatabase.addAction(self.actionList_CoucheDB)
        self.menuDatabase.addAction(self.actionstatic_CoucheDB)
        self.menubar.addAction(self.menuVulnerability.menuAction())
        self.menuVulnerability.addAction(self.actioncve_scanner)
        self.menuVulnerability.addAction(self.actionXSS_scanner)
        self.menuVulnerability.addAction(self.actionSQL_scanner)
        self.menuVulnerability.addAction(self.actionweb_applications)
        self.menuVulnerability.addAction(self.actionShellshock)
        self.menuVulnerability.addAction(self.actioninsecure_crossdomain)
        self.menuVulnerability.addAction(self.actionsourcecode_control)
        self.menuVulnerability.addAction(self.actionInsecureCipherSSL)
        self.menuVulnerability.addAction(self.actionCSRF)
        self.menuVulnerability.addAction(self.actionRFI)
        self.menuVulnerability.addAction(self.actionSSL_inject)
        self.menubar.addAction(self.menuFirewall.menuAction())
        self.menuFirewall.addAction(self.actionWafw00f)
        self.menuFirewall.addAction(self.actionwaf_http)
        self.menuFirewall.addAction(self.actionwaf_detect)
        self.menuFirewall.addAction(self.actionwaf_fingerprint)
        self.menubar.addAction(self.menuAdmin_Panel.menuAction())
        self.menuAdmin_Panel.addAction(self.actionmenulogin)
        self.retranslateUi(MainWindow)
        self.menubar.addAction(self.menuQuit.menuAction())
        self.menuQuit.addAction(self.actionQuit)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Hyperion v3", "Hyperion v3"))
        self.label_2.setText(_translate("MainWindow", "Gif-Label"))
        self.gif = QMovie('red.gif')
        self.label_2.setMovie(self.gif)
        self.gif.start()
        self.menuRecovery.setTitle(_translate("MainWindow", "Recognition"))
        self.menuWeb_server.setTitle(_translate("MainWindow", "Web Server"))
        self.menuMail_Server.setTitle(_translate("MainWindow", "Mail Server"))
        self.menuDatabase.setTitle(_translate("MainWindow", "DataBase"))
        self.menuVulnerability.setTitle(_translate("MainWindow", "Vulnerability"))
        self.menuFirewall.setTitle(_translate("MainWindow", "Firewall"))
        self.menuAdmin_Panel.setTitle(_translate("MainWindow", "Admin Login"))
        self.menuQuit.setTitle(_translate("MainWindow", "Quit"))
        self.actionQuit.setText(_translate("MainWindow", "quitted"))
        self.actionmenu1.setText(_translate("MainWindow", "menu1"))
        self.actionInfos_DNS.setText(_translate("MainWindow", "Infos Whois"))
        self.actionDNS_Champs_MX.setText(_translate("MainWindow", "Infos Network "))
        self.actionHote_IP.setText(_translate("MainWindow", "Infos Geolocation"))
        self.actionRoute_Tcp.setText(_translate("MainWindow", "Scan ports Services "))
        self.actiondeep.setText(_translate("MainWindow", "Scan Deep ports Services "))
        self.actionerr_http.setText(_translate("MainWindow", "Error http page "))
        self.actionExif.setText(_translate("MainWindow", "Exif Datas picture "))
        self.actionInfos_SearchEngins.setText(_translate("MainWindow", "Listing supported HTTP methods"))
        self.actionScraping_email.setText(_translate("MainWindow", "Scraping email"))
        self.actionDiscovering_interesting.setText(_translate("MainWindow", "Discovering Interesting Files"))
        self.actionmod_userdir.setText(_translate("MainWindow", "Mod userdir enumerate accounts"))
        self.actionDetecting_SMTP.setText(_translate("MainWindow", "Detecting SMTP open relays"))
        self.actionEnumerating_SMTP.setText(_translate("MainWindow", "Enumerating SMTP usernames"))
        self.actionIMAP.setText(_translate("MainWindow", "Capability IMAP "))
        self.actionPOP3.setText(_translate("MainWindow", "Capability POP3"))
        self.actionNTLM_SMTP.setText(_translate("MainWindow", "SMTP NTLM authentication"))
        self.actionWafw00f.setText(_translate("MainWindow", "Wafw00f"))
        self.actionwaf_http.setText(_translate("MainWindow", "HTTP WAF"))
        self.actionwaf_detect.setText(_translate("MainWindow", "Detected WAF"))
        self.actionwaf_fingerprint.setText(_translate("MainWindow", "Fingerprint WAF"))
        self.actionscan_DB.setText(_translate("MainWindow", "Type DataBase"))
        self.actionempty_MYSQL.setText(_translate("MainWindow", "Empty password MySQL"))
        self.actionlistall_MYSQL.setText(_translate("MainWindow", "List all databases MySQL"))
        self.actioninfo_msssql.setText(_translate("MainWindow", "Info: ms-sql"))
        self.actioninfo_mongodb.setText(_translate("MainWindow", "Info: MongoDB"))
        self.actionDetecting_MongoDB.setText(_translate("MainWindow", "MongoDB Authentification"))
        self.actionList_CoucheDB.setText(_translate("MainWindow", "Info: CoucheDB"))
        self.actionstatic_CoucheDB.setText(_translate("MainWindow", "Static : CoucheDB"))
        self.actioncve_scanner.setText(_translate("MainWindow", "Infos CVE"))
        self.actionXSS_scanner.setText(_translate("MainWindow", "Infos XSS"))
        self.actionSQL_scanner.setText(_translate("MainWindow", "Infos SQL"))
        self.actionweb_applications.setText(_translate("MainWindow", "web_applications"))
        self.actionShellshock.setText(_translate("MainWindow", "Shellshock"))
        self.actioninsecure_crossdomain.setText(_translate("MainWindow", "insecure crossdomain"))
        self.actionsourcecode_control.setText(_translate("MainWindow", "sourcecode control"))
        self.actionInsecureCipherSSL.setText(_translate("MainWindow", "InsecureCipherSSL"))
        self.actionCSRF.setText(_translate("MainWindow", "Infos CSRF"))
        self.actionRFI.setText(_translate("MainWindow", "Infos RFI"))
        self.actionSSL_inject.setText(_translate("MainWindow", "SSL Injection"))
        self.actionmenulogin.setText(_translate("MainWindow", "Login_Page_Admin"))




class Ui_Dialog_dns(object):
    def setupUi(self, Dialog_dns):
        Dialog_dns.setObjectName("Dialog")
        Dialog_dns.resize(609, 161)
        Dialog_dns.setFixedSize(609, 161)
        Dialog_dns.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Dialog_dns)
        self.label.setGeometry(QtCore.QRect(0, -10, 601, 161))
        self.label.setStyleSheet("image: url(:/newPrefix/Backg2_dns.jpg);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_dns)
        self.lineEdit.setGeometry(QtCore.QRect(110, 90, 341, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog_dns)
        self.pushButton.setGeometry(QtCore.QRect(240, 130, 121, 25))
        self.pushButton.setStyleSheet("background-color: rgb(239, 41, 41);\n"
                                      "color: rgb(243, 243, 243);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog_dns)
        QtCore.QMetaObject.connectSlotsByName(Dialog_dns)

    def retranslateUi(self, Dialog_dns):
        _translate = QtCore.QCoreApplication.translate
        Dialog_dns.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "START"))



class Ui_Dialog_progress_bar(object):
    def setupUi_progress_bar(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(391, 98)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 30, 371, 23))
        self.progressBar.setStyleSheet("color: white;")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 60, 121, 31))
        self.label.setStyleSheet("font: 10pt \"Purisa\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 10, 91, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\">Loading ...</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#aa0000;\">Report HTML</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#ffffff;\">Hyperion v3</span></p></body></html>"))



class Ui_Dialog_error_dns(object):
    def setupUi_error_dns(self, Dialog_error_dns):
        Dialog_error_dns.setObjectName("Dialog")
        Dialog_error_dns.resize(326, 77)
        Dialog_error_dns.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Dialog_error_dns)
        self.label.setGeometry(QtCore.QRect(90, 0, 241, 81))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_error_dns)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 81, 81))
        self.label_2.setStyleSheet("image: url(:/newPrefix/DNS_Error.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog_error_dns)
        QtCore.QMetaObject.connectSlotsByName(Dialog_error_dns)

    def retranslateUi(self, Dialog_error_dns):
        _translate = QtCore.QCoreApplication.translate
        Dialog_error_dns.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">Error DNS : </span><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">N</span><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">o Found !</span></p></body></html>"))




class Ui_Dialog_report(object):  # dialog html GUI # whois report
    def setupUi(self, Dialog_report):
        Dialog_report.setObjectName("Dialog")
        Dialog_report.resize(757, 615)
        Dialog_report.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(Dialog_report)
        self.webEngineView.setGeometry(QtCore.QRect(-1, 0, 757, 615))
        self.webEngineView.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.webEngineView.setStyleSheet("width: 50%")
        current_dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(current_dir, "Whois4.html")
        url = QUrl.fromLocalFile(filename)
        self.webEngineView.setUrl(QtCore.QUrl(url))
        self.webEngineView.setObjectName("webEngineView")

        self.retranslateUi(Dialog_report)
        QtCore.QMetaObject.connectSlotsByName(Dialog_report)

    def retranslateUi(self, Dialog_report):
        _translate = QtCore.QCoreApplication.translate
        Dialog_report.setWindowTitle(_translate("Dialog", "Dialog"))


class Ui_Dialog_pdf(object):
    def setupUi(self, Dialog_pdf):
        Dialog_pdf.setObjectName("Dialog")
        Dialog_pdf.resize(447, 132)
        Dialog_pdf.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Dialog_pdf)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 51))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_pdf)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 141, 51))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_pdf)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 291, 28))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog_pdf)
        self.pushButton.setGeometry(QtCore.QRect(280, 100, 71, 21))
        self.pushButton.setStyleSheet("color: rgb(255, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_pdf)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 100, 71, 20))
        self.pushButton_2.setStyleSheet("color: rgb(170, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Dialog_pdf)
        QtCore.QMetaObject.connectSlotsByName(Dialog_pdf)

    def retranslateUi(self, Dialog_pdf):
        _translate = QtCore.QCoreApplication.translate
        Dialog_pdf.setWindowTitle(_translate("HyperionV3 PDF", "HyperionV3 PDF"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ff5500;\">HyperionV3 Automate Pentesting Informations HTML</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ff5500;\">Ouput Save Results HTML in PDF </span></p></body></html>"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#ff5500;\">Enter Name File PDF :</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Annuler"))
        self.pushButton_2.setText(_translate("Dialog", "Ok"))


class Ui_Dialog_report_champsMX(object):
    def setupUi(self, Dialog_report_champsMX):
        Dialog_report_champsMX.setObjectName("Hyperion network DNS")
        Dialog_report_champsMX.resize(1200, 500)
        Dialog_report_champsMX.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(Dialog_report_champsMX)
        self.webEngineView.setGeometry(QtCore.QRect(-1, 0, 1200, 500))
        self.webEngineView.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.webEngineView.setStyleSheet("width: 50%")
        current_dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(current_dir, "template.html")
        url = QUrl.fromLocalFile(filename)
        self.webEngineView.setUrl(QtCore.QUrl(url))
        self.webEngineView.setObjectName("webEngineView")

        self.retranslateUi(Dialog_report_champsMX)
        QtCore.QMetaObject.connectSlotsByName(Dialog_report_champsMX)

    def retranslateUi(self, Dialog_report_champsMX):
        _translate = QtCore.QCoreApplication.translate
        Dialog_report_champsMX.setWindowTitle(_translate("Hyperion network DNS", "Hyperion network DNS"))


class Controller:
    def __init__(self):
        pass

    def voir_Menu_general(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.ui.actionInfos_DNS.triggered.connect(self.voir_Menu_dns_whois)
        self.ui.actionDNS_Champs_MX.triggered.connect(self.voir_Menu_network_dns)
        self.ui.actionHote_IP.triggered.connect(self.voir_Menu_network_map)
        self.ui.actionerr_http.triggered.connect(self.voir_Menu_err_http)
        self.ui.actionExif.triggered.connect(self.voir_Menu_Exif)
        self.ui.actionRoute_Tcp.triggered.connect(self.voir_Menu_network_advanced)  ### ATTENTION
        self.ui.actiondeep.triggered.connect(self.voir_Menu_deepscan)
        self.ui.actionInfos_SearchEngins.triggered.connect(self.voir_Menu_network_Listing_supported_HTTP_methods)
        self.ui.actionScraping_email.triggered.connect(self.voir_Menu_networt_scrapping_email)

        self.ui.actionDiscovering_interesting.triggered.connect(self.voir_Menu_network_Discovering_interesting)
        self.ui.actionmod_userdir.triggered.connect(self.voir_Menu_network_mod_userdir)
        self.ui.actionDetecting_SMTP.triggered.connect(self.voir_Menu_network_Detecting_SMTP)
        self.ui.actionEnumerating_SMTP.triggered.connect(self.voir_Menu_network_Enum_SMTP)
        self.ui.actionIMAP.triggered.connect(self.voir_Menu_network_IMAP)
        self.ui.actionPOP3.triggered.connect(self.voir_Menu_network_POP3)
        self.ui.actionNTLM_SMTP.triggered.connect(self.voir_Menu_network_NTLM)

        self.ui.actioncve_scanner.triggered.connect(self.voir_Menu_Report_CVE_Scan)
        self.ui.actionXSS_scanner.triggered.connect(self.voir_Menu_Report_XSS_Scan_)
        self.ui.actionSQL_scanner.triggered.connect(self.voir_Menu_Report_SQL_Scan)

        self.ui.actionweb_applications.triggered.connect(self.voir_Menu_Report_web_applications_Scan)
        self.ui.actionShellshock.triggered.connect(self.voir_Menu_Report_Shellshock_Scan)
        self.ui.actioninsecure_crossdomain.triggered.connect(self.voir_Menu_Report_insecure_crossdomain)
        self.ui.actionsourcecode_control.triggered.connect(self.voir_Menu_Report_sourcecode_control_Scan)
        self.ui.actionInsecureCipherSSL.triggered.connect(self.voir_Menu_Report_InsecureCipherSSL)
        self.ui.actionCSRF.triggered.connect(self.voir_Menu_Report_CSRF)
        self.ui.actionRFI.triggered.connect(self.voir_Menu_Report_RFI)

        self.ui.actionSSL_inject.triggered.connect(self.voir_Menu_Report_SSL_Injection)

        self.ui.actionscan_DB.triggered.connect(self.voir_Menu_Type_DataBase)
        self.ui.actionempty_MYSQL.triggered.connect(self.voir_Menu_network_Empty_MYSQL)
        self.ui.actionlistall_MYSQL.triggered.connect(self.voir_Menu_network_listall_MYSQL)
        self.ui.actioninfo_msssql.triggered.connect(self.voir_Menu_network_infos_mssql)
        self.ui.actioninfo_mongodb.triggered.connect(self.voir_Menu_network_infos_mongodb)
        self.ui.actionDetecting_MongoDB.triggered.connect(self.voir_Menu_network_detecting_mongodb)
        self.ui.actionList_CoucheDB.triggered.connect(self.voir_Menu_network_List_CoucheDB)
        self.ui.actionstatic_CoucheDB.triggered.connect(self.voir_Menu_network_CoucheDB_static)
        self.ui.actionWafw00f.triggered.connect(self.voir_Menu_wafw00f)
        self.ui.actionwaf_http.triggered.connect(self.voir_Menu_http_waff)
        self.ui.actionwaf_detect.triggered.connect(self.voir_Menu_detect_waff)
        self.ui.actionwaf_fingerprint.triggered.connect(self.voir_Menu_fingerprint_waff)
        self.ui.actionmenulogin.triggered.connect(self.voir_Menu_Login_General)
        self.ui.actionQuit.triggered.connect(self.voir_menu_quit)
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog_progress_bar()
        self.ui.setupUi_progress_bar(self.Dialog)
        self.ui.progressBar.setProperty("value", 24)

    def progressbar(self):
        self.Dialog.show()


    def voir_menu_quit(self):
        #sys.exit(app.exec_())
        self.MainWindow.close()



    def voir_Menu_dns_whois(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()

        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS General"))
        self.Dialog_dns.show()

        self.ui.pushButton.clicked.connect(self.Report_DNS_General)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_network_dns(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Network"))
        self.Dialog_dns.show()
        # dns1 = self.ui.lineEdit.text()
        self.ui.pushButton.clicked.connect(self.Report_DNS_Network)

    def voir_Menu_network_map(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Geolocation"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_Geolocation)


    def voir_Menu_deepscan(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "Deep Ports Services Scanning"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_Deep_Scan)



    def voir_Menu_network_advanced(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Advanced"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_Advanced)

    def voir_Menu_err_http(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "Errors HTTP"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_err_http)


    def voir_Menu_Exif(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "Exif Datas Picture"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_Exif)

    def voir_Menu_network_Listing_supported_HTTP_methods(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "Listing_supported_HTTP_methods"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_Listing_supported_HTTP_methods)

    def voir_Menu_networt_scrapping_email(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS scrapping_email"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_Scraping_Email)

    def voir_Menu_network_SMB(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS SMB"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_SMB)

    def voir_Menu_network_Discovering_interesting(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Discovering_interesting"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_Discovering_interesting)

    def voir_Menu_network_mod_userdir(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Mod Userdir Enumerate Account"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_mod_userdir)

    def voir_Menu_network_Detecting_SMTP(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Detecting SMTP open relays "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_Detecting_SMTP)

    def voir_Menu_network_Enum_SMTP(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Enumerating SMTP username"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_Enumeration_SMTP)

    def voir_Menu_network_IMAP(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Capability IMAP"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_IMAP)

    def voir_Menu_network_POP3(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Capability POP3"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_POP3)

    def voir_Menu_network_NTLM(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS SMTP NTLM authentification"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_NTLM)

    def voir_Menu_network_the_harvester(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS The Harvester"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_NTLM)

    def voir_Menu_Report_CVE_Scan(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        self.Dialog_dns.show()
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS CVE Scan"))
        self.ui.pushButton.clicked.connect(self.Report_CVE_Scan)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_XSS_Scan_(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS XSS Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_XSS_Scan)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_SQL_Scan(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS SQL Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_SQL_Scan)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_DDOS_Scan(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS DDOS Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DDOS)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_web_applications_Scan(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Web Application Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_web_applications_Scan)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_Shellshock_Scan(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Shellshock Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_Shellshock_Scan)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_insecure_crossdomain_Scan(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Insecure CrossDomain Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_insecure_crossdomain_Scan)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_sourcecode_control_Scan(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "  DNS Source Code Control Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_sourcecode_control_Scan)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_insecure_crossdomain(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Insecure CrossDomain Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_insecure_crossdomain_Scan)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_InsecureCipherSSL(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Insecure SSL Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_InsecureCipherSSL)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_CSRF(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS CSRF Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_CSRF)


    def voir_Menu_Report_RFI(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS RFI Scan"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_RFI)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_SMB_vulnerabilitie(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS SMB_vulnerabilitie"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_SMB_vulnerabilitie)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_SSL_Injection(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS SSL Injection"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_SSL_Injection)
        # self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Report_Nikto(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Report Nikto"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_Nikto)

    def voir_Menu_Type_DataBase(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Type DataBase "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.voir_report_DataBase)

    def voir_Menu_network_Empty_MYSQL(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Empty Password MYSQL "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_Empty_MYSQL)

    def voir_Menu_network_listall_MYSQL(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Listall Database MYSQL "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_listall_MYSQL)

    def voir_Menu_network_infos_mssql(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Info ms-sql "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_info_mssql)

    def voir_Menu_network_infos_mongodb(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Info MongodDB "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_info_mongodb)

    def voir_Menu_network_detecting_mongodb(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Detecting ms-sql "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_detecting_mongodb)

    def voir_Menu_network_List_CoucheDB(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS List CoucheDB "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_List_CoucheDB)

    def voir_Menu_network_CoucheDB_static(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", " DNS Static CoucheDB "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_CoucheDB_static)



    def voir_Menu_TheHarvester(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "TheHarvester "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_DNS_CoucheDB_static)

    def voir_Menu_wafw00f(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "wafw00f "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_wafw00f)

    def voir_Menu_http_waff(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS HTTP WAF "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_HTTP_WAF)

    def voir_Menu_detect_waff(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS Detected WAF"))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_Detect_WAF)

    def voir_Menu_fingerprint_waff(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "DNS fingerprint  WAF "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_Fingerprint_WAF)


    def voir_Menu_Admin_Finder(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "Admin Login "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_Admin_general)

    def voir_Menu_Login_General(self, Dialog_dns):
        self.Dialog_dns = QtWidgets.QDialog()
        self.ui = Ui_Dialog_dns()
        self.ui.setupUi(self.Dialog_dns)
        _translate = QtCore.QCoreApplication.translate
        self.Dialog_dns.setWindowTitle(_translate("Dialog", "Admin Login "))
        self.Dialog_dns.show()
        self.ui.pushButton.clicked.connect(self.Report_found_Admin)  ### placé la liste admin_finder dans le script



    def menu_pdf_annuler(self, Dialog_pdf):
        self.Dialog_pdf.close()

    def menu_pdf_ok(self, Dialog_pdf):
        name_pdf = self.ui.lineEdit.text()

        print(colored("[*] Building File output save PDF ...", "green"))
        pdfkit.from_file('template.html', name_pdf)
        shutil.move(name_pdf, 'PDF')
        print((colored("[*]|---> Output [save] Format PDF :", "green")), name_pdf)
        self.Dialog_pdf.close()
        self.Dialog_report_champsMX.close()


    def Report_DNS_General(self, Dialog_pdf):
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Starting Report_DNS_General :", "green"))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            pass
        import os
        print(colored("[Welcome on the report General Informations] ", 'magenta'))

        dns = self.ui.lineEdit.text()
        import validators
        verifdns = (validators.domain(dns))

        if verifdns == True:
            self.Dialog = QtWidgets.QDialog()

            self.Dialog_dns.close()
            self.MainWindow.close()

            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)

            import socket
            import os
            import html
            import whois

            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            # Create text widget and specify size.
            T = Text(mGui, height=5, width=52)
            # Create label
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()

            mpb["value"] = 10
            mpb.update()

            f = open('template.html', 'wb')

            print((colored("|--> Starting Analyse General Informations DNS :", 'green')), dns)
            print(colored("|-->  ... [Loading] ... ", 'green'))
            print(colored("|--> Scanning Network ... ", 'green'))
            print((colored("|--> DNS :", "green")), dns)

            ip = (socket.gethostbyname(dns))

            import whois

            w = whois.whois(dns)

            domain = (w.domain_name)
            regis = (w.registar)
            whois = (w.whois_server)
            referral = (w.referral_url)
            update = (w.updated_date)
            creation = (w.creation_date)
            expiration = (w.expiration_date)
            name = (w.name_servers)
            sta = (w.status)
            emails = (w.emails)
            dnssec = (w.dnssec)
            name = (w.name)
            org = (w.org)
            adress = (w.adress)
            city = (w.city)
            state = (w.state)
            zipcode = (w.zipcode)
            country = (w.country)
            import os
            import json
            import requests
            r = requests.get('http://nmap.org')
            data1 = r.headers
            versions_srerver = (data1["server"])
            server = (versions_srerver)
            mpb["value"] = 50
            mpb.update()
            message = """<html>
                            <head></head>
                            <body style="background-image: url(border_fait.jpeg);background-repeat: no-repeat;">
                            <body marginwidth="50" marginheight="100" topmargin="10" leftmargin="170">
                            <center>                        
                            <img style="border:10px solid black;" src="Hyperion_red2.jpg">
                            </center>
                            <center>
                            <p style="color: black;font-size:30px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span style="text-decoration: underline;"><B>Report DNS Analyse General</B><p>
                            </center>
                            <p style="color: black;font-size:20px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span><B>Informations General on the DNS :</B><p>
                            <body><p><span style="color: red"><B>DNS Ip Adress : </span><span class="macouleur2">{IP}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS target : </span><span class="macouleur2">{TARGET}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS registar : </span><span class="macouleur2">{REGISTRAR}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS Whois_Server : </span><span class="macouleur3">{WHOIS_SERVER}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS referral_url : </span><span class="macouleur3">{REFERRAL_URL}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS last_updated : </span><span class="macouleur3">{LAST_UPDATED}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS Creation_date : </span><span class="macouleur3">{CREATION}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS expiration_date : </span><span class="macouleur3">{EXPIRATION}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS Name_Servers : </span><span class="macouleur3">{NAME_SERVERS}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS status : </span><span class="macouleur3">{STATUS}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS Emails : </span><span class="macouleur3">{EMAILS}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS_secondary : </span><span class="macouleur3">{DNSSEC}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS Name : </span><span class="macouleur3">{NAME}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS Organisation : </span><span class="macouleur3">{ORGANISATION}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS Adress : </span><span class="macouleur3">{ADRESS}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS City : </span><span class="macouleur3">{CITY}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS State : </span><span class="macouleur3">{STATE}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS Zip_Code : </span><span class="macouleur3">{ZIPCODE}</B></span></p></body>
                            <body><p><span style="color: red"><B>DNS Country : </span><span class="macouleur3">{COUNTRY}</B></span></p></body>
                            <p style="color: black;font-size:20px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span><B> Informations Server Secondary : </B><p>
                            <body><p><span style="color: red"><B> DNS Versions Server : </B></span><span class="macouleur3">{SERVER}</span></p></body
                            </html>""".format(
                IP=ip,
                TARGET=domain,
                REGISTRAR=regis,
                WHOIS_SERVER=whois,
                REFERRAL_URL=referral,
                LAST_UPDATED=update,
                CREATION=creation,
                EXPIRATION=expiration,
                NAME_SERVERS=name,
                STATUS=state,
                EMAILS=emails,
                DNSSEC=dnssec,
                NAME=name,
                ORGANISATION=org,
                ADRESS=adress,
                CITY=city,
                STATE=state,
                ZIPCODE=zipcode,
                COUNTRY=country,
                SERVER=server,

            )

            bytes = message.encode(encoding='UTF-8')
            f.write(bytes)
            f.close()
            print(colored("[*] Scanning and report [General Informations] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            # self.Dialog_report.show()
            self.MainWindow.show()
            mpb["value"] = 100
            mpb.update()
            mGui.destroy()
            self.Dialog_report_champsMX.show()

            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)

            self.Dialog_pdf.show()

            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé

            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))


        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()



    def Report_DNS_Network(self):
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Starting Report_DNS_Network ", "green"))
            print(colored(" [*] <> Building Template HTML ...", "green"))

            pass

        self.Dialog_dns.close()
        dns1 = self.ui.lineEdit.text()

        import validators
        verifdns = (validators.domain(dns1))
        if verifdns == True:
            print(colored("[Welcome on the report Network Informations] ", 'magenta'))
            print((colored("|--> Starting Analyse Network DNS :", 'green')), dns1)
            print(colored("|-->  ... [Loading] ... ", 'green'))
            print(colored("|--> Scanning Network ... ", 'green'))
            print((colored("|--> DNS :", "green")), dns1)
            self.Dialog = QtWidgets.QDialog()

            self.Dialog_dns.close()
            self.MainWindow.close()

            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            import dns.resolver  # sudo pip3 install dnspython
            from tabulate import tabulate
            import matplotlib.image as mpimg
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            # Create text widget and specify size.
            T = Text(mGui, height=5, width=52)
            # Create label
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()

            mpb["value"] = 10
            mpb.update()
            img = mpimg.imread('index.jpeg')

            msg_menu = "Welcome on the report Servers_DNS_Menu Informations :"

            f = open('template.html', 'wb')
            message1 = """<html>
                              <head></head>
                              <body style="background-image: url(border_fait.jpeg);background-repeat: no-repeat;">
                              <body marginwidth="50" marginheight="100" topmargin="10" leftmargin="170">
                              <center>                        
                              <img style="border:10px solid black;" src="Hyperion_red2.jpg">
                              </center>
                              <center>
                              <p style="color: black;font-size:30px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span style="text-decoration: underline;"><B> Menu Infos Network : Champs MX ,A , AAAA ,PTR ,SVR </B><p>
                              </center>
                              <center>
                              <body><p><span style="color: red"><B>DNS target : </B></span><span class="macouleur2"><B>{TARGET}</B></span></p></body>
                              </center>
                              <center>
                              </html>""".format(
                TARGET=dns1,
            )
            bytes = message1.encode(encoding='UTF-8')
            f.write(bytes)

            n = dns.name.from_text(dns1)
            mpb["value"] = 20
            mpb.update()
            LTS_A = []
            try:
                for x in dns.resolver.resolve(dns1, 'A'):
                    A = ([LTS_A.append(x.to_text())])
                    tableau_A = (tabulate([[a] for a in LTS_A], tablefmt='html'))
                    import networkx as nx
                    import matplotlib.pyplot as plt
                    import matplotlib as mpl
                    import pylab

                    mpl.rcParams['toolbar'] = 'None'  # Tools bar interactive off
                    G = nx.Graph()

                    plt.figure(figsize=plt.figaspect(0.5), facecolor=("#00000F"))  # taille de la fenetre

                    # ---------- parti nodes ----------------------

                    for item in LTS_A:  # lists des points (nodes) avec la lists MX
                        G.add_node(item)

                        pass

                    # ------------- Edges connexions----------------------------

                    for item in LTS_A:  # lists des connexion (edges) avec le pont 0 pour le dns (pount central)
                        G.add_edge(dns1, item)  # le point 0 sera le dns

                    # ----------------------------------------------------------

                    pos = nx.spring_layout(G)  # positions for all nodes

                    # ------------------ Text sur MX ---- nodes ----------------------
                    for item in LTS_A:
                        x, y = pos[item]
                        plt.text(x, y + 0.1, s=item, color='white', bbox=dict(facecolor='green', alpha=0.5),
                                 horizontalalignment='center')  # label text informations sur nodes list

                    # ------------------- text sur dns -- node ------------------------
                    x, y = pos[dns1]
                    plt.text(x, y + 0.1, s=dns1, color='white', bbox=dict(facecolor='red', alpha=0.5),
                             horizontalalignment='center')  # label text informations sur nodes DNS
                    # -----------------------------------------------------------------------------------

                    nx.draw_networkx_nodes(G, pos, node=dns1, node_size=120, node_shape='d', node_color='red')
                    nx.draw_networkx_nodes(G, pos, nodelist=LTS_A, node_size=150, node_color='green', node_shape='d')

                    nx.draw_networkx_edges(G, pos, edge_color='white')
                    limits = plt.axis('off')  # RETIRÉ LE CADRE lIMIT
                    plt.savefig('grah_A.jpg')
                message_A = """<html>
                                   <head></head>
                                   <center>
                                   <p style="color: black;font-size:20px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span style="text-decoration: underline;"><B>Mapping Network : Servers Datas ipv4 (A)  </B><p>
                                   </center>
                                   <center>
                                   <img src="grah_A.jpg">
                                   </center>
                                   <body><p><span style="color: red"><B>DNS A  </B></span><span class="macouleur2"><B>{SA}</B></span></p></body>
                                   </html>""".format(
                    SA=tableau_A,
                )

                bytes_A = message_A.encode(encoding='UTF-8')
                f.write(bytes_A)


            except dns.resolver.NoAnswer:
                print(' No answer A ')
                no_RE_A = ("Aucun enregistrement A(ipv4) :" + dns1)
                message_No_A = """<html>
                                  <head></head>
                                  <body><p><span class="macouleur2"><B>{NO_RE_A}</B></span></p></body>
                                  </html>""".format(
                    NO_RE_A=no_RE_A,
                )

                bytes_No_A = message_No_A.encode(encoding='UTF-8')
                f.write(bytes_No_A)
                pass
            mpb["value"] = 50
            mpb.update()
            LTS_AAAA = []
            try:
                for x in dns.resolver.resolve(dns1, 'AAAA'):
                    AAAA = ([LTS_AAAA.append(x.to_text())])
                    tableau_AAAA = (tabulate([[aaaa] for aaaa in LTS_AAAA], tablefmt='html'))
                    import networkx as nx
                    import matplotlib.pyplot as plt
                    import matplotlib as mpl
                    import pylab

                    mpl.rcParams['toolbar'] = 'None'  # Tools bar interactive off
                    G = nx.Graph()

                    plt.figure(figsize=plt.figaspect(0.4), facecolor=("#00000F"))  # taille de la fenetre

                    # ---------- parti nodes ----------------------

                    for item in LTS_AAAA:  # lists des points (nodes) avec la lists MX
                        G.add_node(item)

                        pass

                    # ------------- Edges connexions----------------------------

                    for item in LTS_AAAA:  # lists des connexion (edges) avec le pont 0 pour le dns (pount central)
                        G.add_edge(dns1, item)  # le point 0 sera le dns

                    # ----------------------------------------------------------

                    pos = nx.spring_layout(G)  # positions for all nodes

                    # ------------------ Text sur MX ---- nodes ----------------------
                    for item in LTS_AAAA:
                        x, y = pos[item]
                        plt.text(x, y + 0.1, s=item, color='white', bbox=dict(facecolor='green', alpha=0.5),
                                 horizontalalignment='center')  # label text informations sur nodes list

                    # ------------------- text sur dns -- node ------------------------
                    x, y = pos[dns1]
                    plt.text(x, y + 0.1, s=dns1, color='white', bbox=dict(facecolor='red', alpha=0.5),
                             horizontalalignment='center')  # label text informations sur nodes DNS
                    # -----------------------------------------------------------------------------------

                    nx.draw_networkx_nodes(G, pos, node=dns1, node_size=120, node_shape='d', node_color='red')
                    nx.draw_networkx_nodes(G, pos, nodelist=LTS_AAAA, node_size=150, node_color='green', node_shape='d')

                    nx.draw_networkx_edges(G, pos, edge_color='white')
                    limits = plt.axis('off')  # RETIRÉ LE CADRE lIMIT
                    plt.savefig('grah_AAAA.jpg')
                message_AAAA = """<html>
                                      <head></head>
                                      <center>
                                      <p style="color: black;font-size:20px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span style="text-decoration: underline;"><B>Mapping Network : Servers Datas ipv6 (AAAA)  </B><p>
                                      </center>
                                      <center>
                                      <img src="grah_AAAA.jpg">
                                      </center>
                                      <body><p><span style="color: red"><B>DNS AAAA  </B></span><span class="macouleur2"><B>{AAAA}</B></span></p></body>
                                      </html>""".format(
                    AAAA=tableau_AAAA,
                )

                bytes_A = message_AAAA.encode(encoding='UTF-8')
                f.write(bytes_A)

            except dns.resolver.NoAnswer:
                print('|-----> [*] No answer AAAA ')
                no_RE_AAAA = ("Aucun enregistrement AAAA : " + dns1)
                message_No_AAAA = """<html>
                                      <head></head>
                                      <body><p><span class="macouleur2"><B>{NO_RE_AAAA}</B></span></p></body>
                                      </html>""".format(
                    NO_RE_AAAA=no_RE_AAAA,
                )

                bytes_No_AAAA = message_No_AAAA.encode(encoding='UTF-8')
                f.write(bytes_No_AAAA)
                pass
            mpb["value"] = 75
            mpb.update()
            LTS_mx = []
            try:
                for x in dns.resolver.resolve(dns1, 'MX'):
                    MX = ([LTS_mx.append(x.to_text())])  # ok
                    tableau_mx = (tabulate([[m] for m in LTS_mx], tablefmt='html'))

                    import networkx as nx
                    import matplotlib.pyplot as plt
                    import matplotlib as mpl
                    import pylab

                    mpl.rcParams['toolbar'] = 'None'  # Tools bar interactive off
                    G = nx.Graph()

                    plt.figure(figsize=plt.figaspect(0.5), facecolor=("#00000F"))  # taille de la fenetre

                    # ---------- parti nodes ----------------------

                    for item in LTS_mx:  # lists des points (nodes) avec la lists MX
                        G.add_node(item)

                        pass
                    # ------------- Edges connexions----------------------------

                    for item in LTS_mx:  # lists des connexion (edges) avec le pont 0 pour le dns (pount central)
                        G.add_edge(dns1, item)  # le point 0 sera le dns

                    # ----------------------------------------------------------

                    pos = nx.spring_layout(G)  # positions for all nodes

                    # ------------------ Text sur MX ---- nodes ----------------------
                    for item in LTS_mx:
                        x, y = pos[item]
                        plt.text(x, y + 0.1, s=item, color='white', bbox=dict(facecolor='green', alpha=0.5),
                                 horizontalalignment='center')  # label text informations sur nodes list

                    # ------------------- text sur dns -- node ------------------------
                    x, y = pos[dns1]
                    plt.text(x, y + 0.1, s=dns1, color='white', bbox=dict(facecolor='red', alpha=0.5),
                             horizontalalignment='center')  # label text informations sur nodes DNS
                    # -----------------------------------------------------------------------------------

                    nx.draw_networkx_nodes(G, pos, node=dns1, node_size=120, node_shape='d', node_color='red')
                    nx.draw_networkx_nodes(G, pos, nodelist=LTS_mx, node_size=150, node_color='green', node_shape='d')

                    nx.draw_networkx_edges(G, pos, edge_color='white')
                    limits = plt.axis('off')  # RETIRÉ LE CADRE lIMIT
                    plt.savefig('grah_MX.jpg')

                    # print(LTS_mx)

                message_MX = """<html>
                                    <head></head>
                                    <center>
                                    <p style="color: black;font-size:20px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span style="text-decoration: underline;"><B>Mapping Network : Servers Datas Email (MX)  </B><p>
                                    </center>
                                    <center>
                                    <img src="grah_MX.jpg">
                                    </center>
                                    <body><p><span style="color: red"><B>DNS MX  </B></span><span class="macouleur2"><B>{MX}</B></span></p></body>
                                    </html>""".format(MX=tableau_mx,

                                                      )

                bytes_MX = message_MX.encode(encoding='UTF-8')
                f.write(bytes_MX)

            except dns.resolver.NoAnswer:
                print('|-----> [*] No answer MX ')
                no_RE_MX = ("Aucun enregistrement MX : " + dns1)
                message_No_MX = """<html>
                                              <head></head>
                                              <body><p><span class="macouleur2"><B>{NO_RE_MX}</B></span></p></body>
                                              </html>""".format(
                    NO_RE_MX=no_RE_MX,
                )

                bytes_No_MX = message_No_MX.encode(encoding='UTF-8')
                f.write(bytes_No_MX)
                pass

            import pandas as pd
            import nmap3
            import json
            mpb["value"] = 80
            mpb.update()
            nmap = nmap3.Nmap()
            results = nmap.nmap_dns_brute_script(dns1)
            # print(results)
            mpb["value"] = 85
            mpb.update()
            dump_results = json.dumps(results)
            subdomain = json.loads(dump_results)
            subdomains_list = []
            for item in subdomain:
                SU = (item["hostname"])
                subdomains_list.append(SU)
                pass

            subadress_list = []
            for item in subdomain:
                SU = (item["address"])
                subadress_list.append(SU)
                pass
            df = pd.DataFrame({'hostname': subdomains_list, 'adress': subadress_list})
            # df.set_index('',inplace=True) #retiré la colonnes des chiffres

            html = df.to_html().replace('<th>', '<th style = "color: red">')
            mpb["value"] = 90
            mpb.update()
            from tabulate import tabulate

            import networkx as nx
            import matplotlib.pyplot as plt
            import matplotlib as mpl
            import pylab
            mpl.rcParams['toolbar'] = 'None'  # Tools bar interactive off
            G = nx.Graph()

            plt.figure(figsize=plt.figaspect(0.5), facecolor=("#00000F"))  # taille de la fenetre
            # ---------- parti nodes ----------------------
            for item in subdomains_list:  # lists des points (nodes) avec la lists MX
                G.add_node(item)
                pass
                # ------------- Edges connexions----------------------------

            for item in subdomains_list:  # lists des connexion (edges) avec le pont 0 pour le dns (pount central)
                G.add_edge(dns1, item)  # le point 0 sera le dns

                # ----------------------------------------------------------

            pos = nx.spring_layout(G)  # positions for all nodes

            # ------------------ Text sur list subdomains ---- nodes ----------------------
            for item in subdomains_list:
                x, y = pos[item]
                plt.text(x, y + 0.1, s=item, color='white', bbox=dict(facecolor='green', alpha=0.5),
                         horizontalalignment='center')  # label text informations sur nodes list

                # ------------------- text sur dns -- node ------------------------
                x, y = pos[dns1]
                plt.text(x, y + 0.1, s=dns1, color='white', bbox=dict(facecolor='red', alpha=0.5),
                         horizontalalignment='center')  # label text informations sur nodes DNS
                # -----------------------------------------------------------------------------------

                nx.draw_networkx_nodes(G, pos, node=dns1, node_size=120, node_shape='d', node_color='red')
                nx.draw_networkx_nodes(G, pos, nodelist=subdomains_list, node_size=150, node_color='green',
                                       node_shape='d')

                nx.draw_networkx_edges(G, pos, edge_color='white')
                limits = plt.axis('off')  # RETIRÉ LE CADRE lIMIT
                # plt.show()
                plt.savefig('grah_subdomain.jpg')
            message_sub = """<html>
                                <head></head>
                                <center>
                                <p style="color: black;font-size:20px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span style="text-decoration: underline;"><B>Mapping Network : Servers Datas Subdomains  </B><p>
                                </center>
                                <center>
                                <img src="grah_subdomain.jpg">
                                </center>
                                <body><p><span style="color: red"><B>DNS subdomain  </B></span><span class="macouleur2"><B>{List_subdomains}</B></span></p></body>
                                </html>""".format(List_subdomains=html,
                                                  )

            bytes_sub = message_sub.encode(encoding='UTF-8')
            f.write(bytes_sub)
            mpb["value"] = 100
            mpb.update()
            mGui.destroy()
            self.Dialog_report_champsMX.show()
            self.MainWindow.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()

            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  # ok
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))
            print(colored("[*] Scanning and report [Network] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns1)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()


    def Report_DNS_Geolocation(self):
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("Building Template Report ...", "green"))
            pass

        # self.Dialog_dns.close()
        dns1 = self.ui.lineEdit.text()

        import validators
        verifdns = (validators.domain(dns1))
        if verifdns == True:
            print(colored("[Welcome on the report Geolocation Informations] ", 'magenta'))
            print(colored('|---> [Menu Infos Geolocation : IPs / Location MAP World ] :', "green"))
            print(colored("|---> Starting Report_DNS_Geolocation : ", "green"))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse Network DNS :", 'green')), dns1)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_dns.close()
            self.MainWindow.close()
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)

            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 10
            mpb.update()
            import folium
            import dns.name
            import dns.resolver
            from ip2geotools.databases.noncommercial import DbIpCity
            import socket
            import pandas as pd

            # dns1 = ('nmap.org')
            n = dns.name.from_text(dns1)
            f = open('template.html', 'wb')

            addr1 = socket.gethostbyname(dns1)
            List_city1 = []
            List_region1 = []
            List_country1 = []
            List_lat1 = []
            List_lon1 = []
            datas_dns1 = DbIpCity.get(addr1, api_key='free')
            List_city1.append(datas_dns1.city)
            List_region1.append(datas_dns1.region)
            List_country1.append(datas_dns1.country)
            List_lat1.append(datas_dns1.latitude)
            List_lon1.append(datas_dns1.longitude)
            df1 = pd.DataFrame({'Server DNS': dns1, "Address IP  ": addr1, 'city': List_city1, 'region': List_region1,
                                '   country': List_country1, 'latitude': List_lat1, 'longitude': List_lon1})
            df1.set_index('Server DNS', inplace=True)
            html1 = df1.to_html().replace('<th>', '<th style = "color: black">').replace('<td>',
                                                                                         '<td style = "color: green">')

            locations1 = df1[['latitude', 'longitude']]
            locationlist1 = locations1.values.tolist()
            max1 = len(locationlist1)
            c = folium.Map(location=[46.078025, 6.409053], zoom_start=2, tiles='Stamen Toner')
            c2 = folium.Map(location=[46.078025, 6.409053], zoom_start=2, tiles='Stamen Toner')
            popup_dns1 = """<html>
                                <head></head>
                                <body><p><span style="color: red">*DNS* : </span><span class="macouleur2">{TARGET}</span></p></body>
                                </html>""".format(
                TARGET=datas_dns1,
            )

            for item in locationlist1:
                folium.Marker(location=item, popup=popup_dns1,
                              tooltip='<p style="color:#FF0000";>* Informations Servers * click <p>',
                              icon=folium.features.CustomIcon('dns.png', icon_size=(30, 30))).add_to(c)
                pass

            # legend vue terrain
            folium.TileLayer('Stamen Terrain').add_to(c)
            folium.TileLayer('Stamen Toner').add_to(c)
            folium.TileLayer('Stamen Water Color').add_to(c)
            folium.TileLayer('cartodbpositron').add_to(c)
            folium.TileLayer('cartodbdark_matter').add_to(c)
            folium.LayerControl().add_to(c)
            c.save('maCarte_GPStest.html')

            message1 = """<html>
                          <head></head>
                          <body style="background-image: url(border_fait.jpeg);background-repeat: no-repeat;">
                          <body marginwidth="50" marginheight="0" topmargin="10" leftmargin="170">
                          <center>                        
                          <img style="border:10px solid black;" src="Hyperion_red2.jpg">
                          </center>
                          <center>
                          <p style="color: black;font-size:30px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span style="text-decoration: underline;"><B>Informations Geolocations Mapping Servers</B><p>
                          <center>
                          <body><p><span style="color: black"><B>DNS Target : </span><span style="color: green" class="macouleur2">{TARGET}</B></span></p></body>
                          <center>
                          <p style="color: black;font-size:30px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span style="text-decoration: underline;"><B>Informations Geolocations Mapping Type Servers IPv4 DNS</B><p>
                          <iframe src=maCarte_GPStest.html width=1200 height=450></iframe>
                          <center>
                          <center>
                          <img src="dns.png" width=50 height=50 />
                          </center>
                          <body><p><span class="macouleur2">{geoloc_servers}</span></p></body>
                          <center>
                          </html>""".format(

                TARGET=dns1,
                geoloc_servers=html1,
            )

            bytes = message1.encode(encoding='UTF-8')
            f.write(bytes)



            List_NS = []

            try:
                while True:
                    try:
                        answer = dns.resolver.resolve(n, 'NS')
                    except dns.resolver.NoAnswer:
                        print(" [!] No NS record found for" + n.to_text() + ",attempt with parent ...")
                        no_NS = ("No NS server record with parent: " + dns1)
                        message_No_NS = """<html>
                                           <head></head>
                                           <body><p><span class="macouleur2"><B>{No_NS}</B></span></p></body>
                                           </html>""".format(
                            No_NS=no_NS,
                        )

                        bytes_No_NS = message_No_NS.encode(encoding='UTF-8')
                        f.write(bytes_No_NS)
                        pass

                    else:
                        print(colored("[*] NS record found for the domain ", 'green') + n.to_text())
                        for rdata in answer:
                            List_NS.append(rdata.to_text())
                        break;
                    n = n.parent()
            except dns.name.NoParent:
                print(colored("[!] No NS server found with parent *", 'red'))
                no_NS = ("No NS server record: " + dns1)
                message_No_NS = """<html>
                                       <head></head>
                                       <body><p><span class="macouleur2"><B>{No_NS}</B></span></p></body>
                                       </html>""".format(
                    No_NS=no_NS,
                )

                bytes_No_NS = message_No_NS.encode(encoding='UTF-8')
                f.write(bytes_No_NS)
                pass

            list_ip = []
            for item in List_NS:
                addr = socket.gethostbyname(item)
                list_ip.append(addr)
                pass

            List_city = []
            List_region = []
            List_country = []
            List_lat = []
            List_lon = []
            for item in list_ip:
                response = DbIpCity.get(item, api_key='free')
                List_city.append(response.city)
                List_region.append(response.region)
                List_country.append(response.country)
                List_lat.append(response.latitude)
                List_lon.append(response.longitude)
                pass
            df2 = pd.DataFrame(
                {'Servers DNS': List_NS, "Address IP  ": list_ip, 'city': List_city, 'region': List_region,
                 '   country': List_country, 'latitude': List_lat, 'longitude': List_lon})
            df2.set_index('Servers DNS', inplace=True)
            html2 = df2.to_html(justify="center").replace('<th>', '<th style = "color: black">').replace('<td>',
                                                                                                         '<td style = "color: green">')
            locations2 = df2[['latitude', 'longitude']]
            locationlist2 = locations2.values.tolist()
            max = len(locationlist2)  # compté les points associé au coordonnées > gps = 4

            # ---------------------------------- DNS 1 + dns(2) Multiple ------------------------------------------
            popup_dns2 = """<html>
                                <head></head>
                                <body><p><span style="color: red">*DNS* : </span><span class="macouleur2">{TARGET}</span></p></body>
                                </html>""".format(
                TARGET=List_NS,
            )

            for item in locationlist2:
                folium.Marker(location=item, popup=popup_dns2,
                              tooltip='<p style="color:#FF0000";>* Informations Servers * click <p>',
                              icon=folium.features.CustomIcon('dns2.png', icon_size=(30, 30))).add_to(c2)
                pass

            # legend vue terrain
            folium.TileLayer('Stamen Terrain').add_to(c2)
            folium.TileLayer('Stamen Toner').add_to(c2)
            folium.TileLayer('Stamen Water Color').add_to(c2)
            folium.TileLayer('cartodbpositron').add_to(c2)
            folium.TileLayer('cartodbdark_matter').add_to(c2)
            folium.LayerControl().add_to(c2)
            c2.save('maCarte_GPStest2.html')

            message2 = """<html>
                          <head></head>
                          <center>
                          <p style="color: black;font-size:30px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span style="text-decoration: underline;"><B>Informations Geolocations Mapping Type Servers NS</B><p>
                          <iframe src=maCarte_GPStest2.html width=1200 height=450></iframe>
                          <center>
                          <center>
                          <img src="dns2.png" width=50 height=50 />
                          </center>
                          <body><p><span class="macouleur2">{geoloc_servers2}</span></p></body>
                          <center>
                          </html>""".format(

                geoloc_servers2=html2,
            )

            bytes2 = message2.encode(encoding='UTF-8')
            f.write(bytes2)
            mpb["value"] = 100
            mpb.update()
            mGui.destroy()
            self.Dialog_report_champsMX.show()
            self.MainWindow.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()

            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  # ok
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))
            print(colored("[*] Scanning and report [Network] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns1)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()



    def Report_Deep_Scan(self):
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Menu Scanner_Deep_ports/services]  ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(3)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -sC -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()
            template = html_string
            text_file = open("template.html", "w")
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            message = """<html>
                         <head></head>
                         <img src="Hyperion_red2.jpg">

                           """

            message2 = """<html>
                        <head></head>
                        <body><p></span><span>{TARGET}</span></p></body>
                        </body>
                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            mpb.update()
            time.sleep(3)
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report_DNS_Advanced] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()





    def Report_DNS_Advanced(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Menu Scanner_DNS_Advanced]  ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(3)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -sV -T4 -F -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()
            template = html_string
            text_file = open("template.html", "w")
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            message = """<html>
                         <head></head>
                         <img src="Hyperion_red2.jpg">

                           """

            message2 = """<html>
                        <head></head>
                        <body><p></span><span>{TARGET}</span></p></body>
                        </body>
                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            mpb.update()
            time.sleep(3)
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report_DNS_Advanced] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()


    def Report_err_http(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Menu Scanner Errors HTTP]  ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(3)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p80,443 --script http-errors " + dns + " -oX Extra_Analyse.xml ", shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()
            template = html_string
            text_file = open("template.html", "w")
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            message = """<html>
                         <head></head>
                         <img src="Hyperion_red2.jpg">

                           """

            message2 = """<html>
                        <head></head>
                        <body><p></span><span>{TARGET}</span></p></body>
                        </body>
                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            mpb.update()
            time.sleep(3)
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report Errors HTTP ] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_Exif(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Menu Scanner Exif Datas Picture]  ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(3)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p80,443 --script http-exif-spider -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()
            template = html_string
            text_file = open("template.html", "w")
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            message = """<html>
                         <head></head>
                         <img src="Hyperion_red2.jpg">

                           """

            message2 = """<html>
                        <head></head>
                        <body><p></span><span>{TARGET}</span></p></body>
                        </body>
                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            mpb.update()
            time.sleep(3)
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report Exif Datas Picture] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()






    def Report_DNS_Listing_supported_HTTP_methods(self):
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_Listing_supported_HTTP_methods]  ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))

            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call(
                "nmap -p80,443 --script http-methods,http-trace --script-args http-methods.test-all=true -Pn " + dns + " -oX Extra_Analyse.xml ",
                shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()
            template = html_string
            mpb["value"] = 75
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )

            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_Listing_supported_HTTP_methods] finished with Sucessfull ",
                          'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_Scraping_Email(self):
        import os
        import os
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_Scraping_Email] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            if os.path.exists("template.html"):
                os.remove("template.html")
            else:
                print(colored("|---> Building Template Report HTML ...", "green"))
                pass

            if os.path.exists("Extra_Analyse.html"):
                os.remove("Extra_Analyse.html")
            else:
                print(colored("|---> Building Template Report[2] HTML ...", "green"))
                pass

            if os.path.exists("Extra_Analyse.xml"):
                os.remove("Extra_Analyse.xml")
            else:
                print(colored("|---> Building Template Report XML ...", "green"))
                pass
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call(
                "nmap -p80 --script http-grep --script-args http-grep.builtins=e-mail -Pn " + dns + " -oX Extra_Analyse.xml ",
                shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )

            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_Scraping_Email] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_SMB(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_SMB] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()

            subprocess.call("nmap --script smb-system-info.nse -p445 -Pn " + dns + " -oX  Extra_Analyse.xml ",
                            shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string

            mpb["value"] = 75
            time.sleep(3)
            mpb.update()

            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>
                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report_DNS_SMB] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_Discovering_interesting(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_Discovering_interesting]' ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap --script http-enum -p80 -Pn " + dns + " -oX Extra_Analyse.xml  ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 75
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>
                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report_DNS_Discovering_interesting] finished with Sucessfull ",
                          'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()

            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_mod_userdir(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_mod_userdir_enumerate_accounts]", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p80 --script http-userdir-enum -Pn " + dns + " -oX Extra_Analyse.xml  ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 75
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(
                colored("[*] Scanning and report [Report_DNS_mod_userdir_enumerate_accounts] finished with Sucessfull ",
                        'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_Detecting_SMTP(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_Detecting_SMTP_open_relays] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -sV --script smtp-open-relay -v -Pn " + dns + " -oX Extra_Analyse.xml  ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 75
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>
                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_Detecting_SMTP_open_relays] finished with Sucessfull ",
                          'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_Enumeration_SMTP(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("Welcome on the report [Report_DNS_Enumeration_SMTP_usernames] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))

            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p25 --script smtp-enum-users -Pn " + dns + " -oX Extra_Analyse.xml  ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            template = html_string

            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report_DNS_Enumeration_SMTP_usernames] finished with Sucessfull ",
                          'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_IMAP(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_Capability_IMAP] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p143,993 --script imap-capabilities -Pn " + dns + " -oX Extra_Analyse.xml ",
                            shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 75
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>
                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report_DNS_Capability_IMAP] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_POP3(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_Capability_POP3] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p110 --script pop3-capabilities -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()
            template = html_string
            mpb["value"] = 75
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>
                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report_DNS_Capability_POP3] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_NTLM(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_NTLM_SMTP_authentification]", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p 25,465,587 --script smtp-ntlm-info -Pn " + dns + " -oX Extra_Analyse.xml ",
                            shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 75
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>
                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_NTLM_SMTP_authentification] finished with Sucessfull ",
                          'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()




    def voir_report_DataBase(self):
        import requests
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Starting Report_DNS_General :", "green"))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            pass
        import os
        print(colored("[Welcome on the report Type DataBase] ", 'magenta'))

        dns = self.ui.lineEdit.text()
        import validators
        verifdns = (validators.domain(dns))

        if verifdns == True:
            self.Dialog = QtWidgets.QDialog()

            self.Dialog_dns.close()
            self.MainWindow.close()

            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)

            import socket
            import os
            import html
            import whois

            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            # Create text widget and specify size.
            T = Text(mGui, height=5, width=52)
            # Create label
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()

            mpb["value"] = 10
            mpb.update()

            f = open('template.html', 'wb')

            print((colored("|--> Starting Analyse Type DataBase :", 'green')), dns)
            print(colored("|-->  ... [Loading] ... ", 'green'))
            print(colored("|--> Scanning Network ... ", 'green'))
            print((colored("|--> DNS :", "green")), dns)
            print(colored("|--> PLease patient ...", "green"))
            ip = (socket.gethostbyname(dns))
            hosts = [ip]
            r = requests.get('http://nmap.org')
            data1 = r.headers
            versions_srerver = (data1["server"])
            server = (versions_srerver)
            ports = [1433, 1434, 3306, 1583, 3050, 3351, 5432]
            services = ["TCP Microsoft SQL ", "UDP Microsoft SQL", "TCP [Pervasive SQL]", "[MySQL / MariaDB]",
                        "[Firebird & Interbase]", "[Pervasive SQL]", "[PostgreSQL]"] #ms-sql
            mpb["value"] = 50
            msg = (
                " Analyse DataBase Service And Ports : Microsoft SQL Server ,Pervasive SQL, Firebird & Interbase ,MySQL ,MariaDB ,PostgreSQL ")
            list_statut = []
            list_ip = []
            for host in hosts:
                for port in ports:
                    try:
                        # print(color1 + host + colorP + str(port), file=f)
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(5)
                        result = s.connect_ex((host, port))
                        if result == 0:
                            if port == 1433:
                                print('open')
                            if port == 1434:
                                print('open')
                            if port == 3306:
                                print('open')
                            if port == 1583:
                                print('open')
                            if port == 3050:
                                print('open')
                            if port == 3351:
                                print('open')
                            if port == 5432:
                                print('open')

                            list_statut.append("OPEN")
                            list_ip.append(ip)
                        else:
                            list_statut.append("CLOSE")
                            list_ip.append(ip)
                    except:
                        pass
            df = pd.DataFrame({'Adress_Ip': list_ip, 'Services': services, 'Port': ports, 'status': list_statut})
            mpb["value"] = 70
            html = df.to_html().replace('<th>', '<th style = "color: red">')

            message_sub = """<html>
                                        <head></head>
                                        <center>
                                        <img style="border:10px solid black;" src="Hyperion_red2.jpg">
                                        </center>
                                        <body style="background-image: url(border_fait.jpeg);background-repeat: no-repeat;">
                                        <body marginwidth="50" marginheight="100" topmargin="10" leftmargin="170">
                                        <center>
                                        <body><p><span style="color: red"><B>DNS Target : </B></span><span class="macouleur2"><B>{TARGET}</B></span></p></body>
                                         <body><p><span style="color: red"><B>Type Server : </B></span><span class="macouleur2"><B>{SERVER}</B></span></p></body>
                                        <p style="color: black;font-size:30px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span style="text-decoration:"><B>Informations DataBase Servers</B><p>
                                        <p style="color: black;font-size:20px;text-shadow: 1px 1px 1px red,2px 2px 1px red";><span class="macouleur2"><B>{MSG}</B><p>
                                        <body><p><span style="color: red"><B> Analyse and Indentify Datase Base :</B></span><span class="macouleur2"><B>{List_subdomains}</B></span></p></body>
                                        </center> 
                                        </html>""".format(List_subdomains=html, TARGET=dns, MSG=msg, SERVER=server,
                                                          )
            bytes_sub = message_sub.encode(encoding='UTF-8')
            f.write(bytes_sub)
            f.close()
            print(colored("[*] Scanning and report [General Informations] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            # self.Dialog_report.show()
            self.MainWindow.show()
            mpb["value"] = 100
            mpb.update()
            mGui.destroy()
            self.Dialog_report_champsMX.show()

            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)

            self.Dialog_pdf.show()

            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé

            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))


        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()


    def Report_DNS_listall_MYSQL(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report DNS_listall_MYSQL ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(3)
            mpb.update()

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -sV --script=mysql-databases -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_listall_MYSQL] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_Empty_MYSQL(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()

            print(colored("[Welcome on the report [DNS_Empty_MYSQL] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p3306 --script mysql-empty-password -Pn " + dns + " -oX Extra_Analyse.xml ",
                            shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_Empty_MYSQL] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_info_mssql(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [DNS_info_mssql] ", 'magenta'))
            print(colored('|---> ', "green"))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p1433 --script ms-sql-info -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_info_mssql] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")

            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_info_mongodb(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [DNS_info_mongodb] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p27017 --script mongodb-info -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_info_mongodb] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_detecting_mongodb(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [DNS_detecting_mongodb] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()

            subprocess.call("nmap -p27017 --script mongodb-databases -Pn " + dns + " -oX Extra_Analyse.xml", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_detecting_mongodb] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_List_CoucheDB(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [DNS_List_CoucheDB] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p5984 --script couchdb-databases -Pn " + dns + " -oX Extra_Analyse.xml", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 75
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_List_CoucheDB] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_DNS_CoucheDB_static(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [DNS_CoucheDB_static] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p5984 --script couchdb-stats -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_CoucheDB_static] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    ###################################################################################################################

    def Report_CVE_Scan(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()

        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_CVE_Scan] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -sV --script=vulners -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report_CVE_Scan] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_XSS_Scan(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_XSS] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p80 --script http-unsafe-output-escaping -Pn " + dns + " -oX Extra_Analyse.xml ",
                            shell=True, stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_XSS] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_SQL_Scan(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [SQL_Scan] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()

            subprocess.call("nmap -p80 --script http-sql-injection -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()

            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()

            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [SQL_Scan] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()



    def Report_web_applications_Scan(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            print(colored("[Welcome on the report [DNS_web_applications_Scan] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            subprocess.call("nmap -p80 --script http-default-accounts -Pn " + dns + " -oX Extra_Analyse.xml ",
                            shell=True, stdout=subprocess.DEVNULL)
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_web_applications_Scan] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_Shellshock_Scan(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_Shellshock_Scan] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -sV --script http-shellshock -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_Shellshock_Scan]] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_insecure_crossdomain_Scan(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_insecure_crossdomain_Scan] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))

            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()

            subprocess.call("nmap --script http-cross-domain-policy -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()

            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()

            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_insecure_crossdomain_Scan]] finished with Sucessfull ",
                          'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_sourcecode_control_Scan(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [DNS_sourcecode_control_Scan] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p80 --script http-git -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_sourcecode_control_Scan] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_InsecureCipherSSL(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [DNS_InsecureCipherSSL]] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()

            subprocess.call("nmap --script ssl-enum-ciphers -p 443 -Pn " + dns + " -oX Extra_Analyse.xml", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()

            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [DNS_InsecureCipherSSL] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_CSRF(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_Report_CSRF] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))

            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p80 --script http-csrf -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()

            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report_DNS_Report_CSRF] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_RFI(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_DNS_Report_RFI] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p80 --script http-rfi-spider -Pn " + dns + " -oX Extra_Analyse.xml", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()

            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [Report_DNS_Report_RFI] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")

            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_SMB_vulnerabilitie(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [Report_SMB_vulnerabilitie] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))

            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap --script smb-check-vulns -p445 -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning and report [SMB_vulnerabilitie]] finished with Sucessfull ", 'magenta'))
            print(
                colored("-----------------------------------------------------------------------------------", 'blue'))
            print("")
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_SSL_Injection(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            print(colored("[Welcome on the report [DNS_Report_SSL_Injection] ", 'magenta'))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()

            subprocess.call("nmap -p 443 --script ssl-ccs-injection -Pn " + dns + " -oX Extra_Analyse.xml  ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()

            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()

            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning DNS_Report_SSL_Injection] with Sucessfull ", 'green'))
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_Nikto(self):
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            subprocess.call("nikto -h " + dns, shell=True)
        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_wafw00f(self):
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            subprocess.call("wafw00f " + dns, shell=True)
        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_HTTP_WAF(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()
            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            print(colored('|---> [Firewall : Report_HTTP_WAF]', "green"))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS (WAF) :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p80 --script http-waf-detect -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 75
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning Report_DNS_Advanced with Sucessfull ", 'green'))
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_Detect_WAF(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()

            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            print(colored('|---> [Firewall :  Report_Detect_WAF]', "green"))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS  Detect Waf :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap -p80 --script http-waf-detect -Pn " + dns + " -oX Extra_Analyse.xml ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning Report_DNS_Advanced with Sucessfull ", 'green'))
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_Fingerprint_WAF(self):
        import os
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            self.Dialog_dns.close()
            self.MainWindow.close()

            self.Dialog_report_champsMX = QtWidgets.QDialog()
            self.ui = Ui_Dialog_report_champsMX()
            self.ui.setupUi(self.Dialog_report_champsMX)
            mGui = Tk()
            mGui.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
            mGui.resizable(0, 0)
            mGui.geometry('450x40')
            mGui.title('Hyperion V3')
            style = ttk.Style()
            style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', )
            mpb = ttk.Progressbar(mGui, style="red.Horizontal.TProgressbar", orient="horizontal", length=400,
                                  mode="determinate", )
            mpb.pack()
            T = Text(mGui, height=5, width=52)
            l = Label(mGui, text=" Patient Please ")
            l.config(font=("Impact", 10, 'bold', "italic"))
            l.pack()
            T.pack()
            mpb["maximum"] = 100
            mGui.update_idletasks()
            mpb["value"] = 25
            time.sleep(2)
            mpb.update()
            print(colored('|---> [Firewall : Report_Fingerprint_WAF]', "green"))
            print(colored(" [*] <> Building Template HTML ...", "green"))
            print((colored("|--> Starting Analyse DNS FingerPrint Waf :", 'green')), dns)
            print(colored(" [*] <> [... patient please ...]", "green"))

            mpb["value"] = 50
            time.sleep(3)
            mpb.update()
            subprocess.call("nmap --script=http-waf-fingerprint -Pn " + dns + " -oX Extra_Analyse.xml  ", shell=True,
                            stdout=subprocess.DEVNULL)
            subprocess.call("xsltproc Extra_Analyse.xml -o Extra_Analyse.html", shell=True, stdout=subprocess.DEVNULL)
            f = open('Extra_Analyse.html', 'r')
            html_string = f.read()

            template = html_string
            mpb["value"] = 70
            time.sleep(3)
            mpb.update()
            text_file = open("template.html", "w")
            message = """<html>
                           <head></head>
                           <h2 style="background-color: white;">
                           <center>
                           <img src="Hyperion_red2.jpg" />
                           </center>
                           <center>
                           """

            message2 = """<html>
                        <head></head>
                        <center>

                        <body><p></span><span >{TARGET}</span></p></body>
                        </body>

                        </html>""".format(
                TARGET=template,
            )
            mpb["value"] = 100
            time.sleep(3)
            mpb.update()
            text_file.write(message)
            text_file.write(message2)
            print(colored("[*] Scanning Report_DNS_Advanced with Sucessfull ", 'green'))
            text_file.close()
            mGui.destroy()
            self.MainWindow.show()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))

        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()


    def Report_Admin_Finder(self):
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        verifdns = (validators.domain(dns))
        if verifdns == True:
            subprocess.call("nikto -h " + dns, shell=True)
        else:
            print((colored("[!]|---> [Error DNS no found!]:", "red")), dns)
            self.Dialog_dns.close()
            self.Dialog_error_dns = QtWidgets.QDialog()
            self.ui = Ui_Dialog_error_dns()
            self.ui.setupUi_error_dns(self.Dialog_error_dns)
            self.Dialog_error_dns.show()

    def Report_found_Admin(self):
        import requests as req
        import os
        if os.path.exists("template.html"):
            os.remove("template.html")
        else:
            print(colored("|---> Building Template Report HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.html"):
            os.remove("Extra_Analyse.html")
        else:
            print(colored("|---> Building Template Report[2] HTML ...", "green"))
            pass

        if os.path.exists("Extra_Analyse.xml"):
            os.remove("Extra_Analyse.xml")
        else:
            print(colored("|---> Building Template Report XML ...", "green"))
            pass
        self.Dialog_dns.close()
        dns = self.ui.lineEdit.text()
        print(colored('|---> [Firewall : Report_Admin_general]', "green"))
        print(colored(" [*] <> Building Template HTML ...", "green"))
        print((colored("|--> Starting Analyse DNS Advanced :", 'green')), dns)
        print(colored(" [*] <> [... patient please ...]", "green"))

        verifdns = (validators.domain(dns))
        if verifdns == True:
            def scanner_admin_php():

                php = ['admin/', 'administrator/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'usuarios/',
                       'usuario/', 'administrator/', 'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/',
                       'adminLogin/', 'admin_area/', 'panel-administracion/', 'instadmin/',
                       'memberadmin/', 'administratorlogin/', 'adm/', 'admin/account.php', 'admin/index.php',
                       'admin.php', 'admin.html', 'index.php', 'login.php', 'login.html', 'administrator', 'admin',
                       'adminpanel',
                       'cpanel', 'login', 'wp-login.php', 'administrator', 'admins', 'logins', 'admin.asp', 'login.asp',
                       'adm/', 'admin/', 'admin/account.html', 'admin/login.html', 'admin/login.html',
                       'admin/controlpanel.html',
                       'admin/controlpanel.htm', 'admin/adminLogin.html', 'admin/adminLogin.htm',
                       'admin.htm', 'admin.html', 'adminitem/', 'adminitems/', 'administrator/',
                       'administrator/login.%EXT%', 'administrator.%EXT%', 'administration/',
                       'administration.%EXT%', 'adminLogin/', 'adminlogin.%EXT%', 'admin_area/admin.%EXT%',
                       'admin_area/', 'admin_area/login.%EXT%', 'manager/', 'superuser/',
                       'superuser.%EXT%', 'access/', 'access.%EXT%', 'sysadm/', 'sysadm.%EXT%', 'superman/',
                       'supervisor/', 'panel.%EXT%', 'control/', 'control.%EXT%',
                       'member/', 'member.%EXT%', 'members/', 'user/', 'user.%EXT%', 'cp/', 'uvpanel/', 'manage/',
                       'manage.%EXT%', 'management/', 'management.%EXT%', 'signin/', 'signin.%EXT%', 'log-in/',
                       'log-in.%EXT%', 'log_in/', 'log_in.%EXT%',
                       'sign_in/', 'sign_in.%EXT%', 'sign-in/', 'sign-in.%EXT%', 'users/', 'users.%EXT%', 'accounts/',
                       'accounts.%EXT%', 'bb-admin/login.%EXT%',
                       'bb-admin/admin.%EXT%', 'bb-admin/admin.html', 'administrator/account.%EXT%', 'relogin.htm',
                       'relogin.html', 'check.%EXT%', 'relogin.%EXT%', 'blog/wp-login.%EXT%',
                       'user/admin.%EXT%', 'users/admin.%EXT%', 'registration/', 'processlogin.%EXT%',
                       'checklogin.%EXT%', 'checkuser.%EXT%', 'checkadmin.%EXT%', 'isadmin.%EXT%', 'authenticate.%EXT%',
                       'authentication.%EXT%',
                       'auth.%EXT%', 'authuser.%EXT%', 'authadmin.%EXT%', 'cp.%EXT%', 'modelsearch/login.%EXT%',
                       'moderator.%EXT%', 'moderator/', 'controlpanel/', 'controlpanel.%EXT%',
                       'admincontrol.%EXT%', 'adminpanel.%EXT%', 'fileadmin/', 'fileadmin.%EXT%', 'sysadmin.%EXT%',
                       'admin1.%EXT%', 'admin1.html', 'admin1.htm', 'admin2.%EXT%',
                       'admin2.html', 'yonetim.%EXT%', 'yonetim.html', 'yonetici.%EXT%', 'yonetici.html', 'phpmyadmin/',
                       'myadmin/',
                       'ur-admin.%EXT%', 'ur-admin/', 'Server.%EXT%', 'Server/', 'wp-admin/', 'administr8.%EXT%',
                       'administr8/', 'webadmin/', 'webadmin.%EXT%', 'administratie/',
                       'admins/', 'admins.%EXT%', 'administrivia/', 'Database_Administration/', 'useradmin/',
                       'sysadmins/', 'sysadmins/', 'admin1/',
                       'system-administration/', 'administrators/', 'pgadmin/', 'directadmin/', 'staradmin/',
                       'ServerAdministrator/', 'SysAdmin/', 'administer/', 'LiveUser_Admin/',
                       'sys-admin/', 'typo3/', 'panel/', 'cpanel_file/', 'platz_login/', 'rcLogin/', 'blogindex/',
                       'formslogin/', 'autologin/', 'manuallogin/', 'simpleLogin/', 'loginflat/',
                       'utility_login/', 'showlogin/', 'memlogin/', 'login-redirect/', 'sub-login/', 'wp-login/',
                       'login1/', 'dir-login/', 'login_db/', 'xlogin/',
                       'smblogin/', 'customer_login/', 'UserLogin/', 'login-us/', 'acct_login/', 'bigadmin/',
                       'project-admins/', 'phppgadmin/', 'pureadmin/', 'sql-admin/',
                       'radmind/', 'openvpnadmin/', 'wizmysqladmin/', 'vadmind/', 'ezsqliteadmin/', 'hpwebjetadmin/',
                       'newsadmin/', 'adminpro/', 'Lotus_Domino_Admin/', 'bbadmin/', 'vmailadmin/',
                       'Indy_admin/', 'ccp14admin/', 'irc-macadmin/', 'banneradmin/', 'sshadmin/', 'phpldapadmin/',
                       'macadmin/', 'administratoraccounts/', 'admin4_account/', 'admin4_colon/',
                       'radmind-1/', 'Super-Admin/', 'AdminTools/', 'cmsadmin/', 'SysAdmin2/', 'globes_admin/',
                       'cadmins/', 'phpSQLiteAdmin/', 'navSiteAdmin/', 'server_admin_small/', 'logo_sysadmin/',
                       'system_administration/',
                       'ss_vms_admin_sm/', 'bb-admin/', 'panel-administracion/', 'instadmin/', 'memberadmin/',
                       'administratorlogin/', 'adm.%EXT%', 'admin_login.%EXT%',
                       'panel-administracion/login.%EXT%', 'pages/admin/admin-login.%EXT%', 'pages/admin/',
                       'acceso.%EXT%', 'admincp/login.%EXT%', 'admincp/', 'adminarea/', 'admincontrol/',
                       'affiliate.%EXT%', 'adm_auth.%EXT%', 'memberadmin.%EXT%', 'administratorlogin.%EXT%',
                       'modules/admin/', 'administrators.%EXT%', 'siteadmin/',
                       'siteadmin.%EXT%', 'adminsite/', 'kpanel/', 'vorod/', 'vorod.%EXT%', 'vorud/', 'vorud.%EXT%',
                       'adminpanel/', 'PSUser/', 'secure/', 'webmaster/', 'webmaster.%EXT%', 'autologin.%EXT%',
                       'userlogin.%EXT%', 'admin_area.%EXT%', 'cmsadmin.%EXT%', 'security/', 'usr/', 'root/', 'secret/',
                       'admin/login.%EXT%', 'admin/adminLogin.%EXT%', 'moderator.php',
                       'moderator.html', 'moderator/login.%EXT%', 'moderator/admin.%EXT%', 'yonetici.%EXT%', '0admin/',
                       '0manager/', 'aadmin/', 'cgi-bin/login%EXT%', 'login1%EXT%',
                       'login_admin/', 'login_admin%EXT%', 'login_out/', 'login_out%EXT%', 'login_user%EXT%',
                       'loginerror/', 'loginok/', 'loginsave/', 'loginsuper/', 'loginsuper%EXT%',
                       'login%EXT%', 'logout/', 'logout%EXT%', 'secrets/', 'super1/', 'super1%EXT%', 'super_index%EXT%',
                       'super_login%EXT%', 'supermanager%EXT%', 'superman%EXT%',
                       'superuser%EXT%', 'supervise/', 'supervise/Login%EXT%', 'super%EXT%', 'admin/login.php',
                       'admin/admin.php', 'admin/account.php', 'admin_area/admin.php', 'admin_area/login.php',
                       'siteadmin/login.php', 'siteadmin/index.php',
                       'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html',
                       'admin/admin.html', 'admin_area/index.php', 'bb-admin/index.php', 'bb-admin/login.php',
                       'bb-admin/admin.php', 'admin/home.php', 'admin_area/login.html', 'admin_area/index.html',
                       'admin/controlpanel.php', 'admin.php', 'admincp/index.asp', 'admincp/login.asp',
                       'admincp/index.html', 'admin/account.html', 'adminpanel.html', 'webadmin.html',
                       'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html',
                       'admin_login.html', 'panel-administracion/login.html', 'admin/cp.php', 'cp.php',
                       'administrator/index.php', 'administrator/login.php', 'nsw/admin/login.php',
                       'webadmin/login.php', 'admin/admin_login.php', 'admin_login.php',
                       'administrator/account.php', 'administrator.php', 'admin_area/admin.html',
                       'pages/admin/admin-login.ph', 'admin/admin-login.php', 'admin-login.php',
                       'bb-admin/index.html', 'bb-admin/login.html', 'acceso.php', 'bb-admin/admin.html',
                       'admin/home.html', 'login.php', 'modelsearch/login.php', 'moderator.php', 'moderator/login.php',
                       'moderator/admin.php', 'account.php', 'pages/admin/admin-login.html', 'admin/admin-login.html',
                       'admin-login.html', 'controlpanel.php', 'admincontrol.php',
                       'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html',
                       'rcjakar/admin/login.php', 'adminarea/index.html', 'adminarea/admin.html',
                       'webadmin.php', 'webadmin/index.php', 'webadmin/admin.php', 'admin/controlpanel.html',
                       'admin.html', 'admin/cp.html', 'cp.html', 'adminpanel.php', 'moderator.html',
                       'administrator/index.html', 'administrator/login.html', 'user.html',
                       'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html',
                       'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html',
                       'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html',
                       'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.php',
                       'account.html', 'controlpanel.html', 'admincontrol.html', 'panel-administracion/login.php',
                       'wp-login.php', 'adminLogin.php', 'admin/adminLogin.php',
                       'home.php', 'admin.php', 'adminarea/index.php', 'adminarea/admin.php', 'adminarea/login.php',
                       'panel-administracion/index.php', 'panel-administracion/admin.php', 'modelsearch/index.php',
                       'modelsearch/admin.php', 'admincontrol/login.php', 'adm/admloginuser.php', 'admloginuser.php',
                       'admin2.php', 'admin2/login.php', 'admin2/index.php', 'usuarios/login.php',
                       'adm/index.php', 'adm.php', 'affiliate.php', 'adm_auth.php', 'memberadmin.php',
                       'administratorlogin.php']
                n = (len(php))
                print(n)
                list_404 = []
                list_200 = []
                list_302 = []
                admin_found = []
                site = ("http://www.nmap.org")
                for admin in php:
                    admin = admin.replace("\n", "")
                    admin = "/" + admin
                    host = site + admin
                    # print(host)
                    print(">> Checking... : " + host)
                    resp = req.get(host)
                    list_resp = []
                    list_resp.append(resp)

                    if resp.status_code == 200:
                        print("[*] Admin page Found : " + host)
                        admin_found.append(host)
                        list_200.append(host)
                    elif resp.status_code == 404:
                        list_404.append(host)
                        print("> Admin page not Found : " + host)

                    elif resp.status_code == 302:
                        print("Possible Admin page Redirect(302): " + host)
                    else:
                        print("%s %s %s" % (host, " Interesting response:", resp.status_code))  # autre reponse

                print("[*] >> Total Pages Scanned: ", n)
                print("[*] >> Page Admin Found !!:", admin_found)
                print("[*] >> Scanning Termine ")
                dfwhois = pd.DataFrame({'page404': list_404})
                # dfwhois.set_index('ServerDNS', inplace=True)
                print(dfwhois)
                htmlwhois = dfwhois.to_html(justify="center", border=1).replace('<th>',
                                                                                '<th style = "color: red">').replace(
                    '<td>', '<td style = "color: white">')
                dfwhois2 = pd.DataFrame({'page200': list_200})
                htmlwhois2 = dfwhois2.to_html(justify="center", border=1).replace('<th>',
                                                                                  '<th style = "color: green">').replace(
                    '<td>', '<td style = "color: white">')

                msg_menu = "Welcome on the report Whois_Menu Informations :"
                message = """<html>
                           <head></head>
                           <h2 style="background-color: black;">
                           <center>
                           <img src="Hyperion_red2.jpg">
                           </center>
                           <center>
                           <p style="color:#FF0000";>-- Report Analyse Login Admin Panel  --<p>
                           </center>
                           <center>
                           <body><p><span style="color: green">{TARGET}</span></p></body>
                           <body><p><span style="color: red">Informations Page Login by Brute Force DNS [404]  </span><span >{login}</span></p></body>
                           </center>
                           <center>
                           <body><p><span style="color: red">Informations Page Login [Found!] by Brute Force DNS [200]  </span><span >{login2}</span></p></body>
                           </center>
                           <center>
                           </center>


                            </html>""".format(
                    TARGET=dns,
                    login=htmlwhois,
                    login2=htmlwhois2,
                )
                text_file = open("Infos_champsMX.html", "w")
                # bytes = self.message.encode(encoding='UTF-8')
                text_file.write(message)

            scanner_admin_php()
            self.Dialog_report_champsMX.show()
            self.Dialog_pdf = QtWidgets.QDialog()
            self.ui = Ui_Dialog_pdf()
            self.ui.setupUi(self.Dialog_pdf)
            self.Dialog_pdf.show()
            self.ui.pushButton_2.hide()
            self.ui.lineEdit.textChanged[str].connect(lambda: self.ui.pushButton_2.show())
            self.ui.pushButton.clicked.connect(self.menu_pdf_annuler)  # annulé
            self.ui.pushButton_2.clicked.connect(self.menu_pdf_ok)  #
            self.ui.lineEdit.textChanged[str].connect(
                lambda: self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.voir_Menu_general()
    sys.exit(app.exec_())