ENCODE = {".-": "A",
          "-...": "B",
          "-.-.": "C",
          "-..": "D",
          ".": "E",
          "..-.": "F",
          "--.": "G",
          "....": "H",
          "..": "I",
          ".---": "J",
          "-.-": "K",
          ".-..": "L",
          "--": "M",
          "-.": "N",
          "---": "O",
          ".--.": "P",
          "--.-": "Q",
          ".-.": "R",
          "...": "S",
          "-": "T",
          "..-": "U",
          "...-": "V",
          ".--": "W",
          "-..-": "X",
          "-.--": "Y",
          "--..": "Z",
          "-----": "0",
          ".----": "1",
          "..---": "2",
          "...--": "3",
          "....-": "4",
          ".....": "5",
          "-....": "6",
          "--...": "7",
          "---..": "8",
          "----.": "9",
          "/": " ",
          ".-.-.-": ".", }

morse_list = list(ENCODE.keys())   # coverts the keys of ENCODE dict into a list
character_list = list(ENCODE.values()) # coverts the values of ENCODE dict into a list

class Converter:
    def __init__(self):
        self.text_list = None
        self.morse_list = None
        self.converted_morse_list = []
        self.converted_text_list = []

    def convert_text(self, translate_text):
        self.text_list = list(str(translate_text).upper())
        # converts translate_text into upper case and converts it into a list
        for character in self.text_list:
            for char in character_list:
                if char == character:
                    self.converted_morse_list.append(morse_list[character_list.index(char)])
                    '''takes the index of the character from character list and gets the corresponding value from
                                        morse_list using that index'''
        converted_text = " ".join([item for item in self.converted_morse_list])
        return converted_text

    def convert_morsecode(self, translate_morsecode):
        self.morse_list = translate_morsecode.split(" ")
        for character in self.morse_list:
            for char in morse_list:
                if char==character:
                    self.converted_text_list.append(character_list[morse_list.index(char)])
        converted_morse = "".join([item for item in self.converted_text_list])
        return converted_morse








         







