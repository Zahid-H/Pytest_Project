import logging
#we are using this function to see the logs of test execution
class Log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename='.\\logs\\nopcommerce.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt= "%Y-%m-%d %H:%M:%S", force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger