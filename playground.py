class C(object):
	"""C test class"""
	def __init__(self, arg=''):
		self.arg = arg
	
	@property
	def arg(self):
		return self._arg

	@arg.setter
	def arg(self, argx):
		if isinstance(argx, int):
			raise TypeError('arg mustn\'t be an int!')
		elif not isinstance(argx, str):
			raise TypeError('arg must be a string!')
		else:
			self._arg = argx