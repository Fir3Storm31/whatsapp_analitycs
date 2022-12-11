import re
import pandas as pd
import numpy as np
import os
from collections import Counter
import matplotlib.pyplot as plt

path = 'C:/Users/franc/Desktop/Portfolio coding/Whatsapp'

me = 'Francesco Catalanotti'
nome_contatto = 'Elena Zanchi'

nome_cartella = nome_contatto

writer = me
other_user = nome_contatto

def estraiMessaggi(nome_contatto, writer, other_user):
    conversazioni = [["",""]]
    # "C:\Users\franc\Desktop\Portfolio coding\Whatsapp_chats\Whatsapp chats\WhatsApp Chat with Marco Pinciaroli.txt"
    with open(f"{path}/Whatsapp chats/WhatsApp Chat with {nome_cartella}.txt", 'r', encoding='utf-8') as file:
        # read file as text
        text = file.read()
        # split text by new line
        lines = text.split('\n')
        # drop the first line
        lines.pop(0)

        previous_line = None
        previous_message = None

        # iterate over lines
        for line in lines:
            # check if line contains name
            if re.search(other_user, line):
                previous_line = other_user
                previous_message = line.split(f' - {other_user}: ')
                previous_message = previous_message[1]
            elif re.search('<Media omitted>', line) or re.search('- You ', line) or re.search('changed their phone number to a new number.', line) or re.search('This chat is with a business account.', line):
                pass
            # check if line contains date
            elif re.search(r'\d+-\d+-\d+, \d+:\d+ \S.+\S. - ', line):
                # split line by colon
                split_line = line.split(f' - {writer}: ')
                # split message by space
                #print(split_line)
                if split_line[1] == 'null':
                    previous_line = writer
                    pass
                else:
                    message = split_line[1]
                    if previous_line == writer:
                        conversazioni[-1][1] = conversazioni[-1][1] + '. ' +message
                    else: 
                        conversazioni.append([previous_message, message])
                    previous_line = writer
        
            else:
                if previous_line == writer:
                    conversazioni[-1][1] = conversazioni[-1][1] + ' ' + line

        
        return conversazioni
    
def cloudOfWords(conversazioni):

    conversazioni_table = pd.DataFrame(conversazioni, columns=['input', 'risposta'])

    open(f'{path}/Elaborazioni/csv/WhatsApp Chat with {nome_contatto}.csv', 'w').close()

    conversazioni_table.to_csv(f'{path}/Elaborazioni/csv/WhatsApp Chat with {nome_contatto}.csv', index=False)

cloudOfWords(estraiMessaggi(nome_contatto, writer, other_user))