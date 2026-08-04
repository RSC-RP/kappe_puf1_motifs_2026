#! /usr/bin/env python3

# Script to read in orthologs from a JSON downloaded from VEuPathDb, then
# generate fasta sequences of those orthologs.

import json
import os
import requests

def extract_orthologs(file, genus, syntenic_only = False):
    """
    Given a JSON file from VEuPathDb, extract and filter the orthologs, and
    return a list of transcript IDs.
    """
    with open(file, mode = 'rt') as incon:
        myjson = json.load(incon)
    out = set()
    for rec in myjson['records']:
        ortho = rec['tables']['Orthologs']
        if syntenic_only:
            ortho = [o for o in ortho if o['is_syntenic'] == 'yes']
        ortho = [o for o in ortho if o['organism'].startswith(f"{genus} ")]
        out |= set([f"{o['ortho_gene_source_id']},{o['ortho_source_id']}" for o in ortho])
    return out

def download_fasta(txpt, db = "https://plasmodb.org/plasmo", db2 = "PlasmoDB"):
    """
    Given a VEuPathDb transcript ID, download the protein FASTA.
    """
    payload = {
        'searchConfig': {'parameters': {'primaryKeys': f"{txpt},{db2}"}},
        'reportConfig': {
            "attributes": [
                "primary_key",
                "organism",
                "protein_sequence"
            ],
            "tables": [],
            "attributeFormat": "text"
        }
        }
    url = f"{db}/service/record-types/transcript/searches/single_record_question_TranscriptRecordClasses_TranscriptRecordClass/reports/standard"
    r = requests.post(url, json = payload)
    myjson = json.loads(r.text)
    att = myjson['records'][0]['attributes']
    header = f">{att['primary_key']}|{att['organism']}\n"
    seq = f"{att['protein_sequence']}\n"
    return [header, seq]

#mylines = download_fasta('HEP_00251300,HEP_00251300_t1')

if __name__ == '__main__':
    import sys
    orthojson = sys.argv[1]
    outfile = sys.argv[2]
    db1 = sys.argv[3]
    db2 = sys.argv[4]
    genus = sys.argv[5]

    txpts = extract_orthologs(orthojson, genus)
    with open(outfile, mode = 'wt') as outcon:
        for txpt in txpts:
            mylines = download_fasta(txpt, db = db1, db2 = db2)
            outcon.writelines(mylines)
    sys.exit(0)

