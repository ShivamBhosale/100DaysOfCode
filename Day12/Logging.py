"""DEBUG, INFO, WARNING, ERROR, CRITICAL"""
import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("You have got 10 mails in your inbox")
logging.critical("Components failed!!")
logging.warning("Check mails ASAP")

print("\n")
logger = logging.getLogger("Shivam Bhosale's Logger")
logger.info("You have an exam tommorrow")
logger.critical("Study for the exam")
logger.log(logging.ERROR, "An error occured while compiling")

logger.setLevel(logging.DEBUG)
print("\n")
handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.debug("Debug message")
logger.info("You have completed the process successfully")
