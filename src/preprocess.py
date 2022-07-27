""" Preprocesses raw data for training a deep learning model 
    File log.txt describes exactly what happened. File errors.txt
    describes which files were excluded from processing because they
    do not comply with requirements, e.g., non-512x512 size. The file
    files.txt contains all files included in the processing together 
    with a mapping from the raw file path to the new processed file path
    for easy back-referral.

    Logging these files will happen in a newly created directory
"""
import logging
