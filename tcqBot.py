#!/usr/bin/python2

# LE {t}iny{c}hat{q}uote_Bot FOR NORWACK'S pytiny MODULE
# >https://github.com/alyak/pytiny
import pytiny

# BRINGS IN 9 BOTS, EACH SPEAK WHEN ENTERING, 9TH BOT WILL CONTINUE SPEAKING.
# NOTE: Line 125 & 140 of tinychat.py [#]commented out, or may crash.
# 2015 ~k | WEBSITE:[http://alyak.github.io/tcqBot]

# YOU MAY NEED TO DO THE FOLLOWING FIRST [Debian]:
# torsocks wget https://bootstrap.pypa.io/get-pip.py
# 	>http://pip.readthedocs.org/en/latest/installing.html
# pip install cffi
# 	>If you're missing ffi.h >apt-get install libffi-dev
# pip install python-librtmp
# 	>http://pythonhosted.org/python-librtmp

import socket, re, random, time, urllib, urllib2
from urllib import urlencode
from urllib2 import urlopen, Request

proxy_support = urllib2.ProxyHandler({'https' : '127.0.0.1:8118'})
opener = urllib2.build_opener(proxy_support) # apt-get install privoxy

bots = 8 # TinyChat only allows 10 connections per IP (1 is reserved for botmaster)
    
while not bots <= 0:
	nickGen = random.randint(0, 9)
	# Choice 1: Generate a random name using VOWELS && CONSONANTS + randint
	if nickGen >= 6:
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
			count = random.randint(4, 7)
			length = count - 1
			for i in range(count):
				rnick = (generate_nick(length)) + str(random.randint(1, 9 * count))
	# Choice 2: Pull the first random name generated via rinkworks.com
	elif nickGen <= 3:
		getname = 'http://rinkworks.com/namegen/fnames.cgi?d=1&f=11'
		rname = re.compile(r'<td>.*?</td>')
		ndata = opener.open(getname).read()
		npick = rname.findall(ndata)
		rnick = re.sub(r'<[^>]*?>', '', unicode(npick[0]))
	# Choice 3: Generate a name via random line read @ localhost rnick.txt
	else:
		rnick = random.choice(open("./rnick.txt").readlines())

	tc = pytiny.TinyChat()
	tc.nick(rnick.lower())
	tc.set_room('scenefag') # Your TinyChat room name
	tc.connect()
	buf = tc.recv()
	print buf
	wait = random.randint(10, 60)
	tc.msg('*WHITEPOWER!*', '#0') # Greeting message
	time.sleep(wait)
	bots = bots - 1
	if bots <= 0:
		while True:
			buf = tc.recv()
			print buf
			stfu = random.randint(900, 1800) # Speak every 15-30 minutes
			wp = random.randint(0, 8)
			if wp <= 7:
				getquote = 'http://randomquotesgenerator.com/index.php/rest.html?method=advice/'
				rquote = re.compile(r'<i>.*?</i>')
				qdata = opener.open(getquote).read()
				qpick = rquote.findall(qdata)
				ohai = re.sub(r'<[^>]*?>', '', unicode(qpick[0]))
				tc.msg(ohai)
				time.sleep(stfu)
			elif wp == 8:
				ohai = '*WHITEPOWER!*'
				tc.msg(ohai, '#0')
				time.sleep(stfu)
