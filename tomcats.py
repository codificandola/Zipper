#!/usr/bin/env python

#    Copyright (C) 2015  Andres Cifuentes
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    tomcats V1.0

##################
# Variables


import sys,getopt,threading,subprocess,time

def help():
    msg="\n tomcats.py - Manejo de multiples sesiones de Tomcat. \n\n" \
    "Uso:\n tomcats [options] \n\n" \
        "-h --help        Muestra esta ayuda.\n" \
        "-s [instancia]   Arranca solo la instancia especificada \n" \
        "--startall       Para todas las instancias \n" \
        "-k [instancia]   Para solo la instancia especificada \n" \
        "--stopall        Para todas las instancias\n\n"
    print(msg)

class myThread(threading.Thread):
    def __init__(self, threadID, service, command):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.service = service
        self.command = command

    def run(self):
        subprocess.call(["service", self.service, self.command])


def start(arg):
    services = open('tomcats','r')
    threadid =0
    if not arg:
        for line in services:
            thread = myThread(threadid, line.rstrip('\n'), "start")
            thread.start()
            threadid = threadid + 1
    else:
            thread = myThread(1, arg, "start")
            thread.start()

def stop(arg):
    services = open('tomcats','r')
    if not arg:
        for line in services:
            subprocess.call(["service", line.rstrip('\n') , "stop"])
    else:
            subprocess.call(["service",arg,"stop"])



def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hs:k:",["help","startall","stopall"])
   except getopt.GetoptError:
      print "Error"
      sys.exit(2)
   for op, arg in opts:
      if op in ("-h", "--help"):
         help()
         sys.exit()
      elif op in ("-s", "--startall"):
         start(arg)
      elif op in ("-k", "--stopall"):
         stop(arg)



if __name__ == "__main__":
   main(sys.argv[1:])
