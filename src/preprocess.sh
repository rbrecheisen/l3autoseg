#!/bin/bash
LOGS_DIR="/mnt/localscratch/cds/rbrecheisen/projects/l3autoseg/logs"
NEW_LOG_DIR=$(date +"%Y%m%d-%H%M")
mkdir -p ${LOGS_DIR}/${NEW_LOG_DIR}
