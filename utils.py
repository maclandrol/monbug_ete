#!/usr/bin/env python

# Create a conversion between leaf names and real names
code2name = {
        "Dre":"Drosophila melanogaster",
        "Hsa":"Homo sapiens",
        "Cfa":"Canis familiaris"
        }

# Creates a dictionary with the descriptions of each leaf name
code2desc = {
        "Dre":"""The zebrafish, also known as Danio rerio,
is a tropical freshwater fish belonging to the
minnow family (Cyprinidae).""",
        "Dme":"""True flies are insects of the order Diptera,
possessing a single pair of wings on the
mesothorax and a pair of halteres, derived from
the hind wings, on the metathorax""",
        "Hsa":"""A human is a member of a species
of bipedal primates in the family Hominidae.""",
        "Ptr":"""Chimpanzee, sometimes colloquially
chimp, is the common name for the
two extant species of ape in the genus Pan.""",
        "Mms":"""A mouse is a small mammal belonging to the
order of rodents.""",
        "Cfa": """The dog (Canis lupus familiaris) is a
domesticated subspecies of the Gray Wolf,
a member of the Canidae family of the
orderCarnivora."""
        }

def get_description(node):
    return code2desc[node.name.split('_')[0]]

def get_scientific_name(node):
    return code2name[node.name.split('_')[0]]
    
def get_image(name):
    img_path = "./"
    if name.startswith('Dre'):
        return img_path+"fly.png"
    elif name.startswith('Hsa'):
        return img_path+"human.png"
    else :
        return img_path+"dog.png"