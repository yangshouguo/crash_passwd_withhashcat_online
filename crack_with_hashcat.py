#!/usr/bin/env python
# coding=utf-8
import sys
import os
def print_passwd():
    m = -1
    hashvalue = sys.argv[1]
    if (hashvalue[0]=='$' and hashvalue[2]=='$'):
        type = int(hashvalue[1])
        if (type == 1):
            m = 500
        elif type == 5:
            m = 7400
        elif type == 6:
            m = 1800
        else:
            print 'hash type error'
    saved_file_name = 'crack.out'
    if (m != -1):
        cmd = "hashcat --length-limit-disable -m %d -a 0 -o %s --potfile-disable '%s' %s >/dev/null 2>&1" % (m,saved_file_name,sys.argv[1],sys.argv[2])
        print cmd
        print 'crashing ...'
        retval = os.popen(cmd)
            #print 'no cracked passwd'
        return retval.read()        

def print_help():
    print "please use as: python crack_with_hashcat.py '$1$uOM6WNc4$r3ZGeSB11q6UUSILqek3J1' example.dict"
if len(sys.argv)<3:
    print_help()
else:
    print print_passwd()


