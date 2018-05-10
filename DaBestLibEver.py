# DaBestLibEver.py
"""This wonderful Python library does great stuff,
including translating regular strings into SHOUTED STRINGS!!!"""

def shout(stuff):
  """str -> str
  Converts the string passed to it to all uppercase, with exclamation points.
  >>> shout("Hello")
  'HELLO!!!!!'
  >>> shout("bye")
  'BYE!!!!!'
  """
  return stuff.upper() + "!!!!!"

def whisper(stuff):
	"""str -> str
	Converts the string pass to it to all uppercase, with asterics.
	>>> whisper("HELLO")
	'*hello*'
	>>>whisper("GoOdByE")
	'*goodbye*'
	"""
	return '*' + stuff.lower() + '*'

if __name__ == "__main__":
  import doctest
  doctest.testmod()
