#!/usr/bin/env python

from main import *
import logging
if __name__=='__main__':
    try:
        server = ThreadedHTTPServer(('',port), MyRequestHandler)
	server_thread = threading.Thread(target=server.serve_forever)
	#Exit the server thread when the main thread terminates
	server_thread.setDaemon(True)
	server_thread.start()
        print "Started HTTPServer, listening to port %s" % (port)
	while server_thread.isAlive():
	    sleep(10)
    except KeyboardInterrupt:
	print 'TERM signal recieved, shutting down server'
    finally:
	logging.shutdown()
	server.socket.close()
    	server.shutdown()
