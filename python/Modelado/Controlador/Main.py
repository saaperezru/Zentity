from ResourcesArray import Resources
from DataModelCreator import DataModelCreator
import XMLGenerator
from DataInsertCodeGenerator import DataInsertCodeGenerator
def main():
	path = "C:\\colombia"
	namespace = "Zentity.Flickr"
	xmlParentName = "Images"
	xmlChildName = "Image"
	RA = Resources(path)
	a = RA.build()
	print "[DEBUG] Building Resources Array"
	DMC = DataModelCreator()
	DMC.generate(a,namespace,path)
	print "[DEBUG] Generating Data Model Creator Code"	
	XMLGenerator.extractInfo(path,a[0],xmlParentName,xmlChildName,500)
	print "[DEBUG] Generating ZXML Files"	
	DICG = DataInsertCodeGenerator()
	DICG.generate(a,namespace,path,xmlParentName,xmlChildName)
	print "[DEBUG] Generating Data Insertion Code"
	
if __name__=="__main__":
	main()
