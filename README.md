### Jack Kelly's Bibliography Database

`library.bib` is in UTF8
[`BibLaTeX`](https://www.ctan.org/pkg/biblatex?lang=en) format, _not_
`bibtex` format.  `BibLaTeX` can be considered the successor to `bibtex`.

`keywords.txt` lists most of the `keywords` that I use to categorise
entries.  The list in `keywords.txt` is not exhaustive.

The `*.ipynb` files are IPython Notebook scripts that I have used for
processing my `.bib` files using the excellent [`bibtexparser` package](http://bibtexparser.readthedocs.org).

#### Conventions

##### `title` capitalisation

I try to use the capitalisation scheme used in the PDF version of the
paper.  Note that BibLaTeX respects the capitalisation in the `title`
field without having to use double curly brackets (which bibtex
requires).  Note also that some publishers use different
capitalisation schemes in the HTML version (or database entries) and
PDF versions of papers.  Hence why I try to use the capitalisation
used in the PDF version.

##### `booktitle` for conferences

Perhaps slightly controversially, I remove the `In Proceedings` and
just leave the name of the conference.  I also convert, say, 'second
conference in...' to '2nd conference in...'.  I'm tempted to use
superscripts...

##### `series`

For conferences, I use `series` for the standard acronym for the
conference (without any numbers).  e.g. `booktitle={25th International
Conference on Machine Learning}, series={ICML}`.  This usage is a
little unusual and perhaps I should instead do `booktitle={25th International
Conference on Machine Learning (ICML)}`.

##### `author`

I try to use the full author names.


##### `DOI` versus `URL`

If a paper has a `DOI` which resolves to an open access PDF then, in
general, I won't include a `URL` or `eprint`.
