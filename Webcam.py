import dropbox
import time
import random
import cv2

start_time=time.time()
def take_snapshot():

    number=random.randint(1,100)
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        print("capture")
        ret,frame=videocaptureobject.read()
        imgname="img"+str(number)+".png"
        cv2.imwrite(imgname,frame)
        result=False
        return imgname
    videocaptureobject.release()
    cv2.destroyAllWindows()
def upload_dropbox(img_name):
    accesstoken="n3gxlemsEJoAAAAAAAAAAZUK4AY0DVOmtFbUWDvXrokkk2iFnfNsYBhdsfjZa_30"
    file=img_name
    filefrom=file
    fileto="/newfolder/"+(img_name)
    dbx=dropbox.Dropbox(accesstoken)
    with open(filefrom,'rb') as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded successfully")


def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_dropbox(name)

main()        