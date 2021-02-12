import argparse 
import glob
import os
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("folder")

args=parser.parse_args()

folder=args.folder

filenames=glob.glob('Labels/'+folder+'/*.txt')
os.system(f'mkdir -p Labels/{folder}L')

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

for file in filenames :
	with open(file,'r') as f :
		lines=f.readlines()
		box=[float(p) for p in lines[1].split()]
		img_path=file.split('/')[-1][:-3]+'jpg'
		img=cv2.imread('Images/'+folder+f'/{img_path}')
		bb=convert(img.shape,box)

	fields=file.split('/')
	fields[1]+='L'
	file2='/'.join(fields)	
	
	with open(file2,'w') as f :
		f.write('0 '+' '.join([str(p) for p in bb]))

