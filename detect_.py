# """
# objective 1)   detect image fogery (deep learning method and other methods)

# objective 2)  image analysis 
# """
# import piexif

# image_name = 'images\original2.jpg'
# exif_dict = piexif.load(image_name)

# # Extract thumbnail and save it, if exists
# thumbnail = exif_dict.pop('thumbnail')
# if thumbnail is not None:
#     with open('thumbnail.jpg', 'wb') as f:
#         f.write(thumbnail)

# # Iterate through all the other ifd names and print them

# for ifd in exif_dict:
#     # print(f'{ifd}:')
#     for tag in exif_dict[ifd]:
#         tag_name = piexif.TAGS[ifd][tag]["name"]
#         tag_value = exif_dict[ifd][tag]
#         # Avoid print a large value, just to be pretty
#         if isinstance(tag_value, bytes):
#             tag_value = tag_value[:10]
#         if "Software" in tag_name:
#             if "Photoshop" in tag_value:
#                 print(f'found Photoshop in image metadata:')
#                 print(f'\t{tag_name}: {tag_value}')
#         # print(f'\t{tag_name:25}: {tag_value}')
# print()
import numpy as np

# photoshop = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[2,4,5,8],[5,10,15]]])

x = np.array([[[18, 14, 22, 35, 44, 39, 34, 17],
[14, 16, 21, 34, 28, 23, 12, 12],
[22, 21, 27, 28, 23, 12, 12, 12],
[35, 34, 28, 23, 12, 12, 12, 12],
[44, 28, 23, 12, 12, 12, 12, 12],
[39, 23, 12, 12, 12, 12, 12, 12],
[34, 12, 12, 12, 12, 12, 12, 12],
[17, 12, 12, 12, 12, 12, 12, 12]], 

[[27, 26, 41, 65, 66, 39, 34, 17],
[26, 29, 38, 47, 28, 23, 12, 12],
[41, 38, 47, 28, 23, 12, 12, 12],
[65, 47, 28, 23, 12, 12, 12, 12],
[66, 28, 23, 12, 12, 12, 12, 12],
[39, 23, 12, 12, 12, 12, 12, 12],
[34, 12, 12, 12, 12, 12, 12, 12],
[17, 12, 12, 12, 12, 12, 12, 12]]])

p = x[0]
if p in x:
    print("hello")
# # print(x.ndim)
# for i in range(2):
#     print("the {} array is: {}".format(i,x[i]))
# lumin = np.array([x[:-1] for x in lumline])

# comparison = lumin == qtlum.astype(str)
# print(lumin)
# equal_arrays = comparison.all()
# print(equal_arrays)