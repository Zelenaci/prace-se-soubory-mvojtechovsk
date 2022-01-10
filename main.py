#!/usr/bin/env python3
############################################################################
# Soubor:  main.py
# Datum: 10.1.2022
# Autor: Michal Vojtěchovský
############################################################################
from random import randint, choice, random
import time

############################################################################

def lowerCaseConvertor(file):
    try:
        f = open(f"{file}.txt","r")
    except FileNotFoundError:
        print("soubor nenalezen")
        menu()    
    f2 = open(f"{file}_lowerCase.txt","w")
    for text in f:
        f2.write(text.lower())
    print(f"převod dokončen do souboru {file}_lowerCase.txt")    
    f.close()  
    f2.close()
    return f2


def letterChanger(file):
    try:
        f = open(f"{file}.txt","r")

    except FileNotFoundError:
        print("soubor nenalezen")
        menu()        
    letter1 = input("Zadej písmeno, kterým chceš nahrazovat: ")
    letter2 = input("Zadej písmeno, které cheš nahradit: ")            
    f2 = open(f"{file}_changedLetters.txt","w")
    while True:
        char = f.read(1)   
        if char == "":
            break
        if char == letter2:
            char = letter1
        f2.write(char)
    f.close()  
    f2.close()
    print(f"záměna dokončena do souboru {file}_changedLetters.txt")

def generator():
    file = input("Zadej jméno souboru kam chceš data zapsat: ")
    numberOfWords = int(input("Zadej počet slovíček: "))         
    f = open(f"{file}_generatedText.txt","w")
    samohlasky = "aeiouy"
    souhlasky = "qwrtzpsdfghjklxcvbnm"
    for i in range(numberOfWords):
        for i in range(1,randint(3,5)):
            f.write(choice(samohlasky))
            f.write(choice(souhlasky))
        f.write(" ")
    print(f"generování dokončeno do souboru {file}_generatedText.txt")
        
    f.close()  

def statistic(file):
    letterList = []
    usedLettersList = []
    convertedFile = lowerCaseConvertor(file)
    try:
        f = open(f"{file}_lowerCase.txt","r")
    except FileNotFoundError:
        print("soubor nenalezen")
        menu()      
    f2 = open(f"{file}_statistic.txt","w")
    
    while True:
        char = f.read(1)   
        if char == "":
            break
        letterList.append(char)
    while (len(letterList)) > 0: 
        char = letterList[0]
        if char not in usedLettersList:
            usedLettersList.append(char)
            occurrences = letterList.count(f"{char}")
            f2.write(f"{char} {occurrences} \n")
        letterList.pop(0)
    f.close()  
    f2.close()
    print(f"výpočet dokončen do souboru {file}_statistic.txt")


def menu():
    print("""
    Vítej v našem programu na práci se soubory.

    Co chceš provést?
    1. Převod soubouru na malá písmena.
    2. Nahrazení výskytu zadaného znaku jiným zadaný znakem.
    3. Vypsat statistiku výskytu jednotlivých znaků v souboru.
    4. Generátor nádhodného textu.
    """)
    choice = int(input("volba: "))
    if choice == 1:
        fileRead = input("Zadej jmeno souboru: ")
        lowerCaseConvertor(fileRead)
    elif choice == 2:
        fileRead = input("Zadej jmeno souboru: ")
        letterChanger(fileRead)
    elif choice == 3:
        fileRead = input("Zadej jmeno souboru: ")
        statistic(fileRead)    
    elif choice == 4:
        generator()    
    else:
        print("Neplatná volba, vyber znovu...")
        time.sleep(1.70)
        menu()        
    
menu()
time.sleep(1.2)
print("\n cena jednoho použití je 5kč, posílejte ihned na účet pracvníku: 43-9362940287/0100. Děkujeme \n")
    