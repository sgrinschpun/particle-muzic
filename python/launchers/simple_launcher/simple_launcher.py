import sys
from PyQt4 import QtGui

from simple_launcher_ui import Ui_MainWindow
from phenomena import Phenomena


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self._ui = Ui_MainWindow()
        self._initUI()
        self._connections()
        self._phenomena = Phenomena()

    def _initUI(self):               
        self._ui.setupUi(self)
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2)) 
    
    def _connections(self):
        self._ui.show_particle_btn.clicked.connect(self._sendParticle)

    def _sendParticle(self):
        particle = str(self._ui.particle_select_cbox.currentText())
        number = self._ui.particles_number_spinbox.value()
        print "Sending: {0} {1} ".format(particle, number)
        self._phenomena.addParticle(particle)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
