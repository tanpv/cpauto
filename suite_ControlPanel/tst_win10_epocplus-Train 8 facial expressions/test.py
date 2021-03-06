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
    clickButton(waitForObject(":InsightEpocControlPanelClass.menuPushButton_QPushButton"))
    clickButton(waitForObject(":menuGroupBox.detectionsPushButton_QPushButton"))
    waitForObjectItem(":menuGroupBox.detectionListWidget_QListWidget", "         Facial Expressions")
    clickItem(":menuGroupBox.detectionListWidget_QListWidget", "         Facial Expressions", 100, 19, 0, Qt.LeftButton)
    clickTab(waitForObject(":InsightEpocControlPanelClass.trainingTabWidget_QTabWidget"), "Training")
    mouseClick(waitForObject(":tab_4.expressionCBox_2_QComboBox"), 180, 23, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":tab_4.expressionCBox_2_QComboBox", "Neutral"), 121, 4, 0, Qt.LeftButton)
    openContextMenu(waitForObject(":tab_4.expressionCBox_2_QComboBox"), 120, 26, 0)
    openContextMenu(waitForObject(":tab_4.expressionCBox_2_QComboBox"), 150, 17, 0)
    test.compare(str(waitForObjectExists(":tab_4.trainingControlLabel_QLabel").text), "TRAINING CONTROL")
    clickButton(waitForObject(":tab_4.startTrainingBtn_2_QPushButton"))
    test.vp("VP1")
    clickButton(waitForObject(":Yes_QPushButton"))
    openContextMenu(waitForObject(":tab_4.TrainningInProgressSlider_QProgressBar"), 211, 4, 0)
    clickTab(waitForObject(":InsightEpocControlPanelClass.trainingTabWidget_QTabWidget"), "Sensitivity")
    sendEvent("QWheelEvent", waitForObject(":tab_3.surpriseSlider_QSlider"), 0, 1, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(":tab_3.surpriseSlider_QSlider"), 0, 8, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(":tab_3.surpriseSlider_QSlider"), 0, 9, -120, 0, 2)
    sendEvent("QWheelEvent", waitForObject(":tab_3.surpriseSlider_QSlider"), 0, 9, -120, 0, 2)
    clickTab(waitForObject(":InsightEpocControlPanelClass.trainingTabWidget_QTabWidget"), "Training")
    openContextMenu(waitForObject(":tab_4.startTrainingBtn_2_QPushButton"), 100, 26, 0)
    test.compare(str(waitForObjectExists(":tab_4.startTrainingBtn_2_QPushButton").text), "Start Training")
    test.compare(str(waitForObjectExists(":tab_4.clearTrainingBtn_2_QPushButton").text), "Clear Training")
    sendEvent("QMouseEvent", waitForObject(":tab_4.expressionCBox_2_QComboBox"), QEvent.MouseButtonPress, 156, 22, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(":tab_4.expressionCBox_2_QComboBox"), QEvent.MouseButtonRelease, 156, -15, Qt.LeftButton, 0, 0)
    mouseClick(waitForObjectItem(":tab_4.expressionCBox_2_QComboBox", "Raise Brow"), 108, 6, 0, Qt.LeftButton)
    clickButton(waitForObject(":tab_4.startTrainingBtn_2_QPushButton"))
    openContextMenu(waitForObject(":tab_4.abortTrainingBtn_QPushButton"), 88, 23, 0)
    test.vp("VP2")
    clickButton(waitForObject(":Yes_QPushButton"))
    mouseClick(waitForObjectItem(":tab_4.expressionCBox_2_QComboBox", "Furrow Brow"), 138, 5, 0, Qt.LeftButton)
    clickButton(waitForObject(":tab_4.startTrainingBtn_2_QPushButton"))
    test.vp("VP3")
    clickButton(waitForObject(":Yes_QPushButton"))
    mouseClick(waitForObjectItem(":tab_4.expressionCBox_2_QComboBox", "Smile"), 25, 7, 0, Qt.LeftButton)
    clickButton(waitForObject(":tab_4.startTrainingBtn_2_QPushButton"))
    test.vp("VP4")
    clickButton(waitForObject(":Yes_QPushButton"))
    mouseClick(waitForObjectItem(":tab_4.expressionCBox_2_QComboBox", "Clench"), 71, 9, 0, Qt.LeftButton)
    clickButton(waitForObject(":tab_4.startTrainingBtn_2_QPushButton"))
    test.vp("VP5")
    clickButton(waitForObject(":Yes_QPushButton"))
    mouseClick(waitForObjectItem(":tab_4.expressionCBox_2_QComboBox", "Laugh"), 76, 11, 0, Qt.LeftButton)
    clickButton(waitForObject(":tab_4.startTrainingBtn_2_QPushButton"))
    test.vp("VP6")
    clickButton(waitForObject(":Yes_QPushButton"))
    mouseClick(waitForObjectItem(":tab_4.expressionCBox_2_QComboBox", "Left Smirk"), 74, 11, 0, Qt.LeftButton)
    clickButton(waitForObject(":tab_4.startTrainingBtn_2_QPushButton"))
    test.vp("VP7")
    clickButton(waitForObject(":Yes_QPushButton"))
    mouseClick(waitForObjectItem(":tab_4.expressionCBox_2_QComboBox", "Right Smirk"), 119, 1, 0, Qt.LeftButton)
    clickButton(waitForObject(":tab_4.startTrainingBtn_2_QPushButton"))
    test.vp("VP8")
    clickButton(waitForObject(":Yes_QPushButton"))
