import os
import sys
from pathlib import Path
import time

TIME_TO_DELETE_AFTER = int(sys.argv[1]) # in seconds
DIRECTORY_TO_CHECK = str(sys.argv[2]) # path to directory containing files to be deleted
CURRENT_TIME = time.time()

files = Path(DIRECTORY_TO_CHECK).glob('*')
for file in files:
    createdDate = os.path.getctime(file)
    modifiedDate = os.path.getmtime(file)
    canBeDeleted = (createdDate + TIME_TO_DELETE_AFTER < CURRENT_TIME) and (modifiedDate + TIME_TO_DELETE_AFTER < CURRENT_TIME)
    if canBeDeleted:
        os.remove(file)
        


    

