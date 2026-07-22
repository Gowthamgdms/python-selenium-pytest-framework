import logging
import os

class LogGenerator:

    @staticmethod
    def loggen():

        log_path = os.path.join("logs", "framework.log")

        logging.basicConfig(
            filename=log_path,
            format="%(asctime)s : %(levelname)s : %(message)s",
            datefmt="%d/%m/%Y %I:%M:%S %p",
            level=logging.INFO,
            force=True
        )

        logger = logging.getLogger()

        return logger