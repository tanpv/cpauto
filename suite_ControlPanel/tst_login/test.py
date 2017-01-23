# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierControlpanel")
    clickButton(waitForObject(":InsightEpocControlPanelClass.accountBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnLoginMultiAcc_QPushButton"))
    type(waitForObject(":InsightEpocControlPanelClass.txtUserNameNext_QLineEdit"), "tpv")
    type(waitForObject(":InsightEpocControlPanelClass.txtUserNameNext_QLineEdit"), "<Tab>")
    type(waitForObject(":InsightEpocControlPanelClass.txtPassWNext_QLineEdit"), "Aaa12345678")
    clickButton(waitForObject(":InsightEpocControlPanelClass.btnLoginUserNext_QPushButton"))
    
    # wait 10 s here
    snooze(10)
    
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.accountBtn_QPushButton").text), "tpv")
    clickButton(waitForObject(":InsightEpocControlPanelClass.accountBtn_QPushButton"))
    clickButton(waitForObject(":InsightEpocControlPanelClass.logOutButton_QPushButton"))
