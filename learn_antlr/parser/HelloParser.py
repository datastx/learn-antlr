# Generated from /Users/brianmoore/githib.com/datastx/learn-antlr/learn_antlr/parser/grammar_files/Hello.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,7,2,0,7,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,5,0,2,1,0,0,0,2,
        3,5,1,0,0,3,4,5,3,0,0,4,5,5,2,0,0,5,1,1,0,0,0,0
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Hello'", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "HELLO", "NAME", "WHITESPACE" ]

    RULE_greeting = 0

    ruleNames =  [ "greeting" ]

    EOF = Token.EOF
    HELLO=1
    NAME=2
    WHITESPACE=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GreetingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HELLO(self):
            return self.getToken(HelloParser.HELLO, 0)

        def WHITESPACE(self):
            return self.getToken(HelloParser.WHITESPACE, 0)

        def NAME(self):
            return self.getToken(HelloParser.NAME, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_greeting

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreeting" ):
                return visitor.visitGreeting(self)
            else:
                return visitor.visitChildren(self)




    def greeting(self):

        localctx = HelloParser.GreetingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_greeting)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(HelloParser.HELLO)
            self.state = 3
            self.match(HelloParser.WHITESPACE)
            self.state = 4
            self.match(HelloParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





