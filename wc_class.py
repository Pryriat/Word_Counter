class word_counter:
	self.spe_char_set = ('{','}','(',')','#','<','>','/')
	self.char_num = 0
	self.word_num = 0
	self.spe_char_num = 0
	self.single_comment = 0
	self.multi_comment = 0
	self.is_null = False
	self.file = ''
	def isnull(file):
	'''
	判断文件是否为空
	'''
		t = 0
		for lines in  file.readlines():
			t+=1
		if t == 0:
			return False
		return True

	def char_count(string_line):
	'''
	文件字符数统计
	'''
		char_num = 0
		for x in string_line:
			if x not in self.spe_char_set:
				char_num += 1
		return char_num

	def word_count(string_line):
	'''
	文件单词数统计
	'''
		word_num = 0
		str_pos = 0
		while str_pos < len(string_line)-1:
			if string_line[str_pos] == ' ' and string_line[str_pos+1] != ' ':
				word_num += 1
			str_pos += 1
		return word_num

	def special_count(string_line):
	'''
	特殊字符统计
	'''
		spe_char_num = 0
		for x in string_line:
			if x  in spe_char_set:
				spe_char_num += 1
		return spe_char_num

	def single_comment_count(string_line):
	'''
	单行注释统计
	'''
		if '//' in string_line:
			return 1
		else:
			return 0

	def multi_comment_count(file):
	'''
	多行注释统计
	'''
		multi_comment = 0
		is_end = Ture
		for lines in file.readlines():
			if '/*' in x:
				is_end = False
			if !is_end:
				multi_comment += 1
			if '*/' in x:
				is_end = True
		return multi_comment
	def file_process():
	'''
	文件处理主函数
	'''
		file = open(self.file,'r')
		if is_null(file):
			return
		else:
			self.multi_comment = multi_comment_count(self.file)
			for lines in self.file.readlines():
				self.char_num += char_count(lines)
				self.word_num += word_count(lines)
				self.spe_char_num += special_count(lines)
				self.single_comment += single_comment_count(lines)

	def file_select():
	'''
	文件的选择、通配符处理
	'''
	def ui_main():
	'''
	图形化界面的显示
	'''
	def command_line_proc():
	'''
	命令行参数处理
	'''
