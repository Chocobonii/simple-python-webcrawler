# ######## ##     ## #### ##               ########     ###    ########  ########  #### ########
# ##       ##     ##  ##  ##               ##     ##   ## ##   ##     ## ##     ##  ##     ##
# ##       ##     ##  ##  ##               ##     ##  ##   ##  ##     ## ##     ##  ##     ##
# ######   ##     ##  ##  ##       ####### ########  ##     ## ########  ########   ##     ##
# ##        ##   ##   ##  ##               ##   ##   ######### ##     ## ##     ##  ##     ##
# ##         ## ##    ##  ##               ##    ##  ##     ## ##     ## ##     ##  ##     ##
# ########    ###    #### ########         ##     ## ##     ## ########  ########  ####    ##

import os;
import socket;
import random;
import sys;
import csv;
import time;

# spider = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# spider.settimeout(3);

addrp1 = int(sys.argv[1]);
addrp2 = int(sys.argv[2]);
segmnt = 8;
device = 0;

nullbit = '\x00\x00web-crawler1.0\x00\x00';

kommplete = 0;

def evil_scan (ip_addr, mode):
	# MODE 1 - NORMAL SCAN NO RESTRICTIONS
	# MODE 2 - SMART SCANNING
	# MODE 3 - STEALTHY SCANNING
	# MODE 4 - DEBUG mode
	open_ports = [];
	port_info = [];
	print ("Performing Port scan on host: ", ip_addr);

	if mode == 2:
		print ("smart scanning enabled...");

	closed = 0;
	has_failed = False;
	index = 10;
	while index < 10000:
		sspider = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		# print ("for host {",ip_addr,"} testing port: ",index);
		try:
			sspider.settimeout(3);
			sspider.connect((ip_addr, index));
			sspider.settimeout(None);
		except Exception as err:
			#print ("closed: ", err);
			has_failed = True;
		if has_failed:
			#print ("in scanning port: ", index, " is closed");
			closed += 1;
		else:
			print ("for host {",ip_addr,"} tested port: ",index);
			print ("for host: ", ip_addr, " found open port: ", index);
			sspider.send(bytes(nullbit.encode('utf-8')));
			# perform banner grabbing and storing results for later tests
			port_in = spider.recv(2048);
			open_ports.append(index);
			port_info.append(port_in);
			print(port_in);
		if mode == 2 and index > 100 and len(open_ports) < 2:
			index = 10000;
		if mode == 2 and index > 1000:
			index = 10000;
		if mode == 2 and index > 1000 and len(open_ports) > 60:
			print ("WARN: potential honey pot");
		has_failed = False;
		index += 1;
		sspider.close();
		time.sleep(0.1);

	print ("Port Scanning complete!");
	print ("Open ports found: ", open_ports);

# VARIABLE TO TEST IF HOST IS UP
is_up = True;

while addrp1 <= 255:
	# print ("address 1: ", addrp1);
	while addrp2 <= 255:
		# print ("address 2: ", addrp2);
		while segmnt <= 255:
			while device <= 255:
				spider = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
				print ("generated addr: ", addrp1,".",addrp2,".",segmnt,".",device);
				netaddr = str(addrp1) + "." + str(addrp2) + "." + str(segmnt) + "." + str(device);
				try:
					spider.settimeout(3);
					spider.connect((netaddr, 0));
					spider.settimeout(None);
				except Exception as err:
					# print ("hosts exists but refused to connect");
					print ("error code: ", err.errno);
					if err.errno == None:
						print ("failed to connect, host not found");
						is_up = False;
					else:
						print ("host exists but refused connection");
						is_up = True;
				if is_up:
					print ("Found host in addr: ", netaddr);
					evil_scan(netaddr, int(sys.argv[3]) );
				is_up = True;
				# print ("ping: ", netaddr);
				spider.close();
				time.sleep(0.5);
				device = device + 1;
			segmnt = segmnt + 1;
			device = 0;
		addrp2 = addrp2 + 1;
		segmnt = 0;
	addrp1 = addrp1 + 1;
	addrp2 = 0;
