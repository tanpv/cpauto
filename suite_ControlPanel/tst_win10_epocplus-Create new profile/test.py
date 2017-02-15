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
    clickItem(":menuGroupBox.detectionListWidget_QListWidget", "         Mental Commands", 110, 19, 0, Qt.LeftButton)
    clickButton(waitForObject(":InsightEpocControlPanelClass.userProfileBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnNewProfi_QPushButton"))
    mouseClick(waitForObject(":InsightEpocControlPanelClass.txtNewTraining_QLineEdit"), 26, 20, 0, Qt.LeftButton)
    type(waitForObject(":InsightEpocControlPanelClass.txtNewTraining_QLineEdit"), "push_cm")
    type(waitForObject(":InsightEpocControlPanelClass.txtNewTraining_QLineEdit"), "<Backspace>")
    type(waitForObject(":InsightEpocControlPanelClass.txtNewTraining_QLineEdit"), "<Backspace>")
    type(waitForObject(":InsightEpocControlPanelClass.txtNewTraining_QLineEdit"), "prf")
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnCreateTraining_QPushButton"))
    # wait to create
    snooze(1)
