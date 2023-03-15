# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:58:48 2023

@author: Shoyeb
"""


#                  IMAGE EDITING AND JPG TO PDF CONVERTER


from PIL import Image,ImageEnhance
import os
# ================================ for size ===================================
img1=Image.open("1650611345326_2.jpg")# enter your jpg path 
img1.show()
MAX_SIZE=(250,250)
img1.thumbnail(MAX_SIZE)
img1.save("shoyeb_dp.jpg")#enter your save path location

# ==================== all jpg to pdf(use when you want pdf) ==================

#   for item in os.listdir():
#     if item.endswith(".jpg"):
#         img1=Image.open(item)
#         filename,extension=os.path.splitext(item)
#         img1.save(f"{filename}.png")
          
# ============================== use for sharpness ====================================
        
#img1=Image.open("asdf.jpg")
#enhance=ImageEnhance.Sharpness(img1)
#enhance.enhance().save("shoyeb.jpg")
          
# ================================use for colour change =====================================
 
# img1=Image.open("sdp.jpg")        
# enhance=ImageEnhance.Color(img1)
# enhance.enhance(2).save("colour1.jpg")# for black&white use 0
      
# ================================ use for brightness =================================

# img1=Image.open("sdp.jpg")     
# enhance=ImageEnhance.Brightness(img1)
# enhance.enhance(1).save("brightness.jpg")
    
# ================================ use for contrest ===================================
         
# img1=Image.open("sdp.jpg")        
# enhance=ImageEnhance.Contrast(img1)
# enhance.enhance(1.5).save("contrast.jpg")

