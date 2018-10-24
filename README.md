### ReScience C published articles

In order to publish a new article (after acceptance), you'll need the article
metadata file (YAML format) with all information filled but the actual article
DOI. You'll also need a Zenodo token that you can request from the [sandbox
server](https://sandbox.zenodo.org/account/settings/applications/tokens/new/)
or from the
[actual server](https://zenodo.org/account/settings/applications/tokens/new/).
The sandbox token is expected to be stored in the environment variable
`ZENODO_SANDBOX_TOKEN` while the true token must be stored in `ZENODO_TOKEN`.

The actual publication is a two steps process because you need to reserve a DOI
from Zenodo and a new article number and to communicate them to the author in
order for her to update the PDF and the metadata with the relevant DOI and
article number. Once this is done (and that you have the updated PDF and the
full metadata file), you can actual publish the article on both Zenodo and
Github.


#### Reserve a DOI from Zenodo

You can run the [reserve-doi.py](reserve-doi.py) script using the provided
metadata file. In the example below, we use the actual server but you can first
test the procedure on the sandbox server by using the `--sandbox` switch.

```bash
$ ./reserve-doi.py --zenodo
Request for a new DOI from https://zenodo.org... done!
Article ID:  xxxxx
Article DOI: 10.5281/zenodo.xxxxx

Request for a new article number... done!
Article No:  x
```

#### Reserve a DOI from Zenodo

To get a new article number, you can run the script
[reserve-number.py](reserve-number.py) that will return the next available
article number by parsing the [volumes.yaml](volumes.yaml) file. You will need
to use the `--update` flag to update this file.

```bash
$ ./reserve-number.py --volume x --update
Request for a new article number for volume x
Article No:  x
"volumes.yaml" has been updated, don't forget to commit the change
```

After getting thr article number, make sure to commit and push the change on
the `volumes.yaml` file such that next article number is right.


#### Publishing on Zenodo

Once the DOI and article number has been obtained and both the metadata and the
PDF **have been updated** (author responsability), you can procced with the
actual publication on Zenodo:

```bash
$ ./publish.py --zenodo --metadata metadata.yaml --pdf article.pdf
Uploading content... done!
Uploading metadata... done!
Publishing... done!
Entry is online at https://zenodo.org/record/xxxxx
```


#### Uploading to GitHub
