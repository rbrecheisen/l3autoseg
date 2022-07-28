# l3autoseg
Automatic segmentation of muscle and fat in L3 images

Purpose of this project is (1) to reproduce the CNN created by Leroy Volmer (MAASTRO)
using Keras instead of only TensorFlow and (2) use a standard CNN, like AlexNet, and
transfer learning to try and improve the resulting prediction model.

# Approach
Create trainable dataset from raw data using preprocess.py. The output dataset is 
saved in a timestamped/versioned directory. When you start training on this data
and you get a model that works, version the model as well and make sure to link it
to the training set version, as well as the version of preprocess.py and train.py!!