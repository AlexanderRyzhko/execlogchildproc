'''parent.py'''
import os
import logging

def main():
    proc = ['python', 'child.py']
    logging.warn('parent is logging, pid: {0}'.format(os.getpid()))
    os.execvp(proc[0], proc)

if __name__ == '__main__':
    main()
