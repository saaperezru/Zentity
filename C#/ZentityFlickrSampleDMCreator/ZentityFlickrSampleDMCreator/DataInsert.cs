using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Zentity.Core;
using Zentity.Flickr;
using System.Xml.Serialization;

namespace ZentityFlickrSampleDMCreator
{
    class DataInsert
    {

        private Photos data;

        /// <summary>
        /// Deserializes the specified XML path.
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="xmlPath">The XML path.</param>
        /// <returns></returns>
        private static T Deserialize<T>(string xmlPath)
        {
            XmlSerializer xmlSerializer = new XmlSerializer(typeof(T));
            using (StreamReader xmlStream = new StreamReader(xmlPath))
            {
                T tempObject = (T)xmlSerializer.Deserialize(xmlStream);
                return tempObject;
            }
        }

        private void loadData(string xmlPath)
        {
            data = Deserialize<Photos>(xmlPath);
        }
        /// <summary>
        /// method for converting a UNIX timestamp to a regular
        /// System.DateTime value (and also to the current local time)
        /// </summary>
        /// <param name="timestamp">value to be converted</param>
        /// <returns>converted DateTime in string format</returns>
        private static DateTime ConvertTimestamp(double timestamp)
        {
            //create a new DateTime value based on the Unix Epoch
            DateTime converted = new DateTime(1970, 1, 1, 0, 0, 0, 0);

            //add the timestamp to the value
            DateTime newDateTime = converted.AddSeconds(timestamp);

            //return the value in string format
            return newDateTime.ToLocalTime();
        }


        public void insertData(ZentityContext zenContext, string xmlPath, string imgPath)
        {
            loadData(xmlPath);

            using (ZentityContext context = zenContext)
            {

                foreach (PhotosPhoto p in data.Items)
                {
                    //WARNING : Comparing attribute should be changed to a unique key
                    context.MetadataWorkspace.LoadFromAssembly(System.Reflection.Assembly.Load("Zentity.Flickr"));
                    var existingPres = (from pres in context.Resources
                                        where pres.Title.Equals(p.Title, StringComparison.OrdinalIgnoreCase)
                                        select pres).FirstOrDefault();

                    if (existingPres != null)
                    {
                        Console.WriteLine("[WARNING] Image {0} already exists in database", p.Id);
                        continue;
                    }
                    // Create resources.
                    try
                    {
                        ImageResource img = new ImageResource { Title = p.Title, TagFamilia = (p.TagFamilia == "True"), TagRumba = (p.TagRumba == "True") };
                        context.AddToResources(img);
                        string[] imagesInFolder = Directory.GetFiles(imgPath, p.Id + ".*");
                        // Create a Zentity file.
                        FileInfo ImageFile = new FileInfo(imagesInFolder[0]);
                        Zentity.Core.File fileResource = new Zentity.Core.File();
                        fileResource.Title = ImageFile.Name;
                        fileResource.Size = ImageFile.Length;
                        fileResource.DateAdded = ImageFile.CreationTime;
                        fileResource.DateModified = ImageFile.LastWriteTime;
                        fileResource.FileExtension = ImageFile.Extension;
                        fileResource.MimeType = "image/" + fileResource.FileExtension.Replace(".", string.Empty);
                        // Add the file to context.    
                        context.AddToResources(fileResource);
                        Console.WriteLine("[INFO] Creating image {0}", p.Id);
                        context.SaveChanges();
                        // Now upload the actual binary content of the file.    
                        FileStream fStream = new FileStream(ImageFile.FullName, FileMode.Open, FileAccess.Read);
                        Console.WriteLine("[INFO] Saving image {0} file", p.Id);
                        context.UploadFileContent(fileResource, fStream);
                        //Asociate file with Resource
                        img.Files.Add(fileResource);
                        context.InsertResourceHasFile(fileResource.Id, img.Id);
                        //Save Changes in context
                        Console.WriteLine("[INFO] Associating image {0} and file", p.Id);
                        context.SaveChanges();
                    }catch{
                        Console.WriteLine("[ERROR] During image {0} creation", p.Id);
                        continue;
                    }
                }
                // Retrieve and show resources.
                DisplayImageResources(context);
            }
        }



        private static void DisplayImageResources(ZentityContext context)
        {
            foreach (ImageResource sw in context.Resources.OfType<ImageResource>())
            {
                Console.WriteLine("Id: [{0}], Tag Familia: [{1}], Tag Rumba: [{2}]", sw.Id, sw.TagFamilia, sw.TagRumba);
                foreach (Zentity.Core.File f in sw.Files)
                {
                    //MemoryStream stream = new MemoryStream();

                    Console.WriteLine(" -- BEGIN FILES -- ");
                    //context.DownloadFileContent(f, stream);
                    //stream.Seek(0, SeekOrigin.Begin);
                    //StreamReader reader = new StreamReader(stream);
                    Console.WriteLine("      File Name: [{0}]", f.Title);
                    Console.WriteLine(" -- END FILES -- ");
                }
            }
            Console.WriteLine("----------------------------");
            Console.ReadKey();
        }

        
    }

}

