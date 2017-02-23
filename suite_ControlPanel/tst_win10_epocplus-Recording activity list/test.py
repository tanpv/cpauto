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
    clickButton(waitForObject(":menuGroupBox.calibrationMenuButton_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.step1Button_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.step1Button_QPushButton"))
    mouseClick(waitForObject(":InsightEpocControlPanelClass.listExperimentCB_QComboBox"), 106, 21, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":InsightEpocControlPanelClass.listExperimentCB_QComboBox", "Doodling"), 84, 12, 0, Qt.LeftButton)
    mouseClick(waitForObject(":InsightEpocControlPanelClass.listExperimentCB_QComboBox"), 109, 18, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":InsightEpocControlPanelClass.listExperimentCB_QComboBox", "Gaming"), 71, 9, 0, Qt.LeftButton)
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.listExperimentCB_QComboBox").currentText), "Gaming")
