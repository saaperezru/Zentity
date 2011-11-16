from xml.etree.ElementTree import Element, ElementTree
from os.path import join
class GeneradorCreacion:
    def __init__(self,DataModelModule):
        self.DataModelModule = DataModelModule

    def save(self,path,filename="ModelCreator.cs"):
        namespace = self.DataModelModule.getNombre()
        # Create a file object:
        # in "write" mode
        FILE = open(join(path, "code",filename),"w")
        FILE.write("using Zentity.Core;\n")
        FILE.write("using System.IO;\n")
        FILE.write("using System.Linq;\n\n")
        FILE.write("namespace GeneratedDataModel_" +namespace+"\n")
        FILE.write("{ \n \t class DMCreator \n \t { \n  ")
        FILE.write(" \t \t const string connectionString = @\"provider=System.Data.SqlClient;")
        FILE.write("\n \t \t     metadata=res://*/; provider connection string='Data Source=.;")
        FILE.write("\n \t \t     Initial Catalog=Zentity;Integrated Security=True;MultipleActiveResultSets=True'\";")
        FILE.write("\n\n  \t \t public void CreateDM() \n \t \t { ")
        FILE.write("\n \t \t    ZentityContext context = new ZentityContext(connectionString);")
        FILE.write("\n \t \t   //Create a new module.") 
        FILE.write("\n\t \t    DataModelModule module = new DataModelModule { NameSpace = \"Zentity."+namespace+"\" };")
        FILE.write("\n\t \t   // Create the Resources type.")
        FILE.write("\n\t \t    ResourceType resourceTypeResource = context.DataModel.Modules[\"Zentity.Core\"].ResourceTypes[\"Resource\"];")
        
        for resourceType in self.DataModelModule.getResourceTypes():	    	
            FILE.write("\n\t \t    ResourceType "+ resourceType.name +" = new ResourceType { Name = \""+resourceType.name+"\", BaseType = resourceTypeResource };")
            FILE.write("\n\t \t    module.ResourceTypes.Add("+resourceType.name+"); ")
            FILE.write("\n\t \t    // Create some Scalar Properties.")
            #print arrProperties	
            scalarProperties = resourceType.scalarProperties
            for property in scalarProperties:
                    if(property.default==False):
                            FILE.write("\n\t \t    ScalarProperty " + property.name + " = new ScalarProperty { Name = \"" + property.name + "\", DataType =" + property.dataType+ " };")
                            FILE.write("\n\t \t    "+resourceType.name+".ScalarProperties.Add(" + property.name + ");")
        FILE.write("\n\t \t    // Synchronize to alter the database schema.")
        FILE.write("\n\t \t    context.DataModel.Modules.Add(module);")
        FILE.write("\n\t \t    context.DataModel.Synchronize();\n")
        FILE.write("\n\t \t    // Generate Extensions Assembly.")
        FILE.write("\n\t \t    using (FileStream fout = new FileStream(@\""+join(path, "code",namespace)+".dll\", FileMode.Create, FileAccess.Write))")
        FILE.write("\n\t \t \t {  \n")
        FILE.write("\t \t \t  byte[] rawAssembly = context.DataModel.GenerateExtensionsAssembly(")
        FILE.write("\n\t \t \t    \"Zentity."+namespace + "\", false, null, new string[] { \"Zentity."+namespace + "\" }, null); \n")
        FILE.write("\n\t \t \t   fout.Write(rawAssembly, 0, rawAssembly.Length);  \n")
        #Closes Generate Extensions Assembly()
        FILE.write("\n\t\t      }")
        FILE.write("\n\t \t    // Generate Entity Framework artifacts.\n")
        FILE.write("\n\t \t    EFArtifactGenerationResults results = context.DataModel.GenerateEFArtifacts(\"Zentity."+namespace + "\");")
        FILE.write("\n\t \t    results.Csdls.Where(tuple => tuple.Key == \"Zentity.Core\").First().Value.Save(@\""+join(path, "code","Zentity."+namespace)+".ExtendedCore.csdl\");")
        FILE.write("\n\t \t    results.Csdls.Where(tuple => tuple.Key == \"Zentity."+namespace+"\").First().Value.Save(@\""+join(path, "code","Zentity."+namespace)+".csdl\");")
        FILE.write("\n\t \t    results.Msl.Save(@\""+join(path, "code","Zentity."+namespace)+".Consolidated.msl\");")
        FILE.write("\n\t \t    results.Ssdl.Save(@\""+join(path, "code","Zentity."+namespace)+".Consolidated.ssdl\");\n") 
        #Closes createDM()
        FILE.write("\n\t\t }")
        FILE.write("\n\t\t static void Main(string[] args)")	
        FILE.write("\n\t\t {")
        FILE.write("\n\t\t\t DMCreator creator = new DMCreator();")
        FILE.write("\n\t\t\t creator.CreateDM();")		
        #Closes Main()
        FILE.write("\n\t\t }")		
        #Closes class DMCreator()
        FILE.write("\n\t }")
        #Closes namespace
        FILE.write("\n }")

        FILE.close()


##WARNING: THIS DOESN'T WORKS FOR MORE THAN ONE RESOURCE TYPE IN A DATA MODEL MODULE
## NEITHER DOES FOR RESOURCES WITH NO IMAGES
class GeneradorInsercion:
    def __init__(self,DataModelModule):
        self.estructuraXML = DataModelModule.getResourceTypes()[0].getEstructuraXML()
        self.DataModelModule = DataModelModule

    def save(self,path,filename="ModelUploader.cs"):
        namespace = self.DataModelModule.getNombre()
        # Create a file object:
        # in "write" mode
        FILE = open(join(path, "code",filename),"w")
        #Imports
        FILE.write("using System;\n")
        FILE.write("using System.IO;\n")
        FILE.write("using System.Collections.Generic;\n")
        FILE.write("using System.Linq;\n")
        FILE.write("using System.Text;\n")
        FILE.write("using Zentity.Core;\n")
        FILE.write("using System.Xml.Serialization;")
        FILE.write("using Zentity."+ namespace +";\n")
        
        #Begin namespace
        FILE.write("namespace DataInsert\n")
        FILE.write("{ \n \t class DataInsert \n \t { \n  ")

        FILE.write(" \n \t\t private " + self.estructuraXML.getNodoPadreXML() + " data;")
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
        FILE.write(" \n \t\t\t data = Deserialize<"+self.estructuraXML.getNodoPadreXML()+">(xmlPath);")
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
        
        for RT in self.DataModelModule.getResourceTypes():
            FILE.write(" \n \t\t public void insertData_"+RT.name+"(ZentityContext zenContext, string xmlPath, string imgPath)")
            FILE.write(" \n \t\t {")
            FILE.write(" \n \t\t\t loadData(xmlPath);")
            FILE.write(" \n \t\t\t using (ZentityContext context = zenContext)")
            FILE.write(" \n \t\t\t {")
            #Begin for
            FILE.write(" \n \t\t\t\t foreach ("+self.estructuraXML.getNodoPadreXML()+self.estructuraXML.getNodoHijoXML()+" p in data.Items)")
            FILE.write(" \n \t\t\t\t {")
            FILE.write(" \n \t\t\t\t\t //WARNING : Comparing attribute should be changed to a unique key")
            FILE.write(' \n \t\t\t\t\t context.MetadataWorkspace.LoadFromAssembly(System.Reflection.Assembly.Load("Zentity.'+namespace+'"));')
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
        FILE.write(" \n \t\t\t\t metadata="+join(path,'code',"Zentity."+namespace+'.ExtendedCore.csdl')+"|"+join(path,'code',"Zentity."+namespace+'.csdl')+'|'+join(path,'code',"Zentity."+namespace+'.Consolidated.msl')+"|"+join(path,'code',"Zentity."+namespace+".Consolidated.ssdl;"))
        FILE.write(" \n \t\t\t\t provider connection string='Data Source=.;")
        FILE.write(" \n \t\t\t\t Initial Catalog=Zentity;Integrated Security=True;MultipleActiveResultSets=True'")
        FILE.write(' \n \t\t\t\t ";')

        FILE.write(" \n \t\t\t DataInsert dataUploader = new DataInsert();")
        #Add double slash to the paths so they can be stored as strings in C#
        FILE.write(' \n \t\t\t string imgFolderPath = "'+"\\\\".join(join(path,'images').split('\\'))+'";')
        #Call the data insertor for each resourceType and for each ZXML file
        FILE.write(' \n \t\t\t string ZXMLPath = "'+"\\\\".join(join(path,'ZXML').split('\\'))+'";')
        for RT in self.DataModelModule.getResourceTypes():
            FILE.write(' \n \t\t\t string[] '+RT.name+'ZXMLFiles = Directory.GetFiles(ZXMLPath, "'+self.estructuraXML.getPrefijoXML()+'*.*");')
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



class GeneradorXML:
    def __init__(self,path,ZXMLPrefix=""):
        self.path = path
        self.prefix = ZXMLPrefix

    def save(self,DataModelModule,imagesPerFile=100):
        for RT in DataModelModule.getResourceTypes():
            self.extractInfo(self.path,RT.getInstancias(),RT,RT.getEstructuraXML().getNodoPadreXML(),RT.getEstructuraXML().getNodoHijoXML(),imagesPerFile)
        
    
    def buildImageTree(self,idm,path,properties,xmlChildName):
        root=Element(xmlChildName)
        for sp in properties:
            e = Element(sp.name)
            e.text = sp.extractData(idm)
            root.append(e)
        return root


    def buildImageSTree(self,idArray,path,properties,xmlParentName,xmlChildName):
        root = Element(xmlParentName)
        for i in idArray:
            root.append(self.buildImageTree(i,path,properties,xmlChildName))
        return root
        
    
    def extractInfo(self,path,idsArray,resourceType,xmlParentName,xmlChildName,imagesPerFile = 100):
        for i in range(0,len(idsArray)/imagesPerFile):
            print "[DEBUG] Generating ZXML file #" + str(i)
            ElementTree(self.buildImageSTree(idsArray[i*imagesPerFile:((i+1)*imagesPerFile)],path,resourceType.scalarProperties,xmlParentName,xmlChildName)).write(join(path,resourceType.getEstructuraXML().getPrefijoXML()+str(i)+'.xml'))
        print "[DEBUG] Generating ZXML file #" + str(i)
        ElementTree(ElementTree(self.buildImageSTree(idsArray[((i+1)*imagesPerFile):],path,resourceType.scalarProperties,xmlParentName,xmlChildName)).write(join(path,resourceType.getEstructuraXML().getPrefijoXML()+str(i+1)+'.xml')))
    
