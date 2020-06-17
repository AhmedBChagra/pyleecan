from os import getcwd, rename, remove
from os.path import join, dirname, abspath, split
from re import match

from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from ....Functions.load import load_matlib
from ....Functions.Material.compare_material import compare_material
from ....Functions.Material.replace_material_pyleecan_obj import (
    replace_material_pyleecan_obj,
)
from ....GUI.Tools.GuiOption.Ui_GuiOption import Ui_GUIOption
from ....GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup
from ....definitions import DATA_DIR
from ....GUI import GUI_logger, gui_option
from ....Functions.path_tools import abs_file_path
from ....definitions import edit_config_dict, MATLIB_DIR, config_dict
from ....Functions.load import load_matlib
from ....Classes.Material import Material


class WGuiOption(Ui_GUIOption, QDialog):
    def __init__(self, machine_setup, matlib):
        """
        WGuiOption enable to modify some option in the GUI such as:
            - units
            - material library folder
        
        Parameters:
        machine_setup: DMachineSetup
            Machine widget
        matlib : MatLib
            Material Library 
        """
        QDialog.__init__(self)
        self.setupUi(self)
        self.le_matlib_path.setText(MATLIB_DIR)
        self.machine_setup = machine_setup  # DMachineSetup to access to the machine
        self.matlib = matlib  # dmatlib to access to the material library
        self.c_unit_m.setCurrentIndex(gui_option.unit.unit_m)
        self.c_unit_m2.setCurrentIndex(gui_option.unit.unit_m2)

        # Connections
        self.b_matlib_path.clicked.connect(self.b_define_matlib_dir)
        self.le_matlib_path.textChanged.connect(self.change_matlib_dir)
        self.c_unit_m.currentTextChanged.connect(lambda: self.change_unit(unit="m"))
        self.c_unit_m2.currentTextChanged.connect(lambda: self.change_unit(unit="m2"))

    def b_define_matlib_dir(self):
        """
        b_define_matlib_dir open a dialog to select the matlib directory 
        """
        folder = QFileDialog.getExistingDirectory(self, "Select MatLib directory")
        if folder != self.matlib.ref_path and folder:
            self.le_matlib_path.setText(folder)
        GUI_logger.info("message")

    def change_matlib_dir(self):
        """
        Change the matlib directory and load the new matlib
        """
        matlib_path = self.le_matlib_path.text()
        edit_config_dict("MATLIB_DIR", matlib_path, config_dict)

        self.matlib.load_mat_ref(matlib_path)
        self.matlib.add_machine_mat(self.machine_setup.machine)

    def change_unit(self, unit="m"):
        """
        change_unit changes the unit in the gui options and save this change in the 
        pyleecan default configuration

        unit : str
            unit to update
        """
        global gui_option
        if unit == "m":  # Length unit
            key = "UNIT_M"
            value = self.c_unit_m.currentIndex()
            gui_option.unit.unit_m = value
        elif unit == "m2":  # Surface unit
            key = "UNIT_M2"
            value = self.c_unit_m2.currentIndex()
            gui_option.unit.unit_m2 = value
        else:
            raise ValueError("Unexpected argument in change_unit, unit=" + str(unit))

        edit_config_dict(key, value, config_dict)