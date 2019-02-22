import time
import sys
for i in range(5):
    if i == 4:
        sys.stdout.write('\r')
        sys.stdout.write('100%')
    else:
        sys.stdout.write('\r')
        sys.stdout.write('{:.2%}'.format((i + 1) / 5))
        sys.stdout.flush()
        time.sleep(1)