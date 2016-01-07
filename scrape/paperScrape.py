# paperScrape.py v0.00           damiancclarke             yyyy-mm-dd:2015-05-29
#---|----1----|----2----|----3----|----4----|----5----|----6----|----7----|----8
#
# Scrapes econpapers for all titles, abstracts, etc from all JPE issues.  Based
# on the url http://econpapers.repec.org/article/ucpjpolec/, and screen dumps of
# each issue.
#

import os
import urllib
import urllib2
from urllib2 import urlopen, URLError, HTTPError
import re
"""
#JPE
#-------------------------------------------------------------------------------
#--- (1) out
#-------------------------------------------------------------------------------
nameFile = open('namesJPE.txt', 'w')
absFile =  open('abstractsJPE.txt', 'w')

#-------------------------------------------------------------------------------
#--- (2) dump
#-------------------------------------------------------------------------------
base = 'http://econpapers.repec.org/article/ucpjpolec/'
addresses = ['http://econpapers.repec.org/article/ucpjpolec/default.htm']
for page in range(1,74):
    addresses += [base+'default'+str(page)+'.htm']

for a in addresses:
    source = urllib2.urlopen(a).read()
    papers = re.findall('<dt><a href="(.*)</a>', source)
    for p in papers:
        p = p.split('.htm')
        padd = base+'/'+p[0]+'.htm'
        det = urllib2.urlopen(padd).read()

        name     = re.search('<meta name="citation_title" content="(.*)">',det)
        abstract = re.search('<meta name="citation_abstract" content="(.*)">',det)        
        year     = re.search('<meta name="citation_year" content="(.*)">',det)
        volume   = re.search('<meta name="citation_volume" content="(.*)">',det)

        try:
            abstract = abstract.group(1)
        except:
            abstract = ''
        try:
            year = year.group(1)
        except:
            year = '1893'
        name = name.group(1)
        volume = volume.group(1)

        
        nameFile.write(year + ' | ' + volume + ' | ' + name +'\n')
        absFile.write(year + ' | ' + volume + ' | ' + abstract +'\n')

        print year + name
nameFile.close()
absFile.close()
"""
#QJE
#-------------------------------------------------------------------------------
#--- (1) out
#-------------------------------------------------------------------------------
nameFile = open('namesQJE.txt', 'w')
base = 'http://qje.oxfordjournals.org/content/'

for vol in range(1,131):
    for iss in range(1,5):
        if vol==29 and iss==3:
            print 'NO JOURNAL \n'
        elif vol==31 and iss==1:
            print 'NO JOURNAL \n'
        else:
            dir = base + str(vol) + '/' + str(iss) + '.toc'
            source = urllib2.urlopen(dir).read()
            papers = re.findall('(.*)doi:(.*)', source)
            for p in papers:
                result = re.split('\<.*?\>', p[0])
                title = result[1]
                print title
                year = 1886 + vol
                nameFile.write(str(year) + ' | ' + str(iss) + ' | ' + title +'\n')
                
#-------------------------------------------------------------------------------
#--- (3) count 'fertility' in names and abstracts
#-------------------------------------------------------------------------------
numFname = open('fertCountName.txt', 'w')
numFabst = open('fertCountAbst.txt', 'w')

for line in open('namesJPE.txt', 'r'):
    y = line.split('|')[0]
    fc1=line.count('fertility')
    fc2=line.count('Fertility')
    fc = fc1 + fc2
    words = str(len(re.findall(r'\w+', line)))
    numFname.write(y+';'+str(fc)+';'+words+'\n')
for line in open('namesQJE.txt', 'r'):
    y = line.split('|')[0]
    fc1=line.count('fertility')
    fc2=line.count('Fertility')
    fc = fc1 + fc2
    words = str(len(re.findall(r'\w+', line)))
    numFname.write(y+';'+str(fc)+';'+words+'\n')


for line in open('abstractsJPE.txt', 'r'):
    y = line.split('|')[0]
    fc1=line.count('fertility')
    fc2=line.count('Fertility')
    fc = fc1 + fc2
    words = str(len(re.findall(r'\w+', line)))
    numFabst.write(y+';'+str(fc)+';'+words+'\n')

numFname.close()
numFabst.close()
