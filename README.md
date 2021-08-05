# sr-software-comparison
This project compares features among software that supports systematic reviews of biomedical literature.

# Plotting Features of Systematic Review Software
**Objective:** Make charts comparing the presence of features in top systematic review softwares
**Last Modified:** August 6 2021

#allsr.ipynb
Calculates summary of the feature count and feature percent for each software
Plots summmarized data comparing all SR software.
Exports charts as a PNG.

# groupbyfeature.ipynb
This program divides features based on pre-specificed feature classes. It compares softare based on the number of support features in each feature class.
Generates charts using seaborn and exports the captions of each figure.

# helpers.py
includes functions for reading SR data sheet, summarizing the data, and limitating the dataframe to the top performing software.
