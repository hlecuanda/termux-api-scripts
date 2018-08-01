#!/usr/bin/env python3

cheer_left='*\o\*'
cheer_center='*\o/*'
cheer_right='*/o/*'

gimme='¡dame una {}!'
given='¡{}!'

def pegar(pegamento,pedazos):
    pegado=''
    for pedazo in pedazos:
        pegado += pedazo + pegamento            
    return pegado

def cheerletra(letra):
    ch=[]
    ch.append(cheer_left)
    ch.append(gimme.format(letra)) 
    ch.append(cheer_center)
    ch.append(given.format(letra))
    ch.append(cheer_right)
    cheer=pegar(' ',ch)
    print(cheer)

def spell(frase):
    for letra in frase.upper():
        if letra != ' ':
            cheerletra(letra)


if __name__ == '__main__':
    spell('hola nena')

# vim: ft=python :   

