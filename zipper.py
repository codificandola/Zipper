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
#    Zipper V1.2

import os, tarfile, threading, timeit, subprocess, logging, gzip

work_dir ="/share/BACKUP/ayer/DB/PROD/"
dest_dir = work_dir

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
        logging.info("Starting " + self.name)
        compress(dest_dir, self.name, self.files)
        stop = timeit.default_timer()
        logging.info(self.name + " finished in  " + str(stop - start) + " seconds")




def compress(dest_dir, thread_name, files):
    for f in files:
        st = timeit.default_timer()
        tar = tarfile.open(dest_dir + f + ".gz", "w:gz", compresslevel=1)
        tar.add(f)
        tar.close()
        os.remove(f)


        fn = timeit.default_timer()
        logging.info("Compressing " + f + " in " + thread_name + " finished in " + str(fn - st) + " seconds\n" )


def main():
    logging.basicConfig(filename='zipper.log', level=logging.INFO)
    logging.info('Started Main')

    os.chdir(work_dir)
    allfiles = os.listdir(work_dir)
    # Parto String de archivos en 2

    files0 = allfiles[:len(allfiles) / 2]
    files1 = allfiles[len(allfiles) / 2:]

    thread0 = myThread(0, "Thread-0", files0)
    thread1 = myThread(1, "Thread-1", files1)

    thread0.start()
    thread1.start()


    logging.info('Finished Main')



if __name__ == "__main__":
   main()
