import countTokens
from TitleExtractor import TitleExtractor
from DescriptionExtractor import DescriptionExtractor
from ImageIdExtractor import ImageIdExtractor
import sys
from DateAddedExtractor import DateAddedExtractor
from DateModifiedExtractor import DateModifiedExtractor
from UriExtractor import UriExtractor
from RegionExtractor import RegionExtractor
from CityExtractor import CityExtractor
from ResourceType import ResourceType
from ScalarProperty import ScalarProperty
from FrequentTagExtractor import FrequentTagExtractor
from TagExtractor import TagExtractor
from MostImportantLatentTopicExtractor import MostImportantLatentTopicExtractor
from LatentTopicExtractor import LatentTopicExtractor
from sets import Set
from os.path import join

from LatentTopicGenerator import LatentTopicGenerator

class Resources:

    def setFreqTags(self):
        freqTags= []
        for tuple in self.FrequentTags:
           freqTags.append(tuple[1])       
        return freqTags           
    def buildImageResourceType(self):
        properties = []
        properties.append(ScalarProperty("ImageId","DataTypes.Decimal",ImageIdExtractor()))
        properties.append(ScalarProperty("Title","DataTypes.String",TitleExtractor(),True))
        properties.append(ScalarProperty("Description","DataTypes.String",DescriptionExtractor(),True))
        properties.append(ScalarProperty("Date_Added","DataTypes.DateTime",DateAddedExtractor()))
        properties.append(ScalarProperty("Date_Modified","DataTypes.DateTime",DateModifiedExtractor()))
        properties.append(ScalarProperty("Uri","DataTypes.String",UriExtractor(),True))
        #properties.append(ScalarProperty("Region","DataTypes.String",RegionExtractor()))
        #properties.append(ScalarProperty("City","DataTypes.String",CityExtractor()))    	
        

        #One FacetCategory for each latentTopic, and one Facet Category called Latent topic ()
        LTGen = LatentTopicGenerator(join(self.path,'data'))
        LT = LTGen.getLatentTopics()
        properties.append(ScalarProperty("MFLatentTopics","DataTypes.String",MostImportantLatentTopicExtractor(LT, self.path)))

        for Lt in LT:
            sp =ScalarProperty("LT_" + Lt.name,"DataTypes.Double",LatentTopicExtractor(Lt))
            properties.append(sp)
            mostImportantTag = Lt.name.spli("_")[0]
            contained = False
            for tag in self.FrequentTags:
                if tag == mostImportantTag:
                    contained = True
                    break
            if (not contained):
                #Add to the Frequent Tags the most important tag for each latent topic
                self.FrequentTags.append(Lt.name.split("_")[0])


        properties.append(ScalarProperty("FrequentTag","DataTypes.String",FrequentTagExtractor(Set(self.setFreqTags()))))
        #One FacetCategory for each latentTopic, and one Facet Category called Latent topic ()

        for tuple in self.FrequentTags:
            sp =ScalarProperty("Tag_" + tuple[1],"DataTypes.Boolean",TagExtractor(tuple[1]))
            properties.append(sp)
        
        return ResourceType("ImageResource",properties,0,0, "ZXMLprefix")

    def build(self):
        arrResourcesType = []
        arrResourcesType.append(self.buildImageResourceType())
        return arrResourcesType
    

    def __init__(self,path):
        self.FrequentTags = countTokens.countTokens(join(path,'data','tokens.txt'))
        
        self.path = path
