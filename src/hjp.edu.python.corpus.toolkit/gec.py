#!/usr/bin/env python
# -*- coding:utf-8 -*-

def genSent(inFile, srcFile, tarFile):
    src = open(srcFile, 'a')
    tar = open(tarFile, 'a')
    old = []
    new = []
    ann = False
    end = 0
    for line in open(inFile, 'r'):
        line = line.strip()
        if len(line) > 0:
            if line.startswith("S ", 0, 2):
                line = line[2:]
                tokens = line.split(' ')
                old = tokens
                ann = True
                
            if line.startswith("A ", 0, 2) and "|||" in line:
                line = line[2:]
                tokens = line.split('|||')
                ids = tokens[0].split(' ')
                id1 = int(ids[0])
                id2 = int(ids[1])
                if ann:
                    if id1 > 0:
                        new.extend(old[:id1])
                        if len(tokens[2]) > 0:
                            new.append(tokens[2])
                    else:
                        if len(tokens[2]) > 0:
                            new.append(tokens[2])  
                    ann = False                      
                else:
                    if end < id1:
                        new.extend(old[end:id1])
                    if len(tokens[2]) > 0:
                        new.append(tokens[2])
                end = id2
        else:
            if len(old[end:]) > 0:
                new.extend(old[end:])
            print old
            print new
            src.write(' '.join(old) + '\r\n')
            tar.write(' '.join(new) + '\r\n')
            old = []
            new = []
            end = 0
            ann = False
            
if __name__ == '__main__':
    inFile = '/Users/hjp/Downloads/gec.txt'
    srcFile = '/Users/hjp/Downloads/srcFile.txt'
    tarFile = '/Users/hjp/Downloads/tarFile.txt'
    genSent(inFile, srcFile, tarFile)    
    