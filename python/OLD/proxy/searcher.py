import urllib2, urllib

def bring(url):
	auth_handler = urllib2.ProxyBasicAuthHandler(urllib2.HTTPPasswordMgrWithDefaultRealm())
	auth_handler.add_password(realm=None, uri='http://proxyapp.unal.edu.co:8080/', user='jjsosar', passwd='nacional')
	opener = urllib2.build_opener(auth_handler)
	urllib2.install_opener(opener)
	conn = urllib2.urlopen('http://python.org')
	#return_str = conn.read()
	return conn

def bring2():
	proxy_handler = urllib2.ProxyHandler({'http': 'http://proxyapp.unal.edu.co:8080/'})
	proxy_auth_handler = urllib2.HTTPBasicAuthHandler()
	proxy_auth_handler.add_password('iNacho', 'proxy.unal.edu.co', 'jjsosar', 'nacional')

	opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
	
	urllib2.install_opener(opener)
	conn = urllib2.urlopen('http://python.org')
	#return_str = conn.read()
	return conn
