using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Zentity.Core;
using System.Xml.Serialization;
using Zentity.Modulo3;
using System.Globalization;

namespace DataInsert
{ 
 	 class DataInsert 
 	 { 
   
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
 		 /// <summary> 
 		 /// method for converting a UNIX timestamp to a regular 
 		  ///System.DateTime value (and also to the current local time) 
 		  ///</summary> 
 		  ///<param name="timestamp">value to be converted</param> 
 		  ///<returns>converted DateTime in string format</returns> 
 		 private static DateTime ConvertTimestamp(double timestamp) 
 		 { 
 			 //create a new DateTime value based on the Unix Epoch 
 			DateTime converted = new DateTime(1970, 1, 1, 0, 0, 0, 0); 
 			//add the timestamp to the value 
 			DateTime newDateTime = converted.AddSeconds(timestamp); 
 			//return the value in string format 
 			return newDateTime.ToLocalTime(); 
 		 } 
 		 private ParentImages dataParentImages; 
 		 private void loadParentImagesData(string xmlPath) 
 		 { 
 			dataParentImages= Deserialize<ParentImages>(xmlPath); 
 		 } 
 		 public void insertData_Entidad2(ZentityContext zenContext, string xmlPath, string imgPath) 
 		 { 
 			 loadParentImagesData(xmlPath); 
 			 using (ZentityContext context = zenContext) 
 			 { 
 				 foreach (ParentImagesImage p in dataParentImages.Items) 
 				 { 
 					 //WARNING : Comparing attribute should be changed to a unique key 
 					 context.MetadataWorkspace.LoadFromAssembly(System.Reflection.Assembly.Load("Zentity.Modulo3")); 
 						 // Create resources. 
                     NumberFormatInfo provider = new NumberFormatInfo();
                     provider.NumberDecimalSeparator = ".";
 						 try 
 							 { 
 							 Entidad3 img = new Entidad3 {
 								  Title = p.Title,
 								  Description = p.Description,
 								  Main_Textual_Category = p.Main_Textual_Category,
 								  Main_Visual_Category = p.Main_Visual_Category,
 								  ImageID = p.ImageID,
 								  LTT_PERSONA_USUARIO_EJECUTIVO_ANIMAL = Convert.ToDouble(p.LTT_PERSONA_USUARIO_EJECUTIVO_ANIMAL,provider),
                                  LTT_TIERRA_AGUA_ANIMAL_USUARIO = Convert.ToDouble(p.LTT_TIERRA_AGUA_ANIMAL_USUARIO, provider),
                                  LTV_USUARIO_EJECUTIVO_PERSONA_TIERRA = Convert.ToDouble(p.LTV_USUARIO_EJECUTIVO_PERSONA_TIERRA, provider),
                                  LTV_TIERRA_AGUA_ANIMAL_PERSONA = Convert.ToDouble(p.LTV_TIERRA_AGUA_ANIMAL_PERSONA, provider),
 								  Tag_EJECUTIVO = (p.Tag_EJECUTIVO=="True"),
 								  Tag_PERSONA = (p.Tag_PERSONA=="True"),
 								  Tag_TIERRA = (p.Tag_TIERRA=="True"),
 								  Tag_AGUA = (p.Tag_AGUA=="True"),
 								  Tag_USUARIO = (p.Tag_USUARIO=="True"), 
 							 };
                             Console.WriteLine("[INFO] Image " + img.ImageID + " - " + p.ImageID);
                             Console.WriteLine("[INFO] LTT_PERSONA_USUARIO_EJECUTIVO_ANIMAL :  {0} - {1}", img.LTT_PERSONA_USUARIO_EJECUTIVO_ANIMAL,p.LTT_PERSONA_USUARIO_EJECUTIVO_ANIMAL);
                             Console.Read();
 							 //context.AddToResources(img); 
 							 string[] imagesInFolder = Directory.GetFiles(imgPath, p.ImageID + ".*"); 
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
 							 //context.AddToResources(fileResource); 
 							 Console.WriteLine("[INFO] Creating image {0}", p.ImageID); 
 							 //context.SaveChanges(); 
 							 // Now upload the actual binary content of the file.     
 							 FileStream fStream = new FileStream(ImageFile.FullName, FileMode.Open, FileAccess.Read); 
 							 Console.WriteLine("[INFO] Saving image {0} file", p.ImageID); 
 							 //context.UploadFileContent(fileResource, fStream); 
 							 //Asociate file with Resource 
 							 img.Files.Add(fileResource); 
 							 //context.InsertResourceHasFile(fileResource.Id, img.Id); 
 							 //Save Changes in context 
 							 Console.WriteLine("[INFO] Associating image {0} and file", p.ImageID); 
 							 //context.SaveChanges(); 
 							 } 
 							 catch{ 
 								 Console.WriteLine("[ERROR] During image {0} creation", p.ImageID); 
 								 continue; 
 							 } 
 						 } 
 				 } 
 			 } 
 		 static void Main(string[] args) 
 		 { 
 			 const string connectionString = @"provider=System.Data.SqlClient; 
 				 metadata=C:\\Users\\tuareg\\Desktop\\prueba4\\code\\Zentity.Modulo3.ExtendedCore.csdl|C:\\Users\\tuareg\\Desktop\\prueba4\\code\\Zentity.Modulo3.csdl|C:\\Users\\tuareg\\Desktop\\prueba4\\code\\Zentity.Modulo3.Consolidated.msl|C:\\Users\\tuareg\\Desktop\\prueba4\\code\\Zentity.Modulo3.Consolidated.ssdl; 
 				 provider connection string='Data Source=.; 
 				 Initial Catalog=Zentity;Integrated Security=True;MultipleActiveResultSets=True' 
 				 "; 
 			 DataInsert dataUploader = new DataInsert(); 
 			 string imgFolderPath = "C:\\Users\\tuareg\\Desktop\\prueba4\\images\\"; 
 			 string ZXMLPath = "C:\\Users\\tuareg\\Desktop\\prueba4\\ZXML\\"; 
 			 string[] ZXMLFiles = Directory.GetFiles(ZXMLPath, "Images*.*"); 
 			 foreach (string a in ZXMLFiles) 
 			 { 
 				 ZentityContext zenContext = new ZentityContext(connectionString); 
 				 dataUploader.insertData_Entidad2(zenContext, a, imgFolderPath); 
 			 }
		 }
	 }
 }