from PIL import Image,ImageDraw,ImageFont

RN = ImageFont.truetype("./fonts/roman_font_7.ttf", 28, encoding="unic")


test = {"tier":"GOLD","rank":"IV","lp":33}


def generateimage(values):
    #open image depending on rank
    img = Image.open('./img/' + values["tier"] + ".png")
    #adds width and height to variables
    width, height = img.size

    #DRaw image
    I1 = ImageDraw.Draw(img)

    # roman numeral
    I1.text((width/2-5, 200), values["rank"],"black",RN)
    #lp
    I1.text((width/2-10, 230), str(values["lp"]) + " LP","black")
    #return image save can return raw image
    return img.save("./image.png")



generateimage(test)