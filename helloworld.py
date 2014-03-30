#!/usr/bin/python2.7/
#Filename: helloworld.py

a = 'global'

def test_global():
    '''Global variable test.

    Nice to meet you.'''
    global a
    a = a + 'test'
    return a

print test_global.__doc__ 
print test_global() 
