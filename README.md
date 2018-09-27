### CT-DATA-ANALYSIS
A suite of tools to extract porosity data from CT scan imaging. All of the provided code is designed to work on binary images, the use of non-binary images is at your own risk. The software I used to binarize images was CTAn, a free CT image processing software that can be downloaded at http://bruker-microct.com/products/downloads.htm. If you use are looking at using this program and work for the U of A contact me at spacker@ualberta.ca and we can discuss possible lisencing (Demo versino does not include the plugins required to binarize images).

## Circular Random Slice 
Mimics the action of slicing a sample at any angle. For each slice, the porosity is recorded to an excel sheet. The number of slices generated is up to the user. Each new slice is taken from a random section of the sample as to produce total coverage when numerous slices are taken.

## Simple Porosity Calc
Calculates the porosity for irregular circular shapes. An example of an irregular circle shape is: Image 1 (Salt with intergranular porosity) Note the large gaps around the perimeter of the circle, these gaps make the image irregular and non-solid.
![salt_2_17 03_2k_rec0807](https://user-images.githubusercontent.com/35316529/45987469-d9ce3a80-c02e-11e8-9a0f-b95601038fda.jpg)

## Circular Porosity Calc
Calculates the porosity for regular circular shapes. An example of a regular cirle shape is: Image 2 (Printed Sandstone)
![printed_sandstone_8um_4k_rec0068](https://user-images.githubusercontent.com/35316529/45987387-5e6c8900-c02e-11e8-8916-12869e402015.jpg)

## Generic Porosity Calc
Calculates the porosity for objects of any shape given that the object has a solid boundary (Should be closer to Image 2 than Image 1).
While this method is accurate, it is very slow, so Circular Porosity Calc may be better if your samples have a circular geometery.
An example of a shape that will work better with the Generic Porosity Calc is: Image 3 (Bioturbated Sandstone)
![sandstone_7 92um_4k_rec0249](https://user-images.githubusercontent.com/35316529/46028027-b21db780-c0ac-11e8-9915-0a7743a1c0c4.jpg)

