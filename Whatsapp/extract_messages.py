import re
import pandas as pd
import numpy as np
import os
from collections import Counter
import matplotlib.pyplot as plt

### Exemples of use ###

# path 
path = 'C:/Users/user/Desktop/whatsapp_analitycs/Whatsapp'
# name of the person who is using the program
me = 'Francesco Catalanotti'
# name of the contact
name_contact = 'Mario Rossi'
# name of the file that contains the chat
nome_cartella = name_contact
# name of the person who wrote the message
writer = me
# name of the person who received the message
other_user = name_contact

# list that will collect all the tuples (question, answer)
def extractMessages(name_contact, writer, other_user):
    # list that will collect all the tuples (question, answer)
    conversations = [["",""]]
    # open file for reading with utf-8 encoding
    with open(f"{path}/Whatsapp chats/WhatsApp Chat with {nome_cartella}.txt", 'r', encoding='utf-8') as file:
        # read file as text
        text = file.read()
        # split text by new line
        lines = text.split('\n')
        # drop the first line
        lines.pop(0)
        # set previous writer and message to None
        previous_writer = None
        previous_message = None

        # iterate over lines
        for line in lines:
            # check if line contains the name of the person who received the message
            if re.search(other_user, line):
                previous_writer = other_user
                previous_message = line.split(f' - {other_user}: ')
                # set the message as previous message
                previous_message = previous_message[1]
            # check if line contains an invalid message
            elif re.search('<Media omitted>', line) or re.search('- You ', line) or re.search('changed their phone number to a new number.', line) or re.search('This chat is with a business account.', line):
                pass
            # check if line contains date
            elif re.search(r'\d+-\d+-\d+, \d+:\d+ \S.+\S. - ', line):
                # split line by colon
                split_line = line.split(f' - {writer}: ')
                # check if the message is empty
                if split_line[1] == 'null':
                    previous_writer = writer
                    pass
                else:
                    message = split_line[1]
                    # check if the previous writer is the same as the current writer
                    if previous_writer == writer:
                        # append the message to the previous message
                        conversations[-1][1] = conversations[-1][1] + '. ' + message
                    else: 
                        # append the message to the list of conversations
                        conversations.append([previous_message, message])
                    # set the current writer as the previous writer
                    previous_writer = writer
            else:
                if previous_writer == writer:
                    conversations[-1][1] = conversations[-1][1] + ' ' + line
        # return the list of conversations
        return conversations
    
def conversationToCsv(conversations):
    # create a dataframe from the list of conversations
    conversations_table = pd.DataFrame(conversations, columns=['input', 'risposta'])
    # create a folder for the csv files
    open(f'{path}/Elaborazioni/csv/WhatsApp Chat with {name_contact}.csv', 'w').close()
    # save the dataframe as csv file
    conversations_table.to_csv(f'{path}/Elaborazioni/csv/WhatsApp Chat with {name_contact}.csv', index=False)

if __name__ == "__main__":
    # ask the user to insert the informations needed
    name_contact = input('Inserisci il nome del contatto: ')
    writer = input('Inserisci il nome di chi scrive: ')
    other_user = input('Inserisci il nome di chi riceve i messaggi: ')
    conversationToCsv(extractMessages(name_contact, writer, other_user))