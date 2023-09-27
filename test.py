import os
import sys

candidate_folder = sys.argv[1]
print('Please wait for some seconds before the process done...')
rc = os.system("handle.exe -accepteula %s | findstr pid" %(candidate_folder))
if 0 == rc:
    print('The folder is opened by above process.')
else:
    print('No process open this folder now.')
    