# -*- coding: utf-8 -*- 
'''this is my test file 
'''

import unittest
import time

def loginfo():
    print "this is defunction"
class Function(unittest.TestCase):
    def Fun_Testcase1(self):
        print("this is my first python testcase")
        loginfo()
        time.sleep(1)
    def Fun_Testcase2(self):
        print("this is my second python testcase")
'''
if __name__=="__main__":
    unittest.main()
'''
if __name__=="__main__":
    print "this is pass result"
    #print time.__doc__
else:
    print "this is fail result"



#print time.__dict__

#print __file__

#print __doc__

unittest.main()

print "this is my git test"