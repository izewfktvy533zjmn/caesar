#!/usr/bin/env pytest
import pytest
import lexer


def test_read():
    lxr = lexer.Lexer();
    expected = "test"
    lxr.read(expected)
    actual = lxr.line

    assert actual == expected 
    
