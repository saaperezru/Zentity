from xml.etree.ElementTree import parse,Element
def chargeXML(filename):
    file = open(filename, "r")
    tree = parse(file)
    return tree.getroot()
