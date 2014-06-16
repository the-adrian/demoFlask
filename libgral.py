import os
import sys

def validatePath(strpath):
	""" Valida que la ruta exista, de lo contrario tratara de crearla
		@param strpath: Ruta que se verificara
	"""
	try:
		if not os.path.isdir(strpath):
			## Tratara de crearla
			os.makedirs(strpath)
		return True
	except OSError, err:
		if err.errno == 13:
			print >>sys.stderr, \
				"Can't create log directory \"%s\", check permission" %(strpath)

def separateDate(date):
    return date.split(' ')


