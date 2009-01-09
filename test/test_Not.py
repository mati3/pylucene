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


class NotTestCase(TestCase):
    """
    Unit tests ported from Java Lucene
    """
  
    def testNot(self):

        store = RAMDirectory()
        writer = IndexWriter(store, SimpleAnalyzer(), True)

        d1 = Document()
        d1.add(Field("field", "a b", Field.Store.YES, Field.Index.TOKENIZED))

        writer.addDocument(d1)
        writer.optimize()
        writer.close()

        searcher = IndexSearcher(store)
        query = QueryParser("field", SimpleAnalyzer()).parse("a NOT b")

        hits = searcher.search(query)
        self.assertEqual(0, hits.length())


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
