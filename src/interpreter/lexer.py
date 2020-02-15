#!/usr/bin/env python3


class Lexer:
    def __init__(self, fp):
        self.lin = fp


    def read(self):
        self.line = self.lin.readline()
    

    def close(self):
        self.lin.close()

