import logging


logger = logging

logger.basicConfig(level=logging.WARNING,
                   handlers=[logging.FileHandler("EventLog.log"),
                             logging.StreamHandler()
                             ],
                    format='%(asctime)s %(levelname)s\nFile: [%(filename)s]\nLine: [%(lineno)s]\nMessage: "%(message)s"\n'
                   )

