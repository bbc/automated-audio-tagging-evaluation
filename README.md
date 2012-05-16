Automated DBpedia tagging evaluation resources
==============================================

A set of resources to perform the evaluation reported in our [Automated interlinking of speech radio archives](http://events.linkeddata.org/ldow2012/papers/ldow2012-paper-11.pdf) paper.

Content
-------

* kiwi-evaluation.py : script to run the TopN evaluation described in our paper.
* data/editorial-tags : ground truth editorial tags on a dataset of 132 items from [BBC Programmes](http://www.bbc.co.uk/programmes).
* data/automated-tags : a set of automated tags derived by the framework described in our paper.
* data/automated-transcripts : a set of automated transcripts, generated using [CMU Sphinx](http://cmusphinx.sourceforge.net/), a HUB4 acoustic model and a Gigaword-derived language model.

Getting started
---------------

Running the evaluation with results from the automated tagging described in
our paper.

 $ python evaluation.py 

Licensing terms and authorship
------------------------------

See 'COPYING' and 'AUTHORS' files.
The license in 'COPYING' only applies to the Python code and the automated transcripts and tags.
The editorial data is under the same non-commercial license as the [BBC Programmes](http://www.bbc.co.uk/programmes) data.
