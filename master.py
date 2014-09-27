'''master.py'''
import subprocess
import logging

def main():
    proc = ['python', 'parent.py']
    logpath = 'parent.log'
    with open(logpath, 'wb') as f:
        p = subprocess.Popen(
            proc,
            stdout=f,
            stderr=subprocess.STDOUT)
        logging.warn('task started, waiting to finish')
        res = p.wait()
        logging.warn(res)


if __name__ == '__main__':
    main()
