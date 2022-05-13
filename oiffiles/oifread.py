from oiffile import *


image = OifFile("\\\\sf3\\cicutagroup\\jsm89\\v1_.29March2022_40xAPO.oib")
#print(image.shape)

stuff = image.mainfile
print("WidthConvertValue = {} um".format(stuff['Reference Image Parameter']['WidthConvertValue']))
#stuff=str(stuff)
#with open("mainfile_test.txt", 'a') as f:
        #if new_file:
        #f.write("#" + comment_string + "\n")
#        f.write(stuff)	