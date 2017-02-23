# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierControlpanel")
    clickButton(waitForObject(":InsightEpocControlPanelClass.menuPushButton_QPushButton"))
    clickButton(waitForObject(":menuGroupBox.helpPushButton_QPushButton"))
    sendEvent("QMouseEvent", waitForObject(":menuGroupBox.helpListWidget_QListWidget"), QEvent.MouseButtonPress, 115, 42, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(":menuGroupBox.helpListWidget_QListWidget"), QEvent.MouseButtonRelease, 115, 42, Qt.LeftButton, 0, 0)
    test.compare(str(waitForObjectExists(":OK_QPushButton").text), "OK")
    clickButton(waitForObject(":OK_QPushButton"))
