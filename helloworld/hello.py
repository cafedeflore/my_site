# coding=utf-8
__author__ = 'cafedeflore'
import subprocess

p = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

retval = p.wait()
print "start"
for line in p.stdout.readlines():
    print line,
print "finished"
