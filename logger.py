__author__ = 'aramirez'
import logging
import logging.handlers
import libgral

INFO = 'INFO'
DEBUG = 'DEBUG'
WARNIG = 'WARNING'
ERROR = 'ERROR'
CRITICAL = 'CRITICAL'

def log(FILENAME,NAMEPROC, TYPELOG, DESCRIPTION):
    objlibgral = libgral
    RUTA = "/var/log/KERNOTEK"

    if objlibgral.validatePath(RUTA):
        RUTA =  RUTA + "/"
        FILENAME =  RUTA + FILENAME + ".log"
        logger = logging.getLogger(NAMEPROC)
        LOGFILESIZE = 31457280
        MAXLOGFILES = 5
        logger.setLevel(logging.DEBUG)
        handler = logging.handlers.RotatingFileHandler(filename=FILENAME, mode='a', maxBytes= LOGFILESIZE, backupCount= MAXLOGFILES)
        formatter = logging.Formatter\
                    ('%(asctime)s|%(levelname)-8s|%(name)-5s|%(lineno)4s| %(message)-s')

        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if TYPELOG.upper() == INFO:
            logger.info(DESCRIPTION)

        elif TYPELOG.upper() == DEBUG:
            logger.debug(DESCRIPTION)

        elif TYPELOG.upper() == WARNIG:
            logger.warning(DESCRIPTION)

        elif TYPELOG.upper() == ERROR:
            logger.error(DESCRIPTION)
            return

        elif TYPELOG.upper() == CRITICAL:
            logger.critical(DESCRIPTION)

        else:
            logger.error('Tipo de Log Erroneo')