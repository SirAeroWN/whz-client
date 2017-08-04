# unit test file for testing the conn.py module
#
# created by Will Norvelle on 07/17/2017


# need unittest, duh
import unittest

# also need what we're testing
import conn


# define our test class
class TestCore(unittest.TestCase):

	def setUp(self):
		pass


	# testing contstuctor
	def test_constructor_empty(self):
		c = conn.ConnInfo()
		self.assertEqual(c.host, 'localhost')
		self.assertEqual(c.port, '19001')
		self.assertEqual(c.connType, 'http')

	def test_constructor_full(self):
		c = conn.ConnInfo(host='diff', port='9001', connType='https')
		self.assertEqual(c.host, 'diff')
		self.assertEqual(c.port, '9001')
		self.assertEqual(c.connType, 'https')


	# test port.setter
	def test_port_set_str(self):
		c = conn.ConnInfo()
		c.port = '9001'
		self.assertEqual(c.port, '9001')

	def test_port_set_int(self):
		c = conn.ConnInfo()
		c.port = 9001
		self.assertEqual(c.port, '9001')

	def test_port_set_str_not_digit(self):
		c = conn.ConnInfo()
		with self.assertRaises(ValueError):
			c.port = 'asdf'

	def test_port_set_str_too_large(self):
		c = conn.ConnInfo()
		with self.assertRaises(ValueError):
			c.port = '9999999'

	def test_port_set_int_too_large(self):
		c = conn.ConnInfo()
		with self.assertRaises(ValueError):
			c.port = 9999999


	# test host.setter
	def test_host_set(self):
		c = conn.ConnInfo()
		c.host = 'test'
		self.assertEqual(c.host, 'test')

	def test_host_set_wrong_type(self):
		c = conn.ConnInfo()
		with self.assertRaises(TypeError):
			c.host = 5

	def test_host_set_empty_str(self):
		c = conn.ConnInfo()
		with self.assertRaises(ValueError):
			c.host = ''


	# test connType.setter
	def test_connType_set(self):
		c = conn.ConnInfo()
		c.connType = 'https'
		self.assertEqual(c.connType, 'https')

	def test_connType_set_wrong_type(self):
		c = conn.ConnInfo()
		with self.assertRaises(TypeError):
			c.connType = 5


	# test build address
	def test_build_address_defaults(self):
		c = conn.ConnInfo()
		self.assertEqual(c.buildAddress(url='/dataset'), 'http://localhost:19001/dataset')

	def test_build_address_url_wrong_type(self):
		c = conn.ConnInfo()
		with self.assertRaises(TypeError):
			c.buildAddress(url=5)


	# not testing other parameter validation because it's the exact same logic as tested above (might want to seperate that out, maybe)


	# test reading from config
	def test_read_from_config_default(self):
		c = conn.ConnInfo()
		c.readFromConfig()
		self.assertEqual(c.host, 'dinkleburg')
		self.assertEqual(c.port, '748')
		self.assertEqual(c.connType, 'socks5')
	

# if just running this, then run tests
if __name__ == '__main__':
	unittest.main()