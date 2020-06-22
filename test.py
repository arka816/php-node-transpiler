from phplexer import tokenizer
from phpparser import generateAST

f = open("server.php", "r", encoding="utf-8")
s = f.read()
tokenlist = tokenizer(s[s.find("php")+3:])
root=generateAST(tokenlist)