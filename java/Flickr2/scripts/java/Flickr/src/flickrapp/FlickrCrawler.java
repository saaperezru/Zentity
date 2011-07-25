package flickrapp;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.net.URL;
import java.net.URLConnection;
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

public class FlickrCrawler{
	int M;
	String[] servers;
    String[] ids;
    String[] secrets;
    int numPages;
    String query;
    String PATH;
    
	public FlickrCrawler(int m, int numPages, String query) {
		super();
		this.M = m;
		this.query = query;
		this.servers = new String[M];;
		this.ids = new String[M];
		this.secrets = new String[M];
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
  
	public void search(){
		int i = 1;
		try{
			for(int page=1; page<=numPages; page++){
				 URLConnection uc = new URL("http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=e46aad80b4fff6df3947c4258641b521&per_page=" + M + "&sort=relevance&tags=" + query + "&page=" + page).openConnection();
			        DataInputStream dis = new DataInputStream(uc.getInputStream());
			        FileWriter fw = new FileWriter(new File(PATH + "/pages/page" + page + ".xml"));
			        String nextline;		       
			        
			        
			        while ((nextline = dis.readLine()) != null) {
			        	nextline = new String(nextline.getBytes(), "UTF8");
				        fw.append(nextline);
				        }
			        dis.close();
			        fw.close();
			        downloadImageAndTags(page);
			        System.out.println(i++);
			}
		
		}catch(Exception e){
			e.printStackTrace();
		}
	}
	
	public void getTags(String id){
		
		String tagsURL = "http://api.flickr.com/services/rest/?method=flickr.photos.getInfo&api_key=e46aad80b4fff6df3947c4258641b521&photo_id=" + id;
		try{
			URLConnection uc = new URL(tagsURL).openConnection();
			DataInputStream dis = new DataInputStream(uc.getInputStream());
			FileWriter fw = new FileWriter(new File(PATH + "/xml/" + id + ".xml"));
			String nextline;

			while ((nextline = dis.readLine()) != null) {
				nextline = new String(nextline.getBytes(), "UTF8");
		        fw.append(nextline);
			}
			dis.close();
			fw.close();
		}catch(Exception e){
			e.printStackTrace();
		}
	}
	
	public void downloadImageAndTags(int page){
		String fileXML = PATH + "/pages/" + "page" + page + ".xml";
		File f = new File(fileXML);
        XMLInputFactory factory = XMLInputFactory.newInstance();

		try{
			XMLEventReader r = factory.createXMLEventReader(fileXML, new FileInputStream(f.getAbsolutePath()));
	        int i = -1;
	        while (r.hasNext()) {
	
	            XMLEvent event = r.nextEvent();
	            if (event.isStartElement()) {
	                StartElement element = (StartElement) event;
	                String elementName = element.getName().toString();
	                if (elementName.equals("photo")) {
	                    i++;
	                    Iterator iterator = element.getAttributes();
	
	                    while (iterator.hasNext()) {
	                        Attribute attribute = (Attribute) iterator.next();
	                        QName name = attribute.getName();
	                        String value = attribute.getValue();
	                        if ((name.toString()).equals("server")) {
	                            servers[i] = value;
	                        }
	                        if ((name.toString()).equals("id")) {
	                            ids[i] = value;
	                            getTags(value); // Download tags of image i
	                        }
	                        if ((name.toString()).equals("secret")) {
	                            secrets[i] = value;
	                        }
	                    }
	                    
	                    try {
	            	        String flickrurl = "http://static.flickr.com/" + servers[i] + "/" + ids[i] + "_" + secrets[i] + ".jpg";
	            	        URL u = new URL(flickrurl);
	            			String filename = ids[i] + ".jpg";
	            			filename = filename.substring(filename.lastIndexOf("/") + 1 , filename.length());
	            			File newFile = new File(PATH + "/images", filename);
	            			
	            			BufferedInputStream inStream = new BufferedInputStream(u.openStream());
	            			
	            			FileOutputStream fos = new FileOutputStream(newFile);
	            		
	            			int read;
	            		
	            			while ((read = inStream.read()) != -1) {
	            				fos.write(read);
	            			}
	            			fos.flush();
	            			fos.close();
	            			inStream.close();
	                    } catch (IOException ioe) {
	                        ioe.printStackTrace();
	                    }
	                }
	            } 			    
	          }
        }catch(Exception e){
        	e.printStackTrace();
        }
	}
	
	public void extractTags(){

        XMLInputFactory factory = XMLInputFactory.newInstance();
        String fileXML;
		
        File folder = new File(PATH + "/xml/");
	
		try{
			File[] listOfFiles = folder.listFiles();
			for (int j = 0; j < listOfFiles.length; j++) {
				String text = "";
				
			      if (listOfFiles[j].isFile()) {
			    	fileXML = listOfFiles[j].getName();
			    	
			    	if(fileXML.endsWith("xml")){
			    		System.out.println(fileXML + " " + j);
				    	File file = new File(folder + "/" + fileXML);
				    	DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
				    	DocumentBuilder db = dbf.newDocumentBuilder();
				    	Document doc = db.parse(file);
				    	doc.getDocumentElement().normalize();
				    	NodeList nodeLst = doc.getElementsByTagName("tags");

				    	for (int s = 0; s < nodeLst.getLength(); s++) {
				    		Node fstNode = nodeLst.item(s);	    	    
				    		if (fstNode.getNodeType() == Node.ELEMENT_NODE) {
				    			Element fstElmnt = (Element) fstNode;
				    			NodeList fstNmElmntLst = fstElmnt.getElementsByTagName("tag");
				    			for(int k = 0; k < fstNmElmntLst.getLength(); k++){
				    				Element fstNmElmnt = (Element) fstNmElmntLst.item(k);
				    				NodeList fstNm = fstNmElmnt.getChildNodes();
				    				text = text + " " + ((Node) fstNm.item(0)).getNodeValue();
				    			}
				    		}
				    	}
	
				        try{
	            			String filename = fileXML;
	            			File newFile = new File(PATH + "/txt/" + fileXML);			            			
	            			FileOutputStream fos = new FileOutputStream(newFile);
	            			fos.write(text.getBytes());
	            			fos.flush();
	            			fos.close();
	                    } catch (IOException ioe) {
	                        ioe.printStackTrace();
	                    }
			      	 }
			      }
			  }
        }catch(Exception e){
        	e.printStackTrace();
        }
	}

    public static void main(String args[]) {  
    	
    	if(args.length < 3){
    		System.out.println("Use: java - jar FlickrCrawler.jar numImagesPerPage numPages query");
    	}
    	else{
    		int numImagePerPage = Integer.parseInt(args[0]);
    		int numPages = Integer.parseInt(args[1]);
    		String query = args[2];
	    	FlickrCrawler fc = new FlickrCrawler(numImagePerPage, numPages, query);
	    	fc.search();
	    	fc.extractTags();
    	}
    }
}