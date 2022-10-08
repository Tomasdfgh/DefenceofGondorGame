from tkinter import *
import time
import os

def startGame():
    global current
    updateMap()
    ResourceTabLabel.place(x = 5,y = 5)
    woodAmountLbl.place(x = 80, y = 41)
    moneyAmountLbl.place(x = 80, y = 11)
    stoneAmountLbl.place(x = 80, y = 70)
    oreAmountLbl.place(x = 80, y = 98)
    castleHealthUseLbl.place(x = 140, y = 136, anchor = "center")
    strongHoldLabel.place(x = 702, y = 720, anchor = "center")
#    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
#    upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
    if slot1Var[0:1] == "E":
        slot1EmptyLabel.place(x = 77, y = 666, anchor = "center")
        lodgeLabel1.pack()
        lodgeLabel1.pack_forget()
        sawMillLabel1.pack()
        sawMillLabel1.pack_forget()
        oreRefineryLabel1.pack()
        oreRefineryLabel1.pack_forget()
        stoneFactoryLabel1.pack()
        stoneFactoryLabel1.pack_forget()
    elif slot1Var[0:1] == "L":
        lodgeLabel1.place(x = 77, y = 666, anchor = "center")
    elif slot1Var[0:1] == "O":
        oreRefineryLabel1.place(x = 77, y = 666, anchor = "center")
    elif slot1Var[0:1] == "W":
        sawMillLabel1.place(x = 77, y = 666, anchor = "center")
    elif slot1Var[0:1] == "S":
        stoneFactoryLabel1.place(x = 77, y = 666, anchor = "center")
    if slot2Var[0:1] == "E":
        slot2EmptyLabel.place(x = 170, y = 395, anchor = "center")
        lodgeLabel2.pack()
        lodgeLabel2.pack_forget()
        sawMillLabel2.pack()
        sawMillLabel2.pack_forget()
        oreRefineryLabel2.pack()
        oreRefineryLabel2.pack_forget()
        stoneFactoryLabel2.pack()
        stoneFactoryLabel2.pack_forget()
    elif slot2Var[0:1] == "L":
        lodgeLabel2.place(x = 170, y = 395, anchor = "center")
    elif slot2Var[0:1] == "O":
        oreRefineryLabel2.place(x = 170, y = 395, anchor = "center")
    elif slot2Var[0:1] == "W":
        sawMillLabel2.place(x = 170, y = 395, anchor = "center")
    elif slot2Var[0:1] == "S":
        stoneFactoryLabel2.place(x = 170, y = 395, anchor = "center")
    if slot3Var[0:1] == "E":
        slot3EmptyLabel.place(x = 322, y = 215, anchor = "center")
        lodgeLabel3.pack()
        lodgeLabel3.pack_forget()
        sawMillLabel3.pack()
        sawMillLabel3.pack_forget()
        oreRefineryLabel3.pack()
        oreRefineryLabel3.pack_forget()
        stoneFactoryLabel3.pack()
        stoneFactoryLabel3.pack_forget()
    elif slot3Var[0:1] == "L":
        lodgeLabel3.place(x = 322, y = 215, anchor = "center")
    elif slot3Var[0:1] == "O":
        oreRefineryLabel3.place(x = 322, y = 215, anchor = "center")
    elif slot3Var[0:1] == "W":
        sawMillLabel3.place(x = 322, y = 215, anchor = "center")
    elif slot3Var[0:1] == "S":
        stoneFactoryLabel3.place(x = 322, y = 215, anchor = "center")
    if slot4Var[0:1] == "E":
        slot4EmptyLabel.place(x = 502, y = 107, anchor = "center")
        lodgeLabel4.pack()
        lodgeLabel4.pack_forget()
        sawMillLabel4.pack()
        sawMillLabel4.pack_forget()
        oreRefineryLabel4.pack()
        oreRefineryLabel4.pack_forget()
        stoneFactoryLabel4.pack()
        stoneFactoryLabel4.pack_forget()
    elif slot4Var[0:1] == "L":
        lodgeLabel4.place(x = 502, y = 107, anchor = "center")
    elif slot4Var[0:1] == "O":
        oreRefineryLabel4.place(x = 502, y = 107, anchor = "center")
    elif slot4Var[0:1] == "W":
        sawMillLabel4.place(x = 502, y = 107, anchor = "center")
    elif slot4Var[0:1] == "S":
        stoneFactoryLabel4.place(x = 502, y = 107, anchor = "center")
    if slot5Var[0:1] == "E":
        slot5EmptyLabel.place(x = 930, y = 111, anchor = "center")
        lodgeLabel5.pack()
        lodgeLabel5.pack_forget()
        sawMillLabel5.pack()
        sawMillLabel5.pack_forget()
        oreRefineryLabel5.pack()
        oreRefineryLabel5.pack_forget()
        stoneFactoryLabel5.pack()
        stoneFactoryLabel5.pack_forget()
    elif slot5Var[0:1] == "L":
        lodgeLabel5.place(x = 930, y = 111, anchor = "center")
    elif slot5Var[0:1] == "O":
        oreRefineryLabel5.place(x = 930, y = 111, anchor = "center")
    elif slot5Var[0:1] == "W":
        sawMillLabel5.place(x = 930, y = 111, anchor = "center")
    elif slot5Var[0:1] == "S":
        stoneFactoryLabel5.place(x = 930, y = 111, anchor = "center")
    if slot6Var[0:1] == "E":
        slot6EmptyLabel.place(x = 1093, y = 217, anchor = "center")
        lodgeLabel6.pack()
        lodgeLabel6.pack_forget()
        sawMillLabel6.pack()
        sawMillLabel6.pack_forget()
        oreRefineryLabel6.pack()
        oreRefineryLabel6.pack_forget()
        stoneFactoryLabel6.pack()
        stoneFactoryLabel6.pack_forget()
    elif slot6Var[0:1] == "L":
        lodgeLabel6.place(x = 1093, y = 217, anchor = "center")
    elif slot6Var[0:1] == "O":
        oreRefineryLabel6.place(x = 1093, y = 217, anchor = "center")
    elif slot6Var[0:1] == "W":
        sawMillLabel6.place(x = 1093, y = 217, anchor = "center")
    elif slot6Var[0:1] == "S":
        stoneFactoryLabel6.place(x = 1093, y = 217, anchor = "center")
    if slot7Var[0:1] == "E":
        slot7EmptyLabel.place(x = 1260, y = 421, anchor = "center")
        lodgeLabel7.pack()
        lodgeLabel7.pack_forget()
        sawMillLabel7.pack()
        sawMillLabel7.pack_forget()
        oreRefineryLabel7.pack()
        oreRefineryLabel7.pack_forget()
        stoneFactoryLabel7.pack()
        stoneFactoryLabel7.pack_forget()
    elif slot7Var[0:1] == "L":
        lodgeLabel7.place(x = 1260, y = 421, anchor = "center")
    elif slot7Var[0:1] == "O":
        oreRefineryLabel7.place(x = 1260, y = 421, anchor = "center")
    elif slot7Var[0:1] == "W":
        sawMillLabel7.place(x = 1260, y = 421, anchor = "center")
    elif slot7Var[0:1] == "S":
        stoneFactoryLabel7.place(x = 1260, y = 421, anchor = "center")
    if slot8Var[0:1] == "E":
        slot8EmptyLabel.place(x = 1340, y = 653, anchor = "center")
        lodgeLabel8.pack()
        lodgeLabel8.pack_forget()
        sawMillLabel8.pack()
        sawMillLabel8.pack_forget()
        oreRefineryLabel8.pack()
        oreRefineryLabel8.pack_forget()
        stoneFactoryLabel8.pack()
        stoneFactoryLabel8.pack_forget()
    elif slot8Var[0:1] == "L":
        lodgeLabel8.place(x = 1340, y = 653, anchor = "center")
    elif slot8Var[0:1] == "O":
        oreRefineryLabel8.place(x = 1340, y = 653, anchor = "center")
    elif slot8Var[0:1] == "W":
        sawMillLabel8.place(x = 1340, y = 653, anchor = "center")
    elif slot8Var[0:1] == "S":
        stoneFactoryLabel8.place(x = 1340, y = 653, anchor = "center")
    if slot9Var[0:1] == "E":
        slot9EmptyLabel.place(x = 202, y = 650, anchor = "center")
        lodgeLabel9.pack()
        lodgeLabel9.pack_forget()
        sawMillLabel9.pack()
        sawMillLabel9.pack_forget()
        oreRefineryLabel9.pack()
        oreRefineryLabel9.pack_forget()
        stoneFactoryLabel9.pack()
        stoneFactoryLabel9.pack_forget()
    elif slot9Var[0:1] == "L":
        lodgeLabel9.place(x = 202, y = 650, anchor = "center")
    elif slot9Var[0:1] == "O":
        oreRefineryLabel9.place(x = 202, y = 650, anchor = "center")
    elif slot9Var[0:1] == "W":
        sawMillLabel9.place(x = 202, y = 650, anchor = "center")
    elif slot9Var[0:1] == "S":
        stoneFactoryLabel9.place(x = 202, y = 650, anchor = "center")
    if slot10Var[0:1] == "E":
        slot10EmptyLabel.place(x = 282, y = 433, anchor = "center")
        lodgeLabel10.pack()
        lodgeLabel10.pack_forget()
        sawMillLabel10.pack()
        sawMillLabel10.pack_forget()
        oreRefineryLabel10.pack()
        oreRefineryLabel10.pack_forget()
        stoneFactoryLabel10.pack()
        stoneFactoryLabel10.pack_forget()
    elif slot10Var[0:1] == "L":
        lodgeLabel10.place(x = 282, y = 433, anchor = "center")
    elif slot10Var[0:1] == "O":
        oreRefineryLabel10.place(x = 282, y = 433, anchor = "center")
    elif slot10Var[0:1] == "W":
        sawMillLabel10.place(x = 282, y = 433, anchor = "center")
    elif slot10Var[0:1] == "S":
        stoneFactoryLabel10.place(x = 282, y = 433, anchor = "center")
    if slot11Var[0:1] == "E":
        slot11EmptyLabel.place(x = 418, y = 283, anchor = "center")
        lodgeLabel11.pack()
        lodgeLabel11.pack_forget()
        sawMillLabel11.pack()
        sawMillLabel11.pack_forget()
        oreRefineryLabel11.pack()
        oreRefineryLabel11.pack_forget()
        stoneFactoryLabel11.pack()
        stoneFactoryLabel11.pack_forget()
    elif slot11Var[0:1] == "L":
        lodgeLabel11.place(x = 418, y = 283, anchor = "center")
    elif slot11Var[0:1] == "O":
        oreRefineryLabel11.place(x = 418, y = 283, anchor = "center")
    elif slot11Var[0:1] == "W":
        sawMillLabel11.place(x = 418, y = 283, anchor = "center")
    elif slot11Var[0:1] == "S":
        stoneFactoryLabel11.place(x = 418, y = 283, anchor = "center")
    if slot12Var[0:1] == "E":
        slot12EmptyLabel.place(x = 553, y = 209, anchor = "center")
        lodgeLabel12.pack()
        lodgeLabel12.pack_forget()
        sawMillLabel12.pack()
        sawMillLabel12.pack_forget()
        oreRefineryLabel12.pack()
        oreRefineryLabel12.pack_forget()
        stoneFactoryLabel12.pack()
        stoneFactoryLabel12.pack_forget()
    elif slot12Var[0:1] == "L":
        lodgeLabel12.place(x = 553, y = 209, anchor = "center")
    elif slot12Var[0:1] == "O":
        oreRefineryLabel12.place(x = 553, y = 209, anchor = "center")
    elif slot12Var[0:1] == "W":
        sawMillLabel12.place(x = 553, y = 209, anchor = "center")
    elif slot12Var[0:1] == "S":
        stoneFactoryLabel12.place(x = 553, y = 209, anchor = "center")
    if slot13Var[0:1] == "E":
        slot13EmptyLabel.place(x = 894, y = 222, anchor = "center")
        lodgeLabel13.pack()
        lodgeLabel13.pack_forget()
        sawMillLabel13.pack()
        sawMillLabel13.pack_forget()
        oreRefineryLabel13.pack()
        oreRefineryLabel13.pack_forget()
        stoneFactoryLabel13.pack()
        stoneFactoryLabel13.pack_forget()
    elif slot13Var[0:1] == "L":
        lodgeLabel13.place(x = 894, y = 222, anchor = "center")
    elif slot13Var[0:1] == "O":
        oreRefineryLabel13.place(x = 894, y = 222, anchor = "center")
    elif slot13Var[0:1] == "W":
        sawMillLabel13.place(x = 894, y = 222, anchor = "center")
    elif slot13Var[0:1] == "S":
        stoneFactoryLabel13.place(x = 894, y = 222, anchor = "center")
    if slot14Var[0:1] == "E":
        slot14EmptyLabel.place(x = 1035, y = 317, anchor = "center")
        lodgeLabel14.pack()
        lodgeLabel14.pack_forget()
        sawMillLabel14.pack()
        sawMillLabel14.pack_forget()
        oreRefineryLabel14.pack()
        oreRefineryLabel14.pack_forget()
        stoneFactoryLabel14.pack()
        stoneFactoryLabel14.pack_forget()
    elif slot14Var[0:1] == "L":
        lodgeLabel14.place(x = 1035, y = 317, anchor = "center")
    elif slot14Var[0:1] == "O":
        oreRefineryLabel14.place(x = 1035, y = 317, anchor = "center")
    elif slot14Var[0:1] == "W":
        sawMillLabel14.place(x = 1035, y = 317, anchor = "center")
    elif slot14Var[0:1] == "S":
        stoneFactoryLabel14.place(x = 1035, y = 317, anchor = "center")
    if slot15Var[0:1] == "E":
        slot15EmptyLabel.place(x = 1152, y = 469, anchor = "center")
        lodgeLabel15.pack()
        lodgeLabel15.pack_forget()
        sawMillLabel15.pack()
        sawMillLabel15.pack_forget()
        oreRefineryLabel15.pack()
        oreRefineryLabel15.pack_forget()
        stoneFactoryLabel15.pack()
        stoneFactoryLabel15.pack_forget()
    elif slot15Var[0:1] == "L":
        lodgeLabel15.place(x = 1152, y = 469, anchor = "center")
    elif slot15Var[0:1] == "O":
        oreRefineryLabel15.place(x = 1152, y = 469, anchor = "center")
    elif slot15Var[0:1] == "W":
        sawMillLabel15.place(x = 1152, y = 469, anchor = "center")
    elif slot15Var[0:1] == "S":
        stoneFactoryLabel15.place(x = 1152, y = 469, anchor = "center")
    if slot16Var[0:1] == "E":
        slot16EmptyLabel.place(x = 1209, y = 659, anchor = "center")
        lodgeLabel16.pack()
        lodgeLabel16.pack_forget()
        sawMillLabel16.pack()
        sawMillLabel16.pack_forget()
        oreRefineryLabel16.pack()
        oreRefineryLabel16.pack_forget()
        stoneFactoryLabel16.pack()
        stoneFactoryLabel16.pack_forget()
    elif slot16Var[0:1] == "L":
        lodgeLabel16.place(x = 1209, y = 659, anchor = "center")
    elif slot16Var[0:1] == "O":
        oreRefineryLabel16.place(x = 1209, y = 659, anchor = "center")
    elif slot16Var[0:1] == "W":
        sawMillLabel16.place(x = 1209, y = 659, anchor = "center")
    elif slot16Var[0:1] == "S":
        stoneFactoryLabel16.place(x = 1209, y = 659, anchor = "center")
    if slot17Var[0:1] == "E":
        slot17EmptyLabel.place(x = 316, y = 652, anchor = "center")
        lodgeLabel17.pack()
        lodgeLabel17.pack_forget()
        sawMillLabel17.pack()
        sawMillLabel17.pack_forget()
        oreRefineryLabel17.pack()
        oreRefineryLabel17.pack_forget()
        stoneFactoryLabel17.pack()
        stoneFactoryLabel17.pack_forget()
    elif slot17Var[0:1] == "L":
        lodgeLabel17.place(x = 316, y = 652, anchor = "center")
    elif slot17Var[0:1] == "O":
        oreRefineryLabel17.place(x = 316, y = 652, anchor = "center")
    elif slot17Var[0:1] == "W":
        sawMillLabel17.place(x = 316, y = 652, anchor = "center")
    elif slot17Var[0:1] == "S":
        stoneFactoryLabel17.place(x = 316, y = 652, anchor = "center")
    if slot18Var[0:1] == "E":
        slot18EmptyLabel.place(x = 383, y = 492, anchor = "center")
        lodgeLabel18.pack()
        lodgeLabel18.pack_forget()
        sawMillLabel18.pack()
        sawMillLabel18.pack_forget()
        oreRefineryLabel18.pack()
        oreRefineryLabel18.pack_forget()
        stoneFactoryLabel18.pack()
        stoneFactoryLabel18.pack_forget()
    elif slot18Var[0:1] == "L":
        lodgeLabel18.place(x = 383, y = 492, anchor = "center")
    elif slot18Var[0:1] == "O":
        oreRefineryLabel18.place(x = 383, y = 492, anchor = "center")
    elif slot18Var[0:1] == "W":
        sawMillLabel18.place(x = 383, y = 492, anchor = "center")
    elif slot18Var[0:1] == "S":
        stoneFactoryLabel18.place(x = 383, y = 492, anchor = "center")
    if slot19Var[0:1] == "E":
        slot19EmptyLabel.place(x = 503, y = 368, anchor = "center")
        lodgeLabel19.pack()
        lodgeLabel19.pack_forget()
        sawMillLabel19.pack()
        sawMillLabel19.pack_forget()
        oreRefineryLabel19.pack()
        oreRefineryLabel19.pack_forget()
        stoneFactoryLabel19.pack()
        stoneFactoryLabel19.pack_forget()
    elif slot19Var[0:1] == "L":
        lodgeLabel19.place(x = 503, y = 368, anchor = "center")
    elif slot19Var[0:1] == "O":
        oreRefineryLabel19.place(x = 503, y = 368, anchor = "center")
    elif slot19Var[0:1] == "W":
        sawMillLabel19.place(x = 503, y = 368, anchor = "center")
    elif slot19Var[0:1] == "S":
        stoneFactoryLabel19.place(x = 503, y = 368, anchor = "center")
    if slot20Var[0:1] == "E":
        slot20EmptyLabel.place(x = 924, y = 374, anchor = "center")
        lodgeLabel20.pack()
        lodgeLabel20.pack_forget()
        sawMillLabel20.pack()
        sawMillLabel20.pack_forget()
        oreRefineryLabel20.pack()
        oreRefineryLabel20.pack_forget()
        stoneFactoryLabel20.pack()
        stoneFactoryLabel20.pack_forget()
    elif slot20Var[0:1] == "L":
        lodgeLabel20.place(x = 924, y = 374, anchor = "center")
    elif slot20Var[0:1] == "O":
        oreRefineryLabel20.place(x = 924, y = 374, anchor = "center")
    elif slot20Var[0:1] == "W":
        sawMillLabel20.place(x = 924, y = 374, anchor = "center")
    elif slot20Var[0:1] == "S":
        stoneFactoryLabel20.place(x = 924, y = 374, anchor = "center")
    if slot21Var[0:1] == "E":
        slot21EmptyLabel.place(x = 1042, y = 505, anchor = "center")
        lodgeLabel21.pack()
        lodgeLabel21.pack_forget()
        sawMillLabel21.pack()
        sawMillLabel21.pack_forget()
        oreRefineryLabel21.pack()
        oreRefineryLabel21.pack_forget()
        stoneFactoryLabel21.pack()
        stoneFactoryLabel21.pack_forget()
    elif slot21Var[0:1] == "L":
        lodgeLabel21.place(x = 1042, y = 505, anchor = "center")
    elif slot21Var[0:1] == "O":
        oreRefineryLabel21.place(x = 1042, y = 505, anchor = "center")
    elif slot21Var[0:1] == "W":
        sawMillLabel21.place(x = 1042, y = 505, anchor = "center")
    elif slot21Var[0:1] == "S":
        stoneFactoryLabel21.place(x = 1042, y = 505, anchor = "center")
    if slot22Var[0:1] == "E":
        slot22EmptyLabel.place(x = 1100, y = 660, anchor = "center")
        lodgeLabel22.pack()
        lodgeLabel22.pack_forget()
        sawMillLabel22.pack()
        sawMillLabel22.pack_forget()
        oreRefineryLabel22.pack()
        oreRefineryLabel22.pack_forget()
        stoneFactoryLabel22.pack()
        stoneFactoryLabel22.pack_forget()
    elif slot22Var[0:1] == "L":
        lodgeLabel22.place(x = 1100, y = 660, anchor = "center")
    elif slot22Var[0:1] == "O":
        oreRefineryLabel22.place(x = 1100, y = 660, anchor = "center")
    elif slot22Var[0:1] == "W":
        sawMillLabel22.place(x = 1100, y = 660, anchor = "center")
    elif slot22Var[0:1] == "S":
        stoneFactoryLabel22.place(x = 1100, y = 660, anchor = "center")
    if slot23Var[0:1] == "E":
        slot23EmptyLabel.place(x = 427, y = 674, anchor = "center")
        lodgeLabel23.pack()
        lodgeLabel23.pack_forget()
        sawMillLabel23.pack()
        sawMillLabel23.pack_forget()
        oreRefineryLabel23.pack()
        oreRefineryLabel23.pack_forget()
        stoneFactoryLabel23.pack()
        stoneFactoryLabel23.pack_forget()
    elif slot23Var[0:1] == "L":
        lodgeLabel23.place(x = 427, y = 674, anchor = "center")
    elif slot23Var[0:1] == "O":
        oreRefineryLabel23.place(x = 427, y = 674, anchor = "center")
    elif slot23Var[0:1] == "W":
        sawMillLabel23.place(x = 427, y = 674, anchor = "center")
    elif slot23Var[0:1] == "S":
        stoneFactoryLabel23.place(x = 427, y = 674, anchor = "center")
    if slot24Var[0:1] == "E":
        slot24EmptyLabel.place(x = 980, y = 645, anchor = "center")
        lodgeLabel24.pack()
        lodgeLabel24.pack_forget()
        sawMillLabel24.pack()
        sawMillLabel24.pack_forget()
        oreRefineryLabel24.pack()
        oreRefineryLabel24.pack_forget()
        stoneFactoryLabel24.pack()
        stoneFactoryLabel24.pack_forget()
    elif slot24Var[0:1] == "L":
        lodgeLabel24.place(x = 980, y = 645, anchor = "center")
    elif slot24Var[0:1] == "O":
        oreRefineryLabel24.place(x = 980, y = 645, anchor = "center")
    elif slot24Var[0:1] == "W":
        sawMillLabel24.place(x = 980, y = 645, anchor = "center")
    elif slot24Var[0:1] == "S":
        stoneFactoryLabel24.place(x = 980, y = 645, anchor = "center")
    nextButton.place(x = 1475, y = 100, anchor = "center")
    strongHoldButton.place(x = 1475, y = 200, anchor = "center")
    backButton.place(x = 1475, y = 300, anchor = "center")
    wallButton.place(x = 1475, y = 400, anchor = "center")
    nextDayButton.place(x = 1475, y = 700, anchor = "center")
    troopsButton.place(x = 1475, y = 500, anchor = "center")
    menuButton.place(x = 1475, y = 600, anchor = "center")
    dayLbl.place(x = 1300, y = 25, anchor = "center")
    if current > 25:
        current = 2
    if current == 2:
        slotDestruct()
        slot1()
    if current == 3:
        slotDestruct()
        slot2()
    if current == 4:
        slotDestruct()
        slot3()
    if current == 5:
        slotDestruct()
        slot4()
    if current == 6:
        slotDestruct()
        slot5()
    if current == 7:
        slotDestruct()
        slot6()
    if current == 8:
        slotDestruct()
        slot7()
    if current == 9:
        slotDestruct()
        slot8()
    if current == 10:
        slotDestruct()
        slot9()
    if current == 11:
        slotDestruct()
        slot10()
    if current == 12:
        slotDestruct()
        slot11()
    if current == 13:
        slotDestruct()
        slot12()
    if current == 14:
        slotDestruct()
        slot13()
    if current == 15:
        slotDestruct()
        slot14()
    if current == 16:
        slotDestruct()
        slot15()
    if current == 17:
        slotDestruct()
        slot16()
    if current == 18:
        slotDestruct()
        slot17()
    if current == 19:
        slotDestruct()
        slot18()
    if current == 20:
        slotDestruct()
        slot19()
    if current == 21:
        slotDestruct()
        slot20()
    if current == 22:
        slotDestruct()
        slot21()
    if current == 23:
        slotDestruct()
        slot22()
    if current == 24:
        slotDestruct()
        slot23()
    if current == 25:
        slotDestruct()
        slot24()

def runNextSlot():
    global current
    current += 1
    startGame()

def slotDestruct():
    buildingOptionsLabel.pack()
    buildingOptionsLabel.pack_forget()
    slot1EmptySelectedLabel.pack()
    slot1EmptySelectedLabel.pack_forget()
    slot2EmptySelectedLabel.pack()
    slot2EmptySelectedLabel.pack_forget()
    slot3EmptySelectedLabel.pack()
    slot3EmptySelectedLabel.pack_forget()
    slot4EmptySelectedLabel.pack()
    slot4EmptySelectedLabel.pack_forget()
    slot5EmptySelectedLabel.pack()
    slot5EmptySelectedLabel.pack_forget()
    slot6EmptySelectedLabel.pack()
    slot6EmptySelectedLabel.pack_forget()
    slot7EmptySelectedLabel.pack()
    slot7EmptySelectedLabel.pack_forget()
    slot8EmptySelectedLabel.pack()
    slot8EmptySelectedLabel.pack_forget()
    slot9EmptySelectedLabel.pack()
    slot9EmptySelectedLabel.pack_forget()
    slot10EmptySelectedLabel.pack()
    slot10EmptySelectedLabel.pack_forget()
    slot11EmptySelectedLabel.pack()
    slot11EmptySelectedLabel.pack_forget()
    slot12EmptySelectedLabel.pack()
    slot12EmptySelectedLabel.pack_forget()
    slot13EmptySelectedLabel.pack()
    slot13EmptySelectedLabel.pack_forget()
    slot14EmptySelectedLabel.pack()
    slot14EmptySelectedLabel.pack_forget()
    slot15EmptySelectedLabel.pack()
    slot15EmptySelectedLabel.pack_forget()
    slot16EmptySelectedLabel.pack()
    slot16EmptySelectedLabel.pack_forget()
    slot17EmptySelectedLabel.pack()
    slot17EmptySelectedLabel.pack_forget()
    slot18EmptySelectedLabel.pack()
    slot18EmptySelectedLabel.pack_forget()
    slot19EmptySelectedLabel.pack()
    slot19EmptySelectedLabel.pack_forget()
    slot20EmptySelectedLabel.pack()
    slot20EmptySelectedLabel.pack_forget()
    slot21EmptySelectedLabel.pack()
    slot21EmptySelectedLabel.pack_forget()
    slot22EmptySelectedLabel.pack()
    slot22EmptySelectedLabel.pack_forget()
    slot23EmptySelectedLabel.pack()
    slot23EmptySelectedLabel.pack_forget()
    slot24EmptySelectedLabel.pack()
    slot24EmptySelectedLabel.pack_forget()
    lodgeButton.pack()
    lodgeButton.pack_forget()
    lodgeClicked1.pack()
    lodgeClicked1.pack_forget()
    lodgeClicked2.pack()
    lodgeClicked2.pack_forget()
    lodgeClicked3.pack()
    lodgeClicked3.pack_forget()
    lodgeClicked4.pack()
    lodgeClicked4.pack_forget()
    lodgeClicked5.pack()
    lodgeClicked5.pack_forget()
    lodgeClicked6.pack()
    lodgeClicked6.pack_forget()
    lodgeClicked7.pack()
    lodgeClicked7.pack_forget()
    lodgeClicked8.pack()
    lodgeClicked8.pack_forget()
    lodgeClicked9.pack()
    lodgeClicked9.pack_forget()
    lodgeClicked10.pack()
    lodgeClicked10.pack_forget()
    lodgeClicked11.pack()
    lodgeClicked11.pack_forget()
    lodgeClicked12.pack()
    lodgeClicked12.pack_forget()
    lodgeClicked13.pack()
    lodgeClicked13.pack_forget()
    lodgeClicked14.pack()
    lodgeClicked14.pack_forget()
    lodgeClicked15.pack()
    lodgeClicked15.pack_forget()
    lodgeClicked16.pack()
    lodgeClicked16.pack_forget()
    lodgeClicked17.pack()
    lodgeClicked17.pack_forget()
    lodgeClicked18.pack()
    lodgeClicked18.pack_forget()
    lodgeClicked19.pack()
    lodgeClicked19.pack_forget()
    lodgeClicked20.pack()
    lodgeClicked20.pack_forget()
    lodgeClicked21.pack()
    lodgeClicked21.pack_forget()
    lodgeClicked22.pack()
    lodgeClicked22.pack_forget()
    lodgeClicked23.pack()
    lodgeClicked23.pack_forget()
    lodgeClicked24.pack()
    lodgeClicked24.pack_forget()
    strongHoldClickedLabel.pack()
    strongHoldClickedLabel.pack_forget()
    strongHoldInfoLabel.pack()
    strongHoldInfoLabel.pack_forget()
    strongHoldLvlUseLbl.pack()
    strongHoldLvlUseLbl.pack_forget()
    strongHoldUpgradeButton.pack()
    strongHoldUpgradeButton.pack_forget()
    oreRefineryButton.pack()
    oreRefineryButton.pack_forget()
    oreRefineryClickedOnLabel1.pack()
    oreRefineryClickedOnLabel1.pack_forget()
    oreRefineryClickedOnLabel2.pack()
    oreRefineryClickedOnLabel2.pack_forget()
    oreRefineryClickedOnLabel3.pack()
    oreRefineryClickedOnLabel3.pack_forget()
    oreRefineryClickedOnLabel4.pack()
    oreRefineryClickedOnLabel4.pack_forget()
    oreRefineryClickedOnLabel5.pack()
    oreRefineryClickedOnLabel5.pack_forget()
    oreRefineryClickedOnLabel6.pack()
    oreRefineryClickedOnLabel6.pack_forget()
    oreRefineryClickedOnLabel7.pack()
    oreRefineryClickedOnLabel7.pack_forget()
    oreRefineryClickedOnLabel8.pack()
    oreRefineryClickedOnLabel8.pack_forget()
    oreRefineryClickedOnLabel9.pack()
    oreRefineryClickedOnLabel9.pack_forget()
    oreRefineryClickedOnLabel10.pack()
    oreRefineryClickedOnLabel10.pack_forget()
    oreRefineryClickedOnLabel11.pack()
    oreRefineryClickedOnLabel11.pack_forget()
    oreRefineryClickedOnLabel12.pack()
    oreRefineryClickedOnLabel12.pack_forget()
    oreRefineryClickedOnLabel13.pack()
    oreRefineryClickedOnLabel13.pack_forget()
    oreRefineryClickedOnLabel14.pack()
    oreRefineryClickedOnLabel14.pack_forget()
    oreRefineryClickedOnLabel15.pack()
    oreRefineryClickedOnLabel15.pack_forget()
    oreRefineryClickedOnLabel16.pack()
    oreRefineryClickedOnLabel16.pack_forget()
    oreRefineryClickedOnLabel17.pack()
    oreRefineryClickedOnLabel17.pack_forget()
    oreRefineryClickedOnLabel18.pack()
    oreRefineryClickedOnLabel18.pack_forget()
    oreRefineryClickedOnLabel19.pack()
    oreRefineryClickedOnLabel19.pack_forget()
    oreRefineryClickedOnLabel20.pack()
    oreRefineryClickedOnLabel20.pack_forget()
    oreRefineryClickedOnLabel21.pack()
    oreRefineryClickedOnLabel21.pack_forget()
    oreRefineryClickedOnLabel22.pack()
    oreRefineryClickedOnLabel22.pack_forget()
    oreRefineryClickedOnLabel23.pack()
    oreRefineryClickedOnLabel23.pack_forget()
    oreRefineryClickedOnLabel24.pack()
    oreRefineryClickedOnLabel24.pack_forget()
    stoneFactoryButton.pack()
    stoneFactoryButton.pack_forget()
    sawMillButton.pack()
    sawMillButton.pack_forget()
    stoneFactoryButton.pack()
    stoneFactoryButton.pack_forget()
    stoneFactoryClickedOnLabel1.pack()
    stoneFactoryClickedOnLabel1.pack_forget()
    stoneFactoryClickedOnLabel2.pack()
    stoneFactoryClickedOnLabel2.pack_forget()
    stoneFactoryClickedOnLabel3.pack()
    stoneFactoryClickedOnLabel3.pack_forget()
    stoneFactoryClickedOnLabel4.pack()
    stoneFactoryClickedOnLabel4.pack_forget()
    stoneFactoryClickedOnLabel5.pack()
    stoneFactoryClickedOnLabel5.pack_forget()
    stoneFactoryClickedOnLabel6.pack()
    stoneFactoryClickedOnLabel6.pack_forget()
    stoneFactoryClickedOnLabel7.pack()
    stoneFactoryClickedOnLabel7.pack_forget()
    stoneFactoryClickedOnLabel8.pack()
    stoneFactoryClickedOnLabel8.pack_forget()
    stoneFactoryClickedOnLabel9.pack()
    stoneFactoryClickedOnLabel9.pack_forget()
    stoneFactoryClickedOnLabel10.pack()
    stoneFactoryClickedOnLabel10.pack_forget()
    stoneFactoryClickedOnLabel11.pack()
    stoneFactoryClickedOnLabel11.pack_forget()
    stoneFactoryClickedOnLabel12.pack()
    stoneFactoryClickedOnLabel12.pack_forget()
    stoneFactoryClickedOnLabel13.pack()
    stoneFactoryClickedOnLabel13.pack_forget()
    stoneFactoryClickedOnLabel14.pack()
    stoneFactoryClickedOnLabel14.pack_forget()
    stoneFactoryClickedOnLabel15.pack()
    stoneFactoryClickedOnLabel15.pack_forget()
    stoneFactoryClickedOnLabel16.pack()
    stoneFactoryClickedOnLabel16.pack_forget()
    stoneFactoryClickedOnLabel17.pack()
    stoneFactoryClickedOnLabel17.pack_forget()
    stoneFactoryClickedOnLabel18.pack()
    stoneFactoryClickedOnLabel18.pack_forget()
    stoneFactoryClickedOnLabel19.pack()
    stoneFactoryClickedOnLabel19.pack_forget()
    stoneFactoryClickedOnLabel20.pack()
    stoneFactoryClickedOnLabel20.pack_forget()
    stoneFactoryClickedOnLabel21.pack()
    stoneFactoryClickedOnLabel21.pack_forget()
    stoneFactoryClickedOnLabel22.pack()
    stoneFactoryClickedOnLabel22.pack_forget()
    stoneFactoryClickedOnLabel23.pack()
    stoneFactoryClickedOnLabel23.pack_forget()
    stoneFactoryClickedOnLabel24.pack()
    stoneFactoryClickedOnLabel24.pack_forget()
    sawMillClickedOnLabel1.pack()
    sawMillClickedOnLabel1.pack_forget()
    sawMillClickedOnLabel2.pack()
    sawMillClickedOnLabel2.pack_forget()
    sawMillClickedOnLabel3.pack()
    sawMillClickedOnLabel3.pack_forget()
    sawMillClickedOnLabel4.pack()
    sawMillClickedOnLabel4.pack_forget()
    sawMillClickedOnLabel5.pack()
    sawMillClickedOnLabel5.pack_forget()
    sawMillClickedOnLabel6.pack()
    sawMillClickedOnLabel6.pack_forget()
    sawMillClickedOnLabel7.pack()
    sawMillClickedOnLabel7.pack_forget()
    sawMillClickedOnLabel8.pack()
    sawMillClickedOnLabel8.pack_forget()
    sawMillClickedOnLabel9.pack()
    sawMillClickedOnLabel9.pack_forget()
    sawMillClickedOnLabel10.pack()
    sawMillClickedOnLabel10.pack_forget()
    sawMillClickedOnLabel11.pack()
    sawMillClickedOnLabel11.pack_forget()
    sawMillClickedOnLabel12.pack()
    sawMillClickedOnLabel12.pack_forget()
    sawMillClickedOnLabel13.pack()
    sawMillClickedOnLabel13.pack_forget()
    sawMillClickedOnLabel14.pack()
    sawMillClickedOnLabel14.pack_forget()
    sawMillClickedOnLabel15.pack()
    sawMillClickedOnLabel15.pack_forget()
    sawMillClickedOnLabel16.pack()
    sawMillClickedOnLabel16.pack_forget()
    sawMillClickedOnLabel17.pack()
    sawMillClickedOnLabel17.pack_forget()
    sawMillClickedOnLabel18.pack()
    sawMillClickedOnLabel18.pack_forget()
    sawMillClickedOnLabel19.pack()
    sawMillClickedOnLabel19.pack_forget()
    sawMillClickedOnLabel20.pack()
    sawMillClickedOnLabel20.pack_forget()
    sawMillClickedOnLabel21.pack()
    sawMillClickedOnLabel21.pack_forget()
    sawMillClickedOnLabel22.pack()
    sawMillClickedOnLabel22.pack_forget()
    sawMillClickedOnLabel23.pack()
    sawMillClickedOnLabel23.pack_forget()
    sawMillClickedOnLabel24.pack()
    sawMillClickedOnLabel24.pack_forget()
    lodgeInfo.pack()
    lodgeInfo.pack_forget()
    oreRefineryInfo.pack()
    oreRefineryInfo.pack_forget()
    stoneFactoryInfo.pack()
    stoneFactoryInfo.pack_forget()
    sawMillInfo.pack()
    sawMillInfo.pack_forget()
    slot1LvlLbl.pack()
    slot1LvlLbl.pack_forget()
    slot2LvlLbl.pack()
    slot2LvlLbl.pack_forget()
    slot3LvlLbl.pack()
    slot3LvlLbl.pack_forget()
    slot4LvlLbl.pack()
    slot4LvlLbl.pack_forget()
    slot5LvlLbl.pack()
    slot5LvlLbl.pack_forget()
    slot6LvlLbl.pack()
    slot6LvlLbl.pack_forget()
    slot7LvlLbl.pack()
    slot7LvlLbl.pack_forget()
    slot8LvlLbl.pack()
    slot8LvlLbl.pack_forget()
    slot9LvlLbl.pack()
    slot9LvlLbl.pack_forget()
    slot10LvlLbl.pack()
    slot10LvlLbl.pack_forget()
    slot11LvlLbl.pack()
    slot11LvlLbl.pack_forget()
    slot12LvlLbl.pack()
    slot12LvlLbl.pack_forget()
    slot13LvlLbl.pack()
    slot13LvlLbl.pack_forget()
    slot14LvlLbl.pack()
    slot14LvlLbl.pack_forget()
    slot15LvlLbl.pack()
    slot15LvlLbl.pack_forget()
    slot16LvlLbl.pack()
    slot16LvlLbl.pack_forget()
    slot17LvlLbl.pack()
    slot17LvlLbl.pack_forget()
    slot18LvlLbl.pack()
    slot18LvlLbl.pack_forget()
    slot19LvlLbl.pack()
    slot19LvlLbl.pack_forget()
    slot20LvlLbl.pack()
    slot20LvlLbl.pack_forget()
    slot21LvlLbl.pack()
    slot21LvlLbl.pack_forget()
    slot22LvlLbl.pack()
    slot22LvlLbl.pack_forget()
    slot23LvlLbl.pack()
    slot23LvlLbl.pack_forget()
    slot24LvlLbl.pack()
    slot24LvlLbl.pack_forget()

    otherUpgradeButton.pack()
    otherUpgradeButton.pack_forget()
    wallClickedLabel.pack()
    wallClickedLabel.pack_forget()
    wallInfoLabel.pack()
    wallInfoLabel.pack_forget()

    troopsSelectionLabel.pack()
    troopsSelectionLabel.pack_forget()

    wallLvlLbl.pack()
    wallLvlLbl.pack_forget()

    wallDefenseLbl.pack()
    wallDefenseLbl.pack_forget()
    wallUpgradeButton.pack()
    wallUpgradeButton.pack_forget()

    wallHealButton.pack()
    wallHealButton.pack_forget()

    demolishButton.pack()
    demolishButton.pack_forget()
    cavalryLbl.pack()
    cavalryLbl.pack_forget()
    swordsMenLbl.pack()
    swordsMenLbl.pack_forget()
    spearMenLbl.pack()
    spearMenLbl.pack_forget()
    archersLbl.pack()
    archersLbl.pack_forget()
    archersLbl.pack()
    archersLbl.pack_forget()

    trainOneCavalryButton.pack()
    trainOneCavalryButton.pack_forget()
    trainOneSwordsMenButton.pack()
    trainOneSwordsMenButton.pack_forget()
    trainOneSpearMenButton.pack()
    trainOneSpearMenButton.pack_forget()
    trainOneArchersButton.pack()
    trainOneArchersButton.pack_forget()

    trainOneHundredCavalryButton.pack()
    trainOneHundredCavalryButton.pack_forget()
    trainOneHundredSwordsMenButton.pack()
    trainOneHundredSwordsMenButton.pack_forget()
    trainOneHundredSpearMenButton.pack()
    trainOneHundredSpearMenButton.pack_forget()
    trainOneHundredArchersButton.pack()
    trainOneHundredArchersButton.pack_forget()

    trainOneThousandCavalryButton.pack()
    trainOneThousandCavalryButton.pack_forget()
    trainOneThousandSwordsMenButton.pack()
    trainOneThousandSwordsMenButton.pack_forget()
    trainOneThousandSpearMenButton.pack()
    trainOneThousandSpearMenButton.pack_forget()
    trainOneThousandArchersButton.pack()
    trainOneThousandArchersButton.pack_forget()

    totalTroopsLbl.pack()
    totalTroopsLbl.pack_forget()

    productionUseLbl.pack()
    productionUseLbl.pack_forget()

    gold_upgradeLbl.pack()
    gold_upgradeLbl.pack_forget()
    wood_upgradeLbl.pack()
    wood_upgradeLbl.pack_forget()
    ore_upgradeLbl.pack()
    ore_upgradeLbl.pack_forget()
    stone_upgradeLbl.pack()
    stone_upgradeLbl.pack_forget()

    gold_healLbl.pack()
    gold_healLbl.pack_forget()
    ore_healLbl.pack()
    ore_healLbl.pack_forget()
    wood_healLbl.pack()
    wood_healLbl.pack_forget()
    stone_healLbl.pack()
    stone_healLbl.pack_forget()

    battleReportLabel.pack()
    battleReportLabel.pack_forget()

    trollsLbl.pack()
    trollsLbl.pack_forget()
    urukhaiLbl.pack()
    urukhaiLbl.pack_forget()
    mordorOrcsLbl.pack()
    mordorOrcsLbl.pack_forget()
    GoblinsLbl.pack()
    GoblinsLbl.pack_forget()

    cavalryBeforeLbl.pack()
    cavalryBeforeLbl.pack_forget()
    swordsMenBeforeLbl.pack()
    swordsMenBeforeLbl.pack_forget()
    spearMenBeforeLbl.pack()
    spearMenBeforeLbl.pack_forget()
    archersBeforeLbl.pack()
    archersBeforeLbl.pack_forget()
    trollsafterLbl.pack()
    trollsafterLbl.pack_forget()
    urukhaiafterLbl.pack()
    urukhaiafterLbl.pack_forget()
    mordorOrcsafterLbl.pack()
    mordorOrcsafterLbl.pack_forget()
    GoblinsafterLbl.pack()
    GoblinsafterLbl.pack_forget()
    healthlossLbl.pack()
    healthlossLbl.pack_forget()
    troopsLostLbl.pack()
    troopsLostLbl.pack_forget()
    enemyKilledLbl.pack()
    enemyKilledLbl.pack_forget()

def slot1():
    if slot1Var[0:1] == "E":
        slot1EmptySelectedLabel.place(x = 77, y = 666, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot1Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot1Var[0:1] == "L":
        lodgeClicked1.place(x = 77, y = 666, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot1LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")


    if slot1Var[0:1] == "O":
        oreRefineryClickedOnLabel1.place(x = 77, y = 666, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot1LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot1Var[0:1] == "S":
        stoneFactoryClickedOnLabel1.place(x = 77, y = 666, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot1LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot1Var[0:1] == "W":
        sawMillClickedOnLabel1.place(x = 77, y = 666, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot1LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot2():
    if slot2Var[0:1] == "E":
        slot2EmptySelectedLabel.place(x = 170, y = 395, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot2Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot2Var[0:1] == "L":
        lodgeClicked2.place(x = 170, y = 395, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot2LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot2Var[0:1] == "O":
        oreRefineryClickedOnLabel1.place(x = 170, y = 395, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot2LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot2Var[0:1] == "S":
        stoneFactoryClickedOnLabel2.place(x = 170, y = 395, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot2LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")


    if slot2Var[0:1] == "W":
        sawMillClickedOnLabel2.place(x = 170, y = 395, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot2LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot3():
    if slot3Var[0:1] == "E":
        slot3EmptySelectedLabel.place(x = 322, y = 215, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot3Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot3Var[0:1] == "L":
        lodgeClicked3.place(x = 322, y = 215, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot3LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot3Var[0:1] == "O":
        oreRefineryClickedOnLabel3.place(x = 322, y = 215, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot3LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot3Var[0:1] == "S":
        stoneFactoryClickedOnLabel3.place(x = 322, y = 215, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot3LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")


    if slot3Var[0:1] == "W":
        sawMillClickedOnLabel3.place(x = 322, y = 215, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot3LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot4():
    if slot4Var[0:1] == "E":
        slot4EmptySelectedLabel.place(x = 502, y = 107, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot4Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot4Var[0:1] == "L":
        lodgeClicked4.place(x = 502, y = 107, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot4LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot4Var[0:1] == "O":
        oreRefineryClickedOnLabel4.place(x = 502, y = 107, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot4LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot4Var[0:1] == "S":
        stoneFactoryClickedOnLabel4.place(x = 502, y = 107, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot4LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot4Var[0:1] == "W":
        sawMillClickedOnLabel4.place(x = 502, y = 107, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot4LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot5():
    if slot5Var[0:1] == "E":
        slot5EmptySelectedLabel.place(x = 930, y = 111, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot5Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot5Var[0:1] == "L":
        lodgeClicked5.place(x = 930, y = 111, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot5LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot5Var[0:1] == "O":
        oreRefineryClickedOnLabel5.place(x = 930, y = 111, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot5LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot5Var[0:1] == "S":
        stoneFactoryClickedOnLabel5.place(x = 930, y = 111, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot5LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot5Var[0:1] == "W":
        sawMillClickedOnLabel5.place(x = 930, y = 111, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot5LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")


def slot6():
    if slot6Var[0:1] == "E":
        slot6EmptySelectedLabel.place(x = 1093, y = 217, anchor = "center")
        buildingOptionsLabel.place(x = 200, y = 500, anchor = "center")
        lodgeButton.place(x = 120, y = 350, anchor = "center")
        oreRefineryButton.place(x = 120, y = 450, anchor = "center")
        sawMillButton.place(x = 120, y = 550, anchor = "center")
        stoneFactoryButton.place(x = 120, y = 650, anchor = "center")

    else:
        a = int(slot6Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 190, y = 590, anchor = "center")

    if slot6Var[0:1] == "L":
        lodgeClicked6.place(x = 1093, y = 217, anchor = "center")
        lodgeInfo.place(x = 200, y = 500, anchor = "center")
        slot6LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
        wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

    if slot6Var[0:1] == "O":
        oreRefineryClickedOnLabel6.place(x = 1093, y = 217, anchor = "center")
        oreRefineryInfo.place(x = 200, y = 500, anchor = "center")
        slot6LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

    if slot6Var[0:1] == "S":
        stoneFactoryClickedOnLabel6.place(x = 1093, y = 217, anchor = "center")
        stoneFactoryInfo.place(x = 200, y = 500, anchor = "center")
        slot6LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if slot6Var[0:1] == "W":
        sawMillClickedOnLabel6.place(x = 1093, y = 217, anchor = "center")
        sawMillInfo.place(x = 200, y = 500, anchor = "center")
        slot6LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

def slot7():
    if slot7Var[0:1] == "E":
        slot7EmptySelectedLabel.place(x = 1260, y = 421, anchor = "center")
        buildingOptionsLabel.place(x = 200, y = 500, anchor = "center")
        lodgeButton.place(x = 120, y = 350, anchor = "center")
        oreRefineryButton.place(x = 120, y = 450, anchor = "center")
        sawMillButton.place(x = 120, y = 550, anchor = "center")
        stoneFactoryButton.place(x = 120, y = 650, anchor = "center")

    else:
        a = int(slot7Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 190, y = 590, anchor = "center")

    if slot7Var[0:1] == "L":
        lodgeClicked7.place(x = 1260, y = 421, anchor = "center")
        lodgeInfo.place(x = 200, y = 500, anchor = "center")
        slot7LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
        wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

    if slot7Var[0:1] == "O":
        oreRefineryClickedOnLabel6.place(x = 1260, y = 421, anchor = "center")
        oreRefineryInfo.place(x = 200, y = 500, anchor = "center")
        slot7LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")


    if slot7Var[0:1] == "S":
        stoneFactoryClickedOnLabel7.place(x = 1260, y = 421, anchor = "center")
        stoneFactoryInfo.place(x = 200, y = 500, anchor = "center")
        slot7LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if slot7Var[0:1] == "W":
        sawMillClickedOnLabel7.place(x = 1260, y = 421, anchor = "center")
        sawMillInfo.place(x = 200, y = 500, anchor = "center")
        slot7LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

def slot8():
    if slot8Var[0:1] == "E":
        slot8EmptySelectedLabel.place(x = 1340, y = 653, anchor = "center")
        buildingOptionsLabel.place(x = 200, y = 500, anchor = "center")
        lodgeButton.place(x = 120, y = 350, anchor = "center")
        oreRefineryButton.place(x = 120, y = 450, anchor = "center")
        sawMillButton.place(x = 120, y = 550, anchor = "center")
        stoneFactoryButton.place(x = 120, y = 650, anchor = "center")

    else:
        a = int(slot8Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 190, y = 590, anchor = "center")

    if slot8Var[0:1] == "L":
        lodgeClicked8.place(x = 1340, y = 653, anchor = "center")
        lodgeInfo.place(x = 200, y = 500, anchor = "center")
        slot8LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
        wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

    if slot8Var[0:1] == "O":
        oreRefineryClickedOnLabel8.place(x = 1340, y = 653, anchor = "center")
        oreRefineryInfo.place(x = 200, y = 500, anchor = "center")
        slot8LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

    if slot8Var[0:1] == "S":
        stoneFactoryClickedOnLabel8.place(x = 1340, y = 653, anchor = "center")
        stoneFactoryInfo.place(x = 200, y = 500, anchor = "center")
        slot8LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if slot8Var[0:1] == "W":
        sawMillClickedOnLabel8.place(x = 1340, y = 653, anchor = "center")
        sawMillInfo.place(x = 200, y = 500, anchor = "center")
        slot8LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

def slot9():
    if slot9Var[0:1] == "E":
        slot9EmptySelectedLabel.place(x = 202, y = 650, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot9Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot9Var[0:1] == "L":
        lodgeClicked9.place(x = 202, y = 650, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot9LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot9Var[0:1] == "O":
        oreRefineryClickedOnLabel9.place(x = 202, y = 650, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot9LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot9Var[0:1] == "S":
        stoneFactoryClickedOnLabel9.place(x = 202, y = 650, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot9LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot9Var[0:1] == "W":
        sawMillClickedOnLabel8.place(x = 202, y = 650, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot9LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot10():
    if slot10Var[0:1] == "E":
        slot10EmptySelectedLabel.place(x = 282, y = 433, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot10Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot10Var[0:1] == "L":
        lodgeClicked10.place(x = 282, y = 433, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot10LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot10Var[0:1] == "O":
        oreRefineryClickedOnLabel10.place(x = 282, y = 433, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot10LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot10Var[0:1] == "S":
        stoneFactoryClickedOnLabel10.place(x = 282, y = 433, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot10LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot10Var[0:1] == "W":
        sawMillClickedOnLabel10.place(x = 282, y = 433, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot10LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot11():
    if slot11Var[0:1] == "E":
        slot11EmptySelectedLabel.place(x = 418, y = 283, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot11Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot11Var[0:1] == "L":
        lodgeClicked11.place(x = 418, y = 283, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot11LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot11Var[0:1] == "O":
        oreRefineryClickedOnLabel11.place(x = 418, y = 283, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot11LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot11Var[0:1] == "S":
        stoneFactoryClickedOnLabel11.place(x = 418, y = 283, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot11LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot11Var[0:1] == "W":
        sawMillClickedOnLabel11.place(x = 418, y = 283, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot11LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot12():
    if slot12Var[0:1] == "E":
        slot12EmptySelectedLabel.place(x = 553, y = 209, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot12Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot12Var[0:1] == "L":
        lodgeClicked12.place(x = 553, y = 209, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot12LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot12Var[0:1] == "O":
        oreRefineryClickedOnLabel12.place(x = 553, y = 209, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot12LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot12Var[0:1] == "S":
        stoneFactoryClickedOnLabel12.place(x = 553, y = 209, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot12LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot12Var[0:1] == "W":
        sawMillClickedOnLabel12.place(x = 553, y = 209, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot12LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot13():
    if slot13Var[0:1] == "E":
        slot13EmptySelectedLabel.place(x = 894, y = 222, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot13Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot13Var[0:1] == "L":
        lodgeClicked13.place(x = 894, y = 222, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot13LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot13Var[0:1] == "O":
        oreRefineryClickedOnLabel13.place(x = 894, y = 222, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot13LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot13Var[0:1] == "S":
        stoneFactoryClickedOnLabel13.place(x = 894, y = 222, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot13LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot13Var[0:1] == "W":
        sawMillClickedOnLabel13.place(x = 894, y = 222, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot13LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot14():
    if slot14Var[0:1] == "E":
        slot14EmptySelectedLabel.place(x = 1035, y = 317, anchor = "center")
        buildingOptionsLabel.place(x = 200, y = 500, anchor = "center")
        lodgeButton.place(x = 120, y = 350, anchor = "center")
        oreRefineryButton.place(x = 120, y = 450, anchor = "center")
        sawMillButton.place(x = 120, y = 550, anchor = "center")
        stoneFactoryButton.place(x = 120, y = 650, anchor = "center")

    else:
        a = int(slot14Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 190, y = 590, anchor = "center")

    if slot14Var[0:1] == "L":
        lodgeClicked14.place(x = 1035, y = 317, anchor = "center")
        lodgeInfo.place(x = 200, y = 500, anchor = "center")
        slot14LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
        wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

    if slot14Var[0:1] == "O":
        oreRefineryClickedOnLabel14.place(x = 1035, y = 317, anchor = "center")
        oreRefineryInfo.place(x = 200, y = 500, anchor = "center")
        slot14LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

    if slot14Var[0:1] == "S":
        stoneFactoryClickedOnLabel14.place(x = 1035, y = 317, anchor = "center")
        stoneFactoryInfo.place(x = 200, y = 500, anchor = "center")
        slot14LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if slot14Var[0:1] == "W":
        sawMillClickedOnLabel14.place(x = 1035, y = 317, anchor = "center")
        sawMillInfo.place(x = 200, y = 500, anchor = "center")
        slot14LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

def slot15():
    if slot15Var[0:1] == "E":
        slot15EmptySelectedLabel.place(x = 1152, y = 469, anchor = "center")
        buildingOptionsLabel.place(x = 200, y = 500, anchor = "center")
        lodgeButton.place(x = 120, y = 350, anchor = "center")
        oreRefineryButton.place(x = 120, y = 450, anchor = "center")
        sawMillButton.place(x = 120, y = 550, anchor = "center")
        stoneFactoryButton.place(x = 120, y = 650, anchor = "center")

    else:
        a = int(slot15Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 190, y = 590, anchor = "center")

    if slot15Var[0:1] == "L":
        lodgeClicked15.place(x = 1152, y = 469, anchor = "center")
        lodgeInfo.place(x = 200, y = 500, anchor = "center")
        slot15LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
        wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

    if slot15Var[0:1] == "O":
        oreRefineryClickedOnLabel15.place(x = 1152, y = 469, anchor = "center")
        oreRefineryInfo.place(x = 200, y = 500, anchor = "center")
        slot15LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

    if slot15Var[0:1] == "S":
        stoneFactoryClickedOnLabel15.place(x = 1152, y = 469, anchor = "center")
        stoneFactoryInfo.place(x = 200, y = 500, anchor = "center")
        slot15LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if slot15Var[0:1] == "W":
        sawMillClickedOnLabel15.place(x = 1152, y = 469, anchor = "center")
        sawMillInfo.place(x = 200, y = 500, anchor = "center")
        slot15LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

def slot16():
    if slot16Var[0:1] == "E":
        slot16EmptySelectedLabel.place(x = 1209, y = 659, anchor = "center")
        buildingOptionsLabel.place(x = 200, y = 500, anchor = "center")
        lodgeButton.place(x = 120, y = 350, anchor = "center")
        oreRefineryButton.place(x = 120, y = 450, anchor = "center")
        sawMillButton.place(x = 120, y = 550, anchor = "center")
        stoneFactoryButton.place(x = 120, y = 650, anchor = "center")

    else:
        a = int(slot16Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 190, y = 590, anchor = "center")

    if slot16Var[0:1] == "L":
        lodgeClicked16.place(x = 1209, y = 659, anchor = "center")
        lodgeInfo.place(x = 200, y = 500, anchor = "center")
        slot16LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
        wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

    if slot16Var[0:1] == "O":
        oreRefineryClickedOnLabel16.place(x = 1209, y = 659, anchor = "center")
        oreRefineryInfo.place(x = 200, y = 500, anchor = "center")
        slot16LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

    if slot16Var[0:1] == "S":
        stoneFactoryClickedOnLabel16.place(x = 1209, y = 659, anchor = "center")
        stoneFactoryInfo.place(x = 200, y = 500, anchor = "center")
        slot16LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if slot16Var[0:1] == "W":
        sawMillClickedOnLabel15.place(x = 1209, y = 659, anchor = "center")
        sawMillInfo.place(x = 200, y = 500, anchor = "center")
        slot16LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

def slot17():
    if slot17Var[0:1] == "E":
        slot17EmptySelectedLabel.place(x = 316, y = 652, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot17Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot17Var[0:1] == "L":
        lodgeClicked17.place(x = 316, y = 652, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot17LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot17Var[0:1] == "O":
        oreRefineryClickedOnLabel17.place(x = 316, y = 652, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot17LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot17Var[0:1] == "S":
        stoneFactoryClickedOnLabel17.place(x = 316, y = 652, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot17LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot17Var[0:1] == "W":
        sawMillClickedOnLabel17.place(x = 316, y = 652, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot17LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot18():
    if slot18Var[0:1] == "E":
        slot18EmptySelectedLabel.place(x = 383, y = 492, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot18Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot18Var[0:1] == "L":
        lodgeClicked18.place(x = 383, y = 492, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot18LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot18Var[0:1] == "O":
        oreRefineryClickedOnLabel18.place(x = 383, y = 492, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot18LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot18Var[0:1] == "S":
        stoneFactoryClickedOnLabel18.place(x = 383, y = 492, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot18LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot18Var[0:1] == "W":
        sawMillClickedOnLabel18.place(x = 383, y = 492, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot18LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot19():
    if slot19Var[0:1] == "E":
        slot19EmptySelectedLabel.place(x = 503, y = 368, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot19Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot19Var[0:1] == "L":
        lodgeClicked19.place(x = 503, y = 368, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot19LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot19Var[0:1] == "O":
        oreRefineryClickedOnLabel19.place(x = 503, y = 368, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot19LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot19Var[0:1] == "S":
        stoneFactoryClickedOnLabel19.place(x = 503, y = 368, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot19LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot19Var[0:1] == "W":
        sawMillClickedOnLabel19.place(x = 503, y = 368, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot19LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot20():
    if slot20Var[0:1] == "E":
        slot20EmptySelectedLabel.place(x = 924, y = 374, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot20Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot20Var[0:1] == "L":
        lodgeClicked20.place(x = 924, y = 374, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot20LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot20Var[0:1] == "O":
        oreRefineryClickedOnLabel20.place(x = 924, y = 374, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot20LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot20Var[0:1] == "S":
        stoneFactoryClickedOnLabel20.place(x = 924, y = 374, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot20LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot20Var[0:1] == "W":
        sawMillClickedOnLabel20.place(x = 924, y = 374, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot20LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot21():
    if slot21Var[0:1] == "E":
        slot21EmptySelectedLabel.place(x = 1042, y = 505, anchor = "center")
        buildingOptionsLabel.place(x = 200, y = 500, anchor = "center")
        lodgeButton.place(x = 120, y = 350, anchor = "center")
        oreRefineryButton.place(x = 120, y = 450, anchor = "center")
        sawMillButton.place(x = 120, y = 550, anchor = "center")
        stoneFactoryButton.place(x = 120, y = 650, anchor = "center")

    else:
        a = int(slot21Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 190, y = 590, anchor = "center")

    if slot21Var[0:1] == "L":
        lodgeClicked21.place(x = 1042, y = 505, anchor = "center")
        lodgeInfo.place(x = 200, y = 500, anchor = "center")
        slot21LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
        wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

    if slot21Var[0:1] == "O":
        oreRefineryClickedOnLabel21.place(x = 1042, y = 505, anchor = "center")
        oreRefineryInfo.place(x = 200, y = 500, anchor = "center")
        slot21LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

    if slot21Var[0:1] == "S":
        stoneFactoryClickedOnLabel21.place(x = 1042, y = 505, anchor = "center")
        stoneFactoryInfo.place(x = 200, y = 500, anchor = "center")
        slot21LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if slot21Var[0:1] == "W":
        sawMillClickedOnLabel21.place(x = 1042, y = 505, anchor = "center")
        sawMillInfo.place(x = 200, y = 500, anchor = "center")
        slot21LvlLbl.place(x = 160, y = 570, anchor = "center")
        otherUpgradeButton.place(x = 140, y = 660, anchor = "center")
        demolishButton.place(x = 250, y = 660, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
        gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

def slot22():
    if slot22Var[0:1] == "E":
        slot22EmptySelectedLabel.place(x = 1100, y = 660, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot22Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot22Var[0:1] == "L":
        lodgeClicked22.place(x = 1100, y = 660, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot22LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot22Var[0:1] == "O":
        oreRefineryClickedOnLabel22.place(x = 1100, y = 660, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot22LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot22Var[0:1] == "S":
        stoneFactoryClickedOnLabel22.place(x = 1100, y = 660, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot22LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot22Var[0:1] == "W":
        sawMillClickedOnLabel22.place(x = 1100, y = 660, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot22LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")


def slot23():
    if slot23Var[0:1] == "E":
        slot23EmptySelectedLabel.place(x = 427, y = 674, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot23Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot23Var[0:1] == "L":
        lodgeClicked23.place(x = 427, y = 674, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot23LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot23Var[0:1] == "O":
        oreRefineryClickedOnLabel23.place(x = 427, y = 674, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot23LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot23Var[0:1] == "S":
        stoneFactoryClickedOnLabel23.place(x = 427, y = 674, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot23LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot23Var[0:1] == "W":
        sawMillClickedOnLabel23.place(x = 427, y = 674, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot23LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def slot24():
    if slot24Var[0:1] == "E":
        slot24EmptySelectedLabel.place(x = 980, y = 645, anchor = "center")
        buildingOptionsLabel.place(x = 1200, y = 300, anchor = "center")
        lodgeButton.place(x = 1120, y = 150, anchor = "center")
        oreRefineryButton.place(x = 1120, y = 250, anchor = "center")
        sawMillButton.place(x = 1120, y = 350, anchor = "center")
        stoneFactoryButton.place(x = 1120, y = 450, anchor = "center")

    else:
        a = int(slot24Var[4:])
        level_actual = 300 + 30*(a - 1)
        productionUse.set(str(level_actual))
        productionUseLbl.place(x = 1190, y = 387, anchor = "center")

    if slot24Var[0:1] == "L":
        lodgeClicked24.place(x = 980, y = 645, anchor = "center")
        lodgeInfo.place(x = 1200, y = 300, anchor = "center")
        slot24LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 500 + 50*(a-1)
        wood_up = 300 + 30*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
        wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

    if slot24Var[0:1] == "O":
        oreRefineryClickedOnLabel24.place(x = 980, y = 645, anchor = "center")
        oreRefineryInfo.place(x = 1200, y = 300, anchor = "center")
        slot24LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        ore_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        ore_upgradeUse.set(str(ore_up))
        ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

    if slot24Var[0:1] == "S":
        stoneFactoryClickedOnLabel24.place(x = 980, y = 645, anchor = "center")
        stoneFactoryInfo.place(x = 1200, y = 300, anchor = "center")
        slot24LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        stone_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        stone_upgradeUse.set(str(stone_up))
        stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if slot24Var[0:1] == "W":
        sawMillClickedOnLabel24.place(x = 980, y = 645, anchor = "center")
        sawMillInfo.place(x = 1200, y = 300, anchor = "center")
        slot24LvlLbl.place(x = 1160, y = 370, anchor = "center")
        otherUpgradeButton.place(x = 1140, y = 460, anchor = "center")
        demolishButton.place(x = 1250, y = 460, anchor = "center")

        gold_up = 300 + 30*(a-1)
        wood_up = 500 + 50*(a-1)
        gold_upgradeUse.set(str(gold_up))
        wood_upgradeUse.set(str(wood_up))
        wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
        gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

def turnSlotToLodge():
    global current
    global slot1Var
    global slot2Var
    global slot3Var
    global slot4Var
    global slot5Var
    global slot6Var
    global slot7Var
    global slot8Var
    global slot9Var
    global slot10Var
    global slot11Var
    global slot12Var
    global slot13Var
    global slot14Var
    global slot15Var
    global slot16Var
    global slot17Var
    global slot18Var
    global slot19Var
    global slot20Var
    global slot21Var
    global slot22Var
    global slot23Var
    global slot24Var
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 2000 or w < 500 or s < 500 or o < 500:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        if current == 2:
            slot1Var = slot1Var.replace('E','L')
        if current == 3:
            slot2Var = slot2Var.replace('E','L')
        if current == 4:
            slot3Var = slot3Var.replace('E','L')
        if current == 5:
            slot4Var = slot4Var.replace('E','L')
        if current == 6:
            slot5Var = slot5Var.replace('E','L')
        if current == 7:
            slot6Var = slot6Var.replace('E','L')
        if current == 8:
            slot7Var = slot7Var.replace('E','L')
        if current == 9:
            slot8Var = slot8Var.replace('E','L')
        if current == 10:
            slot9Var = slot9Var.replace('E','L')
        if current == 11:
            slot10Var = slot10Var.replace('E','L')
        if current == 12:
            slot11Var = slot11Var.replace('E','L')
        if current == 13:
            slot12Var = slot12Var.replace('E','L')
        if current == 14:
            slot13Var = slot13Var.replace('E','L')
        if current == 15:
            slot14Var = slot14Var.replace('E','L')
        if current == 16:
            slot15Var = slot15Var.replace('E','L')
        if current == 17:
            slot16Var = slot16Var.replace('E','L')
        if current == 18:
            slot17Var = slot17Var.replace('E','L')
        if current == 19:
            slot18Var = slot18Var.replace('E','L')
        if current == 20:
            slot19Var = slot19Var.replace('E','L')
        if current == 21:
            slot20Var = slot20Var.replace('E','L')
        if current == 22:
            slot21Var = slot21Var.replace('E','L')
        if current == 23:
            slot22Var = slot22Var.replace('E','L')
        if current == 24:
            slot23Var = slot23Var.replace('E','L')
        if current == 25:
            slot24Var = slot24Var.replace('E','L')

        m = m - 2000
        w = w - 500
        s = s - 500
        o = o - 500

    moneyResource = str(m)
    woodResource = str(w)
    stoneResource = str(s)
    oreResource = str(o)

    woodAmount.set(woodResource)
    moneyAmount.set(moneyResource)
    stoneAmount.set(stoneResource)
    oreAmount.set(oreResource)

    slotDestruct()

def turnSlotToOre():
    global current
    global slot1Var
    global slot2Var
    global slot3Var
    global slot4Var
    global slot5Var
    global slot6Var
    global slot7Var
    global slot8Var
    global slot9Var
    global slot10Var
    global slot11Var
    global slot12Var
    global slot13Var
    global slot14Var
    global slot15Var
    global slot16Var
    global slot17Var
    global slot18Var
    global slot19Var
    global slot20Var
    global slot21Var
    global slot22Var
    global slot23Var
    global slot24Var
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)

    if m < 500 or w < 500 or s < 500 or o < 2000:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        if current == 2:
            slot1Var = slot1Var.replace('E','O')
        if current == 3:
            slot2Var = slot2Var.replace('E','O')
        if current == 4:
            slot3Var = slot3Var.replace('E','O')
        if current == 5:
            slot4Var = slot4Var.replace('E','O')
        if current == 6:
            slot5Var = slot5Var.replace('E','O')
        if current == 7:
            slot6Var = slot6Var.replace('E','O')
        if current == 8:
            slot7Var = slot7Var.replace('E','O')
        if current == 9:
            slot8Var = slot8Var.replace('E','O')
        if current == 10:
            slot9Var = slot9Var.replace('E','O')
        if current == 11:
            slot10Var = slot10Var.replace('E','O')
        if current == 12:
            slot11Var = slot11Var.replace('E','O')
        if current == 13:
            slot12Var = slot12Var.replace('E','O')
        if current == 14:
            slot13Var = slot13Var.replace('E','O')
        if current == 15:
            slot14Var = slot14Var.replace('E','O')
        if current == 16:
            slot15Var = slot15Var.replace('E','O')
        if current == 17:
            slot16Var = slot16Var.replace('E','O')
        if current == 18:
            slot17Var = slot17Var.replace('E','O')
        if current == 19:
            slot18Var = slot18Var.replace('E','O')
        if current == 20:
            slot19Var = slot19Var.replace('E','O')
        if current == 21:
            slot20Var = slot20Var.replace('E','O')
        if current == 22:
            slot21Var = slot21Var.replace('E','O')
        if current == 23:
            slot22Var = slot22Var.replace('E','O')
        if current == 24:
            slot23Var = slot23Var.replace('E','O')
        if current == 25:
            slot24Var = slot24Var.replace('E','O')

        m = m - 500
        w = w - 500
        s = s - 500
        o = o - 2000

    moneyResource = str(m)
    woodResource = str(w)
    stoneResource = str(s)
    oreResource = str(o)

    woodAmount.set(woodResource)
    moneyAmount.set(moneyResource)
    stoneAmount.set(stoneResource)
    oreAmount.set(oreResource)

    slotDestruct()

def turnSlotToSawMill():
    global current
    global slot1Var
    global slot2Var
    global slot3Var
    global slot4Var
    global slot5Var
    global slot6Var
    global slot7Var
    global slot8Var
    global slot9Var
    global slot10Var
    global slot11Var
    global slot12Var
    global slot13Var
    global slot14Var
    global slot15Var
    global slot16Var
    global slot17Var
    global slot18Var
    global slot19Var
    global slot20Var
    global slot21Var
    global slot22Var
    global slot23Var
    global slot24Var
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 500 or w < 2000 or s < 500 or o < 500:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:

        if current == 2:
            slot1Var = slot1Var.replace('E','W')
        if current == 3:
            slot2Var = slot2Var.replace('E','W')
        if current == 4:
            slot3Var = slot3Var.replace('E','W')
        if current == 5:
            slot4Var = slot4Var.replace('E','W')
        if current == 6:
            slot5Var = slot5Var.replace('E','W')
        if current == 7:
            slot6Var = slot6Var.replace('E','W')
        if current == 8:
            slot7Var = slot7Var.replace('E','W')
        if current == 9:
            slot8Var = slot8Var.replace('E','W')
        if current == 10:
            slot9Var = slot9Var.replace('E','W')
        if current == 11:
            slot10Var = slot10Var.replace('E','W')
        if current == 12:
            slot11Var = slot11Var.replace('E','W')
        if current == 13:
            slot12Var = slot12Var.replace('E','W')
        if current == 14:
            slot13Var = slot13Var.replace('E','W')
        if current == 15:
            slot14Var = slot14Var.replace('E','W')
        if current == 16:
            slot15Var = slot15Var.replace('E','W')
        if current == 17:
            slot16Var = slot16Var.replace('E','W')
        if current == 18:
            slot17Var = slot17Var.replace('E','W')
        if current == 19:
            slot18Var = slot18Var.replace('E','W')
        if current == 20:
            slot19Var = slot19Var.replace('E','W')
        if current == 21:
            slot20Var = slot20Var.replace('E','W')
        if current == 22:
            slot21Var = slot21Var.replace('E','W')
        if current == 23:
            slot22Var = slot22Var.replace('E','W')
        if current == 24:
            slot23Var = slot23Var.replace('E','W')
        if current == 25:
            slot24Var = slot24Var.replace('E','W')

        m = m - 500
        w = w - 2000
        s = s - 500
        o = o - 500

    moneyResource = str(m)
    woodResource = str(w)
    stoneResource = str(s)
    oreResource = str(o)

    woodAmount.set(woodResource)
    moneyAmount.set(moneyResource)
    stoneAmount.set(stoneResource)
    oreAmount.set(oreResource)

    slotDestruct()

def turnSlotToStoneFactory():
    global current
    global slot1Var
    global slot2Var
    global slot3Var
    global slot4Var
    global slot5Var
    global slot6Var
    global slot7Var
    global slot8Var
    global slot9Var
    global slot10Var
    global slot11Var
    global slot12Var
    global slot13Var
    global slot14Var
    global slot15Var
    global slot16Var
    global slot17Var
    global slot18Var
    global slot19Var
    global slot20Var
    global slot21Var
    global slot22Var
    global slot23Var
    global slot24Var
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    global castleHealth
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 500 or w < 500 or s < 2000 or o < 500:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:

        if current == 2:
            slot1Var = slot1Var.replace('E','S')
        if current == 3:
            slot2Var = slot2Var.replace('E','S')
        if current == 4:
            slot3Var = slot3Var.replace('E','S')
        if current == 5:
            slot4Var = slot4Var.replace('E','S')
        if current == 6:
            slot5Var = slot5Var.replace('E','S')
        if current == 7:
            slot6Var = slot6Var.replace('E','S')
        if current == 8:
            slot7Var = slot7Var.replace('E','S')
        if current == 9:
            slot8Var = slot8Var.replace('E','S')
        if current == 10:
            slot9Var = slot9Var.replace('E','S')
        if current == 11:
            slot10Var = slot10Var.replace('E','S')
        if current == 12:
            slot11Var = slot11Var.replace('E','S')
        if current == 13:
            slot12Var = slot12Var.replace('E','S')
        if current == 14:
            slot13Var = slot13Var.replace('E','S')
        if current == 15:
            slot14Var = slot14Var.replace('E','S')
        if current == 16:
            slot15Var = slot15Var.replace('E','S')
        if current == 17:
            slot16Var = slot16Var.replace('E','S')
        if current == 18:
            slot17Var = slot17Var.replace('E','S')
        if current == 19:
            slot18Var = slot18Var.replace('E','S')
        if current == 20:
            slot19Var = slot19Var.replace('E','S')
        if current == 21:
            slot20Var = slot20Var.replace('E','S')
        if current == 22:
            slot21Var = slot21Var.replace('E','S')
        if current == 23:
            slot22Var = slot22Var.replace('E','S')
        if current == 24:
            slot23Var = slot23Var.replace('E','S')
        if current == 25:
            slot24Var = slot24Var.replace('E','S')

        m = m - 500
        w = w - 500
        s = s - 2000
        o = o - 500

    moneyResource = str(m)
    woodResource = str(w)
    stoneResource = str(s)
    oreResource = str(o)

    woodAmount.set(woodResource)
    moneyAmount.set(moneyResource)
    stoneAmount.set(stoneResource)
    oreAmount.set(oreResource)
    slotDestruct()


def callStronghold():
    slotDestruct()
    strongHoldClickedLabel.place(x = 702, y = 720, anchor = "center")
    strongHoldInfoLabel.place(x = 1200, y = 300, anchor = "center")
    strongHoldLvlUseLbl.place(x = 1150, y = 356)
    strongHoldUpgradeButton.place(x = 1200, y = 460, anchor = "center")
    gold = 200 + 20*(int(strongHoldLvl) - 1)
    wood = 200 + 20*(int(strongHoldLvl) - 1)
    stone = 200 + 20*(int(strongHoldLvl) - 1)
    ore = 200 + 20*(int(strongHoldLvl) - 1)
    gold_upgradeUse.set(str(gold))
    stone_upgradeUse.set(str(stone))
    wood_upgradeUse.set(str(wood))
    ore_upgradeUse.set(str(ore))
    gold_upgradeLbl.place(x = 1170, y = 265, anchor = "center")
    stone_upgradeLbl.place(x = 1170, y = 289, anchor = "center")
    wood_upgradeLbl.place(x = 1170, y = 313, anchor = "center")
    ore_upgradeLbl.place(x = 1170, y = 337, anchor = "center")

def upgrade():
    global strongHoldLvl
    global moneyResource
    global woodResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    gold = 200 + 20*(int(strongHoldLvl) - 1)
    wood = 200 + 20*(int(strongHoldLvl) - 1)
    stone = 200 + 20*(int(strongHoldLvl) - 1)
    ore = 200 + 20*(int(strongHoldLvl) - 1)
    if m < gold or w < wood or s < stone or o < ore:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:

        strongHoldLvl = str(int(strongHoldLvl)+ 1)
        strongHoldLvlUse.set(str(strongHoldLvl))
        m -= gold
        w -= wood
        s -= stone
        o -= ore

        moneyAmount.set(str(m))
        woodAmount.set(str(w))
        stoneAmount.set(str(s))
        oreAmount.set(str(o))

        gold = 200 + 20*(int(strongHoldLvl) - 1)
        wood = 200 + 20*(int(strongHoldLvl) - 1)
        stone = 200 + 20*(int(strongHoldLvl) - 1)
        ore = 200 + 20*(int(strongHoldLvl) - 1)

        gold_upgradeUse.set(gold)
        ore_upgradeUse.set(ore)
        wood_upgradeUse.set(wood)
        stone_upgradeUse.set(stone)

        moneyResource = str(m)
        woodResource = str(w)
        stoneResource = str(s)
        oreResource = str(o)

def nextDay():
    global current
    global day
    global moneyResource
    global stoneResource
    global oreResource
    global woodResource

    global cavalry
    global swordsMen
    global spearMen
    global archers
    global castleHealth

    import random as r
    import time
    r.seed()
    day = str(int(day) + 1)
    dayUse.set(day)
    pauser()
    slotDestruct()
    if slot1Var[0] == "L":
        lvl = int(slot1Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot1Var[0] == "S":
        lvl = int(slot1Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot1Var[0] == "O":
        lvl = int(slot1Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot1Var[0] == "W":
        lvl = int(slot1Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot2Var[0] == "L":
        lvl = int(slot2Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot2Var[0] == "S":
        lvl = int(slot2Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot2Var[0] == "O":
        lvl = int(slot2Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot2Var[0] == "W":
        lvl = int(slot2Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot3Var[0] == "L":
        lvl = int(slot3Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot3Var[0] == "S":
        lvl = int(slot3Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot3Var[0] == "O":
        lvl = int(slot3Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot3Var[0] == "W":
        lvl = int(slot3Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot4Var[0] == "L":
        lvl = int(slot4Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot4Var[0] == "S":
        lvl = int(slot4Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot4Var[0] == "O":
        lvl = int(slot4Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot4Var[0] == "W":
        lvl = int(slot4Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot5Var[0] == "L":
        lvl = int(slot5Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot5Var[0] == "S":
        lvl = int(slot5Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot5Var[0] == "O":
        lvl = int(slot5Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot5Var[0] == "W":
        lvl = int(slot5Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot6Var[0] == "L":
        lvl = int(slot6Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot6Var[0] == "S":
        lvl = int(slot6Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot6Var[0] == "O":
        lvl = int(slot6Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot6Var[0] == "W":
        lvl = int(slot6Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot7Var[0] == "L":
        lvl = int(slot7Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot7Var[0] == "S":
        lvl = int(slot7Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot7Var[0] == "O":
        lvl = int(slot7Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot7Var[0] == "W":
        lvl = int(slot7Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot8Var[0] == "L":
        lvl = int(slot8Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot8Var[0] == "S":
        lvl = int(slot8Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot8Var[0] == "O":
        lvl = int(slot8Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot8Var[0] == "W":
        lvl = int(slot8Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot9Var[0] == "L":
        lvl = int(slot9Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot9Var[0] == "S":
        lvl = int(slot9Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot9Var[0] == "O":
        lvl = int(slot9Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot9Var[0] == "W":
        lvl = int(slot9Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot10Var[0] == "L":
        lvl = int(slot10Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot10Var[0] == "S":
        lvl = int(slot10Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot10Var[0] == "O":
        lvl = int(slot10Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot10Var[0] == "W":
        lvl = int(slot10Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot11Var[0] == "L":
        lvl = int(slot11Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot11Var[0] == "S":
        lvl = int(slot11Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot11Var[0] == "O":
        lvl = int(slot11Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot11Var[0] == "W":
        lvl = int(slot11Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot12Var[0] == "L":
        lvl = int(slot12Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot12Var[0] == "S":
        lvl = int(slot12Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot12Var[0] == "O":
        lvl = int(slot12Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot12Var[0] == "W":
        lvl = int(slot12Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot13Var[0] == "L":
        lvl = int(slot13Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot13Var[0] == "S":
        lvl = int(slot13Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot13Var[0] == "O":
        lvl = int(slot13Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot13Var[0] == "W":
        lvl = int(slot13Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot14Var[0] == "L":
        lvl = int(slot14Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot14Var[0] == "S":
        lvl = int(slot14Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot14Var[0] == "O":
        lvl = int(slot14Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot14Var[0] == "W":
        lvl = int(slot14Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot15Var[0] == "L":
        lvl = int(slot15Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot15Var[0] == "S":
        lvl = int(slot15Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot15Var[0] == "O":
        lvl = int(slot15Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot15Var[0] == "W":
        lvl = int(slot15Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot16Var[0] == "L":
        lvl = int(slot16Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot16Var[0] == "S":
        lvl = int(slot16Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot16Var[0] == "O":
        lvl = int(slot16Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot16Var[0] == "W":
        lvl = int(slot16Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot17Var[0] == "L":
        lvl = int(slot17Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot17Var[0] == "S":
        lvl = int(slot17Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot17Var[0] == "O":
        lvl = int(slot17Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot17Var[0] == "W":
        lvl = int(slot17Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot18Var[0] == "L":
        lvl = int(slot18Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot18Var[0] == "S":
        lvl = int(slot18Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot18Var[0] == "O":
        lvl = int(slot18Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot18Var[0] == "W":
        lvl = int(slot18Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot19Var[0] == "L":
        lvl = int(slot19Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot19Var[0] == "S":
        lvl = int(slot19Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot19Var[0] == "O":
        lvl = int(slot19Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot19Var[0] == "W":
        lvl = int(slot19Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot20Var[0] == "L":
        lvl = int(slot20Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot20Var[0] == "S":
        lvl = int(slot20Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot20Var[0] == "O":
        lvl = int(slot20Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot20Var[0] == "W":
        lvl = int(slot20Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    if slot21Var[0] == "L":
        lvl = int(slot21Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot21Var[0] == "S":
        lvl = int(slot21Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot21Var[0] == "O":
        lvl = int(slot21Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot21Var[0] == "W":
        lvl = int(slot21Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot22Var[0] == "L":
        lvl = int(slot22Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot22Var[0] == "S":
        lvl = int(slot22Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot22Var[0] == "O":
        lvl = int(slot22Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot22Var[0] == "W":
        lvl = int(slot22Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot23Var[0] == "L":
        lvl = int(slot23Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot23Var[0] == "S":
        lvl = int(slot23Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot23Var[0] == "O":
        lvl = int(slot23Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot23Var[0] == "W":
        lvl = int(slot23Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)


    if slot24Var[0] == "L":
        lvl = int(slot24Var[4:]) - 1
        goldCurrent = int(moneyResource)
        goldCurrent += 300 + 50*lvl
        moneyResource = str(goldCurrent)
        moneyAmount.set(moneyResource)
    if slot24Var[0] == "S":
        lvl = int(slot24Var[4:]) - 1
        stoneCurrent = int(stoneResource)
        stoneCurrent += 300 + 50*lvl
        stoneResource = str(stoneCurrent)
        stoneAmount.set(stoneResource)
    if slot24Var[0] == "O":
        lvl = int(slot24Var[4:]) - 1
        oreCurrent = int(oreResource)
        oreCurrent += 300 + 50*lvl
        oreResource = str(oreCurrent)
        oreAmount.set(oreResource)
    if slot24Var[0] == "W":
        lvl = int(slot24Var[4:]) - 1
        woodCurrent = int(woodResource)
        woodCurrent += 300 + 50*lvl
        woodResource = str(woodCurrent)
        woodAmount.set(woodResource)

    current = 1
    chance_of_attack = r.randint(1, 100)
    if int(day) < 10:
        attack = False
    if int(day) >= 10 and int(day) <= 11:
        if chance_of_attack <= int(20*(int(day)-10)):
            attack = True
        else:
            attack = False
    if int(day) > 11 and int(day) <= 126:
        if chance_of_attack <= int(0.003*(int(day) - 11)**2 + 20):
            attack = True
        else:
            attack = False
    if int(day) > 126:
        if chance_of_attack <= 60:
            attack = True
        else:
            attack = False
    if attack == True:
        anAttackOccuredLbl.place(x = 0, y = 0)
        anAttackOccuredLbl.after(600, battle_report)
        goblins_multiplier = r.randint(-20,20)
        mordor_Orcs_multiplier = r.randint(-20,20)
        uruk_Hai_multiplier = r.randint(-10,10)
        trolls_multiplier = r.randint(-10,10)
        dis_factor = r.randint(1,3)

        goblins = round((0.007*(int(day) - 10)**2 + 20)*(1 + (goblins_multiplier/100)))
        mordor_Orcs = round((0.0072*(int(day) - 10)**2 + 20)*(1 + (mordor_Orcs_multiplier/100)))
        uruk_Hai = 0
        trolls = 0
        if int(day) >= 15:
            uruk_Hai = round((0.0001*(int(day) - 15)**2 + 5) * (1 + (uruk_Hai_multiplier/100)))
        if int(day) >= 30:
            if dis_factor == 2 or dis_factor == 1:
                trolls = round((0.0001*(int(day) - 30)**2 + 2) * (1 + (trolls_multiplier/100)))
            if dis_factor == 3:
                trolls = 0
        urukhaiUse.set(str(uruk_Hai))
        trollsUse.set(str(trolls))
        mordorOrcsUse.set(str(mordor_Orcs))
        GoblinsUse.set(str(goblins))
        cavalry_Before = cavalry
        swordsMen_Before = swordsMen
        spearMen_Before = spearMen
        archers_Before = archers
        cavalry_Before_Use.set(cavalry_Before)
        swordsMen_Before_Use.set(swordsMen_Before)
        spearMen_Before_Use.set(spearMen_Before)
        archers_Before_Use.set(archers_Before)
        total_ally_forces = int(spearMen) + int(archers) + int(swordsMen) + int(cavalry)
        total_ally_forces_before = total_ally_forces
        total_opposing_forces = int(trolls) + int(goblins) + int(mordor_Orcs)  + int(uruk_Hai)
        total_opposing_forces_before = total_opposing_forces
        troopsLost = 0
        opponentLost = 0
        while total_ally_forces > 0 and total_opposing_forces > 0:
            cavalry_random = r.randint(-5,15)
            swordsMen_random = r.randint(-5,15)
            spearMen_random = r.randint(-5,15)
            archers_random = r.randint(-5,15)

            trolls_random = r.randint(-10,10)
            goblins_random = r.randint(-10,10)
            mordor_orcs_random = r.randint(-10,10)
            uruk_hai_random = r.randint(-10,10)
            ally_damage_mordor_orcs = 0
            ally_damage_goblins = 0
            ally_damage_urukhai = 0
            ally_damage_trolls = 0

            enemy_damage_cavalry = 0
            enemy_damage_swordsMen = 0
            enemy_damage_spearMen = 0
            enemy_damage_archers = 0

            ally_attack_power = 15 * (1 + (cavalry_random/100)) * int(cavalry) + 20 * (1 + (swordsMen_random/100)) * int(swordsMen) + 30 * (1 + (spearMen_random/100)) * int(spearMen) + 35 * (1 + (archers_random/100)) * int(archers)
            enemy_attack_power = 20 * (1 + (trolls_random/100)) * int(trolls) + 30 * (1 + (goblins_random/100)) * int(goblins) + 10 * (1 + (mordor_orcs_random/100)) * int(mordor_Orcs)  + 20 * (1 + (uruk_hai_random/100)) * int(uruk_Hai)

            while ally_attack_power > 0 and total_opposing_forces > 0:
                if goblins > 0 and trolls == 0 and mordor_Orcs == 0 and uruk_Hai == 0:
                    ally_damage_goblins = 0.9 * ally_attack_power
                if goblins == 0 and trolls > 0 and mordor_Orcs == 0 and uruk_Hai == 0:
                    ally_damage_trolls = 0.7 * ally_attack_power
                if goblins == 0 and trolls == 0 and mordor_Orcs > 0 and uruk_Hai == 0:
                    ally_damage_mordor_orcs = 0.8 * ally_attack_power
                if goblins == 0 and trolls == 0 and mordor_Orcs > 0 and uruk_Hai > 0:
                    ally_damage_urukhai = 0.7 * 0.5 * ally_attack_power
                    ally_damage_mordor_orcs = 0.8 * 0.5 * ally_attack_power
                if goblins > 0 and trolls == 0 and mordor_Orcs > 0 and uruk_Hai == 0:
                    ally_damage_goblins = 0.9 * 0.5 * ally_attack_power
                    ally_damage_mordor_orcs = 0.8 * 0.5 * ally_attack_power
                if goblins > 0 and trolls == 0 and mordor_Orcs > 0 and uruk_Hai > 0:
                    ally_damage_goblins = 0.9 * (0.2 * ally_attack_power)
                    ally_damage_mordor_orcs = 0.8 * (0.25 * ally_attack_power)
                    ally_damage_urukhai = 0.7 * (0.55  * ally_attack_power)
                if goblins > 0 and trolls > 0 and mordor_Orcs == 0 and uruk_Hai == 0:
                    ally_damage_goblins = 0.9 * (0.5 * ally_attack_power)
                    ally_damage_trolls = 0.7 * (0.5 * ally_attack_power)
                if goblins > 0 and trolls == 0 and mordor_Orcs == 0 and uruk_Hai > 0:
                    ally_damage_goblins = 0.9 * (0.5 * ally_attack_power)
                    ally_damage_urukhai = 0.7 * (0.5  * ally_attack_power)
                if goblins == 0 and trolls == 0 and mordor_Orcs > 0 and uruk_Hai > 0:
                    ally_damage_urukhai = 0.7 * (0.5  * ally_attack_power)
                    ally_damage_mordor_orcs = 0.8 * (0.5 * ally_attack_power)
                else:
                    ally_damage_goblins = 0.9 * (0.2 * ally_attack_power)
                    ally_damage_mordor_orcs = 0.8 * (0.25 * ally_attack_power)
                    ally_damage_urukhai = 0.7 * (0.275 * ally_attack_power)
                    ally_damage_trolls = 0.7 * (0.275 * ally_attack_power)
                if ally_damage_goblins >= 5 * int(goblins):
                    ally_damage_goblins -= 5 * int(goblins)
                    goblins = 0
                    ally_damage_goblins = ally_damage_goblins/0.9
                else:
                    goblins = goblins - ally_damage_goblins/5
                    ally_damage_goblins = 0
                if ally_damage_mordor_orcs >= 10*(mordor_Orcs):
                    ally_damage_mordor_orcs -= 10 * mordor_Orcs
                    mordor_Orcs = 0
                    ally_damage_mordor_orcs = ally_damage_mordor_orcs/0.9
                else:
                    mordor_Orcs = mordor_Orcs - ally_damage_mordor_orcs/10
                    ally_damage_mordor_orcs = 0
                if ally_damage_urukhai >= 15 * (uruk_Hai):
                    ally_damage_urukhai -= 15*uruk_Hai
                    uruk_Hai = 0
                    ally_damage_urukhai = ally_damage_urukhai/0.7
                else:
                    uruk_Hai = uruk_Hai - ally_damage_urukhai/15
                    ally_damage_urukHai = 0
                if ally_damage_trolls >= 15 * (trolls):
                    ally_damage_trolls -= 15 * trolls
                    trolls = 0
                    ally_damage_trolls = ally_damage_trolls/0.7
                else:
                    trolls = trolls - ally_damage_trolls/15
                    ally_damage_trolls = 0

                ally_attack_power = ally_damage_goblins + ally_damage_mordor_orcs + ally_damage_urukhai + ally_damage_trolls
                if ally_attack_power < 1:
                    ally_attack_power = 0
                total_opposing_forces = trolls + goblins + mordor_Orcs + uruk_Hai
                if total_opposing_forces < 1:
                    total_opposing_forces = 0
            trolls = round(trolls)
            mordor_Orcs = round(mordor_Orcs)
            goblins = round(goblins)
            uruk_Hai = round(uruk_Hai)

            trolls_after = str(trolls)
            urukhai_after = str(uruk_Hai)
            mordorOrcs_after = str(mordor_Orcs)
            Goblins_after = str(goblins)
            trolls_after_Use.set(trolls_after)
            urukhai_after_Use.set(urukhai_after)
            mordorOrcs_after_Use.set(mordorOrcs_after)
            Goblins_after_Use.set(Goblins_after)
            while enemy_attack_power > 0 and total_ally_forces > 0:
                if float(cavalry) > 0 and float(swordsMen) == 0 and float(spearMen) == 0 and float(archers) == 0:
                    enemy_damage_cavalry = 0.7 * enemy_attack_power
                if float(cavalry) == 0 and float(swordsMen) > 0 and float(spearMen) == 0 and float(archers) == 0:
                    enemy_damage_swordsMen = 0.7 * enemy_attack_power
                if float(cavalry) == 0 and float(swordsMen) == 0 and float(spearMen) > 0 and float(archers) == 0:
                    enemy_damage_spearMen = 0.9 * enemy_attack_power
                if float(cavalry) == 0 and float(swordsMen) == 0 and float(spearMen) == 0 and float(archers) > 0:
                    enemy_damage_archers = 0.95 * enemy_attack_power
                else:
                    enemy_damage_archers = 0.95 * 0.2 * enemy_attack_power
                    enemy_damage_cavalry = 0.7 * 0.275 * enemy_attack_power
                    enemy_damage_swordsMen = 0.7 * 0.275 * enemy_attack_power
                    enemy_damage_spearMen = 0.9 * 0.25  * enemy_attack_power

                if enemy_damage_archers >= 10 * float(archers):
                    enemy_damage_archers -= 10 * float(archers)
                    archers = "0"
                    enemy_damage_archers = enemy_damage_archers/0.95
                else:
                    archers = str(float(archers) - enemy_damage_archers/10)
                    enemy_damage_archers = 0
                    if float(archers) < 0:
                        archers = "0"
                if enemy_damage_cavalry >= 15 * float(cavalry):
                    enemy_damage_cavalry -= 15 * float(cavalry)
                    cavalry = "0"
                    enemy_damage_cavalry = enemy_damage_cavalry/0.7
                else:
                    cavalry = str(float(cavalry) - enemy_damage_cavalry/15)
                    enemy_damage_cavalry = 0
                    if float(cavalry) < 0:
                        cavalry = "0"
                if enemy_damage_swordsMen >= 20 * float(swordsMen):
                    enemy_damage_swordsMen -= 20 * float(swordsMen)
                    swordsMen = "0"
                    enemy_damage_swordsMen = enemy_damage_swordsMen/0.7
                else:
                    swordsMen = str(float(swordsMen) - enemy_damage_swordsMen/10)
                    enemy_damage_swordsMen = 0
                    if float(swordsMen) < 0:
                        swordsMen = "0"
                if enemy_damage_spearMen >= 30 * float(spearMen):
                    enemy_damage_spearMen -= 30 * float(spearMen)
                    spearMen = "0"
                    enemy_damage_spearMen = enemy_damage_spearMen/0.9
                else:
                    spearMen = str(float(spearMen) - enemy_damage_spearMen/10)
                    enemy_damage_spearMen = 0
                    if float(spearMen) < 0:
                        spearMen = "0"
                enemy_attack_power = enemy_damage_archers + enemy_damage_cavalry + enemy_damage_swordsMen + enemy_damage_spearMen
                if enemy_attack_power < 1:
                    enemy_attack_power = 0
                total_ally_forces = round(float(spearMen)) + round(float(swordsMen)) + round(float(cavalry)) + round(float(archers))
                if total_ally_forces < 1:
                    total_ally_forces = 0
            cavalry = str(round(float(cavalry)))
            swordsMen = str(round(float(swordsMen)))
            spearMen = str(round(float(spearMen)))
            archers = str(round(float(archers)))
            cavalryUse.set(cavalry)
            swordsMenUse.set(swordsMen)
            spearMenUse.set(spearMen)
            archersUse.set(archers)
        updateMap()
        healthloss = 0
        castleHealthBefore = float(castleHealth)
        castleHealth = float(castleHealth)
        if total_ally_forces == 0 and total_opposing_forces == 0:
            if total_ally_forces_before >= 1000:
                castleHealth = str(round((0.8 * float(castleHealth))))
            else:
                castleHealth = str(round((0.95 * float(castleHealth))))
        if total_ally_forces > 0:
            if total_ally_forces_before >= 1000:
                if total_ally_forces < (1/2) * total_ally_forces_before:
                    castleHealth = str(round((0.8 * float(castleHealth))))
            else:
                if total_ally_forces < (1/2) * total_ally_forces_before:
                    castleHealth = str(round((0.95 * float(castleHealth))))
        if total_opposing_forces > 0:
            if total_ally_forces_before >= 1000:
                castleHealthholder =  str(round((0.2 * float(castleHealth))))
                castleHealth -= (4 * round(trolls) + 4 * round(uruk_Hai) + 2 * round(mordor_Orcs) + 6 * round(goblins))
                castleHealth -= float(castleHealthholder)
                castleHealth = str(castleHealth)
            else:
                castleHealthholder =  str(round((0.05 * float(castleHealth))))
                castleHealth -= (4 * round(trolls) + 4 * round(uruk_Hai) + 2 * round(mordor_Orcs) + 6 * round(goblins))
                castleHealth -= float(castleHealthholder)
                castleHealth = str(castleHealth)

        if float(castleHealth) <= 0:
            gameOverLbl.place(x = 0, y = 0)
            gameOverText = "You Survived For " + str(day) + " Days"
            gameOverTextUse.set(gameOverText)
            gameOverTextLbl.place(x = 773.5, y = 500, anchor = "center")
            restartGameButton.place(x = 773.5, y = 600, anchor = "center")

        healthloss = round(float(castleHealthBefore) - float(castleHealth))
        healthloss = str(int((-1 * healthloss)))
        castleHealth = int(float(castleHealth))
        castleHealthUse.set(castleHealth)
        healthlossUse.set(healthloss)

        troopsLost = round(float(total_ally_forces_before) - float(total_ally_forces))
        opponentLost = round(float(total_opposing_forces_before) - float(total_opposing_forces))
        troopsLostUse.set(troopsLost)
        enemyKilledUse.set(opponentLost)








    if attack == False:
        nextDayBannerLbl.place(x = 0, y = 0)
        nextDayBannerLbl.after(600, pauser)

def battle_report():
    anAttackOccuredLbl.pack()
    anAttackOccuredLbl.pack_forget()
    battleReportLabel.place(x = 700,y = 400, anchor = "center")
    cavalryBeforeLbl.place(x = 610, y = 265, anchor = "center")
    swordsMenBeforeLbl.place(x = 610, y = 286, anchor = "center")
    spearMenBeforeLbl.place(x  = 610, y = 307, anchor = "center")
    archersBeforeLbl.place(x  = 610, y = 328, anchor = "center")
    trollsafterLbl.place(x = 950, y = 490, anchor = "center")
    urukhaiafterLbl.place(x = 950, y = 511, anchor = "center")
    mordorOrcsafterLbl.place(x = 950, y = 532, anchor = "center")
    GoblinsafterLbl.place(x = 950, y = 553, anchor = "center")
    cavalryLbl.place(x = 610, y = 490, anchor = "center")
    swordsMenLbl.place(x = 610, y = 511, anchor = "center")
    spearMenLbl.place(x = 610, y = 532, anchor = "center")
    archersLbl.place(x = 610, y = 553, anchor = "center")
    trollsLbl.place(x  = 950, y = 265, anchor = "center")
    urukhaiLbl.place(x = 950, y = 286, anchor = "center")
    mordorOrcsLbl.place(x = 950, y = 307, anchor = "center")
    GoblinsLbl.place(x = 950, y = 328, anchor = "center")
    healthlossLbl.place(x = 590, y = 673, anchor = "center")
    troopsLostLbl.place(x = 590 , y = 640, anchor = "center")
    enemyKilledLbl.place(x = 920, y = 640, anchor = "center")

def pauser():
    nextDayBannerLbl.pack()
    nextDayBannerLbl.pack_forget()
    notEnoughFundingLbl.pack()
    notEnoughFundingLbl.pack_forget()
    upgradeStrongholdLbl.pack()
    upgradeStrongholdLbl.pack_forget()

def returnMenu():
    global current
    slotDestruct()
    pauser()
    instructionBackGroundLbl.pack()
    instructionBackGroundLbl.pack_forget()
    castleOutlineLabel.pack()
    castleOutlineLabel.pack_forget()
    slot1EmptyLabel.pack()
    slot1EmptyLabel.pack_forget()
    slot2EmptyLabel.pack()
    slot2EmptyLabel.pack_forget()
    slot3EmptyLabel.pack()
    slot3EmptyLabel.pack_forget()
    slot4EmptyLabel.pack()
    slot4EmptyLabel.pack_forget()
    slot5EmptyLabel.pack()
    slot5EmptyLabel.pack_forget()
    slot6EmptyLabel.pack()
    slot6EmptyLabel.pack_forget()
    slot7EmptyLabel.pack()
    slot7EmptyLabel.pack_forget()
    slot8EmptyLabel.pack()
    slot8EmptyLabel.pack_forget()
    slot9EmptyLabel.pack()
    slot9EmptyLabel.pack_forget()
    slot10EmptyLabel.pack()
    slot10EmptyLabel.pack_forget()
    slot11EmptyLabel.pack()
    slot11EmptyLabel.pack_forget()
    slot12EmptyLabel.pack()
    slot12EmptyLabel.pack_forget()
    slot13EmptyLabel.pack()
    slot13EmptyLabel.pack_forget()
    slot14EmptyLabel.pack()
    slot14EmptyLabel.pack_forget()
    slot15EmptyLabel.pack()
    slot15EmptyLabel.pack_forget()
    slot16EmptyLabel.pack()
    slot16EmptyLabel.pack_forget()
    slot17EmptyLabel.pack()
    slot17EmptyLabel.pack_forget()
    slot18EmptyLabel.pack()
    slot18EmptyLabel.pack_forget()
    slot19EmptyLabel.pack()
    slot19EmptyLabel.pack_forget()
    slot20EmptyLabel.pack()
    slot20EmptyLabel.pack_forget()
    slot21EmptyLabel.pack()
    slot21EmptyLabel.pack_forget()
    slot22EmptyLabel.pack()
    slot22EmptyLabel.pack_forget()
    slot23EmptyLabel.pack()
    slot23EmptyLabel.pack_forget()
    slot24EmptyLabel.pack()
    slot24EmptyLabel.pack_forget()
    strongHoldLabel.pack()
    strongHoldLabel.pack_forget()
    ResourceTabLabel.pack()
    ResourceTabLabel.pack_forget()

    lodgeLabel1.pack()
    lodgeLabel1.pack_forget()
    lodgeLabel2.pack()
    lodgeLabel2.pack_forget()
    lodgeLabel3.pack()
    lodgeLabel3.pack_forget()
    lodgeLabel4.pack()
    lodgeLabel4.pack_forget()
    lodgeLabel5.pack()
    lodgeLabel5.pack_forget()
    lodgeLabel6.pack()
    lodgeLabel6.pack_forget()
    lodgeLabel7.pack()
    lodgeLabel7.pack_forget()
    lodgeLabel8.pack()
    lodgeLabel8.pack_forget()
    lodgeLabel9.pack()
    lodgeLabel9.pack_forget()
    lodgeLabel10.pack()
    lodgeLabel10.pack_forget()
    lodgeLabel11.pack()
    lodgeLabel11.pack_forget()
    lodgeLabel12.pack()
    lodgeLabel12.pack_forget()
    lodgeLabel13.pack()
    lodgeLabel13.pack_forget()
    lodgeLabel14.pack()
    lodgeLabel14.pack_forget()
    lodgeLabel15.pack()
    lodgeLabel15.pack_forget()
    lodgeLabel16.pack()
    lodgeLabel16.pack_forget()
    lodgeLabel17.pack()
    lodgeLabel17.pack_forget()
    lodgeLabel18.pack()
    lodgeLabel18.pack_forget()
    lodgeLabel19.pack()
    lodgeLabel19.pack_forget()
    lodgeLabel20.pack()
    lodgeLabel20.pack_forget()
    lodgeLabel21.pack()
    lodgeLabel21.pack_forget()
    lodgeLabel22.pack()
    lodgeLabel22.pack_forget()
    lodgeLabel23.pack()
    lodgeLabel23.pack_forget()
    lodgeLabel24.pack()
    lodgeLabel24.pack_forget()
    oreRefineryLabel1.pack()
    oreRefineryLabel1.pack_forget()
    oreRefineryLabel2.pack()
    oreRefineryLabel2.pack_forget()
    oreRefineryLabel3.pack()
    oreRefineryLabel3.pack_forget()
    oreRefineryLabel4.pack()
    oreRefineryLabel4.pack_forget()
    oreRefineryLabel5.pack()
    oreRefineryLabel5.pack_forget()
    oreRefineryLabel6.pack()
    oreRefineryLabel6.pack_forget()
    oreRefineryLabel7.pack()
    oreRefineryLabel7.pack_forget()
    oreRefineryLabel8.pack()
    oreRefineryLabel8.pack_forget()
    oreRefineryLabel9.pack()
    oreRefineryLabel9.pack_forget()
    oreRefineryLabel10.pack()
    oreRefineryLabel10.pack_forget()
    oreRefineryLabel11.pack()
    oreRefineryLabel11.pack_forget()
    oreRefineryLabel12.pack()
    oreRefineryLabel12.pack_forget()
    oreRefineryLabel13.pack()
    oreRefineryLabel13.pack_forget()
    oreRefineryLabel14.pack()
    oreRefineryLabel14.pack_forget()
    oreRefineryLabel15.pack()
    oreRefineryLabel15.pack_forget()
    oreRefineryLabel16.pack()
    oreRefineryLabel16.pack_forget()
    oreRefineryLabel17.pack()
    oreRefineryLabel17.pack_forget()
    oreRefineryLabel18.pack()
    oreRefineryLabel18.pack_forget()
    oreRefineryLabel19.pack()
    oreRefineryLabel19.pack_forget()
    oreRefineryLabel20.pack()
    oreRefineryLabel20.pack_forget()
    oreRefineryLabel21.pack()
    oreRefineryLabel21.pack_forget()
    oreRefineryLabel22.pack()
    oreRefineryLabel22.pack_forget()
    oreRefineryLabel23.pack()
    oreRefineryLabel23.pack_forget()
    oreRefineryLabel24.pack()
    oreRefineryLabel24.pack_forget()
    stoneFactoryLabel2.pack()
    stoneFactoryLabel2.pack_forget()
    stoneFactoryLabel1.pack()
    stoneFactoryLabel1.pack_forget()
    stoneFactoryLabel3.pack()
    stoneFactoryLabel3.pack_forget()
    stoneFactoryLabel4.pack()
    stoneFactoryLabel4.pack_forget()
    stoneFactoryLabel5.pack()
    stoneFactoryLabel5.pack_forget()
    stoneFactoryLabel6.pack()
    stoneFactoryLabel6.pack_forget()
    stoneFactoryLabel7.pack()
    stoneFactoryLabel7.pack_forget()
    stoneFactoryLabel8.pack()
    stoneFactoryLabel8.pack_forget()
    stoneFactoryLabel9.pack()
    stoneFactoryLabel9.pack_forget()
    stoneFactoryLabel10.pack()
    stoneFactoryLabel10.pack_forget()
    stoneFactoryLabel11.pack()
    stoneFactoryLabel11.pack_forget()
    stoneFactoryLabel12.pack()
    stoneFactoryLabel12.pack_forget()
    stoneFactoryLabel13.pack()
    stoneFactoryLabel13.pack_forget()
    stoneFactoryLabel14.pack()
    stoneFactoryLabel14.pack_forget()
    stoneFactoryLabel15.pack()
    stoneFactoryLabel15.pack_forget()
    stoneFactoryLabel16.pack()
    stoneFactoryLabel16.pack_forget()
    stoneFactoryLabel17.pack()
    stoneFactoryLabel17.pack_forget()
    stoneFactoryLabel18.pack()
    stoneFactoryLabel18.pack_forget()
    stoneFactoryLabel19.pack()
    stoneFactoryLabel19.pack_forget()
    stoneFactoryLabel20.pack()
    stoneFactoryLabel20.pack_forget()
    stoneFactoryLabel21.pack()
    stoneFactoryLabel21.pack_forget()
    stoneFactoryLabel22.pack()
    stoneFactoryLabel22.pack_forget()
    stoneFactoryLabel23.pack()
    stoneFactoryLabel23.pack_forget()
    stoneFactoryLabel24.pack()
    stoneFactoryLabel24.pack_forget()
    sawMillLabel2.pack()
    sawMillLabel2.pack_forget()
    sawMillLabel1.pack()
    sawMillLabel1.pack_forget()
    sawMillLabel3.pack()
    sawMillLabel3.pack_forget()
    sawMillLabel4.pack()
    sawMillLabel4.pack_forget()
    sawMillLabel5.pack()
    sawMillLabel5.pack_forget()
    sawMillLabel6.pack()
    sawMillLabel6.pack_forget()
    sawMillLabel7.pack()
    sawMillLabel7.pack_forget()
    sawMillLabel8.pack()
    sawMillLabel8.pack_forget()
    sawMillLabel9.pack()
    sawMillLabel9.pack_forget()
    sawMillLabel10.pack()
    sawMillLabel10.pack_forget()
    sawMillLabel11.pack()
    sawMillLabel11.pack_forget()
    sawMillLabel12.pack()
    sawMillLabel12.pack_forget()
    sawMillLabel13.pack()
    sawMillLabel13.pack_forget()
    sawMillLabel14.pack()
    sawMillLabel14.pack_forget()
    sawMillLabel15.pack()
    sawMillLabel15.pack_forget()
    sawMillLabel16.pack()
    sawMillLabel16.pack_forget()
    sawMillLabel17.pack()
    sawMillLabel17.pack_forget()
    sawMillLabel18.pack()
    sawMillLabel18.pack_forget()
    sawMillLabel19.pack()
    sawMillLabel19.pack_forget()
    sawMillLabel20.pack()
    sawMillLabel20.pack_forget()
    sawMillLabel21.pack()
    sawMillLabel21.pack_forget()
    sawMillLabel22.pack()
    sawMillLabel22.pack_forget()
    sawMillLabel23.pack()
    sawMillLabel23.pack_forget()
    sawMillLabel24.pack()
    sawMillLabel24.pack_forget()

    nextButton.pack()
    nextButton.pack_forget()

    strongHoldButton.pack()
    strongHoldButton.pack_forget()
    backButton.pack()
    backButton.pack_forget()
    nextDayButton.pack()
    nextDayButton.pack_forget()
    menuButton.pack()
    menuButton.pack_forget()
    moneyAmountLbl.pack()
    moneyAmountLbl.pack_forget()
    woodAmountLbl.pack()
    woodAmountLbl.pack_forget()
    stoneAmountLbl.pack()
    stoneAmountLbl.pack_forget()
    oreAmountLbl.pack()
    oreAmountLbl.pack_forget()
    castleHealthUseLbl.pack()
    castleHealthUseLbl.pack_forget()

    wallButton.pack()
    wallButton.pack_forget()

    backButtonMenu.pack()
    backButtonMenu.pack_forget()
    instructionTextLbl.pack()
    instructionTextLbl.pack_forget()

    troopsButton.pack()
    troopsButton.pack_forget()

    dayLbl.pack()
    dayLbl.pack_forget()
    current = 1

    castleOutlineLessThan100Label.pack()
    castleOutlineLessThan100Label.pack_forget()
    castleOutlineLessThan1000Label.pack()
    castleOutlineLessThan1000Label.pack_forget()
    castleOutlineLessThan5000Label.pack()
    castleOutlineLessThan5000Label.pack_forget()
    castleOutlineLessThan10000Label.pack()
    castleOutlineLessThan10000Label.pack_forget()
    castleOutlineLessThan15000Label.pack()
    castleOutlineLessThan15000Label.pack_forget()
    castleOutlineLessThan20000Label.pack()
    castleOutlineLessThan20000Label.pack_forget()

    gameOverLbl.pack()
    gameOverLbl.pack_forget()
    gameOverTextLbl.pack()
    gameOverTextLbl.pack_forget()

    restartGameButton.pack()
    restartGameButton.pack_forget()

    objectiveButton.pack()
    objectiveButton.pack_forget()
    functionOfButtonsButton.pack()
    functionOfButtonsButton.pack_forget()
    buildingsButton.pack()
    buildingsButton.pack_forget()
    attackAndDefenceButton.pack()
    attackAndDefenceButton.pack_forget()
    creditButton.pack()
    creditButton.pack_forget()

    MenuBackGroundLabel.place(x = 0,y = 0)
    startButton.place(x = 775, y = 350, anchor = "center")
    InstructionButton.place(x = 775, y = 450, anchor = "center")


def upgradeOther():
    global current
    global slot1Var
    global slot2Var
    global slot3Var
    global slot4Var
    global slot5Var
    global slot6Var
    global slot7Var
    global slot8Var
    global slot9Var
    global slot10Var
    global slot11Var
    global slot12Var
    global slot13Var
    global slot14Var
    global slot15Var
    global slot16Var
    global slot17Var
    global slot18Var
    global slot19Var
    global slot20Var
    global slot21Var
    global slot22Var
    global slot23Var
    global slot24Var
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if current == 2:
        if int(slot1Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot1Var[0] == "L":
                a = int(slot1Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot1Var = slot1Var.replace(slot1Var[4:],str(a))
                    slot1Lvl.set(slot1Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot1Var[0] == "O":
                a = int(slot1Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot1Var = slot1Var.replace(slot1Var[4:],str(a))
                    slot1Lvl.set(slot1Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot1Var[0] == "W":
                a = int(slot1Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot1Var = slot1Var.replace(slot1Var[4:],str(a))
                    slot1Lvl.set(slot1Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot1Var[0] == "S":
                a = int(slot1Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot1Var = slot1Var.replace(slot1Var[4:],str(a))
                    slot1Lvl.set(slot1Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")


    if current == 3:
        if int(slot2Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot2Var[0] == "L":
                a = int(slot2Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot2Var = slot2Var.replace(slot2Var[4:],str(a))
                    slot2Lvl.set(slot2Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot2Var[0] == "O":
                a = int(slot2Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot2Var = slot2Var.replace(slot2Var[4:],str(a))
                    slot2Lvl.set(slot2Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot2Var[0] == "W":
                a = int(slot2Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot2Var = slot2Var.replace(slot2Var[4:],str(a))
                    slot2Lvl.set(slot2Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot2Var[0] == "S":
                a = int(slot2Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot2Var = slot2Var.replace(slot2Var[4:],str(a))
                    slot2Lvl.set(slot2Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 4:
        if int(slot3Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot3Var[0] == "L":
                a = int(slot3Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot3Var = slot3Var.replace(slot3Var[4:],str(a))
                    slot3Lvl.set(slot3Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot3Var[0] == "O":
                a = int(slot3Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot3Var = slot3Var.replace(slot3Var[4:],str(a))
                    slot3Lvl.set(slot3Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot3Var[0] == "W":
                a = int(slot3Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot3Var = slot3Var.replace(slot3Var[4:],str(a))
                    slot3Lvl.set(slot3Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot3Var[0] == "S":
                a = int(slot3Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot3Var = slot3Var.replace(slot3Var[4:],str(a))
                    slot3Lvl.set(slot3Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")



    if current == 5:
        if int(slot4Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot4Var[0] == "L":
                a = int(slot4Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot4Var = slot4Var.replace(slot4Var[4:],str(a))
                    slot4Lvl.set(slot4Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot4Var[0] == "O":
                a = int(slot4Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot4Var = slot4Var.replace(slot4Var[4:],str(a))
                    slot4Lvl.set(slot4Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot4Var[0] == "W":
                a = int(slot4Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot4Var = slot4Var.replace(slot4Var[4:],str(a))
                    slot4Lvl.set(slot4Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot4Var[0] == "S":
                a = int(slot4Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot4Var = slot4Var.replace(slot4Var[4:],str(a))
                    slot4Lvl.set(slot4Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 6:
        if int(slot5Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot5Var[0] == "L":
                a = int(slot5Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot5Var = slot5Var.replace(slot5Var[4:],str(a))
                    slot5Lvl.set(slot5Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot5Var[0] == "O":
                a = int(slot5Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot5Var = slot5Var.replace(slot5Var[4:],str(a))
                    slot5Lvl.set(slot5Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot5Var[0] == "W":
                a = int(slot5Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot5Var = slot5Var.replace(slot5Var[4:],str(a))
                    slot5Lvl.set(slot5Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot5Var[0] == "S":
                a = int(slot5Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot5Var = slot5Var.replace(slot5Var[4:],str(a))
                    slot5Lvl.set(slot5Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 7:
        if int(slot6Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot6Var[0] == "L":
                a = int(slot6Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot6Var = slot6Var.replace(slot6Var[4:],str(a))
                    slot6Lvl.set(slot6Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
                    wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

            if slot6Var[0] == "O":
                a = int(slot6Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot6Var = slot6Var.replace(slot6Var[4:],str(a))
                    slot6Lvl.set(slot6Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

            if slot6Var[0] == "W":
                a = int(slot6Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot6Var = slot6Var.replace(slot6Var[4:],str(a))
                    slot6Lvl.set(slot6Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

            if slot6Var[0] == "S":
                a = int(slot6Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot6Var = slot6Var.replace(slot6Var[4:],str(a))
                    slot6Lvl.set(slot6Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if current == 8:

        if int(slot7Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot7Var[0] == "L":
                a = int(slot7Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot7Var = slot7Var.replace(slot7Var[4:],str(a))
                    slot7Lvl.set(slot7Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
                    wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

            if slot7Var[0] == "O":
                a = int(slot7Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot7Var = slot7Var.replace(slot7Var[4:],str(a))
                    slot7Lvl.set(slot7Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

            if slot7Var[0] == "W":
                a = int(slot7Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot7Var = slot7Var.replace(slot7Var[4:],str(a))
                    slot7Lvl.set(slot7Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

            if slot7Var[0] == "S":
                a = int(slot7Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot7Var = slot7Var.replace(slot7Var[4:],str(a))
                    slot7Lvl.set(slot7Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if current == 9:
        if int(slot8Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot8Var[0] == "L":
                a = int(slot8Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot8Var = slot8Var.replace(slot8Var[4:],str(a))
                    slot8Lvl.set(slot8Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
                    wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

            if slot8Var[0] == "O":
                a = int(slot8Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot8Var = slot8Var.replace(slot8Var[4:],str(a))
                    slot8Lvl.set(slot8Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

            if slot8Var[0] == "W":
                a = int(slot8Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot8Var = slot8Var.replace(slot8Var[4:],str(a))
                    slot8Lvl.set(slot8Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

            if slot8Var[0] == "S":
                a = int(slot8Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot8Var = slot8Var.replace(slot8Var[4:],str(a))
                    slot8Lvl.set(slot8Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if current == 10:
        if int(slot9Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot9Var[0] == "L":
                a = int(slot9Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot9Var = slot9Var.replace(slot9Var[4:],str(a))
                    slot9Lvl.set(slot9Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot9Var[0] == "O":
                a = int(slot9Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot9Var = slot9Var.replace(slot9Var[4:],str(a))
                    slot9Lvl.set(slot9Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot9Var[0] == "W":
                a = int(slot9Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot9Var = slot9Var.replace(slot9Var[4:],str(a))
                    slot9Lvl.set(slot9Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot9Var[0] == "S":
                a = int(slot9Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot9Var = slot9Var.replace(slot9Var[4:],str(a))
                    slot9Lvl.set(slot9Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 11:
        if int(slot10Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot10Var[0] == "L":
                a = int(slot10Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot10Var = slot10Var.replace(slot10Var[4:],str(a))
                    slot10Lvl.set(slot10Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot10Var[0] == "O":
                a = int(slot10Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot10Var = slot10Var.replace(slot10Var[4:],str(a))
                    slot10Lvl.set(slot10Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot10Var[0] == "W":
                a = int(slot10Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot10Var = slot10Var.replace(slot10Var[4:],str(a))
                    slot10Lvl.set(slot10Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot10Var[0] == "S":
                a = int(slot10Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot10Var = slot10Var.replace(slot10Var[4:],str(a))
                    slot10Lvl.set(slot10Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 12:
        if int(slot11Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot11Var[0] == "L":
                a = int(slot11Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot11Var = slot11Var.replace(slot11Var[4:],str(a))
                    slot11Lvl.set(slot11Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot11Var[0] == "O":
                a = int(slot11Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot11Var = slot11Var.replace(slot11Var[4:],str(a))
                    slot11Lvl.set(slot11Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot11Var[0] == "W":
                a = int(slot11Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot11Var = slot11Var.replace(slot11Var[4:],str(a))
                    slot11Lvl.set(slot11Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot11Var[0] == "S":
                a = int(slot11Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot11Var = slot11Var.replace(slot11Var[4:],str(a))
                    slot11Lvl.set(slot11Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 13:
        if int(slot12Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot12Var[0] == "L":
                a = int(slot12Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot12Var = slot12Var.replace(slot12Var[4:],str(a))
                    slot12Lvl.set(slot12Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot12Var[0] == "O":
                a = int(slot12Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot12Var = slot12Var.replace(slot12Var[4:],str(a))
                    slot12Lvl.set(slot12Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot12Var[0] == "W":
                a = int(slot12Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot12Var = slot12Var.replace(slot12Var[4:],str(a))
                    slot12Lvl.set(slot12Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot12Var[0] == "S":
                a = int(slot12Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot12Var = slot12Var.replace(slot12Var[4:],str(a))
                    slot12Lvl.set(slot12Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 14:
        if int(slot13Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot13Var[0] == "L":
                a = int(slot13Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot13Var = slot13Var.replace(slot13Var[4:],str(a))
                    slot13Lvl.set(slot13Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot13Var[0] == "O":
                a = int(slot13Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot13Var = slot13Var.replace(slot13Var[4:],str(a))
                    slot13Lvl.set(slot13Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot13Var[0] == "W":
                a = int(slot13Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot13Var = slot13Var.replace(slot13Var[4:],str(a))
                    slot13Lvl.set(slot13Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot13Var[0] == "S":
                a = int(slot13Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot13Var = slot13Var.replace(slot13Var[4:],str(a))
                    slot13Lvl.set(slot13Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 15:
        if int(slot14Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot14Var[0] == "L":
                a = int(slot14Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot14Var = slot14Var.replace(slot14Var[4:],str(a))
                    slot14Lvl.set(slot14Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
                    wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

            if slot14Var[0] == "O":
                a = int(slot14Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot14Var = slot14Var.replace(slot14Var[4:],str(a))
                    slot14Lvl.set(slot14Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

            if slot14Var[0] == "W":
                a = int(slot14Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot14Var = slot14Var.replace(slot14Var[4:],str(a))
                    slot14Lvl.set(slot14Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

            if slot14Var[0] == "S":
                a = int(slot14Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot14Var = slot14Var.replace(slot14Var[4:],str(a))
                    slot14Lvl.set(slot14Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if current == 16:
        if int(slot15Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot15Var[0] == "L":
                a = int(slot15Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot15Var = slot15Var.replace(slot15Var[4:],str(a))
                    slot15Lvl.set(slot15Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
                    wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

            if slot15Var[0] == "O":
                a = int(slot15Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot15Var = slot15Var.replace(slot15Var[4:],str(a))
                    slot15Lvl.set(slot15Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

            if slot15Var[0] == "W":
                a = int(slot15Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot15Var = slot15Var.replace(slot15Var[4:],str(a))
                    slot15Lvl.set(slot15Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

            if slot15Var[0] == "S":
                a = int(slot15Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot15Var = slot15Var.replace(slot15Var[4:],str(a))
                    slot15Lvl.set(slot15Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if current == 17:
        if int(slot16Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot16Var[0] == "L":
                a = int(slot16Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot16Var = slot16Var.replace(slot16Var[4:],str(a))
                    slot16Lvl.set(slot16Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
                    wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

            if slot16Var[0] == "O":
                a = int(slot16Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot16Var = slot16Var.replace(slot16Var[4:],str(a))
                    slot16Lvl.set(slot16Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

            if slot16Var[0] == "W":
                a = int(slot16Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot16Var = slot16Var.replace(slot16Var[4:],str(a))
                    slot16Lvl.set(slot16Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

            if slot16Var[0] == "S":
                a = int(slot16Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot16Var = slot16Var.replace(slot16Var[4:],str(a))
                    slot16Lvl.set(slot16Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if current == 18:
        if int(slot17Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot17Var[0] == "L":
                a = int(slot17Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot17Var = slot17Var.replace(slot17Var[4:],str(a))
                    slot17Lvl.set(slot17Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot17Var[0] == "O":
                a = int(slot17Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot17Var = slot17Var.replace(slot17Var[4:],str(a))
                    slot17Lvl.set(slot17Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot17Var[0] == "W":
                a = int(slot17Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot17Var = slot17Var.replace(slot17Var[4:],str(a))
                    slot17Lvl.set(slot17Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot17Var[0] == "S":
                a = int(slot17Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot17Var = slot17Var.replace(slot17Var[4:],str(a))
                    slot17Lvl.set(slot17Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 19:
        if int(slot18Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot18Var[0] == "L":
                a = int(slot18Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot18Var = slot18Var.replace(slot18Var[4:],str(a))
                    slot18Lvl.set(slot18Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot18Var[0] == "O":
                a = int(slot18Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot18Var = slot18Var.replace(slot18Var[4:],str(a))
                    slot18Lvl.set(slot18Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot18Var[0] == "W":
                a = int(slot18Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot18Var = slot18Var.replace(slot18Var[4:],str(a))
                    slot18Lvl.set(slot18Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot18Var[0] == "S":
                a = int(slot18Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot18Var = slot18Var.replace(slot18Var[4:],str(a))
                    slot18Lvl.set(slot18Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 20:
        if int(slot19Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot19Var[0] == "L":
                a = int(slot19Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot19Var = slot19Var.replace(slot19Var[4:],str(a))
                    slot19Lvl.set(slot19Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot19Var[0] == "O":
                a = int(slot19Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot19Var = slot19Var.replace(slot19Var[4:],str(a))
                    slot19Lvl.set(slot19Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot19Var[0] == "W":
                a = int(slot19Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot19Var = slot19Var.replace(slot19Var[4:],str(a))
                    slot19Lvl.set(slot19Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot19Var[0] == "S":
                a = int(slot19Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot19Var = slot19Var.replace(slot19Var[4:],str(a))
                    slot19Lvl.set(slot19Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 21:
        if int(slot20Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot20Var[0] == "L":
                a = int(slot20Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot20Var = slot20Var.replace(slot20Var[4:],str(a))
                    slot20Lvl.set(slot20Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot20Var[0] == "O":
                a = int(slot20Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot20Var = slot20Var.replace(slot20Var[4:],str(a))
                    slot20Lvl.set(slot20Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot20Var[0] == "W":
                a = int(slot20Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot20Var = slot20Var.replace(slot20Var[4:],str(a))
                    slot20Lvl.set(slot20Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot20Var[0] == "S":
                a = int(slot20Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot20Var = slot20Var.replace(slot20Var[4:],str(a))
                    slot20Lvl.set(slot20Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 22:
        if int(slot21Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot21Var[0] == "L":
                a = int(slot21Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot21Var = slot21Var.replace(slot21Var[4:],str(a))
                    slot21Lvl.set(slot21Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 180, y = 477, anchor = "center")
                    wood_upgradeLbl.place(x = 180, y = 501, anchor = "center")

            if slot21Var[0] == "O":
                a = int(slot21Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot21Var = slot21Var.replace(slot21Var[4:],str(a))
                    slot21Lvl.set(slot21Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 180, y = 510, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 486, anchor = "center")

            if slot21Var[0] == "W":
                a = int(slot21Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot21Var = slot21Var.replace(slot21Var[4:],str(a))
                    slot21Lvl.set(slot21Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 180, y = 505, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 481, anchor = "center")

            if slot21Var[0] == "S":
                a = int(slot21Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot21Var = slot21Var.replace(slot21Var[4:],str(a))
                    slot21Lvl.set(slot21Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 190, y = 590, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 180, y = 537, anchor = "center")
                    gold_upgradeLbl.place(x = 180, y = 513, anchor = "center")

    if current == 23:
        if int(slot22Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot22Var[0] == "L":
                a = int(slot22Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot22Var = slot22Var.replace(slot22Var[4:],str(a))
                    slot22Lvl.set(slot22Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot22Var[0] == "O":
                a = int(slot22Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot22Var = slot22Var.replace(slot22Var[4:],str(a))
                    slot22Lvl.set(slot22Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot22Var[0] == "W":
                a = int(slot22Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot22Var = slot22Var.replace(slot22Var[4:],str(a))
                    slot22Lvl.set(slot22Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot22Var[0] == "S":
                a = int(slot22Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot22Var = slot22Var.replace(slot22Var[4:],str(a))
                    slot22Lvl.set(slot22Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 24:
        if int(slot23Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:
            if slot23Var[0] == "L":
                a = int(slot23Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot23Var = slot23Var.replace(slot23Var[4:],str(a))
                    slot23Lvl.set(slot23Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot23Var[0] == "O":
                a = int(slot23Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot23Var = slot23Var.replace(slot23Var[4:],str(a))
                    slot23Lvl.set(slot23Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot23Var[0] == "W":
                a = int(slot23Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot23Var = slot23Var.replace(slot23Var[4:],str(a))
                    slot23Lvl.set(slot23Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot23Var[0] == "S":
                a = int(slot23Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot23Var = slot23Var.replace(slot23Var[4:],str(a))
                    slot23Lvl.set(slot23Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

    if current == 25:
        if int(slot24Var[4:]) >= int(strongHoldLvl):
            upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
            upgradeStrongholdLbl.after(1000, pauser)
        else:

            if slot24Var[0] == "L":
                a = int(slot24Var[4:]) + 1
                if m < (500 + 50*(a-2)) or w < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 500 - 50*(a - 2)
                    wood = w - 300 - 30*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot24Var = slot24Var.replace(slot24Var[4:],str(a))
                    slot24Lvl.set(slot24Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 500 + 50*(a-1)
                    wood_up = 300 + 30*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    gold_upgradeLbl.place(x = 1170, y = 279, anchor = "center")
                    wood_upgradeLbl.place(x = 1170, y = 303, anchor = "center")

            if slot24Var[0] == "O":
                a = int(slot24Var[4:]) + 1
                if o < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    ore = o - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    oreResource = str(ore)
                    moneyAmount.set(moneyResource)
                    oreAmount.set(oreResource)

                    slot24Var = slot24Var.replace(slot24Var[4:],str(a))
                    slot24Lvl.set(slot24Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    ore_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    ore_upgradeUse.set(str(ore_up))
                    ore_upgradeLbl.place(x = 1170, y = 308, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 285, anchor = "center")

            if slot24Var[0] == "W":
                a = int(slot24Var[4:]) + 1
                if w < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    wood = w - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    woodResource = str(wood)
                    moneyAmount.set(moneyResource)
                    woodAmount.set(woodResource)

                    slot24Var = slot24Var.replace(slot24Var[4:],str(a))
                    slot24Lvl.set(slot24Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    wood_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    wood_upgradeUse.set(str(wood_up))
                    wood_upgradeLbl.place(x = 1170, y = 305, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 281, anchor = "center")

            if slot24Var[0] == "S":
                a = int(slot24Var[4:]) + 1
                if s < (500 + 50*(a-2)) or m < (300 + 30*(a-2)):
                    notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
                    notEnoughFundingLbl.after(1000, pauser)
                else:
                    gold = m - 300 - 30*(a - 2)
                    stone = s - 500 - 50*(a - 2)
                    moneyResource = str(gold)
                    stoneResource = str(stone)
                    moneyAmount.set(moneyResource)
                    stoneAmount.set(stoneResource)

                    slot24Var = slot24Var.replace(slot24Var[4:],str(a))
                    slot24Lvl.set(slot24Var[4:])

                    level_actual = 300 + 50*(a - 1)
                    productionUse.set(str(level_actual))
                    productionUseLbl.place(x = 1190, y = 387, anchor = "center")

                    gold_up = 300 + 30*(a-1)
                    stone_up = 500 + 50*(a-1)
                    gold_upgradeUse.set(str(gold_up))
                    stone_upgradeUse.set(str(stone_up))
                    stone_upgradeLbl.place(x = 1170, y = 337, anchor = "center")
                    gold_upgradeLbl.place(x = 1170, y = 313, anchor = "center")

def runInstruction():
    startButton.pack()
    startButton.pack_forget()
    InstructionButton.pack()
    InstructionButton.pack_forget()
    MenuBackGroundLabel.pack()
    MenuBackGroundLabel.pack_forget()
    instructionBackGroundLbl.place(x = 0, y = 0)
    backButtonMenu.place(x = 777.5, y = 690, anchor = "center")
    objectiveButton.place(x = 259.17, y = 100, anchor = "center")
    functionOfButtonsButton.place(x = 518.3333, y = 100, anchor = "center")
    buildingsButton.place(x = 777.5, y = 100, anchor = "center")
    attackAndDefenceButton.place(x  = 1036.66, y= 100, anchor = "center")
    creditButton.place(x = 1295.83,  y = 100, anchor = "center")

def showObjective():
    instructionText = '''
You are the commander and city planner of Minas Tirith at the height
of the war of the ring. The objective of the game is for you to ensure
that the city will survive the coming onslaught of the forces of Mordor
and the barbaric Easterlings for as many days as possible. You will
start out your adventure with 20 thousands unit of each resource and also
a 10 days period of peace where no opposing forces will attempt to breach
the city. Once the castle Health reaches 0, the walls have fallen and the
city sacked. The game will be over once castle Health reaches 0.
    '''

    instructionTextUse.set(instructionText)
    instructionTextLbl.place(x = 830, y = 400, anchor = "center")
def showfunctionOfButtons():
    instructionText = '''
Once you have started the game, you will be able to see that there are 7 buttons by the side bar.
These 7 buttons will be the buttons you use to navigate around the game. The functions of the
Buttons are as follows:

Next:
This Button is use to traverse to all building slots in Minas Tirith. Once you click on this Button,
the building slot that you are currently in will turn red. If the building slot is ioccupied with a
building, then the building itself will turn red.

Stronghold:
This Button is used to access the stronghold. Every building in this Minas Tirith must either be
similar in level to the stronghold or lower.

Back:
This Button is use to return to Minas Tirith. Use this button to return to the city after viewing
a building spot, the wall, the stronghold, or a battle report.

Wall:
Use this Button to access the Wall. You can upgrade the wall or heal the castle while viewing the
wall. You will know that you are viewing the wall once the wall is red.

Troops:
This Button allows you to access and train Troops. There are 4 types of troops: cavalry, swordsmen,
spearmen, and archers.

Menu:
The Menu Button allows you to return to the Menu.

Next Day:
Next Day Button allows you to move on to the next day, which you will recieve goods from the buildings
and also a chance of being attacked by the opposing forces. The higher the days you are in, the higher
the chance of you being attacked and by more forces.
    '''

    instructionTextUse.set(instructionText)
    instructionTextLbl.place(x = 830, y = 390, anchor = "center")
    
def showBuildingsFunction():
    instructionText = '''
There are 4 builings that can be built in any building slots and a stronghold in the middle
of Minas Tirith. Each building will produce a unique type of resources such as Gold, Wood,
Ore and Stone.

Lodge:
Lodges produce 300 Gold at level one and have an increase producion of 30 gold per new level
per day. The cost to upgrade any Lodge is 500 gold and 300 wood at level one with an increase
of 50 more gold and 30 more wood to upgrade per level.

Ore Refinery:
Ore refineries produce 300 ore at level one and have an increase production of 30 ore per new
level per day. The cost to upgrade any refinery is 300 gold and 500 ore at level one with an
increase of 30 more gold and 50 more ore to upgrade per level.

Sawmill:
Sawmills produce 300 wood at level one and have an increase production of 30 wood per new level
per day. The cost to upgrade any sawmill is 300 gold and 500 wood at level one with an increase
of 30 more gold and 50 more wood to upgrade per level.

Stone Factory:
Stone Factory produce 300 stone at level one and have an increase production of 30 stone per new
level per day. The cost to upgrade any factory is 300 gold and 500 stone at level one with an
increase of 30 more gold and 50 more stone to upgrade per level.

StrongHold:
The Stronghold produces no resources and only serves as a method to control the level of all other
buildings. All other buildings and structures in Minas Tirith must have the same level as the
StrongHold or less than the StrongHold.

Wall:
The Wall is the most crucial layer of defense in Minas Tirith. The wall also determines the health
of Minas Tirith. When accesing the wall, the health of the castle can be healed and the wall itself
can be upgraded. For each new level of the wall, the maximum health of the castle is increased by 2.
    '''

    instructionTextUse.set(instructionText)
    instructionTextLbl.place(x = 830, y = 390, anchor = "center")
    
def showAttackAndDefence():
    instructionText = '''
There are 4 types of troops in your army and 4 types of opposing troops.

Your troops include:                                Opposing troops include:

Cavalry                                                      Trolls
Attack - 15                                                Attack - 20
Health - 15                                               Health - 15
Defense - 30                                             Defense - 40

Swordsmen                                              Uruk-Hai
Attack - 20			   Attack - 20
Health - 10			   Health - 15
Defense - 30			   Defense - 30

Spearmen                                                  Mordor Orcs
Attack - 30			   Attack - 10
Health - 10			   Health - 10
Defense - 10			   Defense - 20

Archers                                                      Goblins
Attack - 35			   Attack - 30
Health - 10			   Health - 5
Defense - 5			   Defense - 10
    '''

    instructionTextUse.set(instructionText)
    instructionTextLbl.place(x = 830, y = 390, anchor = "center")
    
def credit_final():
    instructionText = '''
Thomas Nguyen, EngSci 2T4 at UofT
Email: tomnguyenvn63@gmail.com
instagram: tom_nguyen_bc
    '''

    instructionTextUse.set(instructionText)
    instructionTextLbl.place(x = 777.5, y = 390, anchor = "center")
    

def openWall():
    slotDestruct()
    wallClickedLabel.place(x = 0,y = 0)
    wallInfoLabel.place(x = 1200, y = 300, anchor = "center")
    wallLvlLbl.place(x = 1150, y = 438, anchor = "center")
    wallDefenseLbl.place(x = 1180, y = 455, anchor = "center")
    wallUpgradeButton.place(x = 1120, y = 495, anchor = "center")
    wallHealButton.place(x = 1250, y = 495, anchor = "center")
    gold = 300 + 50*(int(wallLvl) - 1)
    gold_upgradeUse.set(gold)
    wood = 100 + 20*(int(wallLvl) - 1)
    wood_upgradeUse.set(wood)
    stone = 300 + 50*(int(wallLvl) - 1)
    stone_upgradeUse.set(stone)
    ore = 100 + 20*(int(wallLvl) - 1)
    ore_upgradeUse.set(ore)
    ore_upgradeLbl.place(x = 1185, y = 314, anchor = "center")
    stone_upgradeLbl.place(x = 1185, y = 280, anchor = "center")
    wood_upgradeLbl.place(x = 1185, y = 297, anchor = "center")
    gold_upgradeLbl.place(x = 1185, y = 263, anchor = "center")
    heal_needed = float(maxhealth) - float(castleHealth)
    ore_healUse.set(str(5 * int(heal_needed)))
    gold_healUse.set(str(5 * int(heal_needed)))
    wood_healUse.set(str(5 * int(heal_needed)))
    stone_healUse.set(str(5 * int(heal_needed)))
    gold_healLbl.place(x = 1185, y = 362, anchor = "center")
    stone_healLbl.place(x = 1185, y = 379, anchor = "center")
    wood_healLbl.place(x = 1185, y = 396, anchor = "center")
    ore_healLbl.place(x = 1185, y = 413, anchor = "center")



def upgradeWall():
    global wallLvl
    global wallDefense
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    global maxhealth
    if int(wallLvl) >= int(strongHoldLvl):
        upgradeStrongholdLbl.place(x = 777.5, y = 400, anchor = "center")
        upgradeStrongholdLbl.after(1000, pauser)
    else:
        m = int(moneyResource)
        w = int(woodResource)
        s = int(stoneResource)
        o = int(oreResource)
        a = int(wallLvl)
        if m < (300 + 50*(a - 1)) or w < (100 + 20*(a-1)) or s < (300 + 50*(a-1)) or o <(100 + 20*(a-1)):
            notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
            notEnoughFundingLbl.after(1000, pauser)
        else:
            money  = int(moneyResource) - (300 + 50*(a - 1))
            wood = int(woodResource) - (100 + 20*(a-1))
            stone = int(stoneResource) - (300 + 50*(a-1))
            ore = int(oreResource) - (100 + 20*(a-1))

            moneyResource = str(money)
            woodResource = str(wood)
            stoneResource = str(stone)
            oreResource = str(ore)

            moneyAmount.set(str(money))
            woodAmount.set(str(wood))
            stoneAmount.set(str(stone))
            oreAmount.set(str(ore))

            a += 1
            wallLvl = str(a)
            wallLvlUse.set(wallLvl)
            b = (10 * a) - 10
            wallDefense = str(b + 100)
            wallDefenseUse.set(wallDefense)
            maxhealth = str(100 + b)

            gold = 300 + 50*(int(wallLvl) - 1)
            gold_upgradeUse.set(gold)
            wood_2 = 100 + 20*(int(wallLvl) - 1)
            wood_upgradeUse.set(wood_2)
            stone_2 = 300 + 50*(int(wallLvl) - 1)
            stone_upgradeUse.set(stone_2)
            ore_2 = 100 + 20*(int(wallLvl) - 1)
            ore_upgradeUse.set(ore_2)
            ore_upgradeLbl.place(x = 1185, y = 314, anchor = "center")
            stone_upgradeLbl.place(x = 1185, y = 280, anchor = "center")
            wood_upgradeLbl.place(x = 1185, y = 297, anchor = "center")
            gold_upgradeLbl.place(x = 1185, y = 263, anchor = "center")

            heal_needed = float(maxhealth) - float(castleHealth)
            ore_healUse.set(str(5 * int(heal_needed)))
            gold_healUse.set(str(5 * int(heal_needed)))
            wood_healUse.set(str(5 * int(heal_needed)))
            stone_healUse.set(str(5 * int(heal_needed)))
            gold_healLbl.place(x = 1185, y = 362, anchor = "center")
            stone_healLbl.place(x = 1185, y = 379, anchor = "center")
            wood_healLbl.place(x = 1185, y = 396, anchor = "center")
            ore_healLbl.place(x = 1185, y = 413, anchor = "center")

def healWall():
    global castleHealth
    global maxhealth
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    a = int(float(maxhealth) - float(castleHealth))
    if m < 5*a or w < 5*a or s < 5*a or o < 5*a:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        castleHealth = maxhealth
        castleHealthUse.set(str(maxhealth))
        moneyAmount.set(str(m - 5*a))
        woodAmount.set(str(w - 5*a))
        stoneAmount.set(str(s - 5*a))
        oreAmount.set(str(o - 5*a))

        ore_healUse.set("0")
        gold_healUse.set("0")
        wood_healUse.set("0")
        stone_healUse.set("0")

def demolishBuilding():
    global slot1Var
    global slot2Var
    global slot3Var
    global slot4Var
    global slot5Var
    global slot6Var
    global slot7Var
    global slot8Var
    global slot9Var
    global slot10Var
    global slot11Var
    global slot12Var
    global slot13Var
    global slot14Var
    global slot15Var
    global slot16Var
    global slot17Var
    global slot18Var
    global slot19Var
    global slot20Var
    global slot21Var
    global slot22Var
    global slot23Var
    global slot24Var
    if current == 2:
        slot1Var = "E - 1"
    if current == 3:
        slot2Var = "E - 1"
    if current == 4:
        slot3Var = "E - 1"
    if current == 5:
        slot4Var = "E - 1"
    if current == 6:
        slot5Var = "E - 1"
    if current == 7:
        slot6Var = "E - 1"
    if current == 8:
        slot7Var = "E - 1"
    if current == 9:
        slot8Var = "E - 1"
    if current == 10:
        slot9Var = "E - 1"
    if current == 11:
        slot10Var = "E - 1"
    if current == 12:
        slot11Var = "E - 1"
    if current == 13:
        slot12Var = "E - 1"
    if current == 14:
        slot13Var = "E - 1"
    if current == 15:
        slot14Var = "E - 1"
    if current == 16:
        slot15Var = "E - 1"
    if current == 17:
        slot16Var = "E - 1"
    if current == 18:
        slot17Var = "E - 1"
    if current == 19:
        slot18Var = "E - 1"
    if current == 20:
        slot19Var = "E - 1"
    if current == 21:
        slot20Var = "E - 1"
    if current == 22:
        slot21Var = "E - 1"
    if current == 23:
        slot22Var = "E - 1"
    if current == 24:
        slot23Var = "E - 1"
    if current == 25:
        slot24Var = "E - 1"
    slotDestruct()

def trainTroops():
    slotDestruct()
    troopsSelectionLabel.place(x = 700, y = 400, anchor = "center")
    cavalryLbl.place(x = 165, y = 656, anchor = "center")
    swordsMenLbl.place(x = 540, y = 651, anchor = "center")
    spearMenLbl.place(x = 905, y = 651, anchor = "center")
    archersLbl.place(x = 1280, y = 649, anchor = "center")
    trainOneCavalryButton.place(x = 70, y = 520, anchor = "center")
    trainOneSwordsMenButton.place(x = 435, y = 520, anchor = "center")
    trainOneSpearMenButton.place(x = 795, y = 520, anchor = "center")
    trainOneArchersButton.place(x = 1155, y = 520, anchor = "center")
    trainOneHundredCavalryButton.place(x = 70, y = 565, anchor = "center")
    trainOneHundredSwordsMenButton.place(x = 435, y = 565, anchor = "center")
    trainOneHundredSpearMenButton.place(x = 795, y = 565, anchor = "center")
    trainOneHundredArchersButton.place(x = 1155, y = 565, anchor = "center")
    trainOneThousandCavalryButton.place(x = 70, y = 610, anchor = "center")
    trainOneThousandSwordsMenButton.place(x = 435, y = 610, anchor = "center")
    trainOneThousandSpearMenButton.place(x = 795, y = 610, anchor = "center")
    trainOneThousandArchersButton.place(x = 1155, y = 610, anchor = "center")
    a = int(cavalry)
    b = int(swordsMen)
    c = int(spearMen)
    d = int(archers)
    e = a + b + c + d
    f = str(e)
    totalTroops = f
    totalTroopsUse.set(totalTroops)
    totalTroopsLbl.place(x = 230, y = 685, anchor = "center")


def trainOneCavalry():
    global cavalry
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 30 or s < 10 or o < 30:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 30)
        stoneResource = str(s - 10)
        oreResource = str(o - 30)

        moneyAmount.set(moneyResource)
        stoneAmount.set(stoneResource)
        oreAmount.set(oreResource)

        a = int(cavalry)
        a += 1
        cavalry = str(a)
        cavalryUse.set(cavalry)
        updateMap()
        trainTroops()

def trainOneSwordsMen():
    global swordsMen
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 30 or w < 10 or o < 30:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 30)
        woodResource = str(w - 10)
        oreResource = str(o - 30)
        moneyAmount.set(moneyResource)
        woodAmount.set(woodResource)
        oreAmount.set(oreResource)
        a = int(swordsMen) + 1
        swordsMen = str(a)
        swordsMenUse.set(swordsMen)
        updateMap()
        trainTroops()

def trainOneSpearMen():
    global spearMen
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 10 or w < 30 or o < 30:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 10)
        woodResource = str(w - 30)
        oreResource = str(o - 30)
        moneyAmount.set(moneyResource)
        woodAmount.set(woodResource)
        oreAmount.set(oreResource)
        a = int(spearMen)
        a += 1
        spearMen = str(a)
        spearMenUse.set(spearMen)
        updateMap()
        trainTroops()

def trainOneArcher():
    global archers
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 10 or w < 30 or o < 30:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 10)
        woodResource = str(w - 30)
        oreResource = str(o - 30)
        moneyAmount.set(moneyResource)
        woodAmount.set(woodResource)
        oreAmount.set(oreResource)
        a = int(archers)
        a += 1
        archers = str(a)
        archersUse.set(archers)
        updateMap()
        trainTroops()

def trainOneHundredCavalry():
    global cavalry
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 3000 or s < 1000 or o < 3000:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 3000)
        stoneResource = str(s - 1000)
        oreResource = str(o - 3000)

        moneyAmount.set(moneyResource)
        stoneAmount.set(stoneResource)
        oreAmount.set(oreResource)

        a = int(cavalry)
        a += 100
        cavalry = str(a)
        cavalryUse.set(cavalry)
        updateMap()
        trainTroops()

def trainOneHundredSwordsMen():
    global swordsMen
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 3000 or w < 1000 or o < 3000:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 3000)
        woodResource = str(w - 1000)
        oreResource = str(o - 3000)
        moneyAmount.set(moneyResource)
        woodAmount.set(woodResource)
        oreAmount.set(oreResource)
        a = int(swordsMen) + 100
        swordsMen = str(a)
        swordsMenUse.set(swordsMen)
        updateMap()
        trainTroops()

def trainOneHundredSpearMen():
    global spearMen
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 1000 or w < 3000 or o < 3000:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 1000)
        woodResource = str(w - 3000)
        oreResource = str(o - 3000)
        moneyAmount.set(moneyResource)
        woodAmount.set(woodResource)
        oreAmount.set(oreResource)
        a = int(spearMen)
        a += 100
        spearMen = str(a)
        spearMenUse.set(spearMen)
        updateMap()
        trainTroops()


def trainOneHundredArcher():
    global archers
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 1000 or w < 3000 or o < 3000:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 1000)
        woodResource = str(w - 3000)
        oreResource = str(o - 3000)
        moneyAmount.set(moneyResource)
        woodAmount.set(woodResource)
        oreAmount.set(oreResource)
        a = int(archers)
        a += 100
        archers = str(a)
        archersUse.set(archers)
        updateMap()
        trainTroops()

def trainOneThousandCavalry():
    global cavalry
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 30000 or s < 10000 or o < 30000:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 30000)
        stoneResource = str(s - 10000)
        oreResource = str(o - 30000)

        moneyAmount.set(moneyResource)
        stoneAmount.set(stoneResource)
        oreAmount.set(oreResource)

        a = int(cavalry)
        a += 1000
        cavalry = str(a)
        cavalryUse.set(cavalry)
        updateMap()
        trainTroops()

def trainOneThousandSwordsMen():
    global swordsMen
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 30000 or w < 10000 or o < 30000:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 30000)
        woodResource = str(w - 10000)
        oreResource = str(o - 30000)
        moneyAmount.set(moneyResource)
        woodAmount.set(woodResource)
        oreAmount.set(oreResource)
        a = int(swordsMen) + 1000
        swordsMen = str(a)
        swordsMenUse.set(swordsMen)
        updateMap()
        trainTroops()

def trainOneThousandSpearMen():
    global spearMen
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 10000 or w < 30000 or o < 30000:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 10000)
        woodResource = str(w - 30000)
        oreResource = str(o - 30000)
        moneyAmount.set(moneyResource)
        woodAmount.set(woodResource)
        oreAmount.set(oreResource)
        a = int(spearMen)
        a += 1000
        spearMen = str(a)
        spearMenUse.set(spearMen)
        updateMap()
        trainTroops()


def trainOneThousandArcher():
    global archers
    global woodResource
    global moneyResource
    global stoneResource
    global oreResource
    m = int(moneyResource)
    w = int(woodResource)
    s = int(stoneResource)
    o = int(oreResource)
    if m < 10000 or w < 30000 or o < 30000:
        notEnoughFundingLbl.place(x = 777.5,y = 400, anchor = "center")
        notEnoughFundingLbl.after(1000, pauser)
    else:
        moneyResource = str(m - 10000)
        woodResource = str(w - 30000)
        oreResource = str(o - 30000)
        moneyAmount.set(moneyResource)
        woodAmount.set(woodResource)
        oreAmount.set(oreResource)
        a = int(archers)
        a += 1000
        archers = str(a)
        archersUse.set(archers)
        updateMap()
        trainTroops()

def updateMap():
    a = int(cavalry)
    b = int(swordsMen)
    c = int(spearMen)
    d = int(archers)
    e = a + b + c + d
    f = str(e)
    totalTroops = f
    totalTroopsUse.set(totalTroops)
    tr = int(totalTroops)
    if (tr == 0):
        castleOutlineLabel.place(x= 0,y = 0)
        castleOutlineLessThan100Label.pack()
        castleOutlineLessThan100Label.pack_forget()
        castleOutlineLessThan1000Label.pack()
        castleOutlineLessThan1000Label.pack_forget()
        castleOutlineLessThan5000Label.pack()
        castleOutlineLessThan5000Label.pack_forget()
        castleOutlineLessThan10000Label.pack()
        castleOutlineLessThan15000Label.pack()
        castleOutlineLessThan15000Label.pack_forget()
        castleOutlineLessThan10000Label.pack_forget()
        castleOutlineLessThan20000Label.pack()
        castleOutlineLessThan20000Label.pack_forget()
    if (tr > 0 and tr <= 100):
        castleOutlineLabel.pack()
        castleOutlineLabel.pack_forget()
        castleOutlineLessThan1000Label.pack()
        castleOutlineLessThan1000Label.pack_forget()
        castleOutlineLessThan5000Label.pack()
        castleOutlineLessThan5000Label.pack_forget()
        castleOutlineLessThan10000Label.pack()
        castleOutlineLessThan10000Label.pack_forget()
        castleOutlineLessThan15000Label.pack()
        castleOutlineLessThan15000Label.pack_forget()
        castleOutlineLessThan20000Label.pack()
        castleOutlineLessThan20000Label.pack_forget()
        castleOutlineLessThan100Label.place(x = 0, y = 0)
    if (tr > 100 and tr <= 1000):
        castleOutlineLabel.pack()
        castleOutlineLabel.pack_forget()
        castleOutlineLessThan100Label.pack()
        castleOutlineLessThan100Label.pack_forget()
        castleOutlineLessThan5000Label.pack()
        castleOutlineLessThan5000Label.pack_forget()
        castleOutlineLessThan10000Label.pack()
        castleOutlineLessThan10000Label.pack_forget()
        castleOutlineLessThan15000Label.pack()
        castleOutlineLessThan15000Label.pack_forget()
        castleOutlineLessThan20000Label.pack()
        castleOutlineLessThan20000Label.pack_forget()
        castleOutlineLessThan1000Label.place(x = 0, y = 0)
    if (tr > 1000 and tr <= 5000):
        castleOutlineLabel.pack()
        castleOutlineLabel.pack_forget()
        castleOutlineLessThan100Label.pack()
        castleOutlineLessThan100Label.pack_forget()
        castleOutlineLessThan1000Label.pack()
        castleOutlineLessThan1000Label.pack_forget()
        castleOutlineLessThan15000Label.pack()
        castleOutlineLessThan15000Label.pack_forget()
        castleOutlineLessThan20000Label.pack()
        castleOutlineLessThan20000Label.pack_forget()
        castleOutlineLessThan5000Label.place(x = 0, y = 0)
    if (tr > 5000 and tr <= 10000):
        castleOutlineLabel.pack()
        castleOutlineLabel.pack_forget()
        castleOutlineLessThan100Label.pack()
        castleOutlineLessThan100Label.pack_forget()
        castleOutlineLessThan1000Label.pack()
        castleOutlineLessThan1000Label.pack_forget()
        castleOutlineLessThan5000Label.pack()
        castleOutlineLessThan5000Label.pack_forget()
        castleOutlineLessThan15000Label.pack()
        castleOutlineLessThan15000Label.pack_forget()
        castleOutlineLessThan20000Label.pack()
        castleOutlineLessThan20000Label.pack_forget()
        castleOutlineLessThan10000Label.place(x = 0, y = 0)
    if (tr > 10000 and tr <= 15000):
        castleOutlineLabel.pack()
        castleOutlineLabel.pack_forget()
        castleOutlineLessThan100Label.pack()
        castleOutlineLessThan100Label.pack_forget()
        castleOutlineLessThan1000Label.pack()
        castleOutlineLessThan1000Label.pack_forget()
        castleOutlineLessThan5000Label.pack()
        castleOutlineLessThan5000Label.pack_forget()
        castleOutlineLessThan10000Label.pack()
        castleOutlineLessThan10000Label.pack_forget()
        castleOutlineLessThan20000Label.pack()
        castleOutlineLessThan20000Label.pack_forget()
        castleOutlineLessThan15000Label.place(x = 0, y = 0)
    if (tr > 15000 and tr <= 20000):
        castleOutlineLabel.pack()
        castleOutlineLabel.pack_forget()
        castleOutlineLessThan100Label.pack()
        castleOutlineLessThan100Label.pack_forget()
        castleOutlineLessThan1000Label.pack()
        castleOutlineLessThan1000Label.pack_forget()
        castleOutlineLessThan5000Label.pack()
        castleOutlineLessThan5000Label.pack_forget()
        castleOutlineLessThan10000Label.pack()
        castleOutlineLessThan10000Label.pack_forget()
        castleOutlineLessThan15000Label.pack()
        castleOutlineLessThan15000Label.pack_forget()
        castleOutlineLessThan20000Label.place(x = 0, y = 0)

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

def repath(a):
    last = a.rfind("\\")
    a = a[:last+1] + "DefenceofGondorPhotos" + a[last:]
    b = "\\"
    c = "\\\\"
    a = a.replace(b,c)
    return a

def restartTheGame():
    global moneyResource
    global woodResource
    global stoneResource
    global oreResource
    global castleHealth
    global maxhealth
    global strongHoldLvl
    global slot1Var
    global slot2Var
    global slot3Var
    global slot4Var
    global slot5Var
    global slot6Var
    global slot7Var
    global slot8Var
    global slot9Var
    global slot10Var
    global slot11Var
    global slot12Var
    global slot13Var
    global slot14Var
    global slot15Var
    global slot16Var
    global slot17Var
    global slot18Var
    global slot19Var
    global slot20Var
    global slot21Var
    global slot22Var
    global slot23Var
    global slot24Var
    global day
    global wallLvl
    global wallDefense
    global cavalry
    global swordsMen
    global spearMen
    global archers
    moneyResource = "20000"
    moneyAmount.set(moneyResource)
    woodResource = "20000"
    woodAmount.set(woodResource)
    stoneResource = "20000"
    stoneAmount.set(stoneResource)
    oreResource = "20000"
    oreAmount.set(oreResource)
    castleHealth = "100"
    castleHealthUse.set(castleHealth)
    maxhealth = "100"
    slot1Var = "E - 1"
    slot2Var = "E - 1"
    slot3Var = "E - 1"
    slot4Var = "E - 1"
    slot5Var = "E - 1"
    slot6Var = "E - 1"
    slot7Var = "E - 1"
    slot8Var = "E - 1"
    slot9Var = "E - 1"
    slot10Var = "E - 1"
    slot11Var = "E - 1"
    slot12Var = "E - 1"
    slot13Var = "E - 1"
    slot14Var = "E - 1"
    slot15Var = "E - 1"
    slot16Var = "E - 1"
    slot17Var = "E - 1"
    slot18Var = "E - 1"
    slot19Var = "E - 1"
    slot20Var = "E - 1"
    slot21Var = "E - 1"
    slot22Var = "E - 1"
    slot23Var = "E - 1"
    slot24Var = "E - 1"
    strongHoldLvl = "1"
    strongHoldLvlUse.set(strongHoldLvl)
    wallLvl = "1"
    wallLvlUse.set(wallLvl)
    wallDefense = "100"
    day = "1"
    dayUse.set(day)
    cavalry = "0"
    cavalryUse.set(cavalry)
    swordsMen = "0"
    swordsMenUse.set(swordsMen)
    spearMen = "0"
    spearMenUse.set(spearMen)
    archers = "0"
    archersUse.set(archers)
    wallDefense = "100"
    wallDefenseUse.set(wallDefense)
    returnMenu()







                                                                        #=======GUI=========#

root = Tk()
path_icon = repath(resource_path("Icon.ico"))
root.iconbitmap(path_icon)
root.geometry("1555x800")
root.title("Defence of Gondor")
root.resizable(False,False)
                                                                        #=======Menu=========#
path_1 = repath(resource_path("MenuBackGround.png"))
MenuBackGroundImage = PhotoImage(file = path_1)
MenuBackGroundLabel = Label(root, image = MenuBackGroundImage)
MenuBackGroundLabel.place(x = 0, y = 0)

instructionBackGround = repath(resource_path("InstructionBackGround.png"))
instructionBackGroundImage = PhotoImage(file = instructionBackGround)
instructionBackGroundLbl = Label(root, image = instructionBackGroundImage)

path_2 = repath(resource_path("StartButton.png"))
startButtonImage = PhotoImage(file = path_2)
startButton = Button(root, image = startButtonImage, command = startGame)
startButton.place(x = 777.5, y = 350, anchor = "center")


path_3 = repath(resource_path("InstructionButton.png"))
InstructionButtonImage = PhotoImage(file = path_3)
InstructionButton = Button(root, image = InstructionButtonImage, command = runInstruction)
InstructionButton.place(x = 777.5, y = 450, anchor = "center")

path_4 = repath(resource_path("BackButtonMenu.png"))
backButtonMenuImage = PhotoImage(file = path_4)
backButtonMenu = Button(root, image = backButtonMenuImage, command = returnMenu)

instructionText = ""

instructionTextUse = StringVar()
instructionTextUse.set(instructionText)
instructionTextLbl = Label(root, textvariable = instructionTextUse, justify = "left")

                                                                        #======In Game ======#

path_5 = repath(resource_path("CastleOutline.png"))
castleOutline = PhotoImage(file = path_5)
castleOutlineLabel = Label(root, image = castleOutline)

path_6 = repath(resource_path("CastleOutlineLessThan100.png"))
castleOutlineLessThan100 = PhotoImage(file = path_6)
castleOutlineLessThan100Label = Label(root, image = castleOutlineLessThan100)

path_7 = repath(resource_path("CastleOutlineLessThan1000.png"))
castleOutlineLessThan1000 = PhotoImage(file = path_7)
castleOutlineLessThan1000Label = Label(root, image = castleOutlineLessThan1000)

path_8 = repath(resource_path("CastleOutlineLessThan5000.png"))
castleOutlineLessThan5000 = PhotoImage(file = path_8)
castleOutlineLessThan5000Label = Label(root, image = castleOutlineLessThan5000)

path_9 = repath(resource_path("CastleOutlineLessThan10000.png"))
castleOutlineLessThan10000 = PhotoImage(file = path_9)
castleOutlineLessThan10000Label = Label(root, image = castleOutlineLessThan10000)

path_10 = repath(resource_path("CastleOutlineLessThan15000.png"))
castleOutlineLessThan15000 = PhotoImage(file = path_10)
castleOutlineLessThan15000Label = Label(root, image = castleOutlineLessThan15000)

path_11 = repath(resource_path("CastleOutlineLessThan20000.png"))
castleOutlineLessThan20000 = PhotoImage(file = path_11)
castleOutlineLessThan20000Label = Label(root, image = castleOutlineLessThan20000)

path_12 = repath(resource_path("WallSelected.png"))
wallClickedImage = PhotoImage(file = path_12)
wallClickedLabel = Label(root, image = wallClickedImage)

path_13 = repath(resource_path("ResourceTab.png"))
ResourceTab = PhotoImage(file = path_13)
ResourceTabLabel = Label(root, image = ResourceTab)

path_14 = repath(resource_path("NextButton.png"))
nextButtonImage = PhotoImage(file = path_14)
nextButton = Button(root, image = nextButtonImage, command = runNextSlot)

path_15 = repath(resource_path("StrongHoldButton.png"))
strongHoldButtonImage = PhotoImage(file = path_15)
strongHoldButton = Button(root, image = strongHoldButtonImage, command = callStronghold)

path_16 = repath(resource_path("BackButton.png"))
backButtonImage = PhotoImage(file = path_16)
backButton = Button(root, image = backButtonImage, command = slotDestruct)

path_17 = repath(resource_path("NextDayButton.png"))
nextDayButtonImage = PhotoImage(file = path_17)
nextDayButton = Button(root, image = nextDayButtonImage, command = nextDay)

path_18 = repath(resource_path("MenuButton.png"))
menuButtonImage = PhotoImage(file = path_18)
menuButton = Button(root, image = menuButtonImage, command = returnMenu)

path_19 = repath(resource_path("WallButton.png"))
wallButtonImage = PhotoImage(file = path_19)
wallButton = Button(root, image = wallButtonImage, command = openWall)

moneyResource = "20000"
moneyAmount = StringVar()
moneyAmount.set(moneyResource)
moneyAmountLbl = Label(root, textvariable = moneyAmount)

woodResource = "20000"
woodAmount = StringVar()
woodAmount.set(woodResource)
woodAmountLbl = Label(root, textvariable = woodAmount)

stoneResource = "20000"
stoneAmount = StringVar()
stoneAmount.set(stoneResource)
stoneAmountLbl = Label(root, textvariable = stoneAmount)

oreResource = "20000"
oreAmount = StringVar()
oreAmount.set(oreResource)
oreAmountLbl = Label(root, textvariable = oreAmount)

castleHealth = "100"
castleHealthUse = StringVar()
castleHealthUse.set(castleHealth)
castleHealthUseLbl = Label(root, textvariable = castleHealthUse)

                                                                        #==============#

path_20 = repath(resource_path("StrongHold.png"))
strongHoldImage = PhotoImage(file = path_20)
strongHoldLabel = Label(root, image = strongHoldImage)

path_21 = repath(resource_path("StrongHoldAfterCLicked.png"))
strongHoldClickedImage = PhotoImage(file = path_21)
strongHoldClickedLabel = Label(root, image = strongHoldClickedImage)

path_22 = repath(resource_path("EmptySlot.png"))
slotEmptyImage = PhotoImage(file = path_22)
slot1EmptyLabel = Label(root, image = slotEmptyImage)
slot2EmptyLabel = Label(root, image = slotEmptyImage)
slot3EmptyLabel = Label(root, image = slotEmptyImage)
slot4EmptyLabel = Label(root, image = slotEmptyImage)
slot5EmptyLabel = Label(root, image = slotEmptyImage)
slot6EmptyLabel = Label(root, image = slotEmptyImage)
slot7EmptyLabel = Label(root, image = slotEmptyImage)
slot8EmptyLabel = Label(root, image = slotEmptyImage)
slot9EmptyLabel = Label(root, image = slotEmptyImage)
slot10EmptyLabel = Label(root, image = slotEmptyImage)
slot11EmptyLabel = Label(root, image = slotEmptyImage)
slot12EmptyLabel = Label(root, image = slotEmptyImage)
slot13EmptyLabel = Label(root, image = slotEmptyImage)
slot14EmptyLabel = Label(root, image = slotEmptyImage)
slot15EmptyLabel = Label(root, image = slotEmptyImage)
slot16EmptyLabel = Label(root, image = slotEmptyImage)
slot17EmptyLabel = Label(root, image = slotEmptyImage)
slot18EmptyLabel = Label(root, image = slotEmptyImage)
slot19EmptyLabel = Label(root, image = slotEmptyImage)
slot20EmptyLabel = Label(root, image = slotEmptyImage)
slot21EmptyLabel = Label(root, image = slotEmptyImage)
slot22EmptyLabel = Label(root, image = slotEmptyImage)
slot23EmptyLabel = Label(root, image = slotEmptyImage)
slot24EmptyLabel = Label(root, image = slotEmptyImage)


path_23 = repath(resource_path("EmptySlotClickedOn.png"))
slotEmptySelectedImage = PhotoImage(file = path_23)
slot1EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot2EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot3EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot4EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot5EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot6EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot7EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot8EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot9EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot10EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot11EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot12EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot13EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot14EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot15EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot16EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot17EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot18EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot19EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot20EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot21EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot22EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot23EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)
slot24EmptySelectedLabel = Label(root, image = slotEmptySelectedImage)

path_24 = repath(resource_path("Lodge.png"))
lodgeButtonImage = PhotoImage(file = path_24)

path_25 = repath(resource_path("OreRefinery.png"))
oreRefineryImage = PhotoImage(file = path_25)
oreRefineryLabel1 = Label(root,image = oreRefineryImage)
oreRefineryLabel2 = Label(root,image = oreRefineryImage)
oreRefineryLabel3 = Label(root,image = oreRefineryImage)
oreRefineryLabel4 = Label(root,image = oreRefineryImage)
oreRefineryLabel5 = Label(root,image = oreRefineryImage)
oreRefineryLabel6 = Label(root,image = oreRefineryImage)
oreRefineryLabel7 = Label(root,image = oreRefineryImage)
oreRefineryLabel8 = Label(root,image = oreRefineryImage)
oreRefineryLabel9 = Label(root,image = oreRefineryImage)
oreRefineryLabel10 = Label(root,image = oreRefineryImage)
oreRefineryLabel11 = Label(root,image = oreRefineryImage)
oreRefineryLabel12 = Label(root,image = oreRefineryImage)
oreRefineryLabel13 = Label(root,image = oreRefineryImage)
oreRefineryLabel14 = Label(root,image = oreRefineryImage)
oreRefineryLabel15 = Label(root,image = oreRefineryImage)
oreRefineryLabel16 = Label(root,image = oreRefineryImage)
oreRefineryLabel17 = Label(root,image = oreRefineryImage)
oreRefineryLabel18 = Label(root,image = oreRefineryImage)
oreRefineryLabel19 = Label(root,image = oreRefineryImage)
oreRefineryLabel20 = Label(root,image = oreRefineryImage)
oreRefineryLabel21 = Label(root,image = oreRefineryImage)
oreRefineryLabel22 = Label(root,image = oreRefineryImage)
oreRefineryLabel23 = Label(root,image = oreRefineryImage)
oreRefineryLabel24 = Label(root,image = oreRefineryImage)

path_26 = repath(resource_path("OreRefineryClickedOn.png"))
oreRefineryClickedOnImage = PhotoImage(file = path_26)
oreRefineryClickedOnLabel1 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel2 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel3 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel4 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel5 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel6 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel7 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel8 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel9 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel10 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel11 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel12 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel13 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel14 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel15 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel16 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel17 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel18 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel19 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel20 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel21 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel22 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel23 = Label(root,image = oreRefineryClickedOnImage)
oreRefineryClickedOnLabel24 = Label(root,image = oreRefineryClickedOnImage)

path_27 = repath(resource_path("Sawmill.png"))
sawMillImage = PhotoImage(file = path_27)
sawMillLabel1 = Label(root, image = sawMillImage)
sawMillLabel2 = Label(root, image = sawMillImage)
sawMillLabel3 = Label(root, image = sawMillImage)
sawMillLabel4 = Label(root, image = sawMillImage)
sawMillLabel5 = Label(root, image = sawMillImage)
sawMillLabel6 = Label(root, image = sawMillImage)
sawMillLabel7 = Label(root, image = sawMillImage)
sawMillLabel8 = Label(root, image = sawMillImage)
sawMillLabel9 = Label(root, image = sawMillImage)
sawMillLabel10 = Label(root, image = sawMillImage)
sawMillLabel11 = Label(root, image = sawMillImage)
sawMillLabel12 = Label(root, image = sawMillImage)
sawMillLabel13 = Label(root, image = sawMillImage)
sawMillLabel14 = Label(root, image = sawMillImage)
sawMillLabel15 = Label(root, image = sawMillImage)
sawMillLabel16 = Label(root, image = sawMillImage)
sawMillLabel17 = Label(root, image = sawMillImage)
sawMillLabel18 = Label(root, image = sawMillImage)
sawMillLabel19 = Label(root, image = sawMillImage)
sawMillLabel20 = Label(root, image = sawMillImage)
sawMillLabel21 = Label(root, image = sawMillImage)
sawMillLabel22 = Label(root, image = sawMillImage)
sawMillLabel23 = Label(root, image = sawMillImage)
sawMillLabel24 = Label(root, image = sawMillImage)

path_28 = repath(resource_path("SawmillClickedOn.png"))
sawMillClickedOnImage = PhotoImage(file = path_28)
sawMillClickedOnLabel1 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel2 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel3 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel4 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel5 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel6 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel7 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel8 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel9 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel10 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel11 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel12 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel13 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel14 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel15 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel16 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel17 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel18 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel19 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel20 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel21 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel22 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel23 = Label(root, image = sawMillClickedOnImage)
sawMillClickedOnLabel24 = Label(root, image = sawMillClickedOnImage)

path_29 = repath(resource_path("StoneFactory.png"))
stoneFactoryImage = PhotoImage(file = path_29)
stoneFactoryLabel1 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel2 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel3 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel4 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel5 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel6 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel7 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel8 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel9 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel10 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel11 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel12 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel13 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel14 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel15 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel16 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel17 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel18 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel19 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel20 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel21 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel22 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel23 = Label(root, image = stoneFactoryImage)
stoneFactoryLabel24 = Label(root, image = stoneFactoryImage)

path_30 = repath(resource_path("StoneFactoryClickedOn.png"))
stoneFactoryClickedOnImage = PhotoImage(file = path_30)
stoneFactoryClickedOnLabel1 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel2 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel3 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel4 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel5 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel6 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel7 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel8 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel9 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel10 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel11 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel12 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel13 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel14 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel15 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel16 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel17 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel18 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel19 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel20 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel21 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel22 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel23 = Label(root, image = stoneFactoryClickedOnImage)
stoneFactoryClickedOnLabel24 = Label(root, image = stoneFactoryClickedOnImage)

path_31 = repath(resource_path("Lodge.png"))
lodgeLabelImage = PhotoImage(file = path_31)
lodgeLabel1 = Label(root,image = lodgeLabelImage)
lodgeLabel2 = Label(root, image = lodgeLabelImage)
lodgeLabel3 = Label(root, image = lodgeLabelImage)
lodgeLabel4 = Label(root, image = lodgeLabelImage)
lodgeLabel5 = Label(root, image = lodgeLabelImage)
lodgeLabel6 = Label(root, image = lodgeLabelImage)
lodgeLabel7 = Label(root, image = lodgeLabelImage)
lodgeLabel8 = Label(root, image = lodgeLabelImage)
lodgeLabel9 = Label(root, image = lodgeLabelImage)
lodgeLabel10 = Label(root, image = lodgeLabelImage)
lodgeLabel11 = Label(root, image = lodgeLabelImage)
lodgeLabel12 = Label(root, image = lodgeLabelImage)
lodgeLabel13 = Label(root, image = lodgeLabelImage)
lodgeLabel14 = Label(root, image = lodgeLabelImage)
lodgeLabel15 = Label(root, image = lodgeLabelImage)
lodgeLabel16 = Label(root, image = lodgeLabelImage)
lodgeLabel17 = Label(root, image = lodgeLabelImage)
lodgeLabel18 = Label(root, image = lodgeLabelImage)
lodgeLabel19 = Label(root, image = lodgeLabelImage)
lodgeLabel20 = Label(root, image = lodgeLabelImage)
lodgeLabel21 = Label(root, image = lodgeLabelImage)
lodgeLabel22 = Label(root, image = lodgeLabelImage)
lodgeLabel23 = Label(root, image = lodgeLabelImage)
lodgeLabel24 = Label(root, image = lodgeLabelImage)

path_32 = repath(resource_path("LodgeClickedOn.png"))
lodgeClickedImage = PhotoImage(file = path_32)
lodgeClicked1 = Label(root,image = lodgeClickedImage)
lodgeClicked2 = Label(root,image = lodgeClickedImage)
lodgeClicked3 = Label(root,image = lodgeClickedImage)
lodgeClicked4 = Label(root,image = lodgeClickedImage)
lodgeClicked5 = Label(root,image = lodgeClickedImage)
lodgeClicked6 = Label(root,image = lodgeClickedImage)
lodgeClicked7 = Label(root,image = lodgeClickedImage)
lodgeClicked8 = Label(root,image = lodgeClickedImage)
lodgeClicked9 = Label(root,image = lodgeClickedImage)
lodgeClicked10 = Label(root,image = lodgeClickedImage)
lodgeClicked11 = Label(root,image = lodgeClickedImage)
lodgeClicked12 = Label(root,image = lodgeClickedImage)
lodgeClicked13 = Label(root,image = lodgeClickedImage)
lodgeClicked14 = Label(root,image = lodgeClickedImage)
lodgeClicked15 = Label(root,image = lodgeClickedImage)
lodgeClicked16 = Label(root,image = lodgeClickedImage)
lodgeClicked17 = Label(root,image = lodgeClickedImage)
lodgeClicked18 = Label(root,image = lodgeClickedImage)
lodgeClicked19 = Label(root,image = lodgeClickedImage)
lodgeClicked20 = Label(root,image = lodgeClickedImage)
lodgeClicked21 = Label(root,image = lodgeClickedImage)
lodgeClicked22 = Label(root,image = lodgeClickedImage)
lodgeClicked23 = Label(root,image = lodgeClickedImage)
lodgeClicked24 = Label(root,image = lodgeClickedImage)

path_32 = repath(resource_path("StrongHoldInfo.png"))
strongHoldInfoImage = PhotoImage(file = path_32)
strongHoldInfoLabel = Label(root, image = strongHoldInfoImage)

path_33 = repath(resource_path("UpgradeButton.png"))
upgradeButtonImage = PhotoImage(file = path_33)
strongHoldUpgradeButton = Button(root, image = upgradeButtonImage, command = upgrade)

path_34 = repath(resource_path("LodgeInfo.png"))
lodgeInfoImage = PhotoImage(file = path_34)
lodgeInfo = Label(root, image = lodgeInfoImage)

path_35 = repath(resource_path("OreRefineryInfo.png"))
oreRefineryInfoImage = PhotoImage(file = path_35)
oreRefineryInfo = Label(root, image = oreRefineryInfoImage)

path_36 = repath(resource_path("SawmillInfo.png"))
sawMillInfoImage = PhotoImage(file = path_36)
sawMillInfo = Label(root, image = sawMillInfoImage)

path_37 = repath(resource_path("StoneFactoryInfo.png"))
stoneFactoryInfoImage = PhotoImage(file = path_37)
stoneFactoryInfo = Label(root, image = stoneFactoryInfoImage)

otherUpgradeButton = Button(root, image = upgradeButtonImage, command = upgradeOther)

path_38 = repath(resource_path("WallInfo.png"))
wallInfoImage = PhotoImage(file = path_38)
wallInfoLabel = Label(root, image = wallInfoImage)

path_39 = repath(resource_path("WallUpgradeButton.png"))
wallUpgradeButtonImage = PhotoImage(file = path_39)
wallUpgradeButton = Button(root, image = wallUpgradeButtonImage, command = upgradeWall)

path_40 = repath(resource_path("HealButton.png"))
wallHealButtonImage = PhotoImage(file = path_40)
wallHealButton = Button(root, image = wallHealButtonImage, command = healWall)

path_41 = repath(resource_path("SelectBuildingOption.png"))
buildingOptionsImage = PhotoImage(file = path_41)
buildingOptionsLabel = Label(root, image = buildingOptionsImage)

path_42 = repath(resource_path("DemolishButton.png"))
demolishButtonImage = PhotoImage(file = path_42)
demolishButton = Button(root, image = demolishButtonImage, command = demolishBuilding)

sawMillButton = Button(root, image = sawMillImage, command = turnSlotToSawMill)
stoneFactoryButton = Button(root, image = stoneFactoryImage, command = turnSlotToStoneFactory)
lodgeButton = Button(root, image = lodgeButtonImage, command = turnSlotToLodge)
oreRefineryButton = Button(root, image = oreRefineryImage, command = turnSlotToOre)

path_43 = repath(resource_path("TroopsButton.png"))
troopsButtonImage = PhotoImage(file = path_43)
troopsButton = Button(root, image = troopsButtonImage, command = trainTroops)

path_44 = repath(resource_path("TroopsSelectionBanner.png"))
troopsSelectionImage = PhotoImage(file = path_44)
troopsSelectionLabel = Label(root, image = troopsSelectionImage)

path_45 = repath(resource_path("TrainOneButton.png"))
trainOnePhoto = PhotoImage(file = path_45)
trainOneCavalryButton = Button(root, image = trainOnePhoto, command = trainOneCavalry)
trainOneSwordsMenButton = Button(root, image = trainOnePhoto, command = trainOneSwordsMen)
trainOneSpearMenButton = Button(root, image = trainOnePhoto, command = trainOneSpearMen)
trainOneArchersButton = Button(root, image = trainOnePhoto, command = trainOneArcher)

path_46 = repath(resource_path("TrainOneHundredButton.png"))
trainOneHundredPhoto = PhotoImage(file = path_46)
trainOneHundredCavalryButton = Button(root, image = trainOneHundredPhoto, command = trainOneHundredCavalry)
trainOneHundredSwordsMenButton = Button(root, image = trainOneHundredPhoto, command = trainOneHundredSwordsMen)
trainOneHundredSpearMenButton = Button(root, image = trainOneHundredPhoto, command = trainOneHundredSpearMen)
trainOneHundredArchersButton = Button(root, image = trainOneHundredPhoto, command = trainOneHundredArcher)

path_47 = repath(resource_path("TrainOneThousandButton.png"))
trainOneThousandPhoto = PhotoImage(file = path_47)
trainOneThousandCavalryButton = Button(root, image = trainOneThousandPhoto, command = trainOneThousandCavalry)
trainOneThousandSwordsMenButton = Button(root, image = trainOneThousandPhoto, command = trainOneThousandSwordsMen)
trainOneThousandSpearMenButton = Button(root, image = trainOneThousandPhoto, command = trainOneThousandSpearMen)
trainOneThousandArchersButton = Button(root, image = trainOneThousandPhoto, command = trainOneThousandArcher)

                                                                        #====================#

current = 1
slot1Var = "E - 1"
slot1Lvl = StringVar()
slot1Lvl.set(slot1Var[4])
slot1LvlLbl = Label(root, textvariable = slot1Lvl)

slot2Var = "E - 1"
slot2Lvl = StringVar()
slot2Lvl.set(slot2Var[4])
slot2LvlLbl = Label(root, textvariable = slot2Lvl)

slot3Var = "E - 1"
slot3Lvl = StringVar()
slot3Lvl.set(slot3Var[4])
slot3LvlLbl = Label(root, textvariable = slot3Lvl)

slot4Var = "E - 1"
slot4Lvl = StringVar()
slot4Lvl.set(slot4Var[4])
slot4LvlLbl = Label(root, textvariable = slot4Lvl)

slot5Var = "E - 1"
slot5Lvl = StringVar()
slot5Lvl.set(slot5Var[4])
slot5LvlLbl = Label(root, textvariable = slot5Lvl)

slot6Var = "E - 1"
slot6Lvl = StringVar()
slot6Lvl.set(slot6Var[4])
slot6LvlLbl = Label(root, textvariable = slot6Lvl)

slot7Var = "E - 1"
slot7Lvl = StringVar()
slot7Lvl.set(slot7Var[4])
slot7LvlLbl = Label(root, textvariable = slot7Lvl)

slot8Var = "E - 1"
slot8Lvl = StringVar()
slot8Lvl.set(slot8Var[4])
slot8LvlLbl = Label(root, textvariable = slot8Lvl)

slot9Var = "E - 1"
slot9Lvl = StringVar()
slot9Lvl.set(slot9Var[4])
slot9LvlLbl = Label(root, textvariable = slot9Lvl)

slot10Var = "E - 1"
slot10Lvl = StringVar()
slot10Lvl.set(slot10Var[4])
slot10LvlLbl = Label(root, textvariable = slot10Lvl)

slot11Var = "E - 1"
slot11Lvl = StringVar()
slot11Lvl.set(slot11Var[4])
slot11LvlLbl = Label(root, textvariable = slot11Lvl)

slot12Var = "E - 1"
slot12Lvl = StringVar()
slot12Lvl.set(slot12Var[4])
slot12LvlLbl = Label(root, textvariable = slot12Lvl)

slot13Var = "E - 1"
slot13Lvl = StringVar()
slot13Lvl.set(slot13Var[4])
slot13LvlLbl = Label(root, textvariable = slot13Lvl)

slot14Var = "E - 1"
slot14Lvl = StringVar()
slot14Lvl.set(slot14Var[4])
slot14LvlLbl = Label(root, textvariable = slot14Lvl)

slot15Var = "E - 1"
slot15Lvl = StringVar()
slot15Lvl.set(slot15Var[4])
slot15LvlLbl = Label(root, textvariable = slot15Lvl)

slot16Var = "E - 1"
slot16Lvl = StringVar()
slot16Lvl.set(slot16Var[4])
slot16LvlLbl = Label(root, textvariable = slot16Lvl)

slot17Var = "E - 1"
slot17Lvl = StringVar()
slot17Lvl.set(slot17Var[4])
slot17LvlLbl = Label(root, textvariable = slot17Lvl)

slot18Var = "E - 1"
slot18Lvl = StringVar()
slot18Lvl.set(slot18Var[4])
slot18LvlLbl = Label(root, textvariable = slot18Lvl)

slot19Var = "E - 1"
slot19Lvl = StringVar()
slot19Lvl.set(slot19Var[4])
slot19LvlLbl = Label(root, textvariable = slot19Lvl)

slot20Var = "E - 1"
slot20Lvl = StringVar()
slot20Lvl.set(slot20Var[4])
slot20LvlLbl = Label(root, textvariable = slot20Lvl)

slot21Var = "E - 1"
slot21Lvl = StringVar()
slot21Lvl.set(slot21Var[4])
slot21LvlLbl = Label(root, textvariable = slot21Lvl)

slot22Var = "E - 1"
slot22Lvl = StringVar()
slot22Lvl.set(slot22Var[4])
slot22LvlLbl = Label(root, textvariable = slot22Lvl)

slot23Var = "E - 1"
slot23Lvl = StringVar()
slot23Lvl.set(slot23Var[4])
slot23LvlLbl = Label(root, textvariable = slot23Lvl)

slot24Var = "E - 1"
slot24Lvl = StringVar()
slot24Lvl.set(slot24Var[4])
slot24LvlLbl = Label(root, textvariable = slot24Lvl)

strongHoldLvl = "1"
strongHoldLvlUse = StringVar()
strongHoldLvlUse.set(strongHoldLvl)
strongHoldLvlUseLbl = Label(root, textvariable = strongHoldLvlUse)

wallLvl = "1"
wallLvlUse = StringVar()
wallLvlUse.set(wallLvl)
wallLvlLbl = Label(root, textvariable = wallLvlUse)

wallDefense = "100"
wallDefenseUse = StringVar()
wallDefenseUse.set(wallDefense)
wallDefenseLbl = Label(root, textvariable = wallDefenseUse)

day = "1"
dayUse = StringVar()
dayUse.set(day)
dayLbl = Label(root, textvariable = dayUse)

battleReport = repath(resource_path("BattleReport.png"))
battleReportImage = PhotoImage(file = battleReport)
battleReportLabel = Label(root,image = battleReportImage)

cavalry = "0"
cavalryUse = StringVar()
cavalryUse.set(cavalry)
cavalryLbl = Label(root, textvariable = cavalryUse)

swordsMen = "0"
swordsMenUse = StringVar()
swordsMenUse.set(swordsMen)
swordsMenLbl = Label(root, textvariable = swordsMenUse)

spearMen = "0"
spearMenUse = StringVar()
spearMenUse.set(spearMen)
spearMenLbl = Label(root, textvariable = spearMenUse)

archers = "0"
archersUse = StringVar()
archersUse.set(archers)
archersLbl = Label(root, textvariable = archersUse)

cavalry_Before = "0"
cavalry_Before_Use = StringVar()
cavalry_Before_Use.set(cavalry_Before)
cavalryBeforeLbl = Label(root, textvariable = cavalry_Before_Use)

swordsMen_Before = "0"
swordsMen_Before_Use = StringVar()
swordsMen_Before_Use.set(swordsMen_Before)
swordsMenBeforeLbl = Label(root, textvariable = swordsMen_Before_Use)

spearMen_Before = "0"
spearMen_Before_Use = StringVar()
spearMen_Before_Use.set(spearMen_Before)
spearMenBeforeLbl = Label(root, textvariable = spearMen_Before_Use)

archers_Before = "0"
archers_Before_Use = StringVar()
archers_Before_Use.set(archers_Before)
archersBeforeLbl = Label(root, textvariable = archers_Before_Use)

trolls = "0"
trollsUse = StringVar()
trollsUse.set(trolls)
trollsLbl = Label(root, textvariable = trollsUse)

urukhai = "0"
urukhaiUse = StringVar()
urukhaiUse.set(urukhai)
urukhaiLbl = Label(root, textvariable = urukhaiUse)

mordorOrcs = "0"
mordorOrcsUse = StringVar()
mordorOrcsUse.set(mordorOrcs)
mordorOrcsLbl = Label(root, textvariable = mordorOrcsUse)

Goblins = "0"
GoblinsUse = StringVar()
GoblinsUse.set(Goblins)
GoblinsLbl = Label(root, textvariable = GoblinsUse)

trolls_after = "0"
trolls_after_Use = StringVar()
trolls_after_Use.set(trolls_after)
trollsafterLbl = Label(root, textvariable = trolls_after_Use)

urukhai_after = "0"
urukhai_after_Use = StringVar()
urukhai_after_Use.set(urukhai_after)
urukhaiafterLbl = Label(root, textvariable = urukhai_after_Use)

mordorOrcs_after = "0"
mordorOrcs_after_Use = StringVar()
mordorOrcs_after_Use.set(mordorOrcs_after)
mordorOrcsafterLbl = Label(root, textvariable = mordorOrcs_after_Use)

Goblins_after = "0"
Goblins_after_Use = StringVar()
Goblins_after_Use.set(Goblins_after)
GoblinsafterLbl = Label(root, textvariable = Goblins_after_Use)

totalTroops = "0"
totalTroopsUse = StringVar()
totalTroopsUse.set(totalTroops)
totalTroopsLbl = Label(root, textvariable = totalTroopsUse)

path_48 = repath(resource_path("NextDayBanner.png"))
nextDayBannerImage = PhotoImage(file = path_48)
nextDayBannerLbl = Label(root, image = nextDayBannerImage)

production = "300"
productionUse = StringVar()
productionUse.set(production)
productionUseLbl = Label(root, textvariable = productionUse)

notEnoughFunding = repath(resource_path("NotEnoughFunding.png"))
notEnoughFundingImage = PhotoImage(file = notEnoughFunding)
notEnoughFundingLbl = Label(root, image = notEnoughFundingImage)

upgradeStronghold = repath(resource_path("UpgradeStrongHold.png"))
upgradeStrongholdImage = PhotoImage(file = upgradeStronghold)
upgradeStrongholdLbl = Label(root, image = upgradeStrongholdImage)

anAttackOccured = repath(resource_path("AnAttackOccured.png"))
anAttackOccuredImage = PhotoImage(file = anAttackOccured)
anAttackOccuredLbl = Label(root,image = anAttackOccuredImage)

gold_upgrade = "0"
gold_upgradeUse = StringVar()
gold_upgradeUse.set(gold_upgrade)
gold_upgradeLbl = Label(root, textvariable = gold_upgradeUse)

wood_upgrade = "0"
wood_upgradeUse = StringVar()
wood_upgradeUse.set(wood_upgrade)
wood_upgradeLbl = Label(root, textvariable = wood_upgradeUse)

stone_upgrade = "0"
stone_upgradeUse = StringVar()
stone_upgradeUse.set(stone_upgrade)
stone_upgradeLbl = Label(root, textvariable = stone_upgradeUse)

ore_upgrade = "0"
ore_upgradeUse = StringVar()
ore_upgradeUse.set(ore_upgrade)
ore_upgradeLbl = Label(root, textvariable = ore_upgradeUse)

gold_heal = "0"
gold_healUse = StringVar()
gold_healUse.set(gold_heal)
gold_healLbl = Label(root, textvariable = gold_healUse)

wood_heal = "0"
wood_healUse = StringVar()
wood_healUse.set(wood_heal)
wood_healLbl = Label(root, textvariable = wood_healUse)

stone_heal = "0"
stone_healUse = StringVar()
stone_healUse.set(stone_heal)
stone_healLbl = Label(root, textvariable = stone_healUse)

ore_heal = "0"
ore_healUse = StringVar()
ore_healUse.set(ore_heal)
ore_healLbl = Label(root, textvariable = ore_healUse)

loss = "0"
healthlossUse = StringVar()
healthlossUse.set(loss)
healthlossLbl = Label(root, textvariable = healthlossUse)

maxhealth = "100"

troopsLostUse = StringVar()
troopsLostUse.set("0")
troopsLostLbl = Label(root, textvariable = troopsLostUse)

enemyKilledUse = StringVar()
enemyKilledUse.set("0")
enemyKilledLbl = Label(root, textvariable = enemyKilledUse)

gameOver = repath(resource_path("GameOver.png"))
gameOverImage = PhotoImage(file = gameOver)
gameOverLbl = Label(root, image = gameOverImage)

gameOverText = "You Survived For " + str(day) + " Days"
gameOverTextUse = StringVar()
gameOverTextUse.set(gameOverText)
gameOverTextLbl = Label(root, textvariable = gameOverTextUse)

restartGame = repath(resource_path("RestartMenu.png"))
restartGameImage = PhotoImage( file = restartGame)
restartGameButton = Button(root, image = restartGameImage, command = restartTheGame)

objective = repath(resource_path("Objective.png"))
objectiveImage = PhotoImage(file = objective)
objectiveButton = Button(root, image = objectiveImage, command = showObjective)

functionOfButtons = repath(resource_path("FunctionofButtons.png"))
functionOfButtonsImage = PhotoImage(file = functionOfButtons)
functionOfButtonsButton = Button(root, image = functionOfButtonsImage, command = showfunctionOfButtons)

buildings = repath(resource_path("Buildings.png"))
buildingsImage = PhotoImage(file = buildings)
buildingsButton = Button(root, image = buildingsImage, command = showBuildingsFunction)

attackAndDefence = repath(resource_path("AttackandDefence.png"))
attackAndDefenceImage = PhotoImage(file = attackAndDefence)
attackAndDefenceButton = Button(root, image = attackAndDefenceImage, command = showAttackAndDefence)

credit = repath(resource_path("credit.png"))
creditImage = PhotoImage(file = credit)
creditButton = Button(root, image = creditImage, command = credit_final)


root.mainloop()

