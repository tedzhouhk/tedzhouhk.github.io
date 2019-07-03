import os

dir='source/images/20190702_2/'
f=[]
filearr=os.listdir(dir)
for f in filearr:
    if f.endswith('.jpg'):
        print('- '+dir[6:]+f)
