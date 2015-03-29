#!/usr/bin/python2

# EXAMPLE SCRIPT FOR TINYCHAT BOT
# >https://github.com/alyak/pytiny

# tcqpBot.py DEFAULT PROTOTYPE
# SINGLE BOT / Posts random quotes from randomquotesgenerator.com
#              and occasionally posts <pic> from Tinychat .xml

# NOTE: Line 125 & 140 of tinychat.py (#)commented out, or might crash.
# 2015 ~k

import pytiny
import time, re, random, urllib, urllib2
from urllib import urlencode
from urllib2 import urlopen, Request

proxy_support = urllib2.ProxyHandler({"https" : "127.0.0.1:8118"})
opener = urllib2.build_opener(proxy_support) # apt-get install privoxy

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
def generate_nick(length):
	word = ""
	for i in range(length):
		if i % 2 == 0:
			word += random.choice(CONSONANTS)
		else:
			word += random.choice(VOWELS)
	return word
if __name__ == "__main__":
	count = random.randint(3, 6)
	length = count + 1
	for i in range(count):
		rnick = (generate_nick(length))
		
tc = pytiny.TinyChat()
tc.nick(rnick)
tc.set_room("scenefag")
tc.connect()
	
while True:
	buf = tc.recv()
	print buf
	stfu = random.randint(45, 80)
	getqchoice = random.randint(0, 1)
	if getqchoice == 0:
		getquote = 'http://api.tinychat.com/scenefag.xml' # Would like it to choose random <pic> and not first that it finds.
		rquote = re.compile(r'<pic>.*?</pic>')
		qdata = opener.open(getquote).read()
		qpick = rquote.findall(qdata)
		pic = re.sub(r'<[^>]*?>', '', unicode(qpick[0]))
		ohai = '*Say cheese!* ' + pic # Why is it not saying "Say cheese!" first before posting pic url? fffffffffffff
		if ohai == '':
			getquote = 'http://randomquotesgenerator.com/index.php/rest.html'
			rquote = re.compile(r'<i>.*?</i>')
	elif getqchoice == 1:
		getquote = 'http://randomquotesgenerator.com/index.php/rest.html'
		rquote = re.compile(r'<i>.*?</i>')
	qdata = opener.open(getquote).read()
	qpick = rquote.findall(qdata)
	ohai = re.sub(r'<[^>]*?>', '', unicode(qpick[0]))
	tc.msg(ohai, "#0")
	time.sleep(stfu)
