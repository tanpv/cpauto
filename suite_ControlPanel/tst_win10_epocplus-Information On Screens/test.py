# -*- coding: utf-8 -*-

def main():
    startApplication("EmotivXavierControlpanel")
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.EPOCModeButton_QPushButton").text), "EPOC")
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.InsightModeButton_QPushButton").text), "Insight")
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.tabLabel_QLabel").text), "> HEADSET SETUP GUIDE")
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.LabelCQ_QLabel").text), "     EPOC Electrodes Contact Quality")
    test.compare(str(waitForObjectExists(":InsightEpocControlPanelClass.labelTitle_QLabel").text), " Setup and Pairing")
