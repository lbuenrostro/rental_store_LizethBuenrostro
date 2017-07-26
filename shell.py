# import core
import time 
import sys
typing_speed = 25
def slow_type(t):
    for l in t:
        sys.stdout.write(l) 
        sys.stdout.flush() 
        time.sleep(typing_speed / 970.0)
    return input

def main():
    slow_type('\nWELCOME to Tennis Equipment Rental\n')
    slow_type('\nEntering...\n')
    time.sleep(1)
    
    print('Thanks for stopping by, come back SOON!!') 
if __name__ == '__main__':
    main()
