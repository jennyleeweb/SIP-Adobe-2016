from PIL import Image
im = Image.open("lamppost.jpg")
im.show()
darkBlue= (0, 51, 76)
red= (217, 26, 33)
lightBlue= (112, 150, 158)
yellow= (252, 227, 166)
data_list = list(im.getdata())
index = 0
intensity= data_list[index][0]+ data_list[index][1] +data_list[index][2]
new_pic= []
for i in range(len(data_list)):
    if intensity < 182:
        new_pic.append(darkBlue)
    if intensity > 182 and intensity < 364:
        new_pic.append(red)
    if intensity > 364 and intensity < 546:
        new_pic.append(lightBlue)
    if intensity > 564:
        new_pic.append(yellow)
    index += 1
new = Image.new("RGB",(654, 315), im.putdata(new_pic))
new.save("output.jpg", "jpeg")
new.show()

   
    

    
  
    
