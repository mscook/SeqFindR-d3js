SeqFindR-d3js
=============

**Under heavy development.**

This is an example. Takes a SeqFindR data in JSON format and provides a useful
interactive SeqFindR plot.

Usage
-----

You'll need to clone & install the development branch of SeqFindR as it 
generates the required data for SeqFindR-d3js. The intention is to merger this 
code into the master SeqFindR branch once we have fully tested it.

Then something like this::

    $  python scripts/seqfindr_d3js.py SeqFindR_data_dir output_html_prefix

    i.e.

    $ python scripts/seqfindr_d3js.py data ST131

    will produce:

    ST131.html, d3.v2.js  & data.js

    Load ST131.html into a web browser and enjoy

