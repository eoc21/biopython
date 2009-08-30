'''
Created on Aug 15, 2009
Class to process and OBO file from the World Wide Web.
@author: ed
'''
import urllib2
import sys

class OBOparser():
    """
    A class representing an OBO parser.
    """
    def __init__(self):
        """
        Constructs an OBOparser.
        """
        pass
    
    def setUrl(self,aUrl):
        """
        Set the url of the OBO file to parse.
        Keyword arguments:
        aUrl -- the url where the OBO file resides.
        """
        self.url = aUrl
    
    def readFile(self):
        """
        Reads file from the internet into a list object.
        """
        fileAndExtension = str(self.url).split(".")
        if fileAndExtension[len(fileAndExtension)-1] != "obo":
            raise IOError("Url does not have .obo extension!")
        else:
            oboFileHandle = urllib2.urlopen(self.url)
            self.oboFile = oboFileHandle.readlines()
            return self.oboFile
    
    def createOntologyFromOBOFile(self,datafile):
        """
        Create an ontology of terms (nodes) from a uri / file.
        Keyword arguments:
        datafile -- OBO file object.
        """
        termPresent = False
        typeDefPresent = False
        counter = 0
        term = []
        typeDefTerm = []
        ontology = Ontology()
        for i in range(len(datafile)):
            aline = str(datafile[i]).strip()
            #add meta data to ontology
            if counter == 0:
                ontology.addMetaData(aline)
            if aline == "[Term]":
                termPresent = True
            if aline == "" and typeDefPresent == False :
                termPresent = False
                if counter>0:
                    #add node object iteration here before you empty the list
                    node = Node()
                    for j in range(len(term)):
                        termSplitUp = str(term[j]).split(": ")
                        if termSplitUp[0] == "id":
                            node.id = termSplitUp[1]
                        if termSplitUp[0] == "name":
                            node.name = termSplitUp[1]
                        if termSplitUp[0] == "def":
                            node.definition = termSplitUp[1]
                        if termSplitUp[0] == "relationship":
                            node.relationship = termSplitUp[1]
                        if termSplitUp[0] == "is_a":
                            values = str(termSplitUp[1]).split(" !")
                            #node.isA = termSplitUp[1]
                            node.isA = values[0]
                        if termSplitUp[0] == "related_synonym":
                            node.related_synonym.append(termSplitUp[1])
                        if termSplitUp[0] == "synonym":
                            node.synonym.append(termSplitUp[1])
                        if termSplitUp[0] == "exact_synonym":
                            node.exactSynonym = termSplitUp[1]
                        if termSplitUp[0] == "broad_synonym":
                            node.broadSynonym = termSplitUp[1]
                        if termSplitUp[0] == "narrow_synonym":
                            node.narrowSynonym = termSplitUp[1]
                        if termSplitUp[0] == "xref_analog":
                            node.xrefAnalog = termSplitUp[1]
                        if termSplitUp[0] == "comment":
                            node.comment = termSplitUp[1]
                        if termSplitUp[0] == "is_obsolete":
                            node.isObsolete = termSplitUp[1]
                        if termSplitUp[0] == "alt_id":
                            node.altId = termSplitUp[1]
                        if termSplitUp[0] == "disjoint_from":
                            node.disjointFrom.append(termSplitUp[1])
                        if termSplitUp[0] == "subset":
                            node.subset.append(termSplitUp[1])
                        if termSplitUp[0] == "intersection_of":
                            node.intersectionOf.append(termSplitUp[1])
                        if termSplitUp[0] == "xref":
                            node.xref.append(termSplitUp[1])
                        if termSplitUp[0] == "property_value":
                            node.propertyValue = str(termSplitUp[1])
                    ontology.addTerm(node)
                    term = []
                counter = counter+1
            if termPresent == True:
                term.append(aline)
            elif aline == "[Typedef]":
                typeDefPresent = True

            if typeDefPresent == True:
                typeDefTerm.append(aline)
                typeDefPresent = False
            if aline == "" and termPresent == False and typeDefPresent == True:
                typeDefPresent == False
                typeDefNode = TypeDefNode()
                for j in range(len(typeDefTerm)):
                   if j>0:
                       typeDefTermSplitUp = str(typeDefTerm[j]).split(": ")
                       if typeDefTermSplitUp[0] == "id":
                           typeDefNode.id = typeDefTermSplitUp[1]
                       if typeDefTermSplitUp[0] == "name":
                           typeDefNode.name = typeDefTermSplitUp[1]
                       if typeDefTermSplitUp[0] == "is_transitive":
                           typeDefNode.isTransitive = typeDefTermSplitUp[1]
                       if typeDefTermSplitUp[0] == "is_cyclic":
                           typeDefNode.isCyclic = typeDefTermSplitUp[1]
                ontology.addTypeDef(typeDefNode)
                typeDefTerm = []  
        return ontology

class Node():
    """
    A class representing a node in an OBO ontology.
    """
    def __init__(self):
        """
        Constructs a node in an OBOOntology to store term information.
        """
        self.id = ""
        self.name = ""
        self.definition = ""
        self.relationship = ""
        self.related_synonym = []
        self.isA = ""
        self.synonym = []
        self.exactSynonym = ""
        self.broadSynonym = ""
        self.narrowSynonym = ""
        self.xrefAnalog = ""
        self.comment = ""
        self.isObsolete = ""
        self.altId = ""
        self.disjointFrom = []
        self.subset = []
        self.intersectionOf = []
        self.xref = []
        self.propertyValue = ""
        
    def getId(self):
        """
        Returns id of this node.
        """
        return self.id
    
    def getName(self):
        """
        Returns name of this node.
        """
        return self.name
    
    def getDefinition(self):
        """
        Returns the definition of this node.
        """
        return self.definition
    
    def getRelationship(self):
        """
        Returns the relationship of this node.
        """
        return self.relationship
    
    def getIsA(self):
        """
        Returns the is_A relationship.
        """
        return self.isA
    
    def getRelatedSynonym(self,i):
        """
        Return specific synonym.
        Keyword arguments:
        i -- index to select.
        """
        return self.related_synonym[i]
    
    def getAllRelatedSynonyms(self):
        """
        Returns all the related synonyms.
        """
        return self.related_synonym
    
    def getSynonym(self,i):
        """
        Return synonym.
        Keyword arguments:
        i -- index to select.
        """
        return self.synonym[i]
    
    def getAllSynonyms(self):
        """
        Return all synonyms.
        """
        return self.synonym
    
    def getExactSynonym(self):
        """
        Return exact synonym.
        """
        return self.exactSynonym

    def getBroadSynonym(self):
        """
        Return broad synonym.
        """
        return self.broadSynonym
    
    def getNarrowSynonym(self):
        """
        Return narrow synonym.
        """
        return self.narrowSynonym
    
    def getXrefAnalog(self):
        """
        Return xref analog.
        """
        return self.xrefAnalog
    
    def getComment(self):
        """
        Returns comment.
        """
        return self.comment
    
    def getIsObsolete(self):
        """
        Returns if node is obsolete.
        """
        return self.isObsolete
    
    def getAlternativeId(self):
        """
        Returns alternative id.
        """
        return self.altId

    def getDisjointFrom(self,i):
        """
        Return specific disjoint.
        Keyword arguments:
        i -- index to select.
        """
        return self.disjointFrom[i]
    
    def getAllDisjoint(self):
        """
        Returns all the disjoints.
        """
        return self.disjointFrom
    
    def getSubset(self,i):
        """
        Return specific subset.
        Keyword arguments:
        i -- index to select.
        """
        return self.subset[i]
    
    def getAllSubsets(self):
        """
        Returns all the subsets.
        """
        return self.subset
    
    def getIntersectionOf(self,i):
        """
        Return specific intersection.
        Keyword arguments:
        i -- index to select.
        """
        return self.intersectionOf[i]
    
    def getAllIntersectionsOf(self):
        """
        Returns all the intersections.
        """
        return self.intersectionOf
    
    def getXref(self,i):
        """
        Return specific cross reference.
        Keyword arguments:
        i -- index to select.
        """
        return self.xref[i]
    
    def getAllXrefs(self):
        """
        Returns all the xrefs.
        """
        return self.xref
    
    def getPropertyValue(self):
        """
        Return property value.
        """
        return self.propertyValue
        
class TypeDefNode(Node):
    """
    A class representing a typeDef node in an OBO ontology.
    """
    def __init__(self):
        """
        Instantiates a node of typeDef.
        """
        self.isTransitive = ""
        self.isCyclic = ""
        self.id = ""
        self.name = ""
        self.definition = ""
        self.relationship = ""
        self.related_synonym = []
        self.isA = ""
        self.synonym = []
        self.exactSynonym = ""
        self.broadSynonym = ""
        self.narrowSynonym = ""
        self.xrefAnalog = ""
        self.comment = ""
        self.isObsolete = ""
        self.altId = ""
        self.disjointFrom = []
        self.subset = []
        self.intersectionOf = []
        self.xref = []
        self.propertyValue = ""
    
    def getIsTransitive(self):
        """
        Return if the node is transitive.
        """
        return self.isTransitive
    
    def getIsCyclic(self):
        """
        Returns if the node is cyclic.
        """
        return self.isCyclic

class Ontology():
    """
    A class to represent an OBO ontology.
    """
    def __init__(self):
        """
        Creates an instance of an ontology from an OBO file.
        """
        self.terms = []
        self.typeDefs = []
        self.metaData = []
        
    def addTerm(self,newTerm):
        """
        Adds a new OBO term to the ontology.
        Keyword arguments:
        newTerm -- a new OBO term to be added to the OBO ontology.
        """
        self.terms.append(newTerm)
    
    def addTypeDef(self,typeDef):
        """
        Adds a typedef term.
        Keyword arguments:
        typeDef -- a new typedef term to be added to the OBO ontology.
        """
        self.typeDefs.append(typeDef)
        
    def getAllMetaData(self):
        """
        Returns all meta data.
        """
        return self.metaData
    
    def addMetaData(self,data):
        """
        Adds meta data.
        Keyword arguments:
        data -- line of information to be added to the header.
        """
        self.metaData.append(data)
        
    def getAMetaDataInstance(self,i):
        """
        Returns a meta data instance.
        Keyword arguments:
        i -- index to select.
        """
        return self.metaData[i]
    
    def getTerm(self,i):
        """
        Returns the node given a specific index.
        Keyword arguments:
        i -- index to select.
        """
        return self.terms[i]
    
    def getTypeDefTerm(self,i):
        """
        Return specific typeDef term.
        Keyword arguments:
        i -- index to select.
        """
        return self.typeDefs[i]
    
    def getNumTypeDefTerms(self):
        """
        Returns the number of typeDef nodes in the ontology.
        """
        return len(self.typeDefs)
    
    def getNumTerms(self):
        """
        Returns the number of nodes in the ontology.
        """
        return len(self.terms)
    
    def addTypeDef(self,typeDef):
        """
        Add type definition to the ontology.
        """
        self.typeDefs.append(typeDef)
