#!/usr/bin/env python3
# print directory contents to csv

import os, csv, sys
import docx
import math
import codecs
import datetime

wanted = ['.docx', '.doc', '.pdf', '.DOC', '.PDF', '.DOCX', '.txt', '.TXT', '.pub', '.xls', '.xlsx']

if len(sys.argv) <= 1:
    print("Please provide [1]folder location and [2]output file.csv")
    sys.exit(-1)
    
def convertFileSize(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

def getDocxSummary(file):
    try:
        doc = docx.Document(file)
        ftext = ''
        for p in doc.paragraphs:
            for run in p.runs:
                ftext += run.text
        if len(ftext) > 200:
            return ftext[0:200]
        else:
            return ftext
    except:
        return ''
            

with open(sys.argv[2],'w', encoding='utf-8', newline='') as f:        
    w = csv.writer(f, delimiter=",")
    w.writerow(['file', 'complete path', 'file extension', 'file size', 'content-summary', 'last modified'])
    for path, dirs, files in os.walk(sys.argv[1]):
        print(dirs)
        for filename in files:
            fn, fext = os.path.splitext(filename)

            if fext not in wanted:
                continue
            # check if summary can be provided for some file extensions
            content_summary = ''
            if fext == '.docx' or fext == '.doc':
                content_summary = getDocxSummary(os.path.join(path, filename))

            fsize = convertFileSize(os.path.getsize(os.path.join(path, filename)))
            ftimestamp = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(path, filename)))

            try:
                w.writerow([filename, os.path.join(path, filename), fext, fsize, content_summary, ftimestamp])
                print(path + '/' + filename)
            except UnicodeEncodeError:
                # w.writerow(['UnicodeEncodeError'])
                print('UnicodeError')



