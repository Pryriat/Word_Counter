class word_counter:
	spe_char_set = ('{','}','(',')','#','<','>','/')
	def isnull(file):
	'''
	判断文件是否为空
	'''
		t = 0
		for lines in  file.readlines():
			t+=1
		if t == 0:
			return false
		return true

	def char_count(string_line):
		'''
		文件字符数统计
		'''
		char_num = 0
		for x in string_line:
			if x not in spe_char_set:
				char_num += 1
		return char_num


	def word_count(string_line):
	'''
	文件单词数统计
	'''

	def special_count(string_line):
	'''
	特殊字符统计
	'''
	def comment_count(string——line）
	def file_process():
	'''
	文件处理主函数
	'''
	def file_select():
	'''
	文件的选择、通配符处理
	'''
	def ui_main():
	'''
	图形化界面的显示
	'''
	def command_line_proc()
	'''
	命令行参数处理
	'''
