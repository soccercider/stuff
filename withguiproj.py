from Tkinter import *
import random
from PIL import Image, ImageTk, ImageDraw, ImageFont

#to view image, this file needs to be in the same folder
#as the images used

#if there is a dash in the alcohol
#we parse it so that we get
#the position of the OH group
def n_alcohol(chemical_name):
    for i in range(len(chemical_name)):
        if chemical_name[i]=="-":
            chemical_name=chemical_name[i+1:]
            return i
    return -1

#the main root of the alcohol
#is extracted so it can be found 
#in the dictionary
def n_alcohol_changename(chemical_name):
    for i in range(len(chemical_name)):
        if chemical_name[i]=="-":
            chemical_name=chemical_name[i+1:]
            return chemical_name
        
root=Tk()
root.withdraw()
possible_options=Toplevel()
possible_options.title("ENTER CHEMICAL NAME")
chemical_name_ask=Label(possible_options,text="Please enter a valid chemical name: ")
chemical_name_ask.pack()
chemical_name_entry=Entry(possible_options)
chemical_name_entry.pack()


def draw_chem_structure():
    im1 = Image.open("ChemLetters.tiff")
    Carbon = im1.crop((50,12,68,32))
    Oxygen = im1.crop((26,42,46,63))
    Hydrogen=im1.crop((134,12,152,32))
    im = Image.open("whitesquare.jpg")
    draw = ImageDraw.Draw(im, "RGBA")
    x=300
    y=300
    alcohol_prefix= { 'meth' : 0, 'eth' : 1, 'prop' : 2, 'but' : 3, 'pent' : 4, 'hex' : 5, 'hept' : 6, 'oct' : 7, 'non' : 8, 'dec' : 9}
    alkane_prefix= { 'meth' : 0, 'eth' : 1, 'prop' : 2, 'but' : 3, 'pent' : 4, 'hex' : 5, 'hept' : 6, 'oct' : 7, 'non' : 8, 'dec' : 9}
    ######THIS WORKS###### ALKANES
    chemical_name=chemical_name_entry.get()
    original_entry=chemical_name
    ####AS METHANE AND METHANOL ARE EXCEPTIONS TO SKELETAL STRUCTURE
    ####THEY REQUIRE THE TRADITIONAL MODEL
    if chemical_name=="methane":
        im.paste(Carbon,(x,y))
        draw.line([(x-20, y+10),(x,y+10)], fill=(0,0,0), width=2)
        im.paste(Hydrogen,(x-40,y))
        draw.line([(x+20, y+10),(x+40,y+10)], fill=(0,0,0), width=2)
        im.paste(Hydrogen,(x+40,y))
        draw.line([(x+10, y-20),(x+10,y)], fill=(0,0,0), width=2)
        im.paste(Hydrogen,(x,y-40))
        draw.line([(x+10, y+20),(x+10,y+40)], fill=(0,0,0), width=2)
        im.paste(Hydrogen,(x,y+40))
    if chemical_name=="methanol":
        im.paste(Carbon,(x,y))
        draw.line([(x-20, y+10),(x,y+10)], fill=(0,0,0), width=2)
        im.paste(Hydrogen,(x-40,y))
        draw.line([(x+20, y+10),(x+40,y+10)], fill=(0,0,0), width=2)
        im.paste(Oxygen,(x+40,y))
        im.paste(Hydrogen,(x+60,y))
        draw.line([(x+10, y-20),(x+10,y)], fill=(0,0,0), width=2)
        im.paste(Hydrogen,(x,y-40))
        draw.line([(x+10, y+20),(x+10,y+40)], fill=(0,0,0), width=2)
        im.paste(Hydrogen,(x,y+40))
    if chemical_name[len(chemical_name)-3:]=='ane':
        chemical_name=chemical_name[:len(chemical_name)-3]
        if chemical_name in alkane_prefix and original_entry[len(original_entry)-3:]=='ane' and original_entry!="methane":
            for i in range(alkane_prefix[chemical_name]):
                if i % 2 == 0:
                    draw.line([(x, y),(x+20,y+20)], fill=(0,0,0), width=2)
                    x=x+20
                    y=y+20
                if i % 2 == 1:
                    draw.line([(x, y),(x+20,y-20)], fill=(0,0,0), width=2)
                    x=x+20
                    y=y-20
    #################### END ALKANES

    ### ALCOHOLS

    if chemical_name[len(chemical_name)-4:]=='anol':
        chemical_name=chemical_name[:len(chemical_name)-4]
    haspos=n_alcohol(chemical_name)
    if haspos!=-1:
        attach_OH=int(chemical_name[:1])
        remainder=n_alcohol_changename(chemical_name)
        if remainder in alcohol_prefix and original_entry[len(original_entry)-4:]=='anol' and original_entry!="methanol":
            exception1=True
            for i in range(alcohol_prefix[remainder]):
                if i % 2 == 0:
                    draw.line([(x, y),(x+20,y+20)], fill=(0,0,0), width=2)
                    if i==attach_OH-2:
                        draw.line([(x+20, y+20),(x+20,y+40)], fill=(0,0,0), width=2)
                        im.paste(Oxygen,(x+10,y+40))
                        im.paste(Hydrogen,(x+10,y+60))
                    if attach_OH==1 and exception1==True:
                        draw.line([(x, y),(x-10, y+10)], fill=(0,0,0), width=2)
                        im.paste(Oxygen,(x-30,y+10))
                        im.paste(Hydrogen,(x-50,y+10))
                        exception1=False
                    x=x+20
                    y=y+20                        
                if i % 2 == 1:
                    draw.line([(x, y),(x+20,y-20)], fill=(0,0,0), width=2)
                    if i==attach_OH-2:
                        draw.line([(x+20, y-20),(x+20,y-40)], fill=(0,0,0), width=2)
                        im.paste(Oxygen,(x+10,y-60))
                        im.paste(Hydrogen,(x+10,y-80))
                    x=x+20
                    y=y-20
    else:
        if chemical_name in alcohol_prefix and original_entry[len(original_entry)-4:]=='anol' and original_entry!="methanol":
            for i in range(alcohol_prefix[chemical_name]):
                if i % 2 == 0:
                    draw.line([(x, y),(x+20,y+20)], fill=(0,0,0), width=2)
                    if i==alcohol_prefix[chemical_name]-1:
                        draw.line([(x+20, y+20),(x+30,y+10)], fill=(0,0,0), width=2)
                        im.paste(Oxygen,(x+30,y))
                        im.paste(Hydrogen,(x+50,y))
                    x=x+20
                    y=y+20
                if i % 2 == 1:
                    draw.line([(x, y),(x+20,y-20)], fill=(0,0,0), width=2)
                    if i==alcohol_prefix[chemical_name]-1:
                        draw.line([(x+20, y-20),(x+30,y-10)], fill=(0,0,0), width=2)
                        im.paste(Oxygen,(x+30,y-20))
                        im.paste(Hydrogen,(x+50,y-20))
                    x=x+20
                    y=y-20

    ###############END ALCOHOL

    ####PYRANOSE
    if chemical_name[len(chemical_name)-8:]=='pyranose':
        
        draw.line([(x+20, y),(x+70,y+70)], fill=(0,0,0), width=2)#end at C2
        draw.line([(x+70, y+70),(x+20,y+140)], fill=(0,0,0), width=2)
        draw.line([(x-50, y+140),(x+20,y+140)], fill=(0,0,0), width=2)
        draw.line([(x-50, y+140),(x-100,y+70)], fill=(0,0,0), width=2)
        draw.line([(x-50, y),(x-100,y+70)], fill=(0,0,0), width=2)
        draw.line([(x-50, y),(x,y)], fill=(0,0,0), width=2)
        im.paste(Oxygen,(x+7,y-10))
        if chemical_name[0:5]=='alpha':
            draw.line([(x+70, y+70),(x+80,y+80)], fill=(0,0,0), width=2)#end at C2
            #in the process of completion
            
    #####WATER
    if original_entry=="water":
        im.paste(Oxygen,(x-10,y-20))
        draw.line([(x+9, y),(x+30,y+10)], fill=(0,0,0), width=2)
        draw.line([(x-10, y),(x-30,y+10)], fill=(0,0,0), width=2)
        im.paste(Hydrogen,(x-50,y+10))
        im.paste(Hydrogen,(x+30,y+10))
    im.show()


btn=Button(possible_options, text="Enter", command=draw_chem_structure)
btn.pack()
root.mainloop()
