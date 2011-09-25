class ResourceType:
    def __init__(self,name,scalarProperties,uniqueP,imgP,ZXMLPrefix):
        self.scalarProperties = scalarProperties
        self.name = name
        self.uniqueProperty = scalarProperties[uniqueP]
        self.imgFileProperty = scalarProperties[imgP]
        self.ZXMLPrefix = ZXMLPrefix
