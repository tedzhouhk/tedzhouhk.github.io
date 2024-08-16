import os

dir='source/images/20240815/'
f=[]
filearr=os.listdir(dir)
for f in filearr:
    if f.endswith('.jpg'):
        print('- '+dir[6:]+f)
