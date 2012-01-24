from xml.etree.ElementTree import Element, ElementTree
from os.path import join,exists,isdir
import InterfazZ_Entidad as Entidad
import errno
from os import strerror
class Error(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class CodeGenerator:
    def __init__(self,DataModelModule,codeStoragePath):
        """Creates a code generator that is capapble of building generation model code and code to upload data to this model

        Attributes:

            - DataModelModule -- The DataModelModule for which all code will be generated
            - codeStoragePath -- A valid path for a folder in which code and binaries will be stored.
          """
        self.DataModelModule = DataModelModule
        self.setCodeStoragePath(codeStoragePath)

    def setCodeStoragePath(self,codeStoragePath ):
        if codeStoragePath != None and ((not exists(codeStoragePath)) or (not isdir(codeStoragePath))):
            raise OSError(errno.ENOENT,strerror(errno.ENOENT),codeStoragePath)
        self.codeStoragePath = codeStoragePath 

    def __checkCreationDMMParameters__(self):
        if (not exists(self.codeStoragePath)):
            print "[ERROR] Bad path provided to store code in DMM"
            return False          
        return True

    def saveGenerationCode(self,filename="ModelCreator.cs"):
        if self.__checkCreationDMMParameters__():
            path = self.codeStoragePath
            namespace = self.DataModelModule.getNombre()
            # Create a file object:
            # in "write" mode
            FILE = open(join(path, filename),"w")
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
                scalarProperties = resourceType.getProperties()
                for property in scalarProperties:
                        if not property.isInherited():
                                FILE.write("\n\t \t    ScalarProperty " + property.name + " = new ScalarProperty { Name = \"" + property.name + "\", DataType =" + property.getDataType()+ " };")
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
        else:
            print "[ERROR] Impossible to generate code due to lack of some parameters in the DMM and its parts"




    def __checkInsertionDMMParameters__(self):
        RTNames = set()
        ZXMLPrefix = set()
        for resource in self.DataModelModule.getResourceTypes():
            #Find a identifier variable and set uniqueVariable if there is one
            identifierProperty = None
            propNames = set()
            for prop in resource.getProperties():
            #For each resource type check that all its properties have unique names
                if prop.name in propNames:
                    raise Error("[ERROR] In DMM "+self.DataModelModule.name+", in the RT " + resource.name  +  ", the SP " + prop.name  + " has a repeated name") 
                else:
                    propNames.add(prop.name)
                if prop.isIdentifier():
                    identifierProperty = prop
            #Check that if the visualizationType is IMAGE there is one identifier property
            if identifierProperty == None and resource.getVisualizationType().vType == Entidad.VisualizationType.IMAGE:
                raise Error("[ERROR] In DMM "+self.DataModelModule.name+", the RT " + resource.name  +  " doesn't have a unique identifier property but its Visualization Type is IMAGE") 
            #Check each resource has a unique name
            if resource.name in RTNames:
                raise Error("[ERROR] In DMM "+self.DataModelModule.name+", the RT name " + resource.name  +  " is repeated") 
            else:
                RTNames.add(resource.name)
            #Check XMLStructure 
            if resource.getXMLStructure()==None:
                raise Error("[ERROR] In DMM "+self.DataModelModule.name+", in the RT "+resource.name+" has no XMLStructure")
            else:
                prefix = resource.getXMLStructure().getFilesPrefix()
                #Check each resource type as a unique FilesPrefix
                if prefix in ZXMLPrefix:
                    raise Error("[ERROR] In DMM "+self.DataModelModule.name+", the ZXML Prefix " + prefix + " is repeated")
                else:
                    ZXMLPrefix.add(prefix)
        return True

    def writeImports(self,FILE):
        FILE.write("using System;\n")
        FILE.write("using System.IO;\n")
        FILE.write("using System.Collections.Generic;\n")
        FILE.write("using System.Linq;\n")
        FILE.write("using System.Text;\n")
        FILE.write("using Zentity.Core;\n")
        FILE.write("using System.Xml.Serialization;")
        FILE.write("using Zentity."+ self.DataModelModule.getNombre()+";\n")

    def writeGeneralMethods(self,FILE):

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

    def writeLoadAndInsertDataCode(self,FILE,resource,namespace,loadDataMethodName,insertDataMethodName,dataVariable):

        #Find a identifier variable and set uniqueVariable if there is one
        identifierProperty = None
        for prop in resource.getProperties():
            if prop.isIdentifier():
                identifierProperty = prop
                break


        FILE.write(" \n \t\t private " + resource.getXMLStructure().getParentNodeName() + dataVariable + ";")
        #Begin loadData Method
        FILE.write(" \n \t\t private void "+loadDataMethodName+"(string xmlPath)")
        FILE.write(" \n \t\t {")
        FILE.write(" \n \t\t\t data = Deserialize<"+resource.getXMLStructure().getParentNodeName() +">(xmlPath);")
        FILE.write(" \n \t\t }")
        #Finish loadData Method                   
   
        #Begin InsertData Method
        FILE.write(" \n \t\t public void "+insertDataMethodName+"(ZentityContext zenContext, string xmlPath, string imgPath)")
        FILE.write(" \n \t\t {")
        FILE.write(" \n \t\t\t " + loadDataMethodName+ "(xmlPath);")
        FILE.write(" \n \t\t\t using (ZentityContext context = zenContext)")
        FILE.write(" \n \t\t\t {")
        #Begin for
        FILE.write(" \n \t\t\t\t foreach ("+resource.getXMLStructure().getParentNodeName() +resource.getXMLStructure().getChildNodeName() +" p in data.Items)")
        FILE.write(" \n \t\t\t\t {")
        FILE.write(" \n \t\t\t\t\t //WARNING : Comparing attribute should be changed to a unique key")
        FILE.write(' \n \t\t\t\t\t context.MetadataWorkspace.LoadFromAssembly(System.Reflection.Assembly.Load("Zentity.'+namespace+'"));')
        if identifierProperty !=None:
            FILE.write(" \n \t\t\t\t\t var existingPres = (from pres in context.Resources")
            FILE.write(" \n \t\t\t\t\t\t where pres."+identifierProperty.name +".Equals(p."+identifierProperty.name +", StringComparison.OrdinalIgnoreCase)")
            FILE.write(" \n \t\t\t\t\t\t select pres).FirstOrDefault();")
            FILE.write(" \n \t\t\t\t\t\t if (existingPres != null)")
            FILE.write(" \n \t\t\t\t\t\t {")
            FILE.write(' \n \t\t\t\t\t\t\t Console.WriteLine("[WARNING] Image {0} already exists in database", p.'+identifierProperty.name +');')
            FILE.write(" \n \t\t\t\t\t\t\t continue;")
            FILE.write(" \n \t\t\t\t\t\t }")
        FILE.write(" \n \t\t\t\t\t\t // Create resources.")
        FILE.write(" \n \t\t\t\t\t\t try")
        FILE.write(" \n \t\t\t\t\t\t\t {")
        #Begin resource creation
        FILE.write(" \n \t\t\t\t\t\t\t "+resource.name+" img = new "+resource.name+" {")
        #Begin properties values assignation
        for SP in resource.getProperties():
            FILE.write("\n \t\t\t\t\t\t\t\t "+SP.toCode("p") +",")
        #Finish properties values assignation
        FILE.write(" \n \t\t\t\t\t\t\t };")
        if resource.getVisualizationType().vType == Entidad.VisualizationType.IMAGE:
            FILE.write(" \n \t\t\t\t\t\t\t context.AddToResources(img);")
            FILE.write(' \n \t\t\t\t\t\t\t string[] imagesInFolder = Directory.GetFiles(imgPath, p.'+identifierProperty.name+' + ".*");')
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
            FILE.write(' \n \t\t\t\t\t\t\t Console.WriteLine("[INFO] Creating image {0}", p.'+identifierProperty.name+');')
            FILE.write(" \n \t\t\t\t\t\t\t context.SaveChanges();")
            FILE.write(" \n \t\t\t\t\t\t\t // Now upload the actual binary content of the file.    ")
            FILE.write(" \n \t\t\t\t\t\t\t FileStream fStream = new FileStream(ImageFile.FullName, FileMode.Open, FileAccess.Read);")
            FILE.write(' \n \t\t\t\t\t\t\t Console.WriteLine("[INFO] Saving image {0} file", p.'+identifierProperty.name+');')
            FILE.write(" \n \t\t\t\t\t\t\t context.UploadFileContent(fileResource, fStream);")
            FILE.write(" \n \t\t\t\t\t\t\t //Asociate file with Resource")
            FILE.write(" \n \t\t\t\t\t\t\t img.Files.Add(fileResource);")
            FILE.write(" \n \t\t\t\t\t\t\t context.InsertResourceHasFile(fileResource.Id, img.Id);")
            FILE.write(" \n \t\t\t\t\t\t\t //Save Changes in context")
            FILE.write(' \n \t\t\t\t\t\t\t Console.WriteLine("[INFO] Associating image {0} and file", p.'+identifierProperty.name+');')
            FILE.write(" \n \t\t\t\t\t\t\t context.SaveChanges();")
        FILE.write(" \n \t\t\t\t\t\t\t }")
        FILE.write(" \n \t\t\t\t\t\t\t catch{")
        FILE.write(' \n \t\t\t\t\t\t\t\t Console.WriteLine("[ERROR] During image {0} creation", p.'+identifierProperty.name+');')
        FILE.write(" \n \t\t\t\t\t\t\t\t continue;")
        #Close try/catch
        FILE.write(" \n \t\t\t\t\t\t\t }")
        #Close foreach
        FILE.write(" \n \t\t\t\t\t\t }")
        FILE.write(" \n \t\t\t\t }")
        FILE.write(" \n \t\t\t }")

    def saveInsertionCode(self,zxmlFilesStoragePath,filename="ModelUploader.cs"):
        """Generates code to upload data to the model

        Attributes:
            - zxmlFilesStoragePath -- Path in which the ZXML files were or will be generated
            - filename -- Filename for the generated code that will be stored in the codeStoragePath given in the constructor of the object
        """
        if self.__checkInsertionDMMParameters__():
            namespace = self.DataModelModule.getNombre()
            path = self.codeStoragePath
            if zxmlFilesStoragePath != None and ((not exists(zxmlFilesStoragePath)) or (not isdir(zxmlFilesStoragePath))):
                raise OSError(errno.ENOENT,strerror(errno.ENOENT),zxmlFilesStoragePath)
            # Create a file object:
            # in "write" mode
            FILE = open(join(path,filename),"w")
            #Imports
            self.writeImports(FILE)
            #Begin namespace
            FILE.write("namespace DataInsert\n")
            FILE.write("{ \n \t class DataInsert \n \t { \n  ")
            #Begin Deserialize Method
            self.writeGeneralMethods(FILE)
            #Begin LoadData Methods
            for resource in self.DataModelModule.getResourceTypes():
                loadDataMethodName = "load"+resource.getXMLStructure().getParentNodeName()+"Data"
                dataVariableName = "data"+resource.getXMLStructure().getParentNodeName()
                insertDataMethodName = "insertData_"+resource.name
                self.writeLoadAndInsertDataCode(FILE,resource,namespace,loadDataMethodName,insertDataMethodName,dataVariableName)

            #Begin main method
            FILE.write(" \n \t\t static void Main(string[] args)")
            FILE.write(" \n \t\t {")
            FILE.write(' \n \t\t\t const string connectionString = @"provider=System.Data.SqlClient;')
            FILE.write(" \n \t\t\t\t metadata="+join(path,'code',"Zentity."+namespace+'.ExtendedCore.csdl')+"|"+join(path,'code',"Zentity."+namespace+'.csdl')+'|'+join(path,'code',"Zentity."+namespace+'.Consolidated.msl')+"|"+join(path,'code',"Zentity."+namespace+".Consolidated.ssdl;"))
            FILE.write(" \n \t\t\t\t provider connection string='Data Source=.;")
            FILE.write(" \n \t\t\t\t Initial Catalog=Zentity;Integrated Security=True;MultipleActiveResultSets=True'")
            FILE.write(' \n \t\t\t\t ";')

            FILE.write(" \n \t\t\t DataInsert dataUploader = new DataInsert();")
            for resource in self.DataModelModule.getResourceTypes():
                if resource.getVisualizationType().vType == Entidad.VisualizationType.IMAGE:
                    imagesPath = resource.getVisualizationType().path
                else:
                    imagesPath ="" 
                #Add double slash to the paths so they can be stored as strings in C#
                FILE.write(' \n \t\t\t string imgFolderPath = "'+"\\\\".join(imagesPath.split('\\'))+'";')
                #Call the data insertor for each resourceType and for each ZXML file
                FILE.write(' \n \t\t\t string ZXMLPath = "'+"\\\\".join(zxmlFilesStoragePath.split('\\'))+'";')
                FILE.write(' \n \t\t\t string[] ZXMLFiles = Directory.GetFiles(ZXMLPath, "'+resource.getXMLStructure().getFilesPrefix()+'*.*");')
                FILE.write(" \n \t\t\t foreach (string a in ZXMLFiles)")
                #begin foreach file
                FILE.write(" \n \t\t\t {")
                FILE.write(" \n \t\t\t\t ZentityContext zenContext = new ZentityContext(connectionString);")
                insertDataMethodName = "insertData_"+resource.name
                FILE.write(' \n \t\t\t\t dataUploader.'+insertDataMethodName + '(zenContext, a, imgFolderPath);')
                FILE.write(" \n \t\t\t }")
                #begin foreach file
                #Closes class
            FILE.write("\n\t\t }")
            FILE.write("\n\t }")
            #Closes namespace
            FILE.write("\n }")

            FILE.close()

class ZXMLGenerator:
    def __init__(self,model,zxmlFilesStoragePath):
        if zxmlFilesStoragePath != None and ((not exists(zxmlFilesStoragePath)) or (not isdir(zxmlFilesStoragePath))):
            raise OSError(errno.ENOENT,strerror(errno.ENOENT),zxmlFilesStoragePath)
        self.path = zxmlFilesStoragePath
        self.model = model

    def save(self,imagesPerFile=100):
        for RT in self.model.getResourceTypes():
            self.extractInfo(self.path,RT.getInstancesList(),RT,RT.getXMLStructure().getParentNodeName(),RT.getXMLStructure().getChildNodeName(),imagesPerFile)
    
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
        i = -1
        for i in range(0,len(idsArray)/imagesPerFile):
            print "[DEBUG] Generating ZXML file #" + str(i)
            ElementTree(self.buildImageSTree(idsArray[i*imagesPerFile:((i+1)*imagesPerFile)],path,resourceType.scalarProperties,xmlParentName,xmlChildName)).write(join(path,resourceType.getEstructuraXML().getPrefijoXML()+str(i)+'.xml'))
        print "[DEBUG] Generating ZXML file #" + str(i)
        ElementTree(ElementTree(self.buildImageSTree(idsArray[((i+1)*imagesPerFile):],path,resourceType.getProperties(),xmlParentName,xmlChildName)).write(join(path,resourceType.getXMLStructure().getFilesPrefix()+str(i+1)+'.xml')))
    
