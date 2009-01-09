
import os, sys, unittest, lucene
lucene.initVM(lucene.CLASSPATH)

baseDir = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(baseDir)

import lia.advsearching.MultiFieldQueryParserTest
from lucene import System

System.setProperty("index.dir", os.path.join(baseDir, 'index'))
unittest.main(lia.advsearching.MultiFieldQueryParserTest)
