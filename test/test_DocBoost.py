# ====================================================================
#   Copyright (c) 2004-2008 Open Source Applications Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ====================================================================

from unittest import TestCase, main
from lucene import *


class DocBoostTestCase(TestCase):
    """
    Unit tests ported from Java Lucene
    """
  
    def testDocBoost(self):

        store = RAMDirectory()
        writer = IndexWriter(store, SimpleAnalyzer(), True)
    
        f1 = Field("field", "word", Field.Store.YES, Field.Index.TOKENIZED)
        f2 = Field("field", "word", Field.Store.YES, Field.Index.TOKENIZED)
        f2.setBoost(2.0)
    
        d1 = Document()
        d2 = Document()
        d3 = Document()
        d4 = Document()
        d3.setBoost(3.0)
        d4.setBoost(2.0)
    
        d1.add(f1)                                 # boost = 1
        d2.add(f2)                                 # boost = 2
        d3.add(f1)                                 # boost = 3
        d4.add(f2)                                 # boost = 4
    
        writer.addDocument(d1)
        writer.addDocument(d2)
        writer.addDocument(d3)
        writer.addDocument(d4)
        writer.optimize()
        writer.close()

        scores = [0.0] * 4

        class hitCollector(PythonHitCollector):
            def collect(self, doc, score):
                scores[doc] = score

        IndexSearcher(store).search(TermQuery(Term("field", "word")),
                                    hitCollector())
    
        lastScore = 0.0
        for score in scores:
            self.assert_(score > lastScore)
            lastScore = score


if __name__ == "__main__":
    import sys, lucene
    lucene.initVM(lucene.CLASSPATH)
    if '-loop' in sys.argv:
        sys.argv.remove('-loop')
        while True:
            try:
                main()
            except:
                pass
    else:
         main()
