package flickrapp;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Authenticator;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.Iterator;

import javax.xml.namespace.QName;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.stream.XMLEventReader;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.events.Attribute;
import javax.xml.stream.events.StartElement;
import javax.xml.stream.events.XMLEvent;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import com.aetrion.flickr.util.Base64;

import sun.misc.BASE64Encoder;

public class FlickrCrawler {
	int M;
	int numPages;
	String query;
	String PATH;

	public FlickrCrawler(int m, int numPages, String query) {
		super();
		this.M = m;
		this.query = query;
		this.numPages = numPages;
		PATH = query;

		File q = new File(PATH);
		q.mkdir();
		File pages = new File(PATH + "/pages");
		pages.mkdir();
		File images = new File(PATH + "/images");
		images.mkdir();
		File txt = new File(PATH + "/txt");
		txt.mkdir();
		File xml = new File(PATH + "/xml");
		xml.mkdir();
	}

	public void search(int page) {
		String worksFilePath = PATH + "/pages/worksFile" + String.valueOf(page)
				+ ".txt";

		String xmlFilePath = PATH + "/pages/page" + page + ".xml";
		File xmlFile = new File(xmlFilePath);
		try {
			// FileWriter fwXML = new FileWriter(xmlFile);
			OutputStreamWriter fwXML = new OutputStreamWriter(
					new FileOutputStream(PATH + "/pages/page" + page + ".xml"),
					"UTF-8");
			URLConnection uc = new URL(
					"http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=a71f2335131abbed8c6eaa27bef83416&per_page="
							+ M
							+ "&sort=relevance&tags="
							+ query
							+ "&page="
							+ page).openConnection();
			DataInputStream dis = new DataInputStream(uc.getInputStream());

			String nextline;

			while ((nextline = dis.readLine()) != null) {
				nextline = new String(nextline.getBytes(), "UTF8");
				fwXML.append(nextline);
			}
			dis.close();
			fwXML.close();

			buildWorksFile(worksFilePath, xmlFilePath);

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void buildWorksFile(String worksFilePath, String fileXML) {
		File worksFile = new File(worksFilePath);

		File f = new File(fileXML);
		XMLInputFactory factory = XMLInputFactory.newInstance();

		try {
			FileWriter fwWorks = new FileWriter(worksFile);
			XMLEventReader r = factory.createXMLEventReader(fileXML,
					new FileInputStream(f.getAbsolutePath()));
			int i = -1;
			while (r.hasNext()) {

				XMLEvent event = r.nextEvent();
				if (event.isStartElement()) {
					StartElement element = (StartElement) event;
					String elementName = element.getName().toString();
					if (elementName.equals("photo")) {
						i++;
						Iterator iterator = element.getAttributes();
						String server = "", id = "", secret = "";
						while (iterator.hasNext()) {
							Attribute attribute = (Attribute) iterator.next();
							QName name = attribute.getName();
							String value = attribute.getValue();
							if ((name.toString()).equals("server")) {
								server = value;
							}
							if ((name.toString()).equals("id")) {
								id = value;

							}
							if ((name.toString()).equals("secret")) {
								secret = value;
							}
						}
						String work = server + "." + secret + "." + id
								+ System.getProperty("line.separator");
						fwWorks.append(work.subSequence(0, work.length()));
					}
				}
			}
			fwWorks.close();
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	public void download(int page,int numThreads) {
		String xmlFilePath = PATH + "/pages/worksFile" + page + ".txt";
		ArrayList<Thread> ThreadPool = new ArrayList<Thread>();
		FileInputStream fstream;
		try {
			fstream = new FileInputStream(xmlFilePath);
			DataInputStream in = new DataInputStream(fstream);
			BufferedReader br = new BufferedReader(new InputStreamReader(in));
			String APIKey = "a71f2335131abbed8c6eaa27bef83416";
			
			for (int j=0 ; j<numThreads;j++){
				ThreadPool.add(new FlickrCrawlerThread(j,APIKey, PATH,br));
			}
			for (Thread t : ThreadPool){
				t.start();
			}
//			in.close(); //CUIDADO
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
	}

	public static void main(String args[]) {

		if (args.length < 3) {
			System.out
					.println("Use: java - jar FlickrCrawler.jar numThreads numImagesPerPage numPages query");
		} else {
			// setting proxy
			System.getProperties().put("proxySet", "true");
			System.getProperties().put("proxyHost", "proxy9.unal.edu.co");
			System.getProperties().put("proxyPort", "8080");
			Authenticator.setDefault(new ProxyAuthenticator());
			// end proxy configuration
			int numThreads = Integer.parseInt(args[0]);
			int numImagePerPage = Integer.parseInt(args[1]);
			int numPages = Integer.parseInt(args[2]);
			String query = args[3];
			FlickrCrawler fc = new FlickrCrawler(numImagePerPage, numPages,
					query);
			for (int i = 1; i < numPages + 1; i++) {
				fc.search(i); // Download images addresses xml for page i
				fc.download(i,numThreads); // Download images and tags for each image in page i
			}

			// fc.execute();
			// fc.extractTags();
		}
	}
}