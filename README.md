### Jack Kelly's Bibliography Database

`library.bib` is in UTF8
[`BibLaTeX`](https://www.ctan.org/pkg/biblatex?lang=en) format, _not_
`bibtex` format.  `BibLaTeX` can be considered the successor to `bibtex`.

`keywords.txt` lists most of the `keywords` that I use to categorise
entries.  The list in `keywords.txt` is not exhaustive.

The `*.ipynb` files are IPython Notebook scripts that I have used for
processing my `.bib` files using the excellent [`bibtexparser` package](http://bibtexparser.readthedocs.org).

Please feel free to re-use any of this content.  Also, please do
submit an issue or a pull request if you find any errors!!

### Subjects

* Energy disaggregation (aka NILM, NIALM, NALM)
* Behavioural / psychological studies surrounding NILM
* Climate science
* Climate change legislation
* Machine learning, especially deep learning
* Neuroscience

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


##### `publisher`

I extract the publisher from the conference title and put it into the
`publisher` field.  e.g. I do:

```
booktitle = {2nd International Conference on Embedded Systems for
Energy-Efficient Built Environments},
publisher = {ACM},
series = {BuildSys},
location = {Seoul, South Korea}
```

##### `author`

I try to use the full author names.


##### `DOI` versus `URL`

If a paper has a `DOI` which resolves to an open access PDF then, in
general, I won't include a `URL` or `eprint`.


##### Additional fields

* `dataset` is a single string or a comma separated list of strings of
  the short name of the dataset(s) used.  e.g. `dataset = {UK-DALE,
  REDD}`
* `sampleperiod` is the sample period of the aggregate data in
seconds. Alternatively, use:
*  `samplefrequency` is the sample frequency in Hz of the aggregate data.


##### UTF8

I try to use UTF8 characters instead of ugly LaTeX accent codes.
e.g. I prefer `Bergés` over `Berg\'{e}s`.


### Converting from biblatex to bibtex

I haven't tried this yet but some things that you'd definitely need to
change:

* rename the field `journaltitle` to `journal`
* biblatex uses the `date` field in preference to the `year` and
  `month` field, and date ranges are specified like
  `2015-01-15/2015-01-20`.  I'm not sure if bibtex will be happy with
  that.
* wrap titles in double curly brackets to preserve capitalisation.
* I expect that, for conferences, the contents of the `publisher` and
  `series` fields will need to be moved into the `booktitle` field.
