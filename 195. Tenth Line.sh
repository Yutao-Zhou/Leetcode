# Read from the file file.txt and output the tenth line to stdout.
#!usr/bin/env bash
#### sed ####
# sed -n 10p file.txt

#### tail head ####
tail -n +10 file.txt|head -1