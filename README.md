Automated DBpedia tagging evaluation resources
==============================================

A set of resources to perform the evaluation reported in our [Automated interlinking of speech radio archives](http://events.linkeddata.org/ldow2012/papers/ldow2012-paper-11.pdf) paper.

Content
-------

* kiwi-evaluation.py : script to run the TopN evaluation described in our paper.
* data/editorial-data : ground truth editorial data on a dataset of 132 items from [BBC Programmes](http://www.bbc.co.uk/programmes).
* data/automated-tags : a set of automated tags derived by the framework described in our paper.
* data/automated-transcripts : a set of automated transcripts, generated using [CMU Sphinx](http://cmusphinx.sourceforge.net/), a HUB4 acoustic model and a Gigaword-derived language model.

Data format
-----------

### Editorial data

The data was crawled from [BBC Programmes](http://www.bbc.co.uk/programmes) on the 16th of May, 2012.
Each file is named according to the following pattern: barcode\_pid.json, where the barcode is used
as an identifier across our different datasets, and the pid is the identifier of that programme on the
BBC web site. For example, X0903717\_p002h45s.json can be found [here](http://www.bbc.co.uk/programmes/p002h45s).
This data holds the editorial tags we are evaluating against.

### Automated tags

Each barcode.json holds the automatically derived tags for the programme identified by the barcode.
The JSON has the following shape:

> \[ \{ "score": score, "link": DBpedia URI \}, ... \]

This array is ordered by score descending.

### Automated transcripts

Each sub-directory corresponds to a single programme, which barcode is the name of the directory.
Within each sub-directory, there is one JSON file for a 2 minutes chunk of the programme. For
example transcript-0.json will hold the automated transcript for the first chunk and transcript-1.json
will hold the automated transcript for the second chunk.

The JSON has the following shape:

> \[ "full transcript", \[ \[ term, start, end, score 1, score 2 \], ... \]

Start and end are in seconds and score 1 and 2 respectively captures the acoustic model score
and the language model score.

Getting started
---------------

Running the evaluation with results from the automated tagging described in
our paper.

> $ python evaluation.py 

Evaluating your own algorithm
-----------------------------

1. Fork this repository.
2. Generate JSON files for your automated tags according to the format described above.
3. Replace the content of the data/automated-tags directory with your tags.
4. Run the evaluation script.

Licensing terms and authorship
------------------------------

See 'COPYING' and 'AUTHORS' files.
The license in 'COPYING' only applies to the Python code and the automated transcripts and tags.
The editorial data is under the same [non-commercial license](http://backstage.bbc.co.uk/archives/2005/01/terms_of_use.html)
as the [BBC Programmes](http://www.bbc.co.uk/programmes) data.
