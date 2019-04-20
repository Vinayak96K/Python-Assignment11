import hashlib
import sys
import os

def getChecksum(FilePath):
    hashObj=hashlib.md5()
    if(os.path.isabs(FilePath)==False):
        FilePath=os.path.getabs(FilePath)
    fd=open(FilePath,"rb")
    hashObj.update(fd.read())
    return hashObj.hexdigest()

def main():
    if(len(sys.argv)==2):
        try:
            print("Checksum of file is: {}".format(getChecksum(sys.argv[1])))
        except Exception as eObj:
            print(eObj)
            
    else:
        print("Improper argumnets! ")

if __name__ == "__main__":
    main()