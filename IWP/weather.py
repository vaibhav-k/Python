import sys, webbrowser

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
	print "Give address in command line"
	
webbrowser.open('https://www.google.com/search?q=weather+' + address)