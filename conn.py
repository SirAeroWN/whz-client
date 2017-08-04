# mostly for holding connection info like host and port
#
# created by Will Norvelle on 07/17/2017


# use built in logging library
import logging
# configure logging, will not overwrite if basicConfig already created by importing module
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(filename)s:%(funcName)s: %(message)s', level=logging.DEBUG)

# use pathlib module for checking that config files exist
from pathlib import Path

# main class for holding info and functions
class ConnInfo():
	"""mostly for holding connection info like host and port and related functions"""
	def __init__(self, host='localhost', port=19001, connType='http'):
		self.host = host
		self.port = str(port)
		self.connType = connType

	# property decorators and setters
	@property
	def host(self):
		'''host property'''
		return self._host

	@host.setter
	def host(self, host):
		self._host = self.validateHost(host)

	@property
	def port(self):
		'''port property'''
		return self._port

	@port.setter
	def port(self, port):
		self._port = self.validatePort(port)

	@property
	def connType(self):
		'''connection type property'''
		return self._connType

	@connType.setter
	def connType(self, connType):
		self._connType = self.validateConnType(port)


	# property validation functions
	def validateHost(self, host):
		if type(host) is not str:
			logging.error('host must be of type str')
			raise TypeError('host must be of type str')
		elif host == '':
			logging.error('host cannot be an empty string')
			raise ValueError('host cannot be an empty string')
		else:
			# we are good to go
			return host

	def validatePort(self, port):
		# port can be passed as either a str or an int, need to evaluate to an int either way
		if type(port) not in [str, int]:
			logging.error('port can only be passed as a str or an int')
			raise TypeError('port can only be passed as a str or an int')
		elif type(port) is str and not port.isdigit():
			logging.error('if port passed as str, must consist solely of digits. recieved: {}'.format(port))
			raise ValueError('if port passed as str, must consist solely of digits. recieved: {}'.format(port))
		elif int(port) > 65535:
			logging.error('port number cannot be larger than 65535, passed port was {}'.format(port))
			raise ValueError('port number cannot be larger than 65535, passed port was {}'.format(port))
		else:
			# g2g
			return str(port).strip()

	def validateConnType(self, port):
		# has to be a string
		if type(connType) is not str:
			logging.error('connType must be a str')
			raise TypeError('connType must be a str')
		else:
			# nothing else we can realistically check
			return connType


	# now we get to the utility functions

	# read the values from a config file
	def readFromConfig(self, filePath='whz_conn.config'):
		'''
		Read host, port, and connType from a config file, format as such:

		host=hostname
		port=portnumber
		conntype=connectiontype

		Names are case sensitive, so Host=localhost will not be read but host=LoCaLhOsT is fine. Make sure these are all each on their own line. If there are multiple definitions, the last definition will be used.

		If a value is not found, then it will not be changed from its current value.
		'''

		# fist check that filePath is a string
		if type(filePath) is not str:
			logging.error('expect filepath to be a string, is a {}'.format(type(filepath)))
			raise TypeError('expect filepath to be a string, is a {}'.format(type(filepath)))
		
		# now we need to check that the file exists
		checkFile = Path(filePath)
		if not checkFile.is_file():
			logging.error('file {} could not be found'.format(filePath))
			raise FileNotFoundError('file {} could not be found'.format(filePath))

		# the strings we'll be looking for in the config file:
		hostMarker = 'host='
		portMarker = 'port='
		connTypeMarker = 'conntype='

		# if we've gotten to hear then the file must exist so let's open it
		with open(filePath, 'r') as config:
			# now we should iterate through every line looking for our three values
			for line in config:
				if hostMarker in line:
					self.host = line[len(hostMarker):].strip()
				elif portMarker in line:
					self.port = line[len(portMarker):].strip()
				elif connTypeMarker in line:
					self.connType = line[len(connTypeMarker):].strip()

		# and now we're done and with handles all the cleanup


	def buildAddress(self, url, host=None, port=None, connType=None):
		# if host, port, or connType aren't passed then use property
		host = host or self._host
		port = port or self._port
		connType = connType or self._connType

		# now check that they comply with our validation
		host = self.validateHost(host)
		port = self.validatePort(port)
		connType = self.validateConnType(connType)

		if type(url) is not str:
			logging.error('url must be a str')
			raise TypeError('url must be a str')

		# if we've arrived down here then all the parts are good to go
		address = connType + '://' + host + ':' + port + url
		logging.debug("built address: {}".format(address))
		return address