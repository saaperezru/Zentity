import sys
import ScalarProperty
import DataModelCreator
from ResourcesArray import ResourcesArray
def DataModelCreator(arrResourceType, arrProperties, Namespace, path, filename):	
	namespace = Namespace
	# Create a file object:
	# in "write" mode
	FILE = open(filename,"w")
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
	FILE.write("\n\t \t    DataModelModule module = new DataModelModule { NameSpace = \""+namespace+"\" };")
	FILE.write("\n\t \t   // Create the Resource type.")
	FILE.write("\n\t \t    ResourceType resourceTypeResource = context.DataModel.Modules[\"Zentity.Core\"].ResourceTypes[\"Resource\"];")
	FILE.write("\n\t \t    ResourceType resourceTypeImage = new ResourceType { Name = \"ImageResource\", BaseType = resourceTypeResource };")
	FILE.write("\n\t \t    module.ResourceTypes.Add(resourceTypeImage); ")
	FILE.write("\n\t \t    // Create some Scalar Properties.")
	
	#print arrProperties	
	# for property in arrResourceType.scalarProperties:
		# FILE.write("\n\t \t    ScalarProperty " + property.name + " = new ScalarProperty { Name = \"" + property.name + "\", DataType = DataTypes." + property.dataType+ " };")
		# FILE.write("\n\t \t    resourceTypeImage.ScalarProperties.Add(" + property.name + ");")
		# print property.name
	FILE.write("\n\t \t    // Synchronize to alter the database schema.")
	FILE.write("\n\t \t    context.DataModel.Modules.Add(module);")
	FILE.write("\n\t \t    context.DataModel.Synchronize();\n")
	FILE.write("\n\t \t    // Generate Extensions Assembly.")
	FILE.write("\n\t \t    using (FileStream fout = new FileStream(@\""+path+namespace+".dll\", FileMode.Create, FileAccess.Write))")
	FILE.write("\n\t \t \t {  \n")
	FILE.write("\t \t \t  byte[] rawAssembly = context.DataModel.GenerateExtensionsAssembly(")
	FILE.write("\n\t \t \t    \""+namespace + "\", false, null, new string[] { \""+namespace + "\" }, null); \n")
	FILE.write("\n\t \t \t   fout.Write(rawAssembly, 0, rawAssembly.Length);  \n")
	#Closes Generate Extensions Assembly()
	FILE.write("\n\t\t      }")
	FILE.write("\n\t \t    // Generate Entity Framework artifacts.\n")
	FILE.write("\n\t \t    EFArtifactGenerationResults results = context.DataModel.GenerateEFArtifacts(\""+namespace + "\");")
	FILE.write("\n\t \t    results.Csdls.Where(tuple => tuple.Key == \"Zentity.Core\").First().Value.Save(@\""+path+namespace+".ExtendedCore.csdl\");")
	FILE.write("\n\t \t    results.Csdls.Where(tuple => tuple.Key == \"Zentity.Flickr\").First().Value.Save(@\""+path+namespace+".csdl\");")
	FILE.write("\n\t \t    results.Msl.Save(@\""+path+namespace+".Consolidated.msl\");")
	FILE.write("\n\t \t    results.Ssdl.Save(@\""+path+namespace+".ssdl\");\n") 
	#Closes createDM()
	FILE.write("\n\t\t }")
	#Closes class DMCreator()
	FILE.write("\n\t }")
	#Closes namespace
	FILE.write("\n }")

	FILE.close()
arrayResources = []
arrayResources = ResourcesArray.buildImageResourceType()
arrayProperties = []
arrayProperties.append(ScalarProperty.ScalarProperty("TagRumba", "Boolean", "extractor"))
arrayProperties.append(ScalarProperty.ScalarProperty("TagFamilia", "String", "extractor"))
arrayProperties.append(ScalarProperty.ScalarProperty("TagFrutas", "Image", "extractor"))
DataModelCreator(arrayResources, arrayProperties, "Zentity.Flickr", "C:\Zentity\\")
