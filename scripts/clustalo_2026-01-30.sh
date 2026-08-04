#!/bin/bash

#SBATCH --account=vaughan_plasmod
#SBATCH --partition=cpu-core
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=7500M
#SBATCH --time=0-02:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=Lindsay.Clark@seattlechildrens.org
#SBATCH --chdir=/data/hps/assoc/private/vaughan_plasmod/user/lclar5/logs

cd ../2026-01_kappe_motif

source $HOME/.bashrc

mamba activate clustalo

clustalo \
-i puf1_fasta/closest_puf1.fa \
--seqtype=Protein \
--threads=$SLURM_CPUS_PER_TASK \
--outfmt=clustal \
--out results/clustalo/puf1_2026-01-30.aln
