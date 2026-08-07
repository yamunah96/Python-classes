import logging

def get_logger():
    logger= logging.getLogger("BankingSystem")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        filehandler=logging.FileHandler("banklog.txt",mode='a')
        formatter = logging.Formatter(fmt="%(asctime)s | %(levelname)s | %(name)s |%(message)s",datefmt="%d-%m-%Y %H:%M:%S:%p",)
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
    return logger

