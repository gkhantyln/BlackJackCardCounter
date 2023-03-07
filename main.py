import sys
from PyQt5.QtWidgets import QApplication
from bjc_Project import Template_main


app = QApplication(sys.argv)
bjcProject = Template_main()
sys.exit(app.exec_())
