# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierControlpanel")
    clickButton(waitForObject(":InsightEpocControlPanelClass.accountBtn_QPushButton"))
    mouseClick(waitForObject(":InsightEpocControlPanelClass.label_17_QLabel"), 71, 5, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.btnCreateMultiAcc_QPushButton").text), "Create a new EmotivID")
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnCreateMultiAcc_QPushButton"))
    # wait to redirect
    snooze(10)
