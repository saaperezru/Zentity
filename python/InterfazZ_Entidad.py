class DataModelModule:
    def __init__(self,name,resources,codeStoragePath,zxmlFilesStoragePath):
    """Builds a DataModel Module with the ResourceTypes specified in the argument array resources
    
      Attributes
      ----------
        - name  --  Data Model Module Name, this must be unique among other DMM in the Zentity instance to be used.
        - resources -- An array with the ResourceType instances that have to be assigned to this DMM.
        - codeStoragePath -- A valid path for a folder in which code and binaries will be stored.
        - zxmlFilesStoragePath -- A valid path for a folder in which the generated unified files will be stored. 
    """
        self.name=name
        self.resourceTypes = resources
        self.codeStoragePath = codeStoragePath
        self.zxmlFilesStoragePath = zxmlStoragePath
    def __init__(self,name):
    """Builds a DataModel Module with an empty list of resource types and without codeStoragePath and zxmlFileStoragePath (this must be set manually)
    
      Attributes
      ----------
        - name  --  Data Model Module Name, this must be unique among other DMM in the Zentity instance to be used.

    """
        self.__init__(name,[],None,None)

    def addResourceType(self,resourceType):
      """Adds a resource type to the Data Model Module but returns nothing"""
        self.resourceTypes.append(resourceType)
    
    def getResourceTypes(self):
      """Returns the array of resourceTypes associated with this DMM."""
        return self.resourceTypes
    
    def getNombre(self):
      """Returns the name of this DMM."""
        return self.name

    def setNombre(self,name):
        self.name = name

    def getCodeStoragePath(self):
        return self.codeStoragePath
    def getZXMLFilesStoragePath(self):
        return self.zxmlFilesStoragePath

class ResourceType:
    def __init__(self,name):
    """Builds a Resource Type with the specified name and empty Instances and ScalarProperties arrays
    
      Attributes
      ----------
        - name  --  Resource Type name, this must be unique among other ResourceTypes in others DMM in the Zentity instance to be used.
    """
        self.__init__(name,[],None,[],None)
    def __init__(self,name,scalarProperties,XMLstruct,Instances,visualizationType):
    """Builds a ResourceType with the specified name and ScalarProperties 
    
      Attributes
      ----------
        - name  --  Resource Type name, this must be unique among other ResourceTypes in both this and others DMM in the Zentity instance to be used.
        - scalarProperties -- An array with the ScalarProperties instances that have to be assigned to this .
        - XMLstruct -- An XMLStructure instance with all the info necessary for the ZXML files generation
        - Instances -- An array of the ids of the instances of this RT, this will be passed to the extractors of this RT ScalarProperties
        - visualizationType -- One of the values in the enum VisualizationTypes 
    """
        self.name = name
        self.scalarProperties = scalarProperties
        self.XML = EstructuraXML
        self.Instancias = Instancias
        self.visual = visualizationType
        
    def getXMLStructure(self):
        return self.XML
        
    def getInstancesList(self):
        return self.Instancias

    def addProperty(self,newProperty):
        self.scalarProperties.append(newProperty)

    def addInstance(self,newInstance):
        self.Instancias.append(newInstance)

    def removeInstance(self,removeInstance):
        self.Instancias.remove(removeInstance)

    def setInstanceList(self,instanceList):
        self.Instancias = instanceList

    def getVisualizationType(self):
        return self.visual 

    def setVisualizationType(self,visualizationType):
        self.visual  = visualizationType

    def getProperties(self):
        return self.scalarProperties

class VisualizationTypes:
    IMAGE,NOIMAGE = range(2)

class DataTypes:

    STRING,BOOLEAN,DECIMAL,DOUBLE,SINGLE,BYTE,INT16,INT32,INT64,DATETIME,BINARY = ["DataTypes.Boolean","DataTypes.String","DataTypes.Decimal","DataTypes.Double","DataTypes.Single","DataTypes.Byte","DataTypes.Int16","DataTypes.Int32","DataTypes.Int64","DataTypes.DateTime","DataTypes.Binary"]


class Extractor:
    def extract(self,id):
        print "[WARNING] Abstract method not correctly implemented"
        return None

class ScalarProperty:
   
    #Translation functions dictionary
    DataTypes = {"DataTypes.Boolean":self.__codeBoolean__,
                          "DataTypes.String":self.__codeString__,
                          "DataTypes.Decimal":self.__codeDecimal__,
                          "DataTypes.Double":self.__codeDouble__,
                          "DataTypes.Single":self.__codeSingle__,
                          "DataTypes.Byte":self.__codeByte__,
                          "DataTypes.Int16":self.__codeInt16__,
                          "DataTypes.Int32":self.__codeInt32__,
                          "DataTypes.Int64":self.__codeInt64__,
                          "DataTypes.DateTime":self.__codeDateTime__,
                          "DataTypes.Binary":self.__codeBinary__}

    #BEGINS code translators
    def __codeString__(self,varName):
        return " " + self.name + " = " + varName + "." + self.name
    def __codeBoolean__(self,varName):
        return " " + self.name + " = (" + varName + "." + self.name + '=="True")'
    def __codeDecimal__(self,varName):
        return " " + self.name + " = Convert.ToDecimal(" + varName + "." + self.name + ")"
    def __codeDouble__(self,varName):
        return " " + self.name + " = Convert.ToDouble(" + varName + "." + self.name + ")"
    def __codeSingle__(self,varName):
        return " " + self.name + " = Convert.ToSingle(" + varName + "." + self.name + ")"
    def __codeByte__(self,varName):
        return " " + self.name + " = Convert.ToByte(" + varName + "." + self.name + ")"
    def __codeInt16__(self,varName):
        return " " + self.name + " = Convert.ToInt16(" + varName + "." + self.name + ")"
    def __codeInt32__(self,varName):
        return " " + self.name + " = Convert.ToInt32(" + varName + "." + self.name + ")"
    def __codeInt64__(self,varName):
        return " " + self.name + " = Convert.ToInt64(" + varName + "." + self.name + ")"
    #This piece of code will need this function in the same namespace: (see: http://www.dreamincode.net/code/snippet2093.htm) 
    def __codeDateTime__(self,varName):
        return " " + self.name + " = ConvertTimestamp(Convert.ToDouble(" + varName + "." + self.name + "))"
    def __codeBinary__(self,varName):
        return self.__codeInt32__(varName)
    #ENDS code translators

    def __init__(self,name,dataType,inherit=False,identifier=False):
    """Builds a ScalarProperty with the specified name, no dataType, no extractor and not inherited 
    
      Attributes
      ----------
        - name  --  Scalar Property name, this must be unique among those of the same ResourceTypes (including those inherited from the Zentity base class for ResourceTypes, see "Especificacion de requerimientos" for details)
    """
        self.__init__(name,dataType,None,inherit,identifier)
    def __init__(self,name,dataType,extractor, inherit=False,identifier=False):
    """Builds a ScalarProperty with the name and ScalarProperties 
    
      Attributes
      ----------
        - name  --  Scalar Property name, this must be unique among those of the same ResourceTypes (including those inherited from the Zentity base class for ResourceTypes, see "Especificacion de requerimientos" for details)
        - dataType -- A value from the ENUM DataTypes
        - extractor -- An instance of a class that inherits the class Extractor
        - inherit -- A boolean that specifies if either this ScalarProperty is inherited from the Zentity Base Class (True), or it is not (False). Default : False
        - identifier -- A boolean attribute that indicates wheter or not the value of this Scalar Property is unique among all the instances of the ResourceType to which it belongs. NOTE : If the Resource Type to which this Scalar Property belongs has a IMAGE visualization type, this identifier will be used to parse images and data, i.e. if this is a identifier Scalar Property is the identifier in a ResourceType visualiced with images, this identifier must identify all the images associated to the instances of this Resource Type
    """
        self.name = name
        self.dataType = dataType
        self.extractor = extractor
        self.inherit = inherit 
        self.identifier = identifier
        
    def extractData(self,idm):
        return self.extractor.extract(idm)

    def toCode(self,varName):
        return ScalarProperty.dataTypes[self.dataType](varName)

    def getDataType(self):
        return self.dataType
    def getExtractor(self):
        return self.extractor
    def setDataType(self,dataType):
        self.dataType  = dataType
    def setExtractor(self,extractor):
        self.extractor = extractor
    def setInherited(self,inherit):
        self.inherit = inherit
    def isInherited(self):
        return self.inherit
    def isIdentifier(self):
        return self.identifier
class XMLStructure:
    def __init__(self,parentNodeName,childNodeName,filesPrefix):
    """Builds a XMLStructure object with the specified parameters 
    
      Attributes
      ----------
        - parentNodeName -- The name of the node that will be parent of all instances in the XML files
        - childNodeName -- The name of the node that will contain all the information for one instance in XML files
        - filesPrefix -- A prefix for the generated files
    """
        self.hijo = nodoXMLHijo
        self.padre = nodoXMLPadre
        self.prefijo = XMLPrefijo
    
    def getChildNodeName(self):
        return self.hijo
    def getParentNodeName(self):
        return self.padre
    def getFilesPrefix(self):
        return self.prefijo
