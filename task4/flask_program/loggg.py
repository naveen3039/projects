import logging

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

   

i=int(input('enter a number :'))
if i%2==0:
    logger.info('it is in if condition')
     
