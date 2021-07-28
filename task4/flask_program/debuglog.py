import logging

logging.basicConfig(filename='debug.txt', filemode='w',level=logging.INFO)

def fact(n):
    logging.info(f'input given as entered {n}')
    total=1
    for i in range(n+1):
        logging.info(f'it is in for loop i={i} ')
        total*=i
        logging.info(f'it is in for loop total={total} ')
    return total
print(fact(5))
