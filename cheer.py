#!/usr/bin/env python3
# vim: number nowrap :

import click
                        
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

def quedice(todalafrase):
    ch=[]
    ch.append(cheer_left)
    ch.append('¿Que dice?')
    ch.append(cheer_center)
    ch.append(todalafrase.lower())
    ch.append(cheer_right)
    return pegar(' ',ch)

def noseoye(todalafrase):
    ch=[]
    ch.append(cheer_left)
    ch.append('¡No se oye!')
    ch.append(cheer_center)
    ch.append(todalafrase.lower().capitalize())
    ch.append(cheer_right)
    return pegar(' ',ch)
    
def masfuerte(todalafrase):
    ch=[]
    ch.append(cheer_left)
    ch.append('¡MAS FUERTE!')
    ch.append(cheer_center)
    ch.append(todalafrase.upper())
    ch.append(cheer_right)
    return pegar(' ',ch)
        
def tresveces(todalafrase):
    ch=[]
    ch.append(cheer_left)
    ch.append('¡TRES VECES!')
    ch.append(cheer_center)
    for vez in range(0,3):  
        ch.append(todalafrase.upper())
    ch.append(cheer_right)
    return pegar(' ',ch)
    
def cheerletra(letra):
    ch=[]
    ch.append(cheer_left)
    ch.append(gimme.format(letra)) 
    ch.append(cheer_center)
    ch.append(given.format(letra))
    ch.append(cheer_right)
    cheered=pegar(' ',ch)
    return cheered

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS,   
        short_help='dame una frase, las cheerleaders la usaran en su porra')
@click.argument('frase')
def cheer(frase):
    ch=[]

    for letra in frase.upper():
        if letra != ' ':
            ch.append(cheerletra(letra))
        else:
            ch.append('...')

    ch.append('...') # Legibiliad a la salida
    ch.append(quedice(frase))
    ch.append(noseoye(frase))
    ch.append(masfuerte(frase))
    ch.append(tresveces(frase))

    for line in ch:
        print(line)


if __name__ == '__main__':
    cheer()

# vim: ft=python :   

