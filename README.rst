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


Authors
-------

Hamza Khan (Undergraduate Summer Scholar visiting Beatson Microbial Genomics 
Group from VIT India) and Mitchell Stanton-Cook (BioIT specialist in Beatson 
Microbial Genomics Group)


Help listing
------------

Current listing::

    python seqfindr_d3js.py  -h
    usage: seqfindr_d3js.py [-h] [-v] SeqFindR_data_dir html_prefix

    SeqFindR-d3js v0.0.1 - SeqFindR like plot in D3.js (SeqFindR-d3js)

    positional arguments:
      SeqFindR_data_dir  Full path to SeqFindR data directory
      html_prefix        Name of the HTML file (appends .html to it)

    optional arguments:
      -h, --help         show this help message and exit
      -v, --verbose      verbose output

    Licence: ECL 2.0 by Hamza Khan & Mitchell Stanton-Cook
    <m.stantoncook@gmail.com>

