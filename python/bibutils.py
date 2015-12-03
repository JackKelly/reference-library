from __future__ import print_function, division
import bibtexparser
import codecs

BIB_FILENAME = '../library.bib'


def load_bib(filename=BIB_FILENAME):
    parser = bibtexparser.bparser.BibTexParser()
    parser.ignore_nonstandard_types = False
    parser.homogenise_fields = False
    parser.encoding = 'utf8'

    with codecs.open(filename, mode='r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    return bib_database


def write_bib(database, filename=BIB_FILENAME):
    writer = bibtexparser.bwriter.BibTexWriter()
    bibtex_str = writer.write(database)
    bibtex_str = bibtex_str.encode('utf-8')
    with open(filename, mode='w') as bibtex_file:
        bibtex_file.write(bibtex_str)
