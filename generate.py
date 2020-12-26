import os, sys
import base64
import json

database = {}


for root, dirs, files in os.walk("ansi", topdown=False):
   for name in files:
      if name[0] != '.':
         f=open(os.path.join(root, name), "rb")
         data = base64.encodestring(f.read().replace("Downloaded From P-80 International Information Systems 304-744-2253", ""))
         database[name]=data.split("\n")
         #print( base64.b64decode(data) )



print( "var jsondata = %s ;" % json.dumps(database, indent=4, sort_keys=True) )

