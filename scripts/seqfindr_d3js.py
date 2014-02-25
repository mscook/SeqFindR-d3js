#!/usr/bin/env python

# Copyright 2014 Hamza Khan & Mitchell Stanton-Cook Licensed under the
# Educational Community License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
#      http://www.osedu.org/licenses/ECL-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.

"""
Make interactive SeqFindR like plots.
"""

__title__        = 'SeqFindR-d3js'
__version__      = '0.0.1'
__description__  = "SeqFindR like plot in D3.js" 
__author__       = 'Hamza Khan & Mitchell Stanton-Cook'
__license__      = 'ECL 2.0'
__author_email__ = "m.stantoncook@gmail.com"
__url__         = 'SeqFindR-d3js'

epi = "Licence: %s by %s <%s>" % (__license__, 
                                  __author__,
                                  __author_email__)
__doc__ = " %s v%s - %s (%s)" % ( __title__, 
                                  __version__, 
                                  __description__, 
                                  __url__)

import sys, os, traceback, argparse
import time
import numpy as np
import csv


def core():
    exit()

    matrix=[]  
    reorder_row_matrix=[]  
    strain_labels=[]   
    vfs_list_xlabels=[]
    index_file=[]
    #Reading the values into matrices and lists                           
    with open('matrix.csv', 'rb') as m, open('extra_stuff/reorderedrowmatrix.txt', 'rb') as rrm,open('extra_stuff/strain_labels.txt', 'rb') as sl,open('extra_stuff/vfs_list_xlabels.txt', 'rb') as vfs, open('index.txt', 'rb') as index:   
      for row in rrm:
        reorder_row_matrix.append(row.strip('\n'))
      for row in sl:
        strain_labels.append(row.strip('\n'))
      for row in index:
         index_file.append(row.strip('\n'))
      for row in vfs:
        vfs_list_xlabels.append(row.strip('\n'))           
      reader = csv.reader(m)
      for row in reader:
          matrix.append(row)
    print "matrix-------------"
    print matrix      
    print "\nreorder_row_matrix------------"
    print reorder_row_matrix
    print "\n strain labels"
    print strain_labels
    print "\n vfs_xlabel"
    print vfs_list_xlabels  
    print "\n Index file"
    print index_file                            
    #making a dictionary of strain_labels and their index number.The present matrix is alteretered with its help.            
    dictionary={}
    for i in range(len(strain_labels)):
      dictionary[strain_labels[i]]=i;
    print "the index dictionary is\n"
    print dictionary
    #declaring new matrix and list for storing the altered data as per the input index file.
    new_matrix=[]  
    new_strain_labels=[] 
    #altering data as per the input index file
    for row in index_file:
     print row
     print dictionary[row]
     new_matrix.append(matrix[dictionary[row]])
     new_strain_labels.append(strain_labels[dictionary[row]])
    #print "new_matrix########################################"
    #print new_matrix

    trmatrix=[]
    trmatrix=zip(*new_matrix)
    trmatrix=zip(*trmatrix)
    trmatrix=np.array(trmatrix)
    print trmatrix[0][1] 
    print "transverse matrix-------------"
    print trmatrix  
    fo = open("data.js", "wb")
    fo.write( "var maxData=0.6000000000000000000;\nvar minData=-1.599999999999999944;\nvar data = [");
    for i in range(int(len(trmatrix))):
            fo.write("[");
            for j in range(int(len(trmatrix[i]))):
                fo.write("[");
                c=float(trmatrix[i][j])
                print c
                fo.write(str(c));
                fo.write(", ");
                fo.write(str(i));
                fo.write(", ");
                fo.write(str(j));
                if(j!=(int(len(trmatrix[i])-1))):
                   fo.write("], ");
                else:
                   fo.write("]")   
            if(i!=(int(len(trmatrix))-1)):
                fo.write("],");
            else:
                fo.write("]");    
    fo.write("];\n");
    fo.write("var cols = [");
    for a in range(int(len(vfs_list_xlabels))):
      fo.write("'");
      b = (vfs_list_xlabels[a]).translate(None, " '?.!/;:")
      fo.write(str(b));
      fo.write("'");
      if(a!=int(len(vfs_list_xlabels))-1):
        fo.write(", ");  
    fo.write("];\n");

    fo.write("var rows = [");
    for a in range(int(len(new_strain_labels))):
      fo.write("'");
      fo.write(str(new_strain_labels[a]));
      fo.write("'");
      if(a!=int(len(new_strain_labels))-1):
        fo.write(", ");  
    fo.write("];\n");









if __name__ == '__main__':
    try:
        start_time = time.time()
        
        parser = argparse.ArgumentParser(description=__doc__, epilog=epi)
        parser.add_argument('-v', '--verbose', action='store_true', 
                                default=False, help='verbose output')
        # Required options now positional arguments
        parser.add_argument('SeqFindR_data_dir', action='store', 
                                help='Full path to SeqFindR data directory ')
        parser.add_argument('html_prefix', action='store', 
                                help=('Name of the HTML file (appends .html'
                                    ' to it)'))
        parser.set_defaults(func=core)
        args = parser.parse_args()
        if args.verbose: 
            print "Executing @ " + time.asctime()
        args.func(args)
        if args.verbose:
            print "Ended @ " + time.asctime()
            print 'Exec time minutes %f:' % ((time.time() - start_time) / 60.0)
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
