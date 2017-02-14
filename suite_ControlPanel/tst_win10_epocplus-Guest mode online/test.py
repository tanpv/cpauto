# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierControlpanel")
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.accountBtn_QPushButton").text), "Add User")
    clickButton(waitForObject(":InsightEpocControlPanelClass.accountBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnGuestMultiAcc_QPushButton"))
    # wait to login with guest
    snooze(10)
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.accountBtn_QPushButton").text), "Guest")
    clickButton(waitForObject(":InsightEpocControlPanelClass.menuPushButton_QPushButton"))
    clickButton(waitForObject(":menuGroupBox.calibrationMenuButton_QPushButton"))
    test.compare(waitForObjectExists(":InsightEpocControlPanelClass.startRecordingButton_QPushButton").enabled, False)
