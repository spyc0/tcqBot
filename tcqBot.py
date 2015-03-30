#!/usr/bin/python2

# EXAMPLE SCRIPT FOR TINYCHAT BOT
# >https://github.com/alyak/pytiny

# BRINGS IN 9 BOTS, EACH SPEAK WHEN ENTERING, 9TH BOT WILL CONTINUE SPEAKING.
# NOTE: Line 125 of tinychat.py (#)commented out, or doesnt't work.
# 2015 ~k

# YOU MAY NEED TO DO THE FOLLOWING FIRST [Debian]:
# torsocks wget https://bootstrap.pypa.io/get-pip.py
# 	>http://pip.readthedocs.org/en/latest/installing.html
# pip install cffi
# 	>If you're missing ffi.h >apt-get install libffi-dev
# pip install python-librtmp
# 	>http://pythonhosted.org/python-librtmp

import pytiny
import time, socket, re, random, urllib, urllib2
from urllib import urlencode
from urllib2 import urlopen, Request

proxy_support = urllib2.ProxyHandler({"https" : "127.0.0.1:8118"})
opener = urllib2.build_opener(proxy_support) # apt-get install privoxy

SEED_ = 9
    
while not SEED_ <= 0:
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
		count = random.randint(3, 5)
		length = count + 1
		for i in range(count):
			rnick = (generate_nick(length))
	tc = pytiny.TinyChat()
	tc.nick(rnick)
	tc.set_room("scenefag")
	tc.connect()
	buf = tc.recv()
	print buf
	stfu = random.randint(10, 60)
	tc.msg("*WHITEPOWER!*", "#0")
	time.sleep(stfu)
	SEED_ = SEED_ - 1
	if SEED_ <= 0:
		while True:
			buf = tc.recv()
			print buf
			stfu = random.randint(180, 600) # Every 3-10 mins.
			getquote = 'http://randomquotesgenerator.com/index.php/rest.html'
			rquote = re.compile(r'<i>.*?</i>')
			qdata = opener.open(getquote).read()
			qpick = rquote.findall(qdata)
			ohai = re.sub(r'<[^>]*?>', '', unicode(qpick[0]))
			tc.msg(ohai)
			time.sleep(stfu)
