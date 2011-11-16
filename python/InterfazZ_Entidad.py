class DataModelModule:
    def __init__(self,nombre):
        self.nombre=nombre
        self.resourceTypes = []
    
    def addResourceType(self,resourceType):
        self.resourceTypes.append(resourceType)
    
    def getResourceTypes(self):
        return self.resourceTypes
    
    def getNombre(self):
        return self.nombre

class ResourceType:
    def __init__(self,name,scalarProperties,uniqueP,imgP,EstructuraXML,Instancias):
        self.scalarProperties = scalarProperties
        self.name = name
        #self.uniqueProperty = scalarProperties[uniqueP]
        #self.imgFileProperty = scalarProperties[imgP]
        self.XML = EstructuraXML
        self.Instancias = Instancias
        
    def getEstructuraXML(self):
        return self.XML
        
    def getInstancias(self):
        return self.Instancias


class ScalarProperty:
    #begin code translators
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
    
    def __init__(self,name,dataType,extractor, default=False):
        self.name = name
        self.dataType = dataType
        self.extractor = extractor
        self.default = default
        self.dataTypes = {"DataTypes.Boolean":self.__codeBoolean__,
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
        
    def extractData(self,idm):
        return self.extractor.extract(idm)

    def toCode(self,varName):
        return self.dataTypes[self.dataType](varName)

class EstructuraXML:
    def __init__(self,nodoXMLHijo,nodoXMLPadre,XMLPrefijo):
        self.hijo = nodoXMLHijo
        self.padre = nodoXMLPadre
        self.prefijo = XMLPrefijo
    
    def getNodoHijoXML(self):
        return self.hijo
    def getNodoPadreXML(self):
        return self.padre
    def getPrefijoXML(self):
        return self.prefijo
