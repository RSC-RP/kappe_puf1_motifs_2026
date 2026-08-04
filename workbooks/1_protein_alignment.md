# Alignment of PUF1 proteins from different species

## Overview

We want to align the PUF1 protein sequences from _Plasmodium_ to those of other
species and identify the Pumilio domain. From there, we want to make a prediction
about the RNA sequences targeted by the Pumilio (PUF) domain.

## Obtaining sequences

Downloaded Plasmodium sequences off of plasmodb.org.

``` bash
wget --debug --header 'content-type: application/json' \
-O "json_veupathdb/PVP01_1015200_orthologs.json" \
-H https://plasmodb.org/plasmo/service/record-types/gene/searches/single_record_question_GeneRecordClasses_GeneRecordClass/reports/standard \
--post-data '{
  "searchConfig": {
  "parameters": {
      "primaryKeys": "PVP01_1015200,PlasmoDB"
    }
  },
  "reportConfig": {
    "attributes": [
      "primary_key"
    ],
    "tables": ["Orthologs"],
    "attributeFormat": "text"
  }
}'
```

Then downloaded FASTA of orthologs:

``` bash
mamba activate rcsbpdb_webquery # has "requests" module

python scripts/download_from_ortho_table.py json_veupathdb/PVP01_1015200_orthologs.json \
puf1_fasta/PVP01_1015200_orthologs.fasta \
https://plasmodb.org/plasmo PlasmoDB Plasmodium
```

Get Toxoplasma sequences

``` bash
wget --debug --header 'content-type: application/json' \
-O "json_veupathdb/TGME49_260600_orthologs.json" \
-H https://toxodb.org/toxo/service/record-types/gene/searches/single_record_question_GeneRecordClasses_GeneRecordClass/reports/standard \
--post-data '{
  "searchConfig": {
  "parameters": {
      "primaryKeys": "TGME49_260600,ToxoDB"
    }
  },
  "reportConfig": {
    "attributes": [
      "primary_key"
    ],
    "tables": ["Orthologs"],
    "attributeFormat": "text"
  }
}'

python scripts/download_from_ortho_table.py json_veupathdb/TGME49_260600_orthologs.json \
puf1_fasta/TGME49_260600_orthologs.fasta \
https://toxodb.org/toxo ToxoDB Toxoplasma
```

Model organism sequences were downloaded from UniProt.

Sequences were semi-manually combined into closest_puf1.fa.

## Multiple sequence alignment

Install Clustal Omega, version 1.2.4.

``` bash
mamba env create --name clustalo -c bioconda clustalo
```

Run alignment

``` bash
sbatch scripts/clustalo_2026-01-30.sh
```
