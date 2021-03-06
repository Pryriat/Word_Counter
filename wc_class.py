#coding = UTF-8
import re
import codecs
import getopt
import sys
import glob

class word_counter:
	def __init__(self,opt):
		self.char_num = 0
		self.word_num = 0
		self.lines = 0
		self.nullline = 0
		self.single_comment = 0
		self.multi_comment = 0
		self.code_line = 0
		self.is_null = False
		self.file = ''
		self.opt=opt

	def clear(self):
		self.char_num = 0
		self.word_num = 0
		self.lines = 0
		self.nullline = 0
		self.single_comment = 0
		self.multi_comment = 0
		self.code_line = 0
		self.is_null = False
		self.file = ''

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
		return len(string)

	def word_count(self,string):
		'''
		文件单词数统计
		'''
		word_pattern = re.compile('\S+\s?')
		tmp_result = word_pattern.findall(string)
		return len(tmp_result)

	def line_count(self,string):
		'''
		文件行数统计、空行统计与代码行统计
		'''
		null_line = 0
		code_line = 0
		sepcial_pattern = re.compile('.*\n?')
		tmp_result = sepcial_pattern.findall(string)
		for lines in tmp_result:
			if len(lines.strip()) == 0 or (len(lines.strip()) == 1 and  lines.strip() in ['{','}','#','/','\\','(',')']):
				null_line += 1
			elif len(lines.strip())>=1 and lines[0]!= '/':
				code_line += 1
		return (len(tmp_result)-1,null_line-1,code_line)

	def single_comment_count(self,string):
		'''
		单行注释统计
		'''
		re_pattern = re.compile('//')
		del_pattern = re.compile('"[^"]*//[^"]*"')
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
		del_lines = 0
		flag = 0
		multi_pattern = re.compile('/\*+[^\*]+\*/')
		single_in_multi_pattern = re.compile('//.*')
		del_pattern = re.compile('"[^"]*/\*[^"]*\*/')
		tmp_result = multi_pattern.findall(string)
		if len(tmp_result)>0:
			flag = 1
		for result1 in tmp_result:
			self.single_comment -= len(single_in_multi_pattern.findall(result1))
			for x in result1:
				if x == '\n':
					multi_lines+=1
		del_result = del_pattern.findall(string)
		for x in del_result:
			if x == '\n':
				del_lines += 1
		return multi_lines+flag - del_lines

	def file_process(self,file):
		'''
		文件处理主函数
		'''
		with codecs.open(file, 'r', 'utf-8') as f:
			self.file_string = f.read()
		print('file:'+file,end=' ')
		if self.isnull(self.file_string):
			print('null file!')
			return
		else:
			self.multi_comment += self.multi_comment_count(self.file_string)
			self.single_comment += self.single_comment_count(self.file_string)
			self.char_num += self.char_count(self.file_string)
			self.word_num += self.word_count(self.file_string)
			(self.lines,self.nullline,self.code_line) = self.line_count(self.file_string)
			self.code_line-=-self.multi_comment
			if self.opt['a'] :
				print('character:'+str(self.char_num),end = ' ')
				print('words:'+str(self.word_num),end=' ')
				print('lines:'+str(self.lines),end=' ')
				print('code_line:'+str(self.code_line),end=' ')
				print('null_line:'+str(self.nullline),end=' ')
				print('comment_line:'+str(self.single_comment+self.multi_comment))
			else:
				if not (self.opt['c'] or self.opt['w'] or self.opt['l']):
					print('Please input command\n')
					return
				if self.opt['c']:
					print('character:'+str(self.char_num),end = ' ')
				if self.opt['w']:
					print('words:'+str(self.word_num),end=' ')
				if self.opt['l']:
					print('lines:'+str(self.lines),end=' ')

	def file_select(self):
		print(self.opt['f'])
		file_list = glob.glob(self.opt['f'])
		for x in file_list:
			self.file_process(x)
			self.clear()
