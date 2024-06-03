#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Anjad Badran
# DATE CREATED: 26/5/2024                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    in_files = listdir(image_dir)

    # Tested by Anjad to print 1st (5) files name, but I use full path, cuz putting  pet_images/ only doesn't work!
    # print("\nPrints 5 filenames from folder pet_images############33/")
    # for idx in range(0, 5, 1):
    #  print("{:2d} file: {:>25}".format(idx + 1, in_files[idx]) )

    # create empty dictionary
    results_dic = dict()
    ## Determines number of items in dictionary
    # items_in_dic = len(results_dic)
#     print("\nEmpty Dictionary results_dic - n items", len(results_dic))
#     print("\nno. of in-files ", len(in_files))

    for filename in in_files:
           # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
           # isn't an pet image file
         if filename[0] != ".":
           low_pet_image = filename.lower()
           word_list_pet_image = low_pet_image.split("_")
          #  pet_name = ""
          #  for word in word_list_pet_image:
          #  if word.isalpha():
           pet_name = " ".join([word.strip() for word in word_list_pet_image if word.isalpha()])  
          #  pet_name = pet_name.strip()
           if filename not in results_dic:
                results_dic[filename] = [pet_name]
              
           else:
               print("** Warning: Duplicate files exist in directory:", in_files[idx])

    # Replace None with the results_dic dictionary that you created with this
    # function
    # print("Print Dictionary Test by Anjad", results_dic)
    return results_dic
