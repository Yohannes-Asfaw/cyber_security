def cipher(str1):
    jump = int(input("insert the jump for the cipher encryption: "))
    if jump > 26:
        jump = jump % 26
    str2 = ""
    for i in str1:
        if i == " ":
            str2 += " "
        elif ord(i) + jump > 122:
            tempo = ord(i) + jump - 26
            str2 += chr(tempo)
        else:
            str2 += chr(ord(i) + jump)
    return str2