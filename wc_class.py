#coding = UTF-8
import re
import codecs
class word_counter:
	def __init__(self,file):
		self.char_num = 0
		self.word_num = 0
		self.lines = 0
		self.nullline = 0
		self.single_comment = 0
		self.multi_comment = 0
		self.is_null = False
		self.file = file

	def isnull(self,string):
		'''
		判断文件是否为空
		'''
		null_pattern = re.compile('.|\s')
		tmp_result = null_pattern.findall(string)
		if len(tmp_result) == 0:
			return True
		return False

	def char_count(self,string):
		'''
		文件字符数统计
		'''
		char_pattern = re.compile('[a-zA-Z]')
		tmp_result = char_pattern.findall(string)
		return len(tmp_result)

	def word_count(self,string):
		'''
		文件单词数统计
		'''
		word_pattern = re.compile('\w+')
		tmp_result = word_pattern.findall(string)
		return len(tmp_result)

	def line_count(self,string):
		'''
		文件行数统计与空行统计
		'''
		null_line = 0
		sepcial_pattern = re.compile('.*')
		tmp_result = sepcial_pattern.findall(string)
		for lines in tmp_result:
			if len(lines.replace(' ','').replace('\n','')) <= 1:
				null_line += 1
		return (len(tmp_result),null_line)

	def single_comment_count(self,string):
		'''
		单行注释统计
		'''
		re_pattern = re.compile('//')
		del_pattern = re.compile('"+[^"]+//+[^"]+"')
		multi_in_single_pattern = re.compile('/\*.*')
		tmp_result1 = re_pattern.findall(string)
		tmp_result2 = del_pattern.findall(string)
		for lines in tmp_result1:
			if len(multi_in_single_pattern.findall(lines)) == 1:
				self.multi_comment -= 1
		return len(tmp_result1) - len(tmp_result2)


	def multi_comment_count(self,string):
		'''
		多行注释统计
		'''
		multi_lines = 0
		multi_pattern = re.compile('/\*+[^\*]+\*/')
		single_in_multi_pattern = re.compile('//.*')
		tmp_result = multi_pattern.findall(string)
		for result1 in tmp_result:
			if len(single_in_multi_pattern.findall(result1)) == 1:
				self.single_comment -= 1
			for x in result1:
				if x == '\n':
					multi_lines+=1
		return multi_lines

	def file_process(self):
		'''
		文件处理主函数
		'''
		with codecs.open(self.file, 'r', 'utf-8') as f:
			self.file_string = f.read()
		if self.isnull(self.file_string):
			return
		else:
			self.multi_comment = self.multi_comment_count(self.file_string)
			self.char_num += self.char_count(self.file_string)
			self.word_num += self.word_count(self.file_string)
			(self.lines,self.nullline) = self.line_count(self.file_string)

	def file_select(self):
		'''
		文件的选择、通配符处理
		'''
		pass
	def ui_main(self):
		'''
		图形化界面的显示
		'''
		pass
	def command_line_proc(self):
		'''
		命令行参数处理
		'''
		pass
