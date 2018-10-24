#! /usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright 2018 ReScience C - BSD two-clauses licence
#
# This script takes reserve a DOI on zenodo
# Zenodo REST API at http://developers.zenodo.org
# -----------------------------------------------------------------------------
import json
import requests

def reserve_doi(server, token):
    """ Reserve a new DOI on Zenodo """
    
    headers = { "Content-Type": "application/json" }
    url = 'https://%s/api/deposit/depositions' % server
    response = requests.post(url, params={'access_token': token},
                             json={}, headers=headers)
    if response.status_code != 201:
        raise IOError("%s: " % response.status_code +
                      response.json()["message"])
    data = response.json() 
    return data["id"], data["metadata"]["prereserve_doi"]["doi"]



# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import os
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='DOI pre-reservation on Zenodo')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--sandbox', action='store_true',
                       help='Use the sandbox server')
    group.add_argument('--zenodo',  action='store_true',
                       help='Use the production server')
    args = parser.parse_args()


    if args.sandbox:
        server     = "sandbox.zenodo.org"
        token_name = "ZENODO_SANDBOX_TOKEN"
    else:
        server     = "zenodo.org"
        token_name = "ZENODO_TOKEN"
        
    token = os.getenv(token_name)
    if token is None:
        url = "".format(server)
        print("No token found ({0})".format(token_name))
        print("You can request one from https://{0}/account/settings/applications/tokens/new/".format(server))
        sys.exit(0)

    # Get  necessary
    print("Request for a new DOI from https://{0}... ".format(server), end="")
    article_id, article_doi = reserve_doi(server, token)
    print("done!")
    print("Article ID: ", article_id)
    print("Article DOI:", article_doi)
