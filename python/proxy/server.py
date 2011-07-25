import BaseHTTPServer
import urllib2, urllib
import cgi, random, sys


class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    baseServer = "eutils.ncbi.nlm.nih.gov";

    


    def do_GET(self):
        url = 'http://'+self.baseServer + self.path
        connection = self.bring(url)
        #print "Request made: " + url + " : Code received : " + connection.getcode()
        #If the request made to the server was successfull
        if connection.getcode() == 200:
        #if True:
            # send the response code received
            self.send_response(connection.getcode())
            # build the headers with the received information
            headers = connection.info()
            for header in headers:
                    self.send_header(header,headers[header])
            self.end_headers()
            #send received info
            self.wfile.write(connection.read())
        else:
            self.send_response(404)

    def do_POST(self):
        url = 'http://'+self.baseServer + self.path
        connection = self.bringPost(url)
        #If the request made to the server was successfull
        if connection.getcode() == 200:
        #if True:
            # send the response code received
            self.send_response(connection.getcode())
            # build the headers with the received information
            headers = connection.info()
            for header in headers:
                    self.send_header(header,headers[header])
            self.end_headers()
            #send received info
            self.wfile.write(connection.read())
        else:
            self.send_response(404)
    def bring(self,url):
        auth_handler = urllib2.ProxyBasicAuthHandler(urllib2.HTTPPasswordMgrWithDefaultRealm())
        auth_handler.add_password(realm=None, uri='http://proxyapp.unal.edu.co:8080/', user='jjsosar', passwd='nacional')
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
        conn = urllib2.urlopen(url)
        return conn
    def bringPost(self,url):
        auth_handler = urllib2.ProxyBasicAuthHandler(urllib2.HTTPPasswordMgrWithDefaultRealm())
        auth_handler.add_password(realm=None, uri='http://proxyapp.unal.edu.co:8080/', user='jjsosar', passwd='nacional')
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)        
        
        #form = cgi.FieldStorage(fp=self.rfile, 
         #   headers=self.headers,
         #   environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],})
        data = (self.rfile.read(int(self.headers.getheader('content-length'))))
        req = urllib2.Request (url,data,self.headers)
        conn = urllib2.urlopen(req)
        return conn

if __name__=='__main__':
    PORT = 8000
    try:
        httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
        print "serving at port", PORT
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()
