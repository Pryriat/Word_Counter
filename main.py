#coding = UTF-8
from wc_class import word_counter
from ui_class import wc_ui
import argparse
import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

opt = {}
if len(sys.argv) == 1:
    sys.argv.append('-h')
parser = argparse.ArgumentParser(description='Word_Counter by Chenobyl',add_help=True)
parser.add_argument('-c',help='character counts',action="store_true")
parser.add_argument('-w',help='word counts',action="store_true")
parser.add_argument('-l',help='line counts',action="store_true")
parser.add_argument('-a',help='extra informations',action="store_true")
parser.add_argument('-s',help='match  files',action="store_true")
parser.add_argument('-x',help='',action="store_true")
parser.add_argument('-f',default=None,help='input file')
args = parser.parse_args()
for x,y in args._get_kwargs():
    opt[x]=y
a = word_counter(opt)
if opt['x']:
    app = QApplication(sys.argv)
    u = wc_ui()
    u.show()
    sys.exit(app.exec())
elif opt['s']:
    a.file_select()
else:
    a.file_process(opt['f'])
