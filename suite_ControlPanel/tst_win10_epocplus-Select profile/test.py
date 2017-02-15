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
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.accountBtn_QPushButton").text), "thamvu")
    clickButton(waitForObject(":InsightEpocControlPanelClass.menuPushButton_QPushButton"))
    clickButton(waitForObject(":menuGroupBox.detectionsPushButton_QPushButton"))
    waitForObjectItem(":menuGroupBox.detectionListWidget_QListWidget", "         Mental Commands")
    clickItem(":menuGroupBox.detectionListWidget_QListWidget", "         Mental Commands", 114, 16, 0, Qt.LeftButton)
    clickButton(waitForObject(":InsightEpocControlPanelClass.userProfileBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnSelectProfile_QPushButton"))
    waitForObjectItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "test")
    clickItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "test", 26, 18, 0, Qt.LeftButton)
    # wait to change profile
    snooze(1)
    clickButton(waitForObject(":InsightEpocControlPanelClass.userProfileBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnSelectProfile_QPushButton"))
    waitForObjectItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "okmen")
    clickItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "okmen", 33, 13, 0, Qt.LeftButton)
    # wait to change profile
    snooze(1)
    clickButton(waitForObject(":InsightEpocControlPanelClass.userProfileBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnSelectProfile_QPushButton"))
    waitForObjectItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "estung")
    clickItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "estung", 39, 12, 0, Qt.LeftButton)
    # wait to change profile
    snooze(1)
    clickButton(waitForObject(":InsightEpocControlPanelClass.userProfileBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnSelectProfile_QPushButton"))
    waitForObjectItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "tung")
    clickItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "tung", 44, 15, 0, Qt.LeftButton)
    # wait to change profile
    snooze(1)
    clickButton(waitForObject(":InsightEpocControlPanelClass.userProfileBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnSelectProfile_QPushButton"))
    waitForObjectItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "Default")
    clickItem(":InsightEpocControlPanelClass.profileListSelectWidget_QListWidget", "Default", 41, 12, 0, Qt.LeftButton)
    # wait to change profile
    snooze(1)
    setWindowState(waitForObject(":InsightEpocControlPanelClass_InsightEpocControlPanel"), WindowState.Minimize)
    setWindowState(waitForObject(":InsightEpocControlPanelClass_InsightEpocControlPanel"), WindowState.Normal)
    setWindowState(waitForObject(":InsightEpocControlPanelClass_InsightEpocControlPanel"), WindowState.Minimize)
