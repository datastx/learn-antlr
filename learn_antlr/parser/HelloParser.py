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
        4,1,4,7,2,0,7,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,2,5,0,2,1,
        0,0,0,2,3,5,3,0,0,3,4,7,0,0,0,4,5,5,3,0,0,5,1,1,0,0,0,0
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "WHITESPACE" ]

    RULE_operation = 0

    ruleNames =  [ "operation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NUMBER=3
    WHITESPACE=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.NUMBER)
            else:
                return self.getToken(HelloParser.NUMBER, i)

        def getRuleIndex(self):
            return HelloParser.RULE_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = HelloParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(HelloParser.NUMBER)
            self.state = 3
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 4
            self.match(HelloParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





