'''
Created on Aug 28, 2009
Unit tests for OBO2OWL converter.
@author: ed
'''
import unittest
from OBOparser import *
from OBO2OWLConverter import *
from TestCases import *

class Test(unittest.TestCase):
    """
    Class to test OBOparser and converter functionality.
    """
    url ="http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/amphibian/amphibian_anatomy.obo"
    parser = OBOparser()
    badUrl ="http://chemoinformatician.co.uk"
    
    def testUrlSet(self):
        """
        Test to see if the url of the obo file is set correctly.
        """
        Test.parser.setUrl(Test.url)
        self.assertEqual(Test.parser.url,Test.url)
    
    def testOBOUrl(self):
        """
        Test to see if an exception is raised on handling urls without .obo extension.
        """
        Test.parser.setUrl(Test.badUrl)
        self.assertRaises(IOError,Test.parser.readFile) 
       
    def testNodeClassBasicMutation(self):
        """
        Tests basic mutation methods for node class.
        """ 
        node = Node()
        #Test alternative id.
        node.altId = "AlternativeIdValue"
        self.assertEqual(node.altId, node.getAlternativeId())
        #Test broad synonym
        node.broadSynonym = "BroadSynonym"
        self.assertEqual(node.broadSynonym, node.getBroadSynonym())
        #Test comment
        node.comment = "Comment"
        self.assertEqual(node.comment, node.getComment())
        #Test definition
        node.definition = "Definition"
        self.assertEqual(node.definition, node.getDefinition())
        #Test disjoint from
        node.disjointFrom = "AnotherClass"
        self.assertEqual(node.disjointFrom, node.getAllDisjoint())
        #Test exact synonym
        node.exactSynonym = "ExactSynonym"
        self.assertEqual(node.exactSynonym, node.getExactSynonym())
        #Test id 
        node.id = "Id"
        self.assertEqual(node.id, node.getId())
        #Test intersection of
        node.intersectionOf = "IntersectionOf"
        self.assertEqual(node.intersectionOf, node.getAllIntersectionsOf())
        #Test isA
        node.isA = "AnElephant"
        self.assertEqual(node.isA, node.getIsA())
        #Test isObsolete
        node.isObsolete = "Deprecated"
        self.assertEqual(node.isObsolete, node.getIsObsolete())
        #Test name
        node.name = "Name"
        self.assertEqual(node.name, node.getName())
        #Test narrow synonym
        node.narrowSynonym = "NarrowSynonym"
        self.assertEqual(node.narrowSynonym, node.getNarrowSynonym())
        #Test property value
        node.propertyValue = "PropertyValue"
        self.assertEqual(node.propertyValue, node.getPropertyValue())
        #Test related synonym
        node.related_synonym = "RelatedSynonym"
        self.assertEqual(node.related_synonym, node.getAllRelatedSynonyms())
        #Test relationship
        node.relationship = "PartOf"
        self.assertEqual(node.relationship, node.getRelationship())
        #Test subsets
        node.subset = "Subset"
        self.assertEqual(node.subset, node.getAllSubsets())
        #Test synonyms
        node.synonym = "Synonym"
        self.assertEqual(node.synonym, node.getAllSynonyms())
        #Test xrefs
        node.xref = "SomeCrossReference"
        self.assertEqual(node.xref, node.getAllXrefs())
        #Test xref analog
        node.xrefAnalog =  "XrefAnalog"
        self.assertEqual(node.xrefAnalog, node.getXrefAnalog())
        
    def testTypeDefNode(self):
        """
        Tests additional methods associated with typeDef node.
        """
        aTypeDefNode = TypeDefNode()
        #Test isCyclic
        aTypeDefNode.isCyclic = "true"
        self.assertEqual(aTypeDefNode.isCyclic, aTypeDefNode.getIsCyclic())
        #Test isTransitive
        aTypeDefNode.isTransitive = "false"
        self.assertEqual(aTypeDefNode.isTransitive, aTypeDefNode.getIsTransitive())
    
    def testOBOOntology(self):
        """
        Tests OBO ontology getter setter methods.
        """
        ontology = Ontology()
        #Test adding a header line
        self.assertEqual(len(ontology.metaData),0)
        newHeaderLine = "Extra header information"
        ontology.addMetaData(newHeaderLine)
        self.assertEqual(len(ontology.metaData),1)
        self.assertEqual(len(ontology.metaData),len(ontology.getAllMetaData()))
        self.assertEqual(newHeaderLine,ontology.getAMetaDataInstance(0))
        #Test adding a term
        self.assertEqual(len(ontology.terms),0)
        newTerm = Node()
        ontology.addTerm(newTerm)
        self.assertEqual(len(ontology.terms),1)
        self.assertEqual(len(ontology.terms),ontology.getNumTerms())
        self.assertEqual(newTerm,ontology.getTerm(0))
        #Test adding a typeDef term
        self.assertEqual(len(ontology.typeDefs),0)
        newTypeDef = TypeDefNode()
        ontology.addTypeDef(newTypeDef)
        self.assertEqual(len(ontology.typeDefs),1)
        self.assertEqual(len(ontology.typeDefs),ontology.getNumTypeDefTerms())
        self.assertEqual(newTypeDef,ontology.getTypeDefTerm(0))
    
    def testConstantHeaderClassConverters(self):
        """
        Method tests the OBO to OWL converter methods for the header.
        """
        header = ConstantHeader()
        #Test convert auto generated by.
        header.convertAutoGeneratedBy("OBO-Edit 1.101")
        self.assertEqual("<mo:autoGenerationBy>OBO-Edit 1.101</mo:autoGeneratedBy>",header.autoGenerated)
        #Test convert data version.
        header.convertDataVersion("1.0")
        self.assertEqual("<mo:dataVersion>1.0</mo:dataVersion>",header.dataVersion)
        #Test convert date.
        header.convertDate("18:06:2008 13:34")
        self.assertEqual("<mo:savedDateTime>18:06:2008 13:34</mo:savedDateTime>",header.date)
        #Test convert format version.
        header.convertFormatVersion("1.2")
        self.assertEqual("<mo:formatVersion>1.2</mo:formatVersion>",header.format)
        #Test name space.
        header.convertNameSpace("ProteinNS")
        self.assertEqual("<mo:defaultNamespace>ProteinNS</mo:defaultNamespace>",header.ns)
        header.convertNameSpaceId("AnId")
        self.assertEqual("<mo:namespace-id-rule>AnId</mo:namespace-id-rule>",header.nsIdRule)
        #Test remark.
        header.convertRemark("remark")
        self.assertEqual("<mo:remark>remark</mo:remark>",header.remark)
        #Test saved by.
        header.convertSavedBy("Ed Cannon")
        self.assertEqual("<mo:savedBy>Ed Cannon</mo:savedBy>",header.savedBy)
        #Test subsetDef.
        header.convertSubsetDef("Subset0")
        self.assertEqual("<mo:definedSubset rdf:resource=\"#Subset0\"/>",header.subsetDef)
        #Test typeRef.
        typeRefs = []
        typeRefs.append("TypeRef0")
        typeRefs.append("TypeRef1")
        header.convertTypeRefs(typeRefs)
        self.assertEqual("<owl:imports>TypeRef0</owl:imports>",header.owlImports[0])
        
    def testConvertTerm(self):
        """
        Method tests the OBO term to OWL class converter.
        """
        aTerm = ConvertTerm()
        #Test convert alternative Id.
        aTerm.convertAlternativeId("AnAlternativeId")
        self.assertEqual("<mo:alternateID>AnAlternativeId</mo:alternateID>",aTerm.altId)
        #Test broad synonym.
        broadSynonyms = []
        broadSynonyms.append("BroadSynonym0")
        broadSynonyms.append("BroadSynonym1")
        aTerm.convertBroadSynonyms(broadSynonyms)
        self.assertEqual("<mo:broadSynonym>BroadSynonym0</mo:broadSynonym>",aTerm.broad_synonym[0]) 
        #Test exact synonym.
        exactSynonyms = []
        exactSynonyms.append("ExactSynonym0")
        exactSynonyms.append("ExactSynonym1")
        aTerm.convertExactSynonyms(exactSynonyms)
        self.assertEqual("<mo:exactSynonym>ExactSynonym0</mo:exactSynonym>",aTerm.exact_synonym[0]) 
        #Test isA.
        aTerm.convertIsARelationships("nameSpace", "Human")
        self.assertEqual("<rdfs:subClassOf rdf:resource=\"nameSpace#Human\"/>",aTerm.isA)
        #Test narrow synonym.
        narrowSynonyms = []
        narrowSynonyms.append("NarrowSynonym0")
        narrowSynonyms.append("NarrowSynonym1")
        aTerm.convertNarrowSynonyms(narrowSynonyms)
        self.assertEqual("<mo:narrowSynonym>NarrowSynonym0</mo:narrowSynonym>",aTerm.narrow_synonym[0])
        #Test related synonyms.
        relatedSynonyms = []
        relatedSynonyms.append("RelatedSynonym0")
        relatedSynonyms.append("RelatedSynonym1")
        aTerm.convertRelatedSynonyms(relatedSynonyms)
        self.assertEqual("<mo:relatedSynonym>RelatedSynonym0</mo:relatedSynonym>",aTerm.related_synonym[0])
        #Test relationship.
        expected = "<rdfs:subClassOf>"+"\n"+"<owl:Restriction>"+"\n"+"<owl:onProperty rdf:resource =\"urn:obo-res#part_of\"/>"+"\n"+"<owl:someValuesFrom rdf:resource = \"urn:obo-res#AAO:0000320\"/>"+"\n"+"</owl:Restriction>\n</rdfs:subClassOf>"
        aTerm.convertRelationshipTag("part_of AAO:0000320 ! nasal_skeleton") 
        self.assertEqual(expected,aTerm.relationship)
        #Test subset.
        subsetList = []
        subsetList.append("Subset0")
        aTerm.convertSubset(subsetList)
        self.assertEqual("<mo:inSubset rdf:resource=\"#"+"Subset0"+"\"/>",aTerm.subset[0])
        #Test synonyms.
        synonyms = []
        synonyms.append("Synonym0")
        synonyms.append("Synonym1")
        aTerm.convertSynonyms(synonyms)
        self.assertEqual("<mo:synonym>"+"Synonym0"+"</mo:synonym>",aTerm.synonym[0])
        #Test cross references.
        xrefs = []
        xrefs.append("Cross Ref 0")
        xrefs.append("Cross Ref 1")
        aTerm.convertXref(xrefs)
        self.assertEqual("<mo:xref>"+"Cross Ref 0"+"</mo:xref>",aTerm.xref[0])
        #Test xrefAnalog.
        xrefAnalog = []
        xrefAnalog.append("XrefAnalog0")
        xrefAnalog.append("XrefAnalog1")
        aTerm.convertXrefAnalog(xrefAnalog)
        self.assertEqual("<mo:xrefAnalogous>"+"XrefAnalog0"+"</mo:xrefAnalogous>",aTerm.xrefAnalog[0])
        #Test set comment. 
        aTerm.setComment("This is an important comment.")
        self.assertEqual("<rdfs:comment xml:lang=\"en\">This is an important comment.</rdfs:comment>",aTerm.comment)
        #Test set definition
        aTerm.setDefinition("Python (mythology) serpent, the earth-dragon of Delphi")
        self.assertEqual("<mo:definition>Python (mythology) serpent, the earth-dragon of Delphi</mo:definition>",aTerm.definition)
        #Test set name
        aTerm.setName("Ed")
        self.assertEqual("<rdfs:label xml:lang=\"en\">Ed</rdfs:label>",aTerm.name)
        #Test set term Id
        aTerm.setTermId("AtermId", "OBO", "false")
        self.assertEqual("<owl:Class rdf:about=\"OBO#AtermId\">",aTerm.termId)
        #Test deprecated
        aTerm.setTermId("AtermId", "OBO", "true")
        self.assertEqual("<owl:DeprecatedClass rdf:about=\"OBO#AtermId\">",aTerm.termId)
    
    def testConvertTypeDef(self):
        """
        Method tests the OBO typDef to OWL property converter.
        """
        aProperty = ConvertTypeDef()
        #Test domain.
        aProperty.convertDomain("Rivers")
        self.assertEqual("<rdfs:domain rdf: resources = \"Rivers\"/>",aProperty.domain)
        #Test isA
        aProperty.convertIsA("bone")
        self.assertEqual("<rdfs:subPropertyOf rdf:resource=\"bone\"/>",aProperty.isA)
        #Test is cyclic.
        aProperty.convertIsCyclic("true")
        self.assertEqual("<mo:isCyclic>true</mo:isCyclic>",aProperty.isCyclic)
        #Test is symmetric.
        aProperty.convertIsSymmetric("false")
        self.assertEqual("<mo:isSymmetric>false</mo:isSymmetric>",aProperty.isSymmetric)
        #Test is transitive.
        aProperty.convertIsTransitive("true")
        self.assertEqual("<mo:isTransitive>true</mo:isTransitive>",aProperty.isTransitive)
        #Test name.
        aProperty.convertName("Name")
        self.assertEqual("<mo:name>Name</mo:name>",aProperty.name)
        #Test range.
        aProperty.convertRange("Range")
        self.assertEqual("<rdfs:range rdf:resource = \"Range\"/>",aProperty.range)
        #Test typeDef.
        aProperty.convertTypeDefTitle("id", "false")
        self.assertEqual("<owl:ObjectProperty rdf:about=\"#id\">", aProperty.typeDef)
        aProperty.convertTypeDefTitle("id", "true")
        self.assertEqual("<owl:DeprecatedProperty rdf:about=\"#id\">",aProperty.typeDef)
        
    def testOWLOntology(self):
        """
        Methods to test the OWL ontology class.
        """
        owlOntology = OWLOntology()
        #Test adding header information.
        owlOntology.addHeaderInformation("An additional header: some info")
        self.assertEqual(len(owlOntology.getAllHeaderInformation()),1)
        #Test create new owlClass.
        aNewClass = Node()
        owlOntology.addOWLClass(aNewClass)
        self.assertEqual(len(owlOntology.getAllOWLClasses()),1)
        #Test add property.
        aNewProperty = TypeDefNode()
        owlOntology.addOWLProperty(aNewProperty)
        self.assertEqual(len(owlOntology.getAllProperties()),1)
        #Test add subset.
        owlOntology.addSubset("some value")
        self.assertEqual(len(owlOntology.subsetDef),1)
        #Test setting subset definition.
        owlOntology.addSubsetDefinition("subset definition")
        self.assertEqual("subset definition",owlOntology.getIndividualSubset(0))
        #Test autogenerated by.
        owlOntology.setAutoGeneratedBy("OBO-Edit 2")
        self.assertEqual("OBO-Edit 2",owlOntology.getAutoGeneratedBy())
        #Test get Date.
        owlOntology.setDate("21:05:2009")
        self.assertEqual("21:05:2009",owlOntology.getDate())
        #Test get default name space.
        owlOntology.setDefaultNameSpace("DefaultNameSpace")
        self.assertEqual("DefaultNameSpace",owlOntology.getDefaultNameSpace())
        #Test get format version.
        owlOntology.setFormatVersion("1.2")
        self.assertEqual("1.2",owlOntology.getFormatVersion())
        #Test 
        owlOntology.setNameSpaceIdRule("Name space")
        self.assertEqual("Name space",owlOntology.nsIdRule)
        #Test remark.
        owlOntology.setRemark("Some remark")
        self.assertEqual("Some remark",owlOntology.getRemark())
        #Test saved by.
        owlOntology.setSavedBy("Ed Cannon")
        self.assertEqual("Ed Cannon",owlOntology.getSavedBy())
        #Test type ref.
        owlOntology.setTypeRef("A value")
        self.assertEqual("A value",owlOntology.getTypeRef())
        #Test version.
        owlOntology.setVersion("VersionX")
        self.assertEqual("VersionX",owlOntology.getVersion())
    
    def testConvertOBO2OWL(self):
        """
        Tests conversion from OBO to OWL format for all OBO ontologies hosted at:
        http://www.obofoundry.org/
        """
        aConverter = ConvertOBO2OWL("http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/amphibian/amphibian_anatomy.obo")
        aConverter.convertOBO2OWL("amphibian_anatomy.owl")
        aConverter.uri = "http://ontology1.srv.mst.edu/sarah/amphibian_taxonomy.obo"
        aConverter.convertOBO2OWL("amphibian_taxonomy.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/ascomycete_phenotype.obo"
        aConverter.convertOBO2OWL("ascomycete_phenotype.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/genomic-proteomic/gene_ontology_edit.obo"
        aConverter.convertOBO2OWL("gene_ontology_edit.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/developmental/animal_development/worm/worm_development.obo"
        aConverter.convertOBO2OWL("worm_development.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/worm/worm_anatomy/WBbt.obo"
        aConverter.convertOBO2OWL("WBbt.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/worm_phenotype.obo"
        aConverter.convertOBO2OWL("worm_phenotype.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/cell_type/cell.obo"
        aConverter.convertOBO2OWL("cell.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/genomic-proteomic/gene_ontology_edit.obo"
        aConverter.convertOBO2OWL("gene_ontology_edit1.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/plant_traits/plant_trait.obo"
        aConverter.convertOBO2OWL("plant_trait.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/chemical/chebi.obo"
        aConverter.convertOBO2OWL("chebi.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/caro/caro.obo"
        aConverter.convertOBO2OWL("caro.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/microbial_gross_anatomy/dictyostelium/dictyostelium_anatomy.obo"
        aConverter.convertOBO2OWL("dictyostelium_anatomy.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/developmental/animal_development/fly/fly_development.obo"
        aConverter.convertOBO2OWL("fly_development.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/fly/fly_anatomy.obo"
        aConverter.convertOBO2OWL("fly_anatomy.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/environmental/envo.obo"
        aConverter.convertOBO2OWL("envo.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/evidence_code.obo"
        aConverter.convertOBO2OWL("evidence_code.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/taxonomy/fly_taxonomy.obo"
        aConverter.convertOBO2OWL("fly_taxonomy.owl")
        aConverter.uri = "http://obo.svn.sourceforge.net/viewvc/*checkout*/obo/fma-conversion/trunk/fma2_obo.obo"
        aConverter.convertOBO2OWL("fma2_obo.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/microbial_gross_anatomy/fungi/fungal_anatomy.obo"
        aConverter.convertOBO2OWL("fungal_anatomy.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/human/human-dev-anat-abstract.obo"
        aConverter.convertOBO2OWL("human-dev-anat-abstract.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/human/human-dev-anat-staged.obo"
        aConverter.convertOBO2OWL("human-dev-anat-staged.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/human_disease.obo"
        aConverter.convertOBO2OWL("human_disease.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/infectious_disease.obo"
        aConverter.convertOBO2OWL("infectious_disease.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/mammalian_phenotype.obo"
        aConverter.convertOBO2OWL("mammalian_phenotype.owl")
        aConverter.uri = "http://psidev.cvs.sourceforge.net/*checkout*/psidev/psi/psi-ms/mzML/controlledVocabulary/psi-ms.obo"
        aConverter.convertOBO2OWL("psi-ms.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/fish/medaka_ontology.obo"
        aConverter.convertOBO2OWL("medaka_ontology.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/genomic-proteomic/gene_ontology_edit.obo"
        aConverter.convertOBO2OWL("gene_ontology_edit2.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/mosquito_anatomy.obo"
        aConverter.convertOBO2OWL("mosquito_anatomy.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/mosquito_insecticide_resistance.obo"
        aConverter.convertOBO2OWL("mosquito_insecticide_resistance.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/mouse/adult_mouse_anatomy.obo"
        aConverter.convertOBO2OWL("adult_mouse_anatomy.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/mouse/EMAP.obo"
        aConverter.convertOBO2OWL("EMAP.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/mouse_pathology/mouse_pathology.obo"
        aConverter.convertOBO2OWL("mouse_pathology.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/OBO_REL/ro.obo"
        aConverter.convertOBO2OWL("ro.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/transmission_process.obo"
        aConverter.convertOBO2OWL("transmission_process.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/quality.obo"
        aConverter.convertOBO2OWL("quality.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/developmental/plant_development/plant/po_temporal.obo"
        aConverter.convertOBO2OWL("po_temporal.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/plant_gross_anatomy/plant/po_anatomy.obo"
        aConverter.convertOBO2OWL("po_anatomy.owl")
        aConverter.uri = "http://psidev.sourceforge.net/mod/data/PSI-MOD.obo"
        aConverter.convertOBO2OWL("PSI-MOD.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/genomic-proteomic/pro.obo"
        aConverter.convertOBO2OWL("pro.owl")
        aConverter.uri = "http://psidev.cvs.sourceforge.net/viewvc/*checkout*/psidev/psi/mi/rel25/data/psi-mi25.obo"
        aConverter.convertOBO2OWL("psi-mi25.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/genomic-proteomic/so.obo"
        aConverter.convertOBO2OWL("so.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/caro/spatial.obo"
        aConverter.convertOBO2OWL("spatial.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/spider/spider_comparative_biology.obo"
        aConverter.convertOBO2OWL("spider_comparative_biology.owl")
        aConverter.uri = "http://www.ebi.ac.uk/sbo/exports/Main/SBO_OBO.obo"
        aConverter.convertOBO2OWL("SBO.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/fish/teleost_anatomy.obo"
        aConverter.convertOBO2OWL("teleost_anatomy.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/taxonomy/teleost_taxonomy.obo"
        aConverter.convertOBO2OWL("teleost_taxonomy.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/tick_anatomy.obo"
        aConverter.convertOBO2OWL("tick_anatomy.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/unit.obo"
        aConverter.convertOBO2OWL("unit.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/frog/xenopus_anatomy.obo"
        aConverter.convertOBO2OWL("xenopus_anatomy.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/fish/zebrafish_anatomy.obo"
        aConverter.convertOBO2OWL("zebrafish_anatomy")
        aConverter.uri = "http://4dx.embl.de/4DXpress_4d/edocs/bilateria_mrca.obo"
        aConverter.convertOBO2OWL("bilateria_mrca.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/experimental_conditions/imaging_methods/image.obo"
        aConverter.convertOBO2OWL("image.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/cell_type/DC-CL_deployed.obo"
        aConverter.convertOBO2OWL("DC-CL_deployed")
        aConverter.uri = "http://www.inoh.org/ontologies/EventOntology.obo"
        aConverter.convertOBO2OWL("EventOntology.owl")
        aConverter.uri = "http://bgee.unil.ch/download/homology_ontology.obo"
        aConverter.convertOBO2OWL("homology_ontology.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/human_phenotype.obo"
        aConverter.convertOBO2OWL("human_phenotype.owl")
        aConverter.uri = "http://obo.svn.sourceforge.net/viewvc/obo/ontologies/trunk/HAO/hao.obo"
        aConverter.convertOBO2OWL("hao.owl")
        aConverter.uri = "http://anobase.vectorbase.org/idomal/IDOMAL.obo"
        aConverter.convertOBO2OWL("IDOMAL.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/gross_anatomy/animal_gross_anatomy/multispecies/minimal_anatomical_terminology.obo"
        aConverter.convertOBO2OWL("minimal_anatomical_terminology.owl")
        aConverter.uri = "http://www.inoh.org/ontologies/MoleculeRoleOntology.obo"
        aConverter.convertOBO2OWL("MoleculeRoleOntology.owl")
        aConverter.uri = "ftp://rgd.mcw.edu/pub/data_release/pathway.obo"
        aConverter.convertOBO2OWL("pathway.owl")
        aConverter.uri = "http://www.ebi.ac.uk/~kirill/FIX/fix.obo"
        aConverter.convertOBO2OWL("fix.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/physicochemical/rex.obo"
        aConverter.convertOBO2OWL("rex.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/phenotype/environment/environment_ontology.obo"
        aConverter.convertOBO2OWL("environment_ontology.owl")
        aConverter.uri = "https://psidev.svn.sourceforge.net/svnroot/psidev/psi/sepcv/trunk/sep.obo"
        aConverter.convertOBO2OWL("sep.owl")
        aConverter.uri = "http://gemina.cvs.sourceforge.net/*checkout*/gemina/Gemina/ontologies/gemina_symptom.obo"
        aConverter.convertOBO2OWL("gemina_symptom.owl")
        aConverter.uri = "http://obo.cvs.sourceforge.net/*checkout*/obo/obo/ontology/anatomy/anatomy_xp/uberon.obo"
        aConverter.convertOBO2OWL("uberon.owl")        
              
if __name__ == "__main__":
    unittest.main()