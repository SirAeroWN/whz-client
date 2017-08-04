# unit test file for testing the core.py module
#
# created by Will Norvelle on 07/14/2017


# need unittest, duh
import unittest

# also need what we're testing
import core


# define our test class
class TestCore(unittest.TestCase):
	host = 'localhost'
	port = 19001

	# address builder
	def addressBuilder(self, host, port, url):
		return 'http://' + host + ':' + str(port) + url

	def setUp(self):
		pass

	

# if just running this, then run tests
if __name__ == '__main__':
	unittest.main()