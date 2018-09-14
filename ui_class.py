from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from wc_class import word_counter


class wc_ui(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setMinimumSize(640,480)
        self.opt = opt = {'a':True}
        self.wc = word_counter(self.opt)
        self.setWindowTitle('Word Counter by Chernobyl')
        self.file_label = QLabel()
        self.is_null_label = QLabel('isnull:')
        self.character_label = QLabel('character:')
        self.word_label = QLabel('word:')
        self.line_label = QLabel('line:')
        self.null_line_label = QLabel('null_line:')
        self.code_line_label = QLabel('code_line:')
        self.comment_line_label = QLabel('comment_line:')
        self.mainlayout = QVBoxLayout()
        self.file_button = QPushButton('select file')
        self.file_button.clicked.connect(self.selectfile)

        self.mainlayout.addWidget(self.file_label)
        self.mainlayout.addWidget(self.is_null_label)
        self.mainlayout.addWidget(self.character_label)
        self.mainlayout.addWidget(self.word_label)
        self.mainlayout.addWidget(self.line_label)
        self.mainlayout.addWidget(self.null_line_label)
        self.mainlayout.addWidget(self.code_line_label)
        self.mainlayout.addWidget(self.comment_line_label)
        self.mainlayout.addWidget(self.file_button)

        self.setLayout(self.mainlayout)

    def selectfile(self):
        file_name = QFileDialog.getOpenFileName(self,"select file ","C:\\","c source files(*.c);;cpp source files(*.cpp);;header files(*.h)")
        if len(file_name[0]) == 0:
            return
        self.wc.file_process(file_name[0])
        self.file_label.setText('file: %s'%(file_name[0]))
        self.is_null_label.setText('isnull: %s'%(str(self.wc.is_null)))
        self.character_label.setText('character: %d'%(self.wc.char_num))
        self.word_label.setText('word: %d'%(self.wc.word_num))
        self.line_label.setText('line: %d'%(self.wc.lines))
        self.code_line_label.setText('code_line: %d'%(self.wc.code_line))
        self.comment_line_label.setText('comment_line: %d'%(self.wc.single_comment+self.wc.multi_comment))
        self.null_line_label.setText('null_line: %d'%(self.wc.nullline))
