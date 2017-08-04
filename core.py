# handles direct interaction with WhereHows via making the http requests
#
# created by Will Norvelle on 07/14/2017

# using requests library for working with http requests
import requests

# using built in json library as well
import json

# use built in logging library, assume higher up modules have already done basic configurations
import logging

# wrapper for POST request
def post(address, json=None, data=None, timeout=3, **kwargs):
	# first make sure everything is alright with our arguments
	if type(address) is not str:
		logging.error('address must be of type str')
		raise TypeError('address must be of type str')
	elif address == '':
		logging.error('address cannot be an empty string')
		raise ValueError('address cannot be an empty string')
	elif json == None and data == None:
		# we've nothing to send in the post, so we should error
		logging.error('json and data are both None, one of them must have a value')
		raise TypeError('json and data are both None, one of them must have a value')
	elif json != None and data != None:
		# we have both json and data, but only want one of them defined
		logging.error('json and data both have values, only one of these should be passed')
		raise TypeError('json and data both have values, only one of these should be passed')
	elif type(timeout) not in [int, float]:
		# timeout should be a number
		logging.error('timeout needs to be a float or an int')
		raise TypeError('timeout needs to be a float or an int')
	elif type(retries) not in [int, float]:
		# retries should be a number
		logging.error('retries needs to be a float or an int')
		raise TypeError('retries needs to be a float or an int')

	# we've checked all the parameters to make sure they're fine, so let's make the request
	resp = requests.post(address, json=json, data=data, timeout=timeout, kwargs)
	logging.info('request made without error')

	# WhereHows usually returns 200 even if there was an internal error, the times that it doesn't are bad requests, so we should check for that
	if resp.status_code != 200:
		# we've got a bad status code, so let's raise an error and pass on the relevent info
		logging.error('recieved status code {} instead of 200'.format(resp.status_code))
		raise ValueError('recieved status code {} instead of 200'.format(resp.status_code), resp.text)

	# otherwise, WhereHows returns json, which we can easily convert to a dict, so let's do that
	try:
		respVal = resp.json()
	except json.decoder.JSONDecodeError:
		# it appears that something is wrong with the json, let's return the text instead
		logging.warning('response could not be parsed as json, returning text instead')
		respVal = resp.text

	# and finally we return what we got
	return respVal

# wrapper for PUT request
def put(address, json=None, data=None, timeout=3, **kwargs):
	# first make sure everything is alright with our arguments
	if type(address) is not str:
		logging.error('address must be of type str')
		raise TypeError('address must be of type str')
	elif address == '':
		logging.error('address cannot be an empty string')
		raise ValueError('address cannot be an empty string')
	elif json == None and data == None:
		# we've nothing to send in the post, so we should error
		logging.error('json and data are both None, one of them must have a value')
		raise TypeError('json and data are both None, one of them must have a value')
	elif json != None and data != None:
		# we have both json and data, but only want one of them defined
		logging.error('json and data both have values, only one of these should be passed')
		raise TypeError('json and data both have values, only one of these should be passed')
	elif type(timeout) not in [int, float]:
		# timeout should be a number
		logging.error('timeout needs to be a float or an int')
		raise TypeError('timeout needs to be a float or an int')
	elif type(retries) not in [int, float]:
		# retries should be a number
		logging.error('retries needs to be a float or an int')
		raise TypeError('retries needs to be a float or an int')

	# we've checked all the parameters to make sure they're fine, so let's make the request
	resp = requests.put(address, json=json, data=data, timeout=timeout, kwargs)
	logging.info('request made without error')

	# WhereHows usually returns 200 even if there was an internal error, the times that it doesn't are bad requests, so we should check for that
	if resp.status_code != 200:
		# we've got a bad status code, so let's raise an error and pass on the relevent info
		logging.error('recieved status code {} instead of 200'.format(resp.status_code))
		raise ValueError('recieved status code {} instead of 200'.format(resp.status_code), resp.text)

	# otherwise, WhereHows returns json, which we can easily convert to a dict, so let's do that
	try:
		respVal = resp.json()
	except json.decoder.JSONDecodeError:
		# it appears that something is wrong with the json, let's return the text instead
		logging.warning('response could not be parsed as json, returning text instead')
		respVal = resp.text

	# and finally we return what we got
	return respVal

# wrapper for GET request
def get(address, params={}, timeout=3, **kwargs):
	# first make sure everything is alright with our arguments
	if type(address) is not str:
		logging.error('address must be of type str')
		raise TypeError('address must be of type str')
	elif address == '':
		logging.error('address cannot be an empty string')
		raise ValueError('address cannot be an empty string')
	elif type(timeout) not in [int, float]:
		# timeout should be a number
		logging.error('timeout needs to be a float or an int')
		raise TypeError('timeout needs to be a float or an int')

	# now that our arguments are probably ok, let's make the request
	resp = requests.get(address, params=params, timeout=timeout, kwargs)
	logging.info('request made without error')

	# again, we usually get a 200 unless something went catastophically wrong
	if resp.status_code != 200:
		# we've got a bad status code, so let's raise an error and pass on the relevent info
		logging.error('recieved status code {} instead of 200'.format(resp.status_code))
		raise ValueError('recieved status code {} instead of 200'.format(resp.status_code), resp.text)

	# we should be getting json back if we get a 200, but sometimes it isn't json, so let's be able to handle that
	try:
		respVal = resp.json()
	except json.decoder.JSONDecodeError:
		# it appears that something is wrong with the json, let's return the text instead
		logging.warning('response could not be parsed as json, returning text instead')
		respVal = resp.text

	# and finally we return what we got
	return respVal