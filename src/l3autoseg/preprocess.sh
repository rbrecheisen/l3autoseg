#!/bin/bash

TIMESTAMP=$(date +"%Y%m%d-%H%M")
LOG_DIR="/mnt/localscratch/cds/rbrecheisen/projects/l3autoseg/logs/preprocess.py/${TIMESTAMP}"
PROCESSED_DIR="/mnt/localscratch/cds/rbrecheisen/projects/l3autoseg/processed/${TIMESTAMP}"
mkdir -p ${LOG_DIR}
mkdir -p ${PROCESSED_DIR}
cp preprocess.py ${NEW_LOG_DIR}

