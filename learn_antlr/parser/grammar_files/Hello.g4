grammar Hello;

NUMBER: [0-9]+;
WHITESPACE: [ \t\r\n]+ -> skip;

start: NUMBER ('+' | '-') NUMBER;