# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog
import urllib2
import re

def upload():
    filename = tkFileDialog.askopenfilename()
    file = open(filename, 'rb').read()
    print filename
    # data = filename.split('/').[-1]
    req = urllib2.urlopen()
    # html = urllib2.urlopen(req).read()
    # reg = r'<a href="(.*?)">'
    # url = re.findall(reg, html)[0]
    # url = 'http://127.0.0.1:5000/%s' %url
    # entry.delete(0, END)
    # entry.insert(END, url)


def download():
    path = tkFileDialog.asksaveasfilename(defaultextension=entry.get().split('.')[-1])
    file = urllib2.urlopen(entry.get()).read()
    with open(path, 'wb') as fn:
        fn.write(file)
root = Tk()
root.title('文件分享')
root.geometry('+900+300')

entry = Entry(root, width=40)
entry.grid()

button_upload = Button(root, text='Upload', command=upload)
button_upload.grid()
button_download = Button(root, text='Download', command=download)
button_download.grid()

mainloop()