import base64
def toASCII():
    try:
        file1=open("textTest.txt","r+")
        data=file1.read()
    except:
        print("file1 couldn't found")

    try:
        file2=open("ascii.txt","w+")
    
    except:
        print("file2 couldn't found")

    for character in data:
        num=ord(character)
        file2.write("<"+str(num)+">")

def fromASCII():
    import base64
    try:
        file1=open("ascii.txt","r+")
        data=file1.read()
    except:
        print("file couldn't found")
    try:
        file2=open("ascii2.txt","w+")
    except:
        print("file couldn't found")
    collect=False
    num=""
    for character in data:
    
        if character=="<":
            collect=True
            continue
        if character==">":
            collect=False
            num=int(num)
            num=chr(num)
            num=str(num)
            file2.write(num)
            num=""
        if collect==True:
            num=num+character
    

def videoToText():
    with open("al.mp4", "rb") as videoFile:
        text = base64.b64encode(videoFile.read())
        file = open("textTest.txt", "wb") 
        file.write(text)
        file.close()

def textToVideo():
    file=open("ascii2.txt","r+")
    text=file.read()
    fh = open("video.mp4", "wb")
    fh.write(base64.b64decode(text))
    fh.close()


videoToText()
toASCII()
fromASCII()
textToVideo()