# Generated from /Users/brianmoore/githib.com/datastx/learn-antlr/learn_antlr/parser/grammar_files/Hello.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete generic visitor for a parse tree produced by HelloParser.

class HelloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloParser#greeting.
    def visitGreeting(self, ctx:HelloParser.GreetingContext):
        return self.visitChildren(ctx)



del HelloParser