# Download gene ontology terms for P. yoelii

``` bash
cd json_veupathdb

wget --debug --header 'content-type: application/json' -O Pyoelii17X_GOterms.json \
-H https://plasmodb.org/plasmo/service/record-types/transcript/searches/GenesByTaxon/reports/standard \
--post-data '{
  "searchConfig": {
    "parameters": {
      "organism": "[\"Plasmodium yoelii yoelii 17X\"]"
    },
    "wdkWeight": 10
  },
  "reportConfig": {
    "attributes": [
      "primary_key",
      "organism",
      "gene_location_text",
      "gene_product",
      "predicted_go_id_component",
      "predicted_go_component",
      "predicted_go_id_function",
      "predicted_go_function",
      "predicted_go_id_process",
      "predicted_go_process",
      "annotated_go_id_component",
      "annotated_go_component",
      "annotated_go_id_function",
      "annotated_go_function",
      "annotated_go_id_process",
      "annotated_go_process",
      "ec_numbers",
      "ec_numbers_derived"
    ],
    "tables": [],
    "attributeFormat": "text"
  }
}'
```

Download for vivax

``` bash
cd json_veupathdb

wget --debug --header 'content-type: application/json' -O PvivaxP01_GOterms.json \
-H https://plasmodb.org/plasmo/service/record-types/transcript/searches/GenesByTaxon/reports/standard \
--post-data '{
  "searchConfig": {
    "parameters": {
      "organism": "[\"Plasmodium vivax P01\"]"
    },
    "wdkWeight": 10
  },
  "reportConfig": {
    "attributes": [
      "primary_key",
      "organism",
      "gene_location_text",
      "gene_product",
      "predicted_go_id_component",
      "predicted_go_component",
      "predicted_go_id_function",
      "predicted_go_function",
      "predicted_go_id_process",
      "predicted_go_process",
      "annotated_go_id_component",
      "annotated_go_component",
      "annotated_go_id_function",
      "annotated_go_function",
      "annotated_go_id_process",
      "annotated_go_process",
      "ec_numbers",
      "ec_numbers_derived"
    ],
    "tables": [],
    "attributeFormat": "text"
  }
}'
```

Parse into JSON of GO terms

``` bash
python3 ../scripts/parse_go_2026-03-04.py Pyoelii17X_GOterms.json Pyoelii17X

python3 ../scripts/parse_go_2026-03-04.py PvivaxP01_GOterms.json PvivaxP01
```
