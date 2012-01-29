using Zentity.Core;
using System.IO;
using System.Linq;

namespace GeneratedDataModel_Modulo2
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
	 	    DataModelModule module = new DataModelModule { NameSpace = "Zentity.Modulo2" };
	 	   // Create the Resources type.
	 	    ResourceType resourceTypeResource = context.DataModel.Modules["Zentity.Core"].ResourceTypes["Resource"];
	 	    ResourceType Entidad2 = new ResourceType { Name = "Entidad2", BaseType = resourceTypeResource };
	 	    module.ResourceTypes.Add(Entidad2); 
	 	    // Create some Scalar Properties.
	 	    ScalarProperty Main_Textual_Category = new ScalarProperty { Name = "Main_Textual_Category", DataType =DataTypes.String };
	 	    Entidad2.ScalarProperties.Add(Main_Textual_Category);
	 	    ScalarProperty Main_Visual_Category = new ScalarProperty { Name = "Main_Visual_Category", DataType =DataTypes.String };
	 	    Entidad2.ScalarProperties.Add(Main_Visual_Category);
	 	    ScalarProperty ImageID = new ScalarProperty { Name = "ImageID", DataType =DataTypes.String };
	 	    Entidad2.ScalarProperties.Add(ImageID);
	 	    ScalarProperty LTT_PERSONA_USUARIO_EJECUTIVO_ANIMAL = new ScalarProperty { Name = "LTT_PERSONA_USUARIO_EJECUTIVO_ANIMAL", DataType =DataTypes.Double };
	 	    Entidad2.ScalarProperties.Add(LTT_PERSONA_USUARIO_EJECUTIVO_ANIMAL);
	 	    ScalarProperty LTT_TIERRA_AGUA_ANIMAL_USUARIO = new ScalarProperty { Name = "LTT_TIERRA_AGUA_ANIMAL_USUARIO", DataType =DataTypes.Double };
	 	    Entidad2.ScalarProperties.Add(LTT_TIERRA_AGUA_ANIMAL_USUARIO);
	 	    ScalarProperty LTV_USUARIO_EJECUTIVO_PERSONA_TIERRA = new ScalarProperty { Name = "LTV_USUARIO_EJECUTIVO_PERSONA_TIERRA", DataType =DataTypes.Double };
	 	    Entidad2.ScalarProperties.Add(LTV_USUARIO_EJECUTIVO_PERSONA_TIERRA);
	 	    ScalarProperty LTV_TIERRA_AGUA_ANIMAL_PERSONA = new ScalarProperty { Name = "LTV_TIERRA_AGUA_ANIMAL_PERSONA", DataType =DataTypes.Double };
	 	    Entidad2.ScalarProperties.Add(LTV_TIERRA_AGUA_ANIMAL_PERSONA);
	 	    ScalarProperty Tag_EJECUTIVO = new ScalarProperty { Name = "Tag_EJECUTIVO", DataType =DataTypes.Boolean };
	 	    Entidad2.ScalarProperties.Add(Tag_EJECUTIVO);
	 	    ScalarProperty Tag_PERSONA = new ScalarProperty { Name = "Tag_PERSONA", DataType =DataTypes.Boolean };
	 	    Entidad2.ScalarProperties.Add(Tag_PERSONA);
	 	    ScalarProperty Tag_TIERRA = new ScalarProperty { Name = "Tag_TIERRA", DataType =DataTypes.Boolean };
	 	    Entidad2.ScalarProperties.Add(Tag_TIERRA);
	 	    ScalarProperty Tag_AGUA = new ScalarProperty { Name = "Tag_AGUA", DataType =DataTypes.Boolean };
	 	    Entidad2.ScalarProperties.Add(Tag_AGUA);
	 	    ScalarProperty Tag_USUARIO = new ScalarProperty { Name = "Tag_USUARIO", DataType =DataTypes.Boolean };
	 	    Entidad2.ScalarProperties.Add(Tag_USUARIO);
	 	    // Synchronize to alter the database schema.
	 	    context.DataModel.Modules.Add(module);
	 	    context.DataModel.Synchronize();

	 	    // Generate Extensions Assembly.
	 	    using (FileStream fout = new FileStream(@"../data/code/Zentity.Modulo2.dll", FileMode.Create, FileAccess.Write))
	 	 	 {  
	 	 	  byte[] rawAssembly = context.DataModel.GenerateExtensionsAssembly(
	 	 	    "Zentity.Modulo2", false, null, new string[] { "Zentity.Modulo2" }, null); 

	 	 	   fout.Write(rawAssembly, 0, rawAssembly.Length);  

		      }
	 	    // Generate Entity Framework artifacts.

	 	    EFArtifactGenerationResults results = context.DataModel.GenerateEFArtifacts("Zentity.Modulo2");
	 	    results.Csdls.Where(tuple => tuple.Key == "Zentity.Core").First().Value.Save(@"../data/code/Zentity.Modulo2.ExtendedCore.csdl");
	 	    results.Csdls.Where(tuple => tuple.Key == "Zentity.Modulo2").First().Value.Save(@"../data/code/Zentity.Modulo2.csdl");
	 	    results.Msl.Save(@"../data/code/Zentity.Modulo2.Consolidated.msl");
	 	    results.Ssdl.Save(@"../data/code/Zentity.Modulo2.Consolidated.ssdl");

		 }
		 static void Main(string[] args)
		 {
			 DMCreator creator = new DMCreator();
			 creator.CreateDM();
		 }
	 }
 }