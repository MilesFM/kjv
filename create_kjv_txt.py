# https://ebible.org/Scriptures/eng-kjv2006_readaloud.zip

import os
import re

output = "kjv.txt"

ignore_files = ["copr.htm", "eng-kjv2006_000_000_000_read.txt", "keys.asc", "signature.txt.asc", __file__.split("\\")[-1], output]

books = dict()

write_file = open(output, "w")

for filename in os.listdir(os.getcwd()):
    with open(os.path.join(os.getcwd(), filename), 'r') as read_file:
        if filename not in ignore_files:
            chapt_and_book_file = filename[16:-9]
            this_split = chapt_and_book_file.split("_")
            book_name = this_split[0].lower()

            file_lines = read_file.readlines(1)
            write_this_lol = re.sub(r'\W+', '', file_lines[0][1:])

            books[book_name] = write_this_lol


for key, value in books.items():
    write_file.write(key + "\t" + value + "\n")

for filename in os.listdir(os.getcwd()):
    with open(os.path.join(os.getcwd(), filename), 'r') as read_file:
        if filename not in ignore_files:
            chapt_and_book_file = filename[16:-9]
            this_split = chapt_and_book_file.split("_")
            book_name = this_split[0].lower()
            chapter_name = str(int(this_split[1]))

            file_lines = read_file.readlines()

            for i in range(2, len(file_lines)):
                this_line = file_lines[i]
                write_file.write(book_name + chapter_name + ":" + str(i - 1) + " " + this_line[:-2] + "\n")

write_file.close()
