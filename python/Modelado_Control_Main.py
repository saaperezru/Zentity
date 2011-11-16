from InterfazZ_Entidad import DataModelModule
from InterfazZ_Entidad import ResourceType
from InterfazZ_Entidad import ScalarProperty
from InterfazZ_Entidad import EstructuraXML
from InterfazNMF_Control import TypeLatentTopicGenerator
from InterfazNMF_Control import ImageMatrix
from InterfazNMF_Control import LTvsLT as VS
from Modelado_Vista_extractMatlabMatrix import MatlabExtract
from Modelado_Entidad_Matriz import Matriz
from os.path import join
from numpy import *
from Modelado_Entidad import DescriptionExtractor
from Modelado_Entidad import  ImageIdExtractor
from Modelado_Entidad import LatentTopicExtractor
from Modelado_Entidad import MostImportantLatentTopicExtractor
from Modelado_Entidad import TagExtractor
from Modelado_Entidad import TitleExtractor
from InterfazZ_Control import GeneradorXML
from InterfazZ_Control import GeneradorInsercion 
from InterfazZ_Control import GeneradorCreacion 
import Image




pat = "E:\\Renata"


LTGenerator = TypeLatentTopicGenerator()

Tt = join(pat,"data","textual","Tt_iter_634.mat")
H = join(pat,"data","textual","H_iter_634.mat")
ListaDocumentos = join(pat,"imgIdsTraining.mat")

textual = LTGenerator.createTypeLatentTopic(1,"Latent Topics textual", "LTT", ListaDocumentos,5,Tt,H)


extMatlab = MatlabExtract(join(pat,"data","visual"))
Tt = extMatlab.getTtMatrix("Tt_iter_1.mat")
H = extMatlab.getHMatrix("H_iter_1.mat")


visual = LTGenerator.createTypeLatentTopic(2,"Latent Topics Visuales", "LTV", ListaDocumentos,5,Tt,H)

comparisonMatrixCreator = VS()
M = comparisonMatrixCreator.createLTvsLT(ListaDocumentos,textual,visual)

IP=ImageMatrix()
IP.imagePrint(20,join(pat,"imagetmp.png"),M,M.shape[0],M.shape[1],0,0)

##TArray = textual.ArrayLatentTopics[:]
##VArray = visual.ArrayLatentTopics[:]
##Errores=[]
##minimo=float("inf")
##minimoi=0
##for i in xrange(0,100,10):
##        path=join(pat,"image"+str(i)+".png")
##        MF=calculateMF(M,5,i,path,textual,visual,ListaDocumentos)
##        MF=abs(MF-(ones(MF.shape)*len(ListaDocumentos)/(MF.shape[0]*MF.shape[1])))
##        MF = MF*MF
##        MF=dot(ones((1,MF.shape[0])),MF)
##        MF=dot(MF,ones((MF.shape[1],1)))
##        Errores.append(MF)
##        if MF< minimo:
##                minimo=MF
##                minimoi=i
##        visual.ArrayLatentTopics = VArray[:]
##        textual.ArrayLatentTopics = TArray[:]
##        print i


#textual,visual,MF=calculateMF(ListaDocumentos,textual,visual,0)


SL,S1,S2=comparisonMatrixCreator.LTSelection(ListaDocumentos,textual,visual,21)
SLD=[]
for data in LD:
        i=LT1.getMostImportantLatentTopic(data)
        j=LT2.getMostImportantLatentTopic(data)
        for pair in SL:
                if pair==(i,j):
                        SLD.append(data)


#Textual matrix for tag extractor

Xt = genfromtxt(join(pat,"features","text","index_bf.txt"))
tmp = open(join(pat,"features","text","tokens_bf.txt"))
columnas = []
for line in tmp:
	columnas.append(line.split(",")[0])

Xt = Matriz(ListaDocumentos,columnas,Xt)

######Generacin modelo

###Frequent Tags

freqTags = columnas[0:9]
freqTags = set(freqTags)



##Scalar properties
properties=[]
properties.append(ScalarProperty("Title","DataTypes.String",TitleExtractor(pat),True))
properties.append(ScalarProperty("ImageId","DataTypes.String",ImageIdExtractor()))
properties.append(ScalarProperty("Description","DataTypes.String",DescriptionExtractor(pat),True))




#One FacetCategory for each latentTopic, and one Facet Category called Latent topic ()
##Textual
properties.append(ScalarProperty("MFTLatentTopics","DataTypes.String",MostImportantLatentTopicExtractor(textual)))
for i in S1:
        LT=textual.ArrayLatentTopics[i]
        #Add facet category for this LT
        properties.append(ScalarProperty(textual.abreviature+str(LT.id)+"_" + LT.name.replace("/","___").replace("-","__"),"DataTypes.Double",LatentTopicExtractor(LT)))
        #Add words in name to set of tags
        for word in LT.name.split("_"):
                freqTags.add(word)

##Visual
properties.append(ScalarProperty("MFVLatentTopics","DataTypes.String",MostImportantLatentTopicExtractor(visual)))
for i in S2:
        LT=visual.ArrayLatentTopics[i]
        #Add facet category for this LT
        properties.append(ScalarProperty(visual.abreviature+str(LT.id)+"_" + LT.name.replace("/","___").replace("-","__"),"DataTypes.Double",LatentTopicExtractor(LT)))
        #Add words in name to set of tags
        for word in LT.name.split("_"):
                freqTags.add(word)


#One facet category for every tag

for t in freqTags:
            sp = ScalarProperty("Tag_" + t,"DataTypes.Boolean",TagExtractor(t,Xt))
            properties.append(sp)
            

##Resource Types

DataModel = DataModelModule("RENATA5")

XML = EstructuraXML("image","images","ZXML")

DataModel.addResourceType(ResourceType("ImagenRenata5",properties,0,0,XML,ListaDocumentos))

GC = GeneradorCreacion(DataModel)
GC.save(pat)

GI = GeneradorInsercion(DataModel)
GI.save(pat)

GX = GeneradorXML(join(pat,"ZXML"))
GX.save(DataModel,500)

