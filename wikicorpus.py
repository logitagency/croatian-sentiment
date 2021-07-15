#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from gensim.corpora import WikiCorpus

def next_fname(output_dir, num=0):
    """Get the next filename to use for writing new articles."""
    count = 0
    fname = output_dir + '/' + '{:>07d}'.format(num) + '.txt'
    return count, (num+1), fname

def make_corpus(input_file, output_dir, size=10000):
    """Convert Wikipedia xml dump file to text corpus"""
    wiki = WikiCorpus(input_file)
    count, num, fname = next_fname(output_dir)
    output = open(fname, 'w')

    # iterate over texts and store them
    for text in wiki.get_texts():
        output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
        count += 1
        if (count == size):
            print('%s Done.' % fname)
            output.close()
            count, num, fname = next_fname(output_dir, num)
            output = open(fname, 'w')

    # clean up resources
    output.close()
    print('Completed.')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python wikicorpus.py <wikipedia_dump_file> <destination_directory> <file_size>')
        sys.exit(1)
    print(sys.argv)
    input_file      = sys.argv[1]
    outupt_dir = sys.argv[2]
    file_size  = sys.argv[3] if len(sys.argv) > 3 else None
    make_corpus(input_file, outupt_dir)