import ResourcesArray
from os.path import join
class DataInsertCodeGenerator:

    def generate(self,resourceTypes,namespace,path,xmlParentName,xmlChildName,filename="DataInsert.cs"):

	# Create a file object:
	# in "write" mode
	FILE = open(join(path,'code',filename),"w")
	#Imports
	FILE.write("using System;\n")
	FILE.write("using System.IO;\n")
        FILE.write("using System.Collections.Generic;\n")
        FILE.write("using System.Linq;\n")
        FILE.write("using System.Text;\n")
        FILE.write("using Zentity.Core;\n")
        FILE.write("using System.Xml.Serialization;")
        FILE.write("using "+ namespace +";\n")
        
        #Begin namespace
	FILE.write("namespace DataInsert\n")
	FILE.write("{ \n \t class DataInsert \n \t { \n  ")

        FILE.write(" \n \t\t private " + xmlParentName + " data;")
        #Begin Deserialize Method
        FILE.write(" \n \t\t /// <summary>")
        FILE.write(" \n \t\t /// Deserializes the specified XML path.")
        FILE.write(" \n \t\t /// </summary>")
        FILE.write(' \n \t\t /// <typeparam name="T"></typeparam>')
        FILE.write(' \n \t\t /// <param name="xmlPath">The XML path.</param>')
        FILE.write(" \n \t\t /// <returns></returns>")
        FILE.write(" \n \t\t private static T Deserialize<T>(string xmlPath)")
        #Open Deserialize method
        FILE.write(" \n \t\t {")
        FILE.write(" \n \t\t\t XmlSerializer xmlSerializer = new XmlSerializer(typeof(T));")
        FILE.write(" \n \t\t\t using (StreamReader xmlStream = new StreamReader(xmlPath))")
        #Open using
        FILE.write(" \n \t\t\t {")
        FILE.write(" \n \t\t\t\t T tempObject = (T)xmlSerializer.Deserialize(xmlStream);")
        FILE.write(" \n \t\t\t\t return tempObject;")
        #Close using
        FILE.write(" \n \t\t\t }")
        #Close Deserialize method                   
        FILE.write(" \n \t\t }")
        #Finish Deserialize Method                   
        #Begin loadData Method
        FILE.write(" \n \t\t private void loadData(string xmlPath)")
        FILE.write(" \n \t\t {")
        FILE.write(" \n \t\t\t data = Deserialize<"+xmlParentName+">(xmlPath);")
        FILE.write(" \n \t\t }")
        #Finish loadData Method                   
        #Begin ConvertTimestamp Method
        FILE.write(" \n \t\t /// <summary>")
        FILE.write(" \n \t\t /// method for converting a UNIX timestamp to a regular")
        FILE.write(" \n \t\t  ///System.DateTime value (and also to the current local time)")
        FILE.write(" \n \t\t  ///</summary>")
        FILE.write(' \n \t\t  ///<param name="timestamp">value to be converted</param>')
        FILE.write(" \n \t\t  ///<returns>converted DateTime in string format</returns>")
        FILE.write(" \n \t\t private static DateTime ConvertTimestamp(double timestamp)")
        FILE.write(" \n \t\t {")
        FILE.write(" \n \t\t\t //create a new DateTime value based on the Unix Epoch")
        FILE.write(" \n \t\t\tDateTime converted = new DateTime(1970, 1, 1, 0, 0, 0, 0);")
        FILE.write(" \n \t\t\t//add the timestamp to the value")
        FILE.write(" \n \t\t\tDateTime newDateTime = converted.AddSeconds(timestamp);")
        FILE.write(" \n \t\t\t//return the value in string format")
        FILE.write(" \n \t\t\treturn newDateTime.ToLocalTime();")
        FILE.write(" \n \t\t }")

        for RT in resourceTypes:
            FILE.write(" \n \t\t public void insertData_"+RT.name+"(ZentityContext zenContext, string xmlPath, string imgPath)")
            FILE.write(" \n \t\t {")
            FILE.write(" \n \t\t\t loadData(xmlPath);")
            FILE.write(" \n \t\t\t using (ZentityContext context = zenContext)")
            FILE.write(" \n \t\t\t {")
            #Begin for
            FILE.write(" \n \t\t\t\t foreach ("+xmlParentName+xmlChildName+" p in data.Items)")
            FILE.write(" \n \t\t\t\t {")
            FILE.write(" \n \t\t\t\t\t //WARNING : Comparing attribute should be changed to a unique key")
            FILE.write(' \n \t\t\t\t\t context.MetadataWorkspace.LoadFromAssembly(System.Reflection.Assembly.Load("'+namespace+'"));')
            FILE.write(" \n \t\t\t\t\t var existingPres = (from pres in context.Resources")
            FILE.write(" \n \t\t\t\t\t\t where pres."+RT.uniqueProperty.name+".Equals(p."+RT.uniqueProperty.name+", StringComparison.OrdinalIgnoreCase)")
            FILE.write(" \n \t\t\t\t\t\t select pres).FirstOrDefault();")
            FILE.write(" \n \t\t\t\t\t\t if (existingPres != null)")
            FILE.write(" \n \t\t\t\t\t\t {")
            FILE.write(' \n \t\t\t\t\t\t\t Console.WriteLine("[WARNING] Image {0} already exists in database", p.'+RT.uniqueProperty.name+');')
            FILE.write(" \n \t\t\t\t\t\t\t continue;")
            FILE.write(" \n \t\t\t\t\t\t }")
            FILE.write(" \n \t\t\t\t\t\t // Create resources.")
            FILE.write(" \n \t\t\t\t\t\t try")
            FILE.write(" \n \t\t\t\t\t\t\t {")
            #Begin resource creation
            FILE.write(" \n \t\t\t\t\t\t\t "+RT.name+" img = new "+RT.name+" {")
            #Begin properties values assignation
            for SP in RT.scalarProperties:
                FILE.write("\n \t\t\t\t\t\t\t\t "+SP.toCode("p") +",")
            #Finish properties values assignation
            FILE.write(" \n \t\t\t\t\t\t\t };")
            FILE.write(" \n \t\t\t\t\t\t\t context.AddToResources(img);")
            FILE.write(' \n \t\t\t\t\t\t\t string[] imagesInFolder = Directory.GetFiles(imgPath, p.'+RT.imgFileProperty.name+' + ".*");')
            #Finish new entity creation
            FILE.write(" \n \t\t\t\t\t\t\t // Create a Zentity file.")
            FILE.write(" \n \t\t\t\t\t\t\t FileInfo ImageFile = new FileInfo(imagesInFolder[0]);")
            FILE.write(" \n \t\t\t\t\t\t\t Zentity.Core.File fileResource = new Zentity.Core.File();")
            FILE.write(" \n \t\t\t\t\t\t\t fileResource.Title = ImageFile.Name;")
            FILE.write(" \n \t\t\t\t\t\t\t fileResource.Size = ImageFile.Length;")
            FILE.write(" \n \t\t\t\t\t\t\t fileResource.DateAdded = ImageFile.CreationTime;")
            FILE.write(" \n \t\t\t\t\t\t\t fileResource.DateModified = ImageFile.LastWriteTime;")
            FILE.write(" \n \t\t\t\t\t\t\t fileResource.FileExtension = ImageFile.Extension;")
            FILE.write(' \n \t\t\t\t\t\t\t fileResource.MimeType = "image/" + fileResource.FileExtension.Replace(".", string.Empty);')
            FILE.write(" \n \t\t\t\t\t\t\t // Add the file to context.    ")
            FILE.write(" \n \t\t\t\t\t\t\t context.AddToResources(fileResource);")
            FILE.write(' \n \t\t\t\t\t\t\t Console.WriteLine("[INFO] Creating image {0}", p.'+RT.uniqueProperty.name+');')
            FILE.write(" \n \t\t\t\t\t\t\t context.SaveChanges();")
            FILE.write(" \n \t\t\t\t\t\t\t // Now upload the actual binary content of the file.    ")
            FILE.write(" \n \t\t\t\t\t\t\t FileStream fStream = new FileStream(ImageFile.FullName, FileMode.Open, FileAccess.Read);")
            FILE.write(' \n \t\t\t\t\t\t\t Console.WriteLine("[INFO] Saving image {0} file", p.'+RT.uniqueProperty.name+');')
            FILE.write(" \n \t\t\t\t\t\t\t context.UploadFileContent(fileResource, fStream);")
            FILE.write(" \n \t\t\t\t\t\t\t //Asociate file with Resource")
            FILE.write(" \n \t\t\t\t\t\t\t img.Files.Add(fileResource);")
            FILE.write(" \n \t\t\t\t\t\t\t context.InsertResourceHasFile(fileResource.Id, img.Id);")
            FILE.write(" \n \t\t\t\t\t\t\t //Save Changes in context")
            FILE.write(' \n \t\t\t\t\t\t\t Console.WriteLine("[INFO] Associating image {0} and file", p.'+RT.uniqueProperty.name+');')
            FILE.write(" \n \t\t\t\t\t\t\t context.SaveChanges();")
            FILE.write(" \n \t\t\t\t\t\t\t }")
            FILE.write(" \n \t\t\t\t\t\t\t catch{")
            FILE.write(' \n \t\t\t\t\t\t\t\t Console.WriteLine("[ERROR] During image {0} creation", p.'+RT.uniqueProperty.name+');')
            FILE.write(" \n \t\t\t\t\t\t\t\t continue;")
            #Close try/catch
            FILE.write(" \n \t\t\t\t\t\t\t }")
            #Close foreach
            FILE.write(" \n \t\t\t\t\t\t }")
            FILE.write(" \n \t\t\t\t }")
            FILE.write(" \n \t\t\t }")
        #Begin main method
        FILE.write(" \n \t\t static void Main(string[] args)")
        FILE.write(" \n \t\t {")
        FILE.write(' \n \t\t\t const string connectionString = @"provider=System.Data.SqlClient;')
        FILE.write(" \n \t\t\t\t metadata="+join(path,'code',namespace+'.ExtendedCore.csdl')+"|"+join(path,'code',namespace+'.csdl')+'|'+join(path,'code',namespace+'.Consolidated.msl')+"|"+join(path,'code',namespace+".Consolidated.ssdl;"))
        FILE.write(" \n \t\t\t\t provider connection string='Data Source=.;")
        FILE.write(" \n \t\t\t\t Initial Catalog=Zentity;Integrated Security=True;MultipleActiveResultSets=True'")
        FILE.write(' \n \t\t\t\t ";')

        FILE.write(" \n \t\t\t DataInsert dataUploader = new DataInsert();")
        #Add double slash to the paths so they can be stored as strings in C#
        FILE.write(' \n \t\t\t string imgFolderPath = "'+"\\\\".join(join(path,'images').split('\\'))+'";')
        #Call the data insertor for each resourceType and for each ZXML file
        FILE.write(' \n \t\t\t string ZXMLPath = "'+"\\\\".join(join(path,'ZXML').split('\\'))+'";')
        for RT in resourceTypes:
            FILE.write(' \n \t\t\t string[] '+RT.name+'ZXMLFiles = Directory.GetFiles(ZXMLPath, "'+RT.ZXMLPrefix+'*.*");')
            FILE.write(" \n \t\t\t foreach (string a in "+RT.name+"ZXMLFiles)")
            #begin foreach file
            FILE.write(" \n \t\t\t {")
            FILE.write(" \n \t\t\t\t ZentityContext zenContext = new ZentityContext(connectionString);")
            FILE.write(' \n \t\t\t\t dataUploader.insertData_'+RT.name+'(zenContext, a, imgFolderPath);')
            FILE.write(" \n \t\t\t }")
            #begin foreach file
	#Closes class
        FILE.write("\n\t\t }")
	FILE.write("\n\t }")
	#Closes namespace
	FILE.write("\n }")

	FILE.close()

                   
