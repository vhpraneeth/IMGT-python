#!/usr/bin/env python3

from PIL import Image
# Tasks
# when config is generated, use (0,0,0)-`

conf_r = { } ; conf_w = { }

def itest():
  conf_w = {}  # conf_w for writing, dict[a]=0,0,0 ... write 0,0,0 in image
  for itm in conf_r.keys():
    conf_w[conf_r[itm]] = itm
  from PIL import Image
  img = Image.open('black.png')
  #img = img.convert("RGBA")
  px = img.load()
  for x in range(img.size[1]//2): 
      px[x, x] = (0, 0, 155)  # rgb
  print(px[4,4])
  img.save("bla.png")
  Image.open('bla.png')

def write_to_image(my_text = "hello", fname="black.png"):  # text to image - write
  #my_text = "helloolleh"
  print("Writing",my_text,"to image",fname)
  width, height = img.size 
  height=1  # testing purpose
  for ht in range(height):
    for wd in range(len(my_text)):
      tp = conf_w[my_text[wd]]
      px[wd,ht] = tuple( int(item) for item in tp[1:-1].split(',') )
  img.save(fnam)
  print("Text written to image")
  return True

def erase(fnam="black.png"):
  global img
  global px
  height=1  # testing purpose
  width, height = img.size 
  for ht in range(height):
    for wd in range(width):
      px[wd,ht] = (0, 0, 0)
  img.save(fnam)

def read_image():  # image to text - load and display/print
  #global img
  from PIL import Image
  img = Image.open('black.png')
  #img = img.convert("RGBA")
  px = img.load()
  width, height = img.size 
  height=1  # testing purpose
  for ht in range(height):
    for wd in range(width):
      tx = conf_r[str(px[wd,ht])]
      print(tx, end='')
    print()
  return True


def generate_conf():  # Generate fresh conf
  from random import shuffle
  abc = list('abcdefghijklmnopqrstuvwxyz .,`')
  shuffle(abc)
  rgb = [ ]
  for r in range(4):
    for g in range(3):
      for b in range(3):
        rgb.append( str((r,g,b)) )
  shuffle(rgb)
  rgb.remove('(0, 0, 0)')
  abc.remove('`')
  global conf_r
  global conf_w
  conf_r = { }
  conf_w = { }
  for x in range(len(abc)):
    conf_r[rgb[x]] = abc[x]
  conf_r['(0, 0, 0)'] = '`'
  for itm in conf_r.keys():  # make conf_w
    conf_w[conf_r[itm]] = itm
  print("Conf generated") #conf_r)



def read_conf(fname="conf.imgt"):  #  file to dictionary - load
  global conf_r
  global conf_w
  with open(fname) as file:
    conf = file.read()[:-1]
  conf = conf.split('\n')
  conf_r = {  }
  for lin in conf:
    cha = lin[-1]
    colr = lin[:-2]
    conf_r[colr] = cha
  conf_w = {}  # conf_w
  for itm in conf_r.keys():
    conf_w[conf_r[itm]] = itm
  print("Reading conf from file")
  return 0



def write_conf(fname="conf.imgt"):  #  dictionary to file - write
  conf = ""
  for itm in conf_r.keys():
    conf = conf + itm + '-' + conf_r[itm] + '\n'
  with open(fname, 'w') as file:
    file.write(conf)
  return 0


# https://www.askpython.com/python/python-command-line-arguments

i = input("Do you need a new conf? (y/n) : ")
if 'y' in i:
  generate_conf()
  write_conf()
else:
  read_conf()

fnam = input("Enter the file name of image : ")
if len(fnam)<3:
  fnam = "black.png"
img = Image.open(fnam)
#img = img.convert("RGBA")
px = img.load()
print("Image opened")

if 'w' in input("Do you want to read image or write? (r/w) : "):
  txt = input("Enter text : ")
  write_to_image(txt, fname=fnam)
else:
  read_image()

print("Done")

# img


# References  
'''
  https://pillow.readthedocs.io/en/stable/reference/PixelAccess.html
  https://www.bing.com/search?q=python+image+edit+pixel&FORM=AWRE
'''

# Recycle bin - code
'''  
width, height = img.size 
for x in range(img.size[1]//2): 
    img.putpixel( (x, x), (255, 0, 0, 255) ) 
#img.show() 
'''
