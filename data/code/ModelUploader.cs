using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Zentity.Core;
using System.Xml.Serialization;using Zentity.Modulo2;
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
 					 context.MetadataWorkspace.LoadFromAssembly(System.Reflection.Assembly.Load("Zentity.Modulo2")); 
 					 var existingPres = (from pres in context.Resources 
 						 where pres.ImageID.Equals(p.ImageID, StringComparison.OrdinalIgnoreCase) 
 						 select pres).FirstOrDefault(); 
 						 if (existingPres != null) 
 						 { 
 							 Console.WriteLine("[WARNING] Image {0} already exists in database", p.ImageID); 
 							 continue; 
 						 } 
 						 // Create resources. 
 						 try 
 							 { 
 							 Entidad2 img = new Entidad2 {
 								  Title = p.Title,
 								  Description = p.Description,
 								  Main_Textual_Category = p.Main_Textual_Category,
 								  Main_Visual_Category = p.Main_Visual_Category,
 								  ImageID = p.ImageID,
 								  LTT_PERSONA_USUARIO_EJECUTIVO_ANIMAL = Convert.ToDouble(p.LTT_PERSONA_USUARIO_EJECUTIVO_ANIMAL),
 								  LTT_TIERRA_AGUA_ANIMAL_USUARIO = Convert.ToDouble(p.LTT_TIERRA_AGUA_ANIMAL_USUARIO),
 								  LTV_USUARIO_EJECUTIVO_PERSONA_TIERRA = Convert.ToDouble(p.LTV_USUARIO_EJECUTIVO_PERSONA_TIERRA),
 								  LTV_TIERRA_AGUA_ANIMAL_PERSONA = Convert.ToDouble(p.LTV_TIERRA_AGUA_ANIMAL_PERSONA),
 								  Tag_EJECUTIVO = (p.Tag_EJECUTIVO=="True"),
 								  Tag_PERSONA = (p.Tag_PERSONA=="True"),
 								  Tag_TIERRA = (p.Tag_TIERRA=="True"),
 								  Tag_AGUA = (p.Tag_AGUA=="True"),
 								  Tag_USUARIO = (p.Tag_USUARIO=="True"), 
 							 }; 
 							 context.AddToResources(img); 
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
 							 context.AddToResources(fileResource); 
 							 Console.WriteLine("[INFO] Creating image {0}", p.ImageID); 
 							 context.SaveChanges(); 
 							 // Now upload the actual binary content of the file.     
 							 FileStream fStream = new FileStream(ImageFile.FullName, FileMode.Open, FileAccess.Read); 
 							 Console.WriteLine("[INFO] Saving image {0} file", p.ImageID); 
 							 context.UploadFileContent(fileResource, fStream); 
 							 //Asociate file with Resource 
 							 img.Files.Add(fileResource); 
 							 context.InsertResourceHasFile(fileResource.Id, img.Id); 
 							 //Save Changes in context 
 							 Console.WriteLine("[INFO] Associating image {0} and file", p.ImageID); 
 							 context.SaveChanges(); 
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
 				 metadata=../data/code/code/Zentity.Modulo2.ExtendedCore.csdl|../data/code/code/Zentity.Modulo2.csdl|../data/code/code/Zentity.Modulo2.Consolidated.msl|../data/code/code/Zentity.Modulo2.Consolidated.ssdl; 
 				 provider connection string='Data Source=.; 
 				 Initial Catalog=Zentity;Integrated Security=True;MultipleActiveResultSets=True' 
 				 "; 
 			 DataInsert dataUploader = new DataInsert(); 
 			 string imgFolderPath = "../data/images/"; 
 			 string ZXMLPath = "../data/ZXML/"; 
 			 string[] ZXMLFiles = Directory.GetFiles(ZXMLPath, "Images*.*"); 
 			 foreach (string a in ZXMLFiles) 
 			 { 
 				 ZentityContext zenContext = new ZentityContext(connectionString); 
 				 dataUploader.insertData_Entidad2(zenContext, a, imgFolderPath); 
 			 }
		 }
	 }
 }