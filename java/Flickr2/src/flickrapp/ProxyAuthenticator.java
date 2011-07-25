package flickrapp;

import java.net.Authenticator;
import java.net.InetAddress;
import java.net.PasswordAuthentication;

public class ProxyAuthenticator extends Authenticator{
	
	 protected PasswordAuthentication getPasswordAuthentication() {
//		    String promptString = getRequestingPrompt();
//		    System.out.println(promptString);
//		    String hostname = getRequestingHost();
//		    System.out.println(hostname);
//		    InetAddress ipaddr = getRequestingSite();
//		    System.out.println(ipaddr);
//		    int port = getRequestingPort();

		    String username = "jjsosar";
		    String password = "nacional";
		    return new PasswordAuthentication(username, password.toCharArray());
		  }
}
