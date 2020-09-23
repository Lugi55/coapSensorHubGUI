# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:53:46 2020

@author: Heimgartner
"""


from coapthon.client.helperclient import HelperClient
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QComboBox, QLineEdit
from PyQt5 import QtCore





def main():
    def on_getButtton():
        host = str(lineEdit.text())
        port = 5683
        client = HelperClient(server=(host, port))
        response = client.get(str(comboBox.currentText()),timeout=1)
        if(response==None):
            client.stop()
            label.setText("No answer")
        else:
            label.setText(str(response.payload).replace(",","\n"))

    app = QApplication([])
    window = QWidget()
    window.setGeometry(100,100,500,400)
    layout = QVBoxLayout()
    label = QLabel("default")
    getButton = QPushButton('GET');
    comboBox = QComboBox()
    lineEdit = QLineEdit()

    getButton.clicked.connect(on_getButtton)
    layout.addWidget(lineEdit)
    layout.addWidget(comboBox)
    layout.addWidget(label)
    [comboBox.addItem(i) for i in path]
    layout.addWidget(getButton,alignment=QtCore.Qt.AlignBottom)
    window.setLayout(layout)
    window.show()
    app.exec_()




path=[
"CAN/AEC/State",
"CAN/AEC/SoC_pct",
"CAN/AEC/Errors",
"CAN/AEC/Warnings",
"CAN/AEC/Error_from_Node_ID",
"CAN/AEC/Voltage_V",
"CAN/AEC/System_Maximum_String_Cell_Voltage_V",
"CAN/AEC/System_Minimum_String_Cell_Voltage_V",
"CAN/AEC/System_Heater_Status",
"CAN/AEC/SoH_pct",
"CAN/AEC/Hottest_Module_Temperature_C",
"CAN/AEC/Coldest_Module_Temperature_C",
"CAN/AEC/SW_Version",
"CAN/AEC/Relays_Status",
"CAN/AEC/Remaining_Capacity_Ah",
"CAN/AEC/Time_Remaining_mins",
"CAN/AEC/Lifetime_Charged_kWh",
"CAN/AEC/ISO_Monitor_kOhm",
"CAN/AEC/Permitted_Charge_Current_Amp",
"CAN/AEC/Permitted_Discharge_Current_Amp",
"CAN/AEC/Alive_Counter",
"CAN/AEC/Current_Amp",

"CAN/Module1/Maximum_String_Cells_Voltage_V",
"CAN/Module1/Minimum_String_Cells_Voltage_V",
"CAN/Module1/Errors",
"CAN/Module1/Heater_Status",
"CAN/Module1/Maximum_Module_Temperature_C",
"CAN/Module1/Minimum_Module_Temperature_C",
"CAN/Module1/Voltage_mV",

"CAN/Module2/Maximum_String_Cells_Voltage_V",
"CAN/Module2/Minimum_String_Cells_Voltage_V",
"CAN/Module2/Errors",
"CAN/Module2/Heater_Status",
"CAN/Module2/Maximum_Module_Temperature_C",
"CAN/Module2/Minimum_Module_Temperature_C",
"CAN/Module2/Voltage_mV",

"CAN/Module3/Maximum_String_Cells_Voltage_V",
"CAN/Module3/Minimum_String_Cells_Voltage_V",
"CAN/Module3/Errors",
"CAN/Module3/Heater_Status",
"CAN/Module3/Maximum_Module_Temperature_C",
"CAN/Module3/Minimum_Module_Temperature_C",
"CAN/Module3/Voltage_mV",

"CAN/Module4/Maximum_String_Cells_Voltage_V",
"CAN/Module4/Minimum_String_Cells_Voltage_V",
"CAN/Module4/Errors",
"CAN/Module4/Heater_Status",
"CAN/Module4/Maximum_Module_Temperature_C",
"CAN/Module4/Minimum_Module_Temperature_C",
"CAN/Module4/Voltage_mV",

"CAN/Module5/Maximum_String_Cells_Voltage_V",
"CAN/Module5/Minimum_String_Cells_Voltage_V",
"CAN/Module5/Errors",
"CAN/Module5/Heater_Status",
"CAN/Module5/Maximum_Module_Temperature_C",
"CAN/Module5/Minimum_Module_Temperature_C",
"CAN/Module5/Voltage_mV",

"CAN/Module6/Maximum_String_Cells_Voltage_V",
"CAN/Module6/Minimum_String_Cells_Voltage_V",
"CAN/Module6/Errors",
"CAN/Module6/Heater_Status",
"CAN/Module6/Maximum_Module_Temperature_C",
"CAN/Module6/Minimum_Module_Temperature_C",
"CAN/Module6/Voltage_mV",

"CAN/Module7/Maximum_String_Cells_Voltage_V",
"CAN/Module7/Minimum_String_Cells_Voltage_V",
"CAN/Module7/Errors",
"CAN/Module7/Heater_Status",
"CAN/Module7/Maximum_Module_Temperature_C",
"CAN/Module7/Minimum_Module_Temperature_C",
"CAN/Module7/Voltage_mV",
]    


main()


