#coding = UTF-8
from wc_class import word_counter

a = word_counter('.\simple_reverse.c')
a.file_process()
print('isnull:',a.is_null)
print('char_num',a.char_num)
print('word_num',a.word_num)
print('lines',a.lines)
print('null_line',a.nullline)
