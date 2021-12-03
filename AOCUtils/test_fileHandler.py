import AOCUtils
from AOCUtils.fileHandler import *

stringLines = openFileAsLineArray("testfile1")
intLines = openFileAsIntArray("testfile2")

def testWhitespace():
    assert stringLines[6] == "6455"
    assert stringLines[7] == "56 6"

def testContent():
    assert int(stringLines[0]) == 7

def testInt():
    assert intLines[6] == 6455

def testLength():
    assert len(stringLines) == 10
    assert len(intLines) == 9