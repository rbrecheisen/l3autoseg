""" Different loaders to be used for training and prediction. There are different ways
    to do this. For one, you can load everything at once as a single HDFS file. You can
    also load data file by file. 

    First need to find out what options Keras has to load data.
"""


def load_h5(d):
    """ Loads HDFS data from local directory """
    pass


def load_from_xnat():
    """ Loads data from XNAT and stored in /mnt/localscratch/cds/rbrecheisen/data 
    and then calls load_dir()
    """
    pass

