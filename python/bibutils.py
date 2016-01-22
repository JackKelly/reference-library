from __future__ import print_function, division
import bibtexparser
from bibtexparser.customization import convert_to_unicode
import codecs

BIB_FILENAME = '../library.bib'


def load_bib(filename=BIB_FILENAME, stringio=None):
    parser = bibtexparser.bparser.BibTexParser()
    parser.ignore_nonstandard_types = False
    parser.homogenise_fields = False
    parser.customization = convert_to_unicode  # convert latex escape code (like `\'{e}`) to UTF8
    parser.encoding = 'utf8'

    if stringio:
        bib_database = bibtexparser.load(stringio, parser=parser)
    else:
        with codecs.open(filename, mode='r', encoding='utf-8') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file, parser=parser)

    return bib_database


def write_bib(database, filename=BIB_FILENAME):
    writer = bibtexparser.bwriter.BibTexWriter()
    bibtex_str = writer.write(database)
    bibtex_str = bibtex_str.encode('utf-8')
    with open(filename, mode='w') as bibtex_file:
        bibtex_file.write(bibtex_str)
