import InterfazZ_Control as Control
import InterfazZ_Entidad as Entidad 

class DefExtractor(Entidad.Extractor):
    def extract(self,idm):
        return idm

#Lets create the DMM
DMM = Entidad.DataModelModule("Modelo")
#And one RT
RT1 = Entidad.ResourceType("Entidad1")
#We must define an XMLStructure
RT1.setXMLStructure(Entidad.XMLStructure("Padre","Hijo","Ent1"))
#As well as a VisualizationType
RT1.setVisualizationType(Entidad.VisualizationType(Entidad.VisualizationType.IMAGE,"/"))
#And an InstanceList 
RT1.addInstance("I1")
RT1.addInstance("I2")
RT1.addInstance("I3")
RT1.addInstance("I4")
RT1.addInstance("I5")
#Finally we add this Resource Type to the DMM Model
DMM.addResourceType(RT1)
#Now add the SP to this RT1
#We will use the same extractor for all of them
ext = DefExtractor()
RT1.addProperty(Entidad.ScalarProperty("Prop1",Entidad.DataTypes.STRING,ext,False,True))
RT1.addProperty(Entidad.ScalarProperty("Prop2",Entidad.DataTypes.DATETIME,ext))
RT1.addProperty(Entidad.ScalarProperty("Prop3",Entidad.DataTypes.INT16,ext))

Gen = Control.CodeGenerator(DMM,"/home/tuareg/Documents/Work/Zentity/scripts/")
Gen.saveGenerationCode()
zxmlDirectory = "/home/tuareg/Documents/Work/Zentity/scripts/"
ZXML = Control.ZXMLGenerator(DMM,zxmlDirectory)
ZXML.save()
Gen.saveInsertionCode(zxmlDirectory)

