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
# Zipper V1.0

import os, tarfile, threading, timeit

work_dir = "/home/ancifuentes/Documents/Bacula/pdf/"
dest_dir = "/home/ancifuentes/Documents/Bacula/test/"

# work_dir="/home/ancifuentes/Documents/wars_tomcat5_20150318/"
# dest_dir= "/home/ancifuentes/Documents/wars_comprimidos/"

ext = ".gz"
files = []


class myThread(threading.Thread):
    def __init__(self, threadID, name, files):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.files = files

    def run(self):
        start = timeit.default_timer()
        print "Starting " + self.name

        compress(dest_dir, self.name, self.files)

        stop = timeit.default_timer()
        print self.name + " ha terminado en  " + str(stop - start) + " segundos"


# print "Exiting " + self.name


def compress(dest_dir, thread_name, files):
    for f in files:
        tar = tarfile.open(dest_dir + f + ".gz", "w:gz")
        print "Compressing " + f + " in " + thread_name + "\n"
        tar.add(f)
        tar.close()


os.chdir(work_dir)
allfiles = os.listdir(work_dir)
# Parto String de archivos en 2
files1 = allfiles[:len(allfiles) / 2]
files2 = allfiles[len(allfiles) / 2:]

thread1 = myThread(1, "Thread-1", files1)
thread2 = myThread(2, "Thread-2", files2)
thread1.start()
thread2.start()
