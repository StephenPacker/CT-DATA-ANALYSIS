### CT-DATA-ANALYSIS
A suite of tools to extract porosity information from CT scan data. All of the provided code is designed to work on binary images, the use of non-binary images is at your own risk. The software I used to binarize images was CTAn, a free CT image processing software that can be downloaded at http://bruker-microct.com/products/downloads.htm.

## Circular Random Slice 
Mimics the action of slicing a sample at any angle. For each slice, the porosity is recorded to an excel sheet, and this procedure can be ran any number of times with the slices being taken from a new random section of the smaple.

## Simple Porosity Calc
Calculates the porosity for irregular circular shapes. An example of an irregular cirle shape is: Image 1 (Salt with intergran porosity)
![salt_2_17 03_2k_rec0807](https://user-images.githubusercontent.com/35316529/45987469-d9ce3a80-c02e-11e8-9a0f-b95601038fda.jpg)

## Circular Porosity Calc
Calculates the porosity for regular circular shapes. An example of a regular cirle shape is: Image 2 (Printed Sandstone)
![printed_sandstone_8um_4k_rec0068](https://user-images.githubusercontent.com/35316529/45987387-5e6c8900-c02e-11e8-8916-12869e402015.jpg)

## Generic Porosity Calc
Calculates the porosity for objects of any shape given that the object has a solid boundary (Should be closer to Image 2 than Image 1).
If your sample is circular, this method while being accurate, is very slow, so Circular Porosity Calc may be better.
An example of a shape that will work better with the Generic Porosity Calc is: Image 3 (Bioturbated Sandstone)

