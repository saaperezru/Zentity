using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Zentity.Core;
using System.Xml.Serialization;using Zentity.DMMTest1;
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
 		 private ParentImagesdataParentImages; 
 		 private void loadParentImagesData(string xmlPath) 
 		 { 
 			 data = Deserialize<ParentImages>(xmlPath); 
 		 } 
 		 public void insertData_RTTest1(ZentityContext zenContext, string xmlPath, string imgPath) 
 		 { 
 			 loadParentImagesData(xmlPath); 
 			 using (ZentityContext context = zenContext) 
 			 { 
 				 foreach (ParentImagesImage p in data.Items) 
 				 { 
 					 //WARNING : Comparing attribute should be changed to a unique key 
 					 context.MetadataWorkspace.LoadFromAssembly(System.Reflection.Assembly.Load("Zentity.DMMTest1")); 
 					 var existingPres = (from pres in context.Resources 
 						 where pres.Title.Equals(p.Title, StringComparison.OrdinalIgnoreCase) 
 						 select pres).FirstOrDefault(); 
 						 if (existingPres != null) 
 						 { 
 							 Console.WriteLine("[WARNING] Image {0} already exists in database", p.Title); 
 							 continue; 
 						 } 
 						 // Create resources. 
 						 try 
 							 { 
 							 RTTest1 img = new RTTest1 {
 								  Title = (p.Title=="True"),
 								  Description = (p.Description=="True"),
 								  Main_Textual_Category = (p.Main_Textual_Category=="True"),
 								  Main_Visual_Category = (p.Main_Visual_Category=="True"),
 								  ImageID = (p.ImageID=="True"),
 								  LTT_P_T_H_F = (p.LTT_P_T_H_F=="True"),
 								  LTT_L_E_I_M = (p.LTT_L_E_I_M=="True"),
 								  LTT_O_D_E_Q = (p.LTT_O_D_E_Q=="True"),
 								  LTT_T_S_J_P = (p.LTT_T_S_J_P=="True"),
 								  LTT_E_M_R_O = (p.LTT_E_M_R_O=="True"),
 								  LTT_Q_T_C_R = (p.LTT_Q_T_C_R=="True"),
 								  LTT_J_L_C_D = (p.LTT_J_L_C_D=="True"),
 								  LTT_G_I_C_S = (p.LTT_G_I_C_S=="True"),
 								  LTT_S_D_T_Q = (p.LTT_S_D_T_Q=="True"),
 								  LTV_J_T_Q_E = (p.LTV_J_T_Q_E=="True"),
 								  LTV_S_G_C_L = (p.LTV_S_G_C_L=="True"),
 								  LTV_N_E_R_D = (p.LTV_N_E_R_D=="True"),
 								  LTV_N_O_E_C = (p.LTV_N_O_E_C=="True"),
 								  LTV_N_Q_A_G = (p.LTV_N_Q_A_G=="True"),
 								  LTV_A_Q_O_F = (p.LTV_A_Q_O_F=="True"),
 								  LTV_G_N_T_H = (p.LTV_G_N_T_H=="True"),
 								  LTV_H_T_G_M = (p.LTV_H_T_G_M=="True"),
 								  LTV_H_F_E_C = (p.LTV_H_F_E_C=="True"),
 								  LTV_E_B_N_J = (p.LTV_E_B_N_J=="True"),
 								  Tag_A = (p.Tag_A=="True"),
 								  Tag_B = (p.Tag_B=="True"),
 								  Tag_E = (p.Tag_E=="True"),
 								  Tag_D = (p.Tag_D=="True"),
 								  Tag_G = (p.Tag_G=="True"),
 								  Tag_F = (p.Tag_F=="True"),
 								  Tag_I = (p.Tag_I=="True"),
 								  Tag_H = (p.Tag_H=="True"),
 								  Tag_J = (p.Tag_J=="True"),
 								  Tag_M = (p.Tag_M=="True"),
 								  Tag_L = (p.Tag_L=="True"),
 								  Tag_O = (p.Tag_O=="True"),
 								  Tag_N = (p.Tag_N=="True"),
 								  Tag_Q = (p.Tag_Q=="True"),
 								  Tag_P = (p.Tag_P=="True"),
 								  Tag_S = (p.Tag_S=="True"),
 								  Tag_T = (p.Tag_T=="True"), 
 							 }; 
 							 context.AddToResources(img); 
 							 string[] imagesInFolder = Directory.GetFiles(imgPath, p.Title + ".*"); 
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
 							 Console.WriteLine("[INFO] Creating image {0}", p.Title); 
 							 context.SaveChanges(); 
 							 // Now upload the actual binary content of the file.     
 							 FileStream fStream = new FileStream(ImageFile.FullName, FileMode.Open, FileAccess.Read); 
 							 Console.WriteLine("[INFO] Saving image {0} file", p.Title); 
 							 context.UploadFileContent(fileResource, fStream); 
 							 //Asociate file with Resource 
 							 img.Files.Add(fileResource); 
 							 context.InsertResourceHasFile(fileResource.Id, img.Id); 
 							 //Save Changes in context 
 							 Console.WriteLine("[INFO] Associating image {0} and file", p.Title); 
 							 context.SaveChanges(); 
 							 } 
 							 catch{ 
 								 Console.WriteLine("[ERROR] During image {0} creation", p.Title); 
 								 continue; 
 							 } 
 						 } 
 				 } 
 			 } 
 		 static void Main(string[] args) 
 		 { 
 			 const string connectionString = @"provider=System.Data.SqlClient; 
 				 metadata=../data/code/code/Zentity.DMMTest1.ExtendedCore.csdl|../data/code/code/Zentity.DMMTest1.csdl|../data/code/code/Zentity.DMMTest1.Consolidated.msl|../data/code/code/Zentity.DMMTest1.Consolidated.ssdl; 
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
 				 dataUploader.insertData_RTTest1(zenContext, a, imgFolderPath); 
 			 }
		 }
	 }
 }