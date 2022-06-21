MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
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
}

# morse_decoder("... --- -- .   - . -..- -") == "Some text"
# morse_decoder("..--- ----- .---- ---..") == "2018"
# morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"

def morse_decoder(code):
    code = code.replace('   ', '  ')
    print(code)
    code = code.split(' ')
    print(code)
    results = []
    for c in code:
        if c in MORSE:
            results.append(MORSE[c])
        elif c == '':
            results.append(' ')
    print(results)
    result = ''.join(results)
    return result[0].upper() + result[1:]

print(morse_decoder("... --- -- .   - . -..- -"))