import h5py
print("Opened")
f = h5py.File('InceptionV3_set4_set3_B10_E100_F299.h5', 'r+')
del f['optimizer_weights']
f.close()
print("Done")