'''child.py'''
import os
import logging
import time

def main():
    logging.warn('child is logging, pid: {0}'.format(os.getpid()))
    time.sleep(15)
    logging.warn('child is logging, pid: {0}'.format(os.getpid()))

if __name__ == '__main__':
    main()
