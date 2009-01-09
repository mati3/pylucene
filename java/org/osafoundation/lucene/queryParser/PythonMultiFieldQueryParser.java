/* ====================================================================
 *   Copyright (c) 2004-2008 Open Source Applications Foundation
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 * ====================================================================
 */

package org.osafoundation.lucene.queryParser;

import java.util.Vector;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.search.Query;
import org.apache.lucene.queryParser.MultiFieldQueryParser;
import org.apache.lucene.queryParser.ParseException;


public class PythonMultiFieldQueryParser extends MultiFieldQueryParser {

    private long pythonObject;

    public PythonMultiFieldQueryParser(String[] fields, Analyzer analyzer)
    {
        super(fields, analyzer);
    }

    public void pythonExtension(long pythonObject)
    {
        this.pythonObject = pythonObject;
    }
    public long pythonExtension()
    {
        return this.pythonObject;
    }

    public void finalize()
        throws Throwable
    {
        pythonDecRef();
    }

    public native void pythonDecRef();
    public native Query getBooleanQuery(Vector clauses);
    public native Query getFieldQuery(String field, String queryText);
    public native Query getFieldQuery(String field, String queryText, int slop);
    public native Query getFuzzyQuery(String field, String termText,
                                      float minSimilarity);
    public native Query getPrefixQuery(String field, String termText);
    public native Query getRangeQuery(String field,
                                      String part1, String part2,
                                      boolean inclusive);
    public native Query getWildcardQuery(String field, String termText);
}
