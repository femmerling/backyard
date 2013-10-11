import json
import uuid
import base64
import re

def new_parser(passed_object, payload_data):
	"""
	Maps passed json object from client into expected object.
	Use this for creation of new object by passing an instantiated 
	empty object into the passed_object variable
	"""
	payload = json.loads(payload_data)
	for key, value in payload.items():
		if hasattr(passed_object, key):
			setattr(passed_object, key, value)
	return passed_object

def edit_parser(passed_object, payload_data):
	"""
	Maps value from passed json object for data edit purposes.
	You need to pass in object resulting from query into the
	passed_object variable
	"""
	payload = json.loads(payload_data)
	for key, value in payload.items():
		if key != "id" and key != "created_on" and value != None:
			if hasattr(passed_object, key):
				setattr(passed_object, key, value)
	return passed_object

def generate_key():
    """
    Basic key generator. Great for AppEngine
    Generates a uuid, encodes it with base32 and strips it's padding.
    This reduces the string size from 32 to 26 chars.
    """
    return base64.b32encode(uuid.uuid4().bytes).strip('=').lower()

def thousand_separator(x=0, sep='.', dot=','):
	"""
	Added thousand separators to desired numbers
	"""
	num, _, frac = str(x).partition(dot)
	num = re.sub(r'(\d{3})(?=\d)', r'\1'+sep, num[::-1])[::-1]
	if frac:
		num += dot + frac
	return num

def json_date_format(date):
	if date:
		date = date.isoformat()
	return date

