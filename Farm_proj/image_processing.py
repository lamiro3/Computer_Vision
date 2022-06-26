import cv2
import numpy as np
import os
import glob

def equalize(imgs):
    rows, cols = img.shape[:2]
    hist = cv2.calcHist([img])

base_dir = '/content/drive/MyDrive/img_for_train'
vanila_imgs = []

dirs = [d for d in glob.glob(base_dir+'/*') if os.path.isdir(d)]
print('Collecting vanila img set...')

for dir in dirs:
    id = int(dir.split('/')[5].split('_')[1])
    files = glob.glob(dir+'/*.jpg')
    print('\t path:%s, %dfiles'%(dir, len(files)))
    
    for file in files:
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        vanila_imgs.append(img)




