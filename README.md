# PvPUF1 motif analysis in _Plasmodium vivax_ and _P. yoelii_

This repository accompanies the submitted manuscript:

Gigliola Zanghi, Kim Chi Vo, Lindsay V. Clark, Sumana Chakravarty, Erika L. Flannery,
Vorada Chuenchob, Yo Cao, Hardik Patel, Nastaran Rezakhani, Lucia Pazzagli,
Matthew E. Fishbaugher, Sebastian A. Mikolajczak, Wanlapa Roobsoong,
Jetsumon Sattabongkot, B. Kim Lee Sim, Stephen L. Hoffman, Ashley M. Vaughan,
and Stefan H. I. Kappe (2026)
"Parasite and host factors associated with malaria parasite liver stage latency."

This code was authored by Lindsay Clark at Research Scientific Computing,
Seattle Children's Research Institute.

See the `workbooks` folder for notebooks describing the analysis. Files are
numbered to indicate their order for the analysis.

This code is archived on Zenodo: [![DOI](https://zenodo.org/badge/1323124748.svg)](https://doi.org/10.5281/zenodo.21825603)

## System requirements

* `1_protein_alignment.md` and `6_download_go.md` were run using
  - Rocky Linux 9.8
  - Clustal Omega 1.2.4
  - Python 3.13.9
* The five `.qmd` files (2-5, 7) have been run on both:
  - R 4.4 on Windows 11 (necessary for generation of figures using Arial font)
  - R 4.5 on Rocky Linux 9.8 (all `wget` commands were run on Linux)
 
 No non-standard hardware is required.
 
 ## Installation guide
 
 Python and R can be installed using standard approaches.  The python `requests`
 module is required for the script `download_from_ortho_table.py`. For R,
 required Bioconductor packages include:
 
 * Biostrings
 * msa
 * GenomicRanges
 * edgeR
 * fgsea
 
 And required CRAN packages include:
 
 * jsonlite
 * dplyr
 * plotrix
 * showtext
 * ggplot2
 * ggrepel
 * ggtext
 
 Clustal Omega can be obtained as the `clustalo` package from bioconda.
 
 All software can be installed in one hour or less on a standard system.
 
 ## Instructions
 
 To reproduce the analysis, work through the following sets of notebooks.
 
 * `1_protein_alignment.md`
   - For identifying and aligning orthologous proteins to PvPUF01.
   - This notebook contains a series of commands to be run from a bash terminal.
   - For Python steps, the `requests` module must be installed.
   - This notebook may be skipped when reproducing the analysis; the outputs
   `puf1_fasta/closest_puf1.fa` and `results/clustalo/puf1_2026-01-30.aln` are
   included in the repository.
 * `2_explore_pumilio.qmd`
   - Contains notes on how the predicted binding motif UGUANNNUA was determined.
   - A standard Quarto notebook with R code that can be executed in RStudio.
   - The only output is a set of PDFs, saved to `results/clustalo`, displaying
   the protein sequence alignment at Pumilio domains. These are not necessary
   for running the downstream notebooks.
 * `3_genomes_orthologs.qmd`
   - Downloads public data for _Plasmodium vivax_ and _P. yoelii_.
   - The `wget` commands to download the reference genomes and annotations are
   necessary for downstream notebooks. These FASTA and GFF files are saved in
   the `resources` directory after running the corresponding chunk.
   - The `wget` command to download a JSON of orthology information, and the
   R commands to process that JSON, can potentially be skipped since the output
   is saved in the repository as `resources/vivax_yoelii_orthologs_2026-02-11.csv`.
* `4_predicted_utrs.qmd`
  - Defines 3' UTR and 5' UTR regions in _P. vivax_ and _P. yoelii_
  - A standard Quarto notebook with R code that can be executed in RStudio.
  - Generates the output `results/R_objects/pred_UTR_GRanges_2026-03-25.RData`,
  required for downstream notebooks.
* `5_gene_expression.qmd`
  - Identifies expressed genes in _P. vivax_ and _P. yoelii_, and differentially
  expressed genes in _P. vivax_
  - A standard Quarto notebook with R code that can be executed in RStudio.
  - The required input `results/counts_vivax.txt` is included in this repository.
  - The required input `geo/GSE337317_P_yoelii_gene_counts.txt.gz` needs to be
  downloaded from the Gene Expression Omnibus (search for GSE337317) before
  running the notebook.
  - The output `results/R_objects/expressed_orthologs.rds` is required for
  downstream notebooks.
  - The output `results/vivax_dge_results.txt` is included in this repository.
  - Includes code to generate the Venn diagram in Supplementary Figure 5
* `6_download_go.md`
  - Downloads gene ontology terms for _P. vivax_ and _P. yoelii_ and parses them
  into a JSON format for the downstream notebook.
  - Contains commands to be executed at the bash terminal
  - Outputs twelve JSON files into the `json_veupathdb` directory. These are
  required for the downstream notebook.
* `7_motif_enrichment.qmd`
  - Identifies which motif sequences are found within which regions of which
  transcripts
  - Uses the Poisson test to determine if motifs are found more frequently than
  would be expected under random chance
  - Runs a T-test to demonstrate association of certain motifs with differential
  gene expression
  - Tests for overrepresentation of gene ontology terms in sets of genes with motifs
  - A standard Quarto notebook with R code that can be executed in RStudio.
  - Generates component figures from Fig. 5 and Supplementary Fig. 5
  - Outputs five files into the `results` folder, included in this repository:
    - `Motif_enrichment_2026-05-28.txt` - Poisson test result for motif enrichment
    - `fora_2026-06-11.csv` - gene ontology overrepresentation results
    - `matches_pv_2026-06-11.csv` - motif locations within _P. vivax_ genes
    - `matches_py_2026-06-11.csv` - motif locations within _P. yoelii_ genes
    - `orthologs_2026-06-11.csv` - orthologs between _P. vivax_ and _P. yoelii_,
    marked by whether each ortholog has a motif
