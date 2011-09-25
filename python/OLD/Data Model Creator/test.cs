using Zentity.Core;
using System.IO;
using System.Linq;

namespace GeneratedDataModel_Zentity.Flickr
{ 
 	 class DMCreator 
 	 { 
   	 	 const string connectionString = @"provider=System.Data.SqlClient;
 	 	     metadata=res://*/; provider connection string='Data Source=.;
 	 	     Initial Catalog=Zentity;Integrated Security=True;MultipleActiveResultSets=True'";

  	 	 public void CreateDM() 
 	 	 { 
 	 	    ZentityContext context = new ZentityContext(connectionString);
 	 	   //Create a new module.
	 	    DataModelModule module = new DataModelModule { NameSpace = "Zentity.Flickr };
	 	   // Create the Resource type.
	 	    ResourceType resourceTypeResource = context.DataModel.Modules["Zentity.Core"].ResourceTypes["Resource"];
	 	    ResourceType resourceTypeImage = new ResourceType { Name = "ImageResource", BaseType = resourceTypeResource };
	 	    module.ResourceTypes.Add(resourceTypeImage); 
	 	    // Create some Scalar Properties.
	 	    ScalarProperty TagRumba = new ScalarProperty { Name = "TagRumba", DataType = DataTypes.Boolean };
	 	    resourceTypeImage.ScalarProperties.Add(TagRumba);
	 	    ScalarProperty TagFamilia = new ScalarProperty { Name = "TagFamilia", DataType = DataTypes.String };
	 	    resourceTypeImage.ScalarProperties.Add(TagFamilia);
	 	    ScalarProperty TagFrutas = new ScalarProperty { Name = "TagFrutas", DataType = DataTypes.Image };
	 	    resourceTypeImage.ScalarProperties.Add(TagFrutas);
	 	    // Synchronize to alter the database schema.
	 	    context.DataModel.Modules.Add(module);
	 	    context.DataModel.Synchronize();

	 	    // Generate Extensions Assembly.
	 	    using (FileStream fout = new FileStream(@"C:\Zentity\Zentity.Flickr.dll", FileMode.Create, FileAccess.Write))
	 	 	 {  
	 	 	  byte[] rawAssembly = context.DataModel.GenerateExtensionsAssembly(
	 	 	    "Zentity.Flickr", false, null, new string[] { "Zentity.Flickr" }, null); 

	 	 	   fout.Write(rawAssembly, 0, rawAssembly.Length);  

		      }
	 	    // Generate Entity Framework artifacts.

	 	    EFArtifactGenerationResults results = context.DataModel.GenerateEFArtifacts("Zentity.Flickr");
	 	    results.Csdls.Where(tuple => tuple.Key == "Zentity.Core").First().Value.Save(@"C:\Zentity\Zentity.Flickr.ExtendedCore.csdl");
	 	    results.Csdls.Where(tuple => tuple.Key == "Zentity.Flickr").First().Value.Save(@"C:\Zentity\Zentity.Flickr.csdl");
	 	    results.Msl.Save(@"C:\Zentity\Zentity.Flickr.Consolidated.msl");
	 	    results.Ssdl.Save(@"C:\Zentity\Zentity.Flickr.ssdl");

		 }
	 }
 }