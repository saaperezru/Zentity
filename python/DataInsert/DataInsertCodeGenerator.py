import ResourcesArray
class DataInsertCodeGenerator:

    def generate(resourceTypes,filename,namespace):
        namespace = Namespace
	# Create a file object:
	# in "write" mode
	FILE = open(filename,"w")
	#Imports
	FILE.write("using System;\n")
	FILE.write("using System.IO;\n")
        FILE.write("using System.Collections.Generic;\n")
        FILE.write("using System.Linq;\n")
        FILE.write("using System.Text;\n")
        FILE.write("using Zentity.Core;\n")
        FILE.write("using System.Xml.Serialization;")
        for RT in resourceTypes:
            FILE.write("using "+ resourceType.name +";\n")
        
        #Begin namespace
	FILE.write("namespace DataInsert_" +namespace+"\n")
	FILE.write("{ \n \t class DataInsert \n \t { \n  ")

        FILE.write("{ \n \t\t private Photos data;")
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
        FILE.write(" \n \t\t\t data = Deserialize<Photos>(xmlPath);")
        FILE.write(" \n \t\t }")
        #Finish loadData Method                   
        #Begin ConvertTimestamp Method
        FILE.write(" \n \t\t /// <summary>")
        FILE.write(" \n \t\t  method for converting a UNIX timestamp to a regular")
        FILE.write(" \n \t\t  System.DateTime value (and also to the current local time)")
        FILE.write(" \n \t\t  </summary>")
        FILE.write(' \n \t\t  <param name="timestamp">value to be converted</param>')
        FILE.write(" \n \t\t  <returns>converted DateTime in string format</returns>")
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
            FILE.write("{ \n \t\t\t\t foreach (PhotosPhoto p in data.Items)")
            FILE.write(" \n \t\t\t\t {")
            FILE.write(" \n \t\t\t\t\t //WARNING : Comparing attribute should be changed to a unique key")
            FILE.write(' \n \t\t\t\t\t\t context.MetadataWorkspace.LoadFromAssembly(System.Reflection.Assembly.Load("'+namespace+'"));')
            FILE.write(" \n \t\t\t\t\t\t var existingPres = (from pres in context.Resources")
            FILE.write(" \n \t\t\t\t\t\t\t where pres."+RT.uniqueProperty.name+".Equals(p."+RT.uniqueProperty.name+", StringComparison.OrdinalIgnoreCase)")
            FILE.write(" \n \t\t\t\t\t\t\t select pres).FirstOrDefault();")
            FILE.write(" \n \t\t\t\t\t\t\t if (existingPres != null)")
            FILE.write(" \n \t\t\t\t\t\t\t {")
            FILE.write(' \n \t\t\t\t\t\t\t\t Console.WriteLine("[WARNING] Image {0} already exists in database", p.Id);')
            FILE.write(" \n \t\t\t\t\t\t\t\t continue;")
            FILE.write(" \n \t\t\t\t\t\t\t }")
            FILE.write(" \n \t\t\t\t\t\t\t // Create resources.")
            FILE.write(" \n \t\t\t\t\t\t\t try")
            FILE.write(" \n \t\t\t\t\t\t\t\t {")
            #Begin resource creation
            FILE.write(" \n \t\t\t\t\t\t\t\t "+RT.name+" img = new "+RT.name+" {")
            #Begin properties values assignation
            for SP in RT.scalarProperties:
                FILE.write("{\n \t\t\t\t\t\t\t\t\t "+SP.name + " = " SP.toCode("p") +",")
            #Finish properties values assignation
            FILE.write(" \n \t\t\t\t\t\t\t\t };")
            FILE.write(" \n \t\t\t\t\t\t\t\t context.AddToResources(img);")
            FILE.write(' \n \t\t\t\t\t\t\t\t string[] imagesInFolder = Directory.GetFiles(imgPath, p.'+RT.imgFileProperty.name+' + ".*");')
            #Finish new entity creation
            FILE.write(" \n \t\t\t\t\t\t\t\t // Create a Zentity file.")
            FILE.write(" \n \t\t\t\t\t\t\t\t FileInfo ImageFile = new FileInfo(imagesInFolder[0]);")
            FILE.write(" \n \t\t\t\t\t\t\t\t Zentity.Core.File fileResource = new Zentity.Core.File();")
            FILE.write(" \n \t\t\t\t\t\t\t\t fileResource.Title = ImageFile.Name;")
            FILE.write(" \n \t\t\t\t\t\t\t\t fileResource.Size = ImageFile.Length;")
            FILE.write(" \n \t\t\t\t\t\t\t\t fileResource.DateAdded = ImageFile.CreationTime;")
            FILE.write(" \n \t\t\t\t\t\t\t\t fileResource.DateModified = ImageFile.LastWriteTime;")
            FILE.write(" \n \t\t\t\t\t\t\t\t fileResource.FileExtension = ImageFile.Extension;")
            FILE.write(' \n \t\t\t\t\t\t\t\t fileResource.MimeType = "image/" + fileResource.FileExtension.Replace(".", string.Empty);')
            FILE.write(" \n \t\t\t\t\t\t\t\t // Add the file to context.    ")
            FILE.write(" \n \t\t\t\t\t\t\t\t context.AddToResources(fileResource);")
            FILE.write(' \n \t\t\t\t\t\t\t\t Console.WriteLine("[INFO] Creating image {0}", p.Id);')
            FILE.write(" \n \t\t\t\t\t\t\t\t context.SaveChanges();")
            FILE.write(" \n \t\t\t\t\t\t\t\t // Now upload the actual binary content of the file.    ")
            FILE.write(" \n \t\t\t\t\t\t\t\t FileStream fStream = new FileStream(ImageFile.FullName, FileMode.Open, FileAccess.Read);")
            FILE.write(' \n \t\t\t\t\t\t\t\t Console.WriteLine("[INFO] Saving image {0} file", p.Id);')
            FILE.write(" \n \t\t\t\t\t\t\t\t context.UploadFileContent(fileResource, fStream);")
            FILE.write(" \n \t\t\t\t\t\t\t\t //Asociate file with Resource")
            FILE.write(" \n \t\t\t\t\t\t\t\t img.Files.Add(fileResource);")
            FILE.write(" \n \t\t\t\t\t\t\t\t context.InsertResourceHasFile(fileResource.Id, img.Id);")
            FILE.write(" \n \t\t\t\t\t\t\t\t //Save Changes in context")
            FILE.write(' \n \t\t\t\t\t\t\t\t Console.WriteLine("[INFO] Associating image {0} and file", p.Id);')
            FILE.write(" \n \t\t\t\t\t\t\t\t context.SaveChanges();")
            FILE.write(" \n \t\t\t\t\t\t\t\t }catch{")
            FILE.write(' \n \t\t\t\t\t\t\t\t Console.WriteLine("[ERROR] During image {0} creation", p.Id);')
            FILE.write(" \n \t\t\t\t\t\t\t\t continue;")
            #Close try/catch
            FILE.write(" \n \t\t\t\t\t\t\t\t }")
            #Close foreach
            FILE.write(" \n \t\t\t\t\t\t\t }")

            FILE.write(" \n \t\t\t\t\t\t\t // Retrieve and show resources.")
            FILE.write(" \n \t\t\t\t\t\t\t DisplayImageResources(context);")
            FILE.write(" \n \t\t\t\t\t\t }")
            FILE.write(" \n \t\t\t\t\t }")

	#Closes class 
	FILE.write("\n\t }")
	#Closes namespace
	FILE.write("\n }")

	FILE.close()

if __name__=="__main__":
    a = []
    a.append(ResourcesArray.buildImageResourceType)
    generate(a,"C:\\test.cs","Zentity.Flickr")
                   
