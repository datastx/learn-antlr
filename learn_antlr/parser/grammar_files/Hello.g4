grammar Hello;

HELLO: 'Hello';
NAME: [a-zA-Z]+;
WHITESPACE: ' ';
greeting: HELLO WHITESPACE NAME;
