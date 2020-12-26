import logging

logger = logging

logger.basicConfig(level=logging.WARNING,
                   format='%(levelname)s %(asctime)s \nFile: [%(filename)s]\nLine: [%(lineno)s]\nMessage: "%(message)s"\n',
                   handlers=[
                       logging.FileHandler("EventLog.log"),
                       logging.StreamHandler()
                   ]
                   )


