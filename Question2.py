import hashlib
import sys
import os

def getChecksum(FilePath):
    hashObj=hashlib.md5()
    if(os.path.isabs(FilePath)==False):
        FilePath=os.path.abspath(FilePath)
    fd=open(FilePath,"rb")
    hashObj.update(fd.read())
    return str(hashObj.hexdigest())

def ReportDuplicate(dirFilePath):
    fd=open('Log.txt','a+')
    if(os.path.isabs(dirFilePath)==False):
        dirFilePath=os.path.getabs(dirFilePath)
    if(os.path.isdir(dirFilePath)):
        for foldername,subfolder,filename in os.walk(dirFilePath):
            dVar=dict()
            for file in filename:
                strCheckSum=getChecksum(str(dirFilePath+'/'+file))
                if((dVar.get(strCheckSum)!=None)):
                    fd.write(str(dirFilePath+'/'+file+'\n'))
                else:
                    dVar.update({strCheckSum :str(dirFilePath+'/'+file) })
            break

def main():
    if(len(sys.argv)==2):
        try:
            ReportDuplicate(sys.argv[1])
        except Exception as eObj:
            print(eObj)
            
    else:
        print("Improper argumnets! ")

if __name__ == "__main__":
    main()