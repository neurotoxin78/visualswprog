# PyQt4Template. Created on 14.04.2015
# Copyright (C) 2014 Andreas Schulz <andi.schulz@me.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 US

import sys
from os import path
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4.QtGui import QApplication

thisfile = path.abspath(__file__)
sys.path.insert(0, path.normpath(path.join(path.dirname(thisfile), '..')))

from widgets.mainwindow import MainWindow


def main(argv=None):
    if not argv:
        argv = sys.argv

    app = QApplication(argv)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
