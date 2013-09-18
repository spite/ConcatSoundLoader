#!/usr/bin/python

import sys
import os
import struct

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
for grp in sys.argv[1:]:
  b = os.path.getsize( grp )
  sys.stdout.write( struct.pack( 'I', b ) )
  f = open( grp, 'r' )
  sys.stdout.write( f.read() )
