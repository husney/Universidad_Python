import logging

logger = logging

logger.basicConfig(level=logging.DEBUG, 
                   format='%(asctime)s %(levelname)s \nfile: [%(filename)s] line: [%(lineno)s] message: [%(message)s]\n',
                   handlers=[
                       logging.FileHandler ('MiLog.log'),
                       logging.StreamHandler()
                   ])
