# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierControlpanel")
    clickButton(waitForObject(":InsightEpocControlPanelClass.accountBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnLoginMultiAcc_QPushButton"))
    type(waitForObject(":InsightEpocControlPanelClass.txtUserNameNext_QLineEdit"), "thamvu")
    type(waitForObject(":InsightEpocControlPanelClass.txtUserNameNext_QLineEdit"), "<Tab>")
    type(waitForObject(":InsightEpocControlPanelClass.txtPassWNext_QLineEdit"), "Humg1991")
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnLoginUserNext_QPushButton"))
    # wait to login
    snooze(10)
    clickButton(waitForObject(":InsightEpocControlPanelClass.menuPushButton_QPushButton"))
    clickButton(waitForObject(":menuGroupBox.detectionsPushButton_QPushButton"))
    waitForObjectItem(":menuGroupBox.detectionListWidget_QListWidget", "         Mental Commands")
    clickItem(":menuGroupBox.detectionListWidget_QListWidget", "         Mental Commands", 122, 16, 0, Qt.LeftButton)
    clickButton(waitForObject(":InsightEpocControlPanelClass.userProfileBtn_QPushButton"))
    mouseClick(waitForObject(":InsightEpocControlPanelClass.lblProfileName_QLabel"), 15, 32, 0, Qt.LeftButton)
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnRenameProfile_QPushButton"))
    doubleClick(waitForObject(":InsightEpocControlPanelClass.txtCurrentProfile_QLineEdit"), 57, 15, 0, Qt.LeftButton)
    type(waitForObject(":InsightEpocControlPanelClass.txtCurrentProfile_QLineEdit"), "test_rn")
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnRenameCurrent_QPushButton"))
    # wait to rename
    snooze(1)
