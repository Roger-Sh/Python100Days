import logging

a=1
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(lineno)d -  %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')



