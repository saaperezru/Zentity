using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Zentity.Core;
using System.IO;
using System.Collections.Generic;
namespace ZentityFlickrSampleDMCreator
{
    class Program
    {
        static void Main(string[] args)
        {
            string imgFolderPath = "C:\\Zentity";
            string[] imagesInFolder = Directory.GetFiles(imgFolderPath, "p*.*");
            foreach (string a in imagesInFolder)
            {
                Console.WriteLine("      File Name: [{0}]", a); 
            }
            Console.ReadKey();
            //DMCreator creator = new DMCreator();
            //creator.createDM();
            const string connectionString =  @"provider=System.Data.SqlClient;
            metadata=C:\Zentity\Zentity.Flickr.ExtendedCore.csdl|C:\Zentity\Zentity.Flickr.csdl|C:\Zentity\Zentity.Flickr.Consolidated.msl|C:\Zentity\Zentity.Flickr.Consolidated.ssdl; 
            provider connection string='Data Source=.;
            Initial Catalog=Zentity;Integrated Security=True;MultipleActiveResultSets=True'";
            //ZentityContext zenContext = new ZentityContext(connectionString);
            //DataInsert dataUploader = new DataInsert();
            //string xmlPath = "C:\\Zentity\\xml\\fotos.xml";
            
            //dataUploader.insertData(zenContext,xmlPath,imgFolderPath);
            
            
            
            //test(imgFolderPath, "f3");
            //Console.ReadKey();
            //Cleaner clean = new Cleaner();
            //clean.deleteALL(zenContext);

        }

        private static void test(string imgPath,string Id)
        {
            string[] imagesInFolder = Directory.GetFiles(imgPath, Id + ".*");
            // Create a Zentity file.
            FileInfo ImageFile = new FileInfo(imagesInFolder[0]);
            Console.WriteLine("      File Name: [{0}]", ImageFile.Name); 
        }
        

    }
}
