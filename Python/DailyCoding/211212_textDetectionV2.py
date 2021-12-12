import cv2
from pytesseract import pytesseract
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import Image

class EasyEats:


    # Source, 
    # http://marininfo.org/Healthcare/Sweeteners_and_Glycemic_Index.htm
    indexList = {"alitame":0, "aspartame":0, "agave syrup":11, "brazzein":0, "brown rice syrup":25, "curculin":0, "cyclamate":0, "dextrose":100, "erythritol":0, "glucose":100, "fructose":21, "glycyrrhizin":0, "hf cs":63, "hsh":3, "honey":50, "hf corn syrup":87, "inulin":1, "isomalt":2., "isomaltitol":2, "lactitol":6, "lactose":46,"lactulose":0, "miraculin":0, "monellin":0,  "maltose":105, "molasses":55, "maple syrup":54, "mannitol":2, "maltodextrin":110, "neotame":0, "pentadin":0, "palatinose":2, "sucralose":0, "saccharin":0, "stevia":0, "sorghum":50, "sorbitol":9, "sucrose":63, "thaumatin":0, "tagatose":0, "trehalose":70, "table sugar":80, "xylitol":10,"corn syrup":75}
    
    def ingredients(self):
        img = Image.open("Figures/ig2.png")

        words_in_image = pytesseract.image_to_string(img)
        words_in_image = words_in_image.split()
        output = []
        for word in words_in_image:
            output.append(word.upper())

        return output

    def isSuitable(self):
        gi = 0
        cnt = 0
        itemList = [item.lower() for item in self.ingredients()]

        # Sum of Glycemic Index
        # Find good/normal/bad items
        good, normal, bad = [], [] ,[]
        for item in itemList:
            if item in self.indexList:
                score = self.indexList[item]
                if score < 55:
                    good.append(item)
                elif score < 69:
                    normal.append(item)
                else:
                    bad.append(item)
                gi += self.indexList[item]
                cnt += 1

        # Gi base
        # Low-GI foods have a GI value under 55, while medium-GI foods are between 51–69 and high-GI foods are over 70. High-GI foods raise blood sugar quickly because they contain sugars that are easily absorbed by the gut.


        if cnt == 0:
            return print("Cannot decide")
        else: 
            gi = gi/cnt
            if gi < 55:
                return print("Good because of ", good)
            elif gi < 69:
                return print("Normal because of ", normal)
            else:
                return print("Not recommended because of ", bad)


test = EasyEats()
print(test.isSuitable())