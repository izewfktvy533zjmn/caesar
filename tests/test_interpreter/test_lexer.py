#!/usr/bin/env pytest
import os
import sys

import pytest
import interpreter.lexer as lxr

    
def test_read():
    expected = "test"
    file_name = "test"
    
    with open(file_name, 'w') as fp:
        fp.write(expected)
    
    fp = open(file_name, 'r')

    lexer = lxr.Lexer(fp)
    lexer.read()
    actual = lexer.line
    
    lexer.close()
    os.remove(file_name)

    assert actual == expected 
    
