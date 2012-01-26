using Zentity.Core;
using System.IO;
using System.Linq;

namespace GeneratedDataModel_DMMTest1
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
	 	    DataModelModule module = new DataModelModule { NameSpace = "Zentity.DMMTest1" };
	 	   // Create the Resources type.
	 	    ResourceType resourceTypeResource = context.DataModel.Modules["Zentity.Core"].ResourceTypes["Resource"];
	 	    ResourceType RTTest1 = new ResourceType { Name = "RTTest1", BaseType = resourceTypeResource };
	 	    module.ResourceTypes.Add(RTTest1); 
	 	    // Create some Scalar Properties.
	 	    ScalarProperty Title = new ScalarProperty { Name = "Title", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Title);
	 	    ScalarProperty Description = new ScalarProperty { Name = "Description", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Description);
	 	    ScalarProperty Main_Textual_Category = new ScalarProperty { Name = "Main_Textual_Category", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Main_Textual_Category);
	 	    ScalarProperty Main_Visual_Category = new ScalarProperty { Name = "Main_Visual_Category", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Main_Visual_Category);
	 	    ScalarProperty LTT_P_T_H_F = new ScalarProperty { Name = "LTT_P_T_H_F", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTT_P_T_H_F);
	 	    ScalarProperty LTT_L_E_I_M = new ScalarProperty { Name = "LTT_L_E_I_M", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTT_L_E_I_M);
	 	    ScalarProperty LTT_O_D_E_Q = new ScalarProperty { Name = "LTT_O_D_E_Q", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTT_O_D_E_Q);
	 	    ScalarProperty LTT_T_S_J_P = new ScalarProperty { Name = "LTT_T_S_J_P", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTT_T_S_J_P);
	 	    ScalarProperty LTT_E_M_R_O = new ScalarProperty { Name = "LTT_E_M_R_O", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTT_E_M_R_O);
	 	    ScalarProperty LTT_Q_T_C_R = new ScalarProperty { Name = "LTT_Q_T_C_R", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTT_Q_T_C_R);
	 	    ScalarProperty LTT_J_L_C_D = new ScalarProperty { Name = "LTT_J_L_C_D", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTT_J_L_C_D);
	 	    ScalarProperty LTT_G_I_C_S = new ScalarProperty { Name = "LTT_G_I_C_S", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTT_G_I_C_S);
	 	    ScalarProperty LTT_S_D_T_Q = new ScalarProperty { Name = "LTT_S_D_T_Q", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTT_S_D_T_Q);
	 	    ScalarProperty LTV_J_T_Q_E = new ScalarProperty { Name = "LTV_J_T_Q_E", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTV_J_T_Q_E);
	 	    ScalarProperty LTV_S_G_C_L = new ScalarProperty { Name = "LTV_S_G_C_L", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTV_S_G_C_L);
	 	    ScalarProperty LTV_N_E_R_D = new ScalarProperty { Name = "LTV_N_E_R_D", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTV_N_E_R_D);
	 	    ScalarProperty LTV_N_O_E_C = new ScalarProperty { Name = "LTV_N_O_E_C", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTV_N_O_E_C);
	 	    ScalarProperty LTV_N_Q_A_G = new ScalarProperty { Name = "LTV_N_Q_A_G", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTV_N_Q_A_G);
	 	    ScalarProperty LTV_A_Q_O_F = new ScalarProperty { Name = "LTV_A_Q_O_F", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTV_A_Q_O_F);
	 	    ScalarProperty LTV_G_N_T_H = new ScalarProperty { Name = "LTV_G_N_T_H", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTV_G_N_T_H);
	 	    ScalarProperty LTV_H_T_G_M = new ScalarProperty { Name = "LTV_H_T_G_M", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTV_H_T_G_M);
	 	    ScalarProperty LTV_H_F_E_C = new ScalarProperty { Name = "LTV_H_F_E_C", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTV_H_F_E_C);
	 	    ScalarProperty LTV_E_B_N_J = new ScalarProperty { Name = "LTV_E_B_N_J", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(LTV_E_B_N_J);
	 	    ScalarProperty Tag_A = new ScalarProperty { Name = "Tag_A", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_A);
	 	    ScalarProperty Tag_B = new ScalarProperty { Name = "Tag_B", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_B);
	 	    ScalarProperty Tag_E = new ScalarProperty { Name = "Tag_E", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_E);
	 	    ScalarProperty Tag_D = new ScalarProperty { Name = "Tag_D", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_D);
	 	    ScalarProperty Tag_G = new ScalarProperty { Name = "Tag_G", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_G);
	 	    ScalarProperty Tag_F = new ScalarProperty { Name = "Tag_F", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_F);
	 	    ScalarProperty Tag_I = new ScalarProperty { Name = "Tag_I", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_I);
	 	    ScalarProperty Tag_H = new ScalarProperty { Name = "Tag_H", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_H);
	 	    ScalarProperty Tag_J = new ScalarProperty { Name = "Tag_J", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_J);
	 	    ScalarProperty Tag_M = new ScalarProperty { Name = "Tag_M", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_M);
	 	    ScalarProperty Tag_L = new ScalarProperty { Name = "Tag_L", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_L);
	 	    ScalarProperty Tag_O = new ScalarProperty { Name = "Tag_O", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_O);
	 	    ScalarProperty Tag_N = new ScalarProperty { Name = "Tag_N", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_N);
	 	    ScalarProperty Tag_Q = new ScalarProperty { Name = "Tag_Q", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_Q);
	 	    ScalarProperty Tag_P = new ScalarProperty { Name = "Tag_P", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_P);
	 	    ScalarProperty Tag_S = new ScalarProperty { Name = "Tag_S", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_S);
	 	    ScalarProperty Tag_T = new ScalarProperty { Name = "Tag_T", DataType =DataTypes.Boolean };
	 	    RTTest1.ScalarProperties.Add(Tag_T);
	 	    // Synchronize to alter the database schema.
	 	    context.DataModel.Modules.Add(module);
	 	    context.DataModel.Synchronize();

	 	    // Generate Extensions Assembly.
	 	    using (FileStream fout = new FileStream(@"../data/code/code/DMMTest1.dll", FileMode.Create, FileAccess.Write))
	 	 	 {  
	 	 	  byte[] rawAssembly = context.DataModel.GenerateExtensionsAssembly(
	 	 	    "Zentity.DMMTest1", false, null, new string[] { "Zentity.DMMTest1" }, null); 

	 	 	   fout.Write(rawAssembly, 0, rawAssembly.Length);  

		      }
	 	    // Generate Entity Framework artifacts.

	 	    EFArtifactGenerationResults results = context.DataModel.GenerateEFArtifacts("Zentity.DMMTest1");
	 	    results.Csdls.Where(tuple => tuple.Key == "Zentity.Core").First().Value.Save(@"../data/code/code/Zentity.DMMTest1.ExtendedCore.csdl");
	 	    results.Csdls.Where(tuple => tuple.Key == "Zentity.DMMTest1").First().Value.Save(@"../data/code/code/Zentity.DMMTest1.csdl");
	 	    results.Msl.Save(@"../data/code/code/Zentity.DMMTest1.Consolidated.msl");
	 	    results.Ssdl.Save(@"../data/code/code/Zentity.DMMTest1.Consolidated.ssdl");

		 }
		 static void Main(string[] args)
		 {
			 DMCreator creator = new DMCreator();
			 creator.CreateDM();
		 }
	 }
 }