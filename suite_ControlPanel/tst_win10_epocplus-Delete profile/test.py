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
    clickItem(":menuGroupBox.detectionListWidget_QListWidget", "         Mental Commands", 85, 8, 0, Qt.LeftButton)
    clickButton(waitForObject(":InsightEpocControlPanelClass.userProfileBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnDeleteProfile_QPushButton"))
    scrollTo(waitForObject(":listProfile_QScrollBar"), 1)
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnSelectProfile_QPushButton"))
    scrollTo(waitForObject(":profileListSelectWidget_QScrollBar"), 2)
    waitForObjectItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "push\\_prf")
    clickItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "push\\_prf", 47, 7, 0, Qt.LeftButton)
    clickButton(waitForObject(":InsightEpocControlPanelClass.userProfileBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnDeleteProfile_QPushButton"))
    waitForObjectItem(":InsightEpocControlPanelClass.listProfile_QListWidget", "push\\_prf\\_replace")
    clickItem(":InsightEpocControlPanelClass.listProfile_QListWidget", "push\\_prf\\_replace", 96, 13, 0, Qt.LeftButton)
    waitForObjectItem(":InsightEpocControlPanelClass.listProfile_QListWidget", "push\\_prf\\_replace")
    doubleClickItem(":InsightEpocControlPanelClass.listProfile_QListWidget", "push\\_prf\\_replace", 154, 12, 0, Qt.LeftButton)
    # wait to delete profile
    snooze(1)