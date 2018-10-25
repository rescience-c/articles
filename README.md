### ReScience C published articles

In order to publish a new article (after acceptance), you'll need to have the
article metadata file (YAML format) and the corresponding article PDF. The
metadata file should be missing the article DOI, number and URL. The first step
is to request this information from Zenodo. Before proceeding further, you'll
need a Zenodo token that can be requested from the [sandbox
server](https://sandbox.zenodo.org/account/settings/applications/tokens/new/)
and from the [actual
server](https://zenodo.org/account/settings/applications/tokens/new/).  The
sandbox token is expected to be stored in the environment variable
`ZENODO_SANDBOX_TOKEN` while the true token must be stored in `ZENODO_TOKEN`.
**We strongly advise you to first test the procedure on the sandbox server**


#### Pre-Publication (article DOI, URL and number)

You can run the [process.py](process.py) script using the provided metadata
file. In the example below, we use the actual server but you can first test the
procedure on the sandbox server by using the `--sandbox` switch.

```bash
$ ./process.py --zenodo --metadata metadata.yaml --pdf article.pdf
Article #: y
Article ID: xxxxx
Article DOI: 10.5281/zenodo.xxxxx
Article URL: https://zenodo.org/record/xxxxxx/file/article.pdf
```

You need to give this information back to author(s) such that they can update
the metadata file as well as the article that display the DOI in the left
margin (make sure they actually update this information).


#### Publication (Zenodo and GitHub)

In order to publish the final article, you'll need to run the
[publish.py](publish.py) script:

```bash
$ ./publish.py --zenodo --metadata metadata.yaml --pdf article.pdf
Uploading content... done!
Uploading metadata... done!
Publishing... done!
Entry is online at https://zenodo.org/record/xxxxx
```

This will create a new public record on Zenodo and this will also create a new
local directory corresponding to the entry. This means you need to push your
changes on GitHub and make a pull request (the commit will have been created
automatically).


#### Website update

To have the new article to appear on the website, you'll need to generate the
bibtex entry using the [yaml-to-bibtex.py](yaml-to-bibtex.py) script and to add
this entry to the
[published.bib](https://github.com/rescience-c/rescience-c.github.io/blob/sources/_bibliography/published.bib)
file on the website (you can do it directly from the GitHub interface).

If you previously added the entry to the
[under_review.bib](https://github.com/rescience-c/rescience-c.github.io/blob/sources/_bibliography/under_review.bib) file, don't forget to remove it.


