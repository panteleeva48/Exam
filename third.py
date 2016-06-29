import re
import os
def readfile(name):
    file = open(name, 'r', encoding = 'utf-8')
    fileread = file.read()
    file.close()
    return fileread

def init1 (fileread):
    initname1 = re.findall(' ([А-ЯЁ]\. [А-ЯЁ][а-яё]+)[^-а-яАЯё]',fileread)
    initname2 = re.findall(' ([А-ЯЁ]\. [А-ЯЁ][а-яё]+\-[А-ЯЁ][а-яё]+)\W',fileread)
#    print(initname2)
    initname = initname1 + initname2
#    print(initname)
    allnames = ''
    for elem in initname:
        allnames = allnames + elem + '\n'
    print(allnames)
    return initname

init1(readfile('ex.txt'))

def init2(fileread,initname):
    name1 = re.findall('([А-ЯЁ]\. [А-ЯЁ]\. [А-ЯЁ][а-яё]+)\W',fileread)
    name2 = re.findall('([А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+)\W',fileread)
    names = name1 + name2 + initname
#    n = ''
#    for i in name:
#        n = n + i + '\n'
#    print(n)
    return names

#init2(readfile('ex.txt'),init1(readfile('ex.txt')))

def sep(names):
#    print(names)
    new = []
    for l in names:
        s = re.sub('([А-ЯЁ]\. )|([А-ЯЁ][а-яё]+ )','',l)
        new.append(s)
#    print(new)
    return(new)

#sep(init2(readfile('ex.txt'),init1(readfile('ex.txt'))))

def make(new):
    for one in new:
        try:
            os.makedirs(one)
        except OSError: 
            pass

make(sep(init2(readfile('ex.txt'),init1(readfile('ex.txt')))))

def findsent(fileread,new):
    filesplit = re.split('[.?!]',fileread)
#    print(filesplit)
    for el in new:
        if el


splitsent(readfile('ex1.txt'))
    
    
