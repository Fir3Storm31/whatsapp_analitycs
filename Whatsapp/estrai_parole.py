import re
import pandas as pd
import numpy as np
import os
from collections import Counter
import matplotlib.pyplot as plt

me = 'Francesco Catalanotti' # name of the person who is using the program
name_contact = 'Davide Dorigo' # name of the contact

name_file_chat = name_contact # name of the file that contains the chat

writer = me # name of the person who wrote the message
other_user = name_contact # name of the person who received the message

def estraiParole(name_contact, writer, other_user):
    # list that will collect all the words
    words = []
    # path to the directory that contains the folder with the chats
    path = 'C:/Users/franc/Desktop/Portfolio coding/Whatsapp'
    # open file for reading with utf-8 encoding
    with open(f"{path}/Whatsapp chats/WhatsApp Chat with {name_file_chat}.txt", 'r', encoding='utf-8') as file:
        # read file as text
        text = file.read()
        # split text by new line
        lines = text.split('\n')
        # drop the first line
        lines.pop(0)
        # set previous writer to None
        previous_writer = None
        # iterate over lines
        for line in lines:
            # check if line contains name of the person who received the message
            if re.search(other_user, line):
                previous_writer = other_user
            # check if line contains an invalid message
            elif re.search('<Media omitted>', line) or re.search('- You ', line) or re.search('changed their phone number to a new number.', line) or re.search('This chat is with a business account.', line):
                pass
            # check if line contains date
            elif re.search(r'\d+-\d+-\d+, \d+:\d+ \S.+\S. - ', line):
                # set previous_writer to the person who wrote the message
                previous_writer = writer
                # split line by name of the person who wrote the message
                split_line = line.split(f' - {writer}: ')
                # check if the message is empty
                if split_line[1] == 'null':
                    pass
                else:
                    # split message by space to get all the words
                    message = split_line[1].split()
                    # iterate over words
                    for word in message:
                        # check if word is longer than 3 characters
                        if len(word) > 3:
                            # append word to words list
                            words.append(word.lower().strip('\'"?!,.():;*/-_'))
            # check if line is the continuation of a message
            else:
                # check if previous_writer is the person who wrote the message
                if previous_writer == writer:
                    # split line by space to get all the words
                    message = line.split()
                    # iterate over words
                    for word in message:
                        # check if word is longer than 3 characters
                        if len(word) > 3:
                            # append word to words list
                            words.append(word.lower().strip('\'"?!,.():;*/-_'))
        # create/open a new file to store the words
        with open(f'{path}/Elaborazioni/words/Words with {name_file_chat}.py', 'w', encoding='utf-16') as file:
            # write words to file
            file.write(f'{words}')
        # create a Counter object to count the words
        collected_words = Counter(words)
        # return the Counter object
        return collected_words
    
# function to create a bar graph
def barGraph(collected_words):
    # get the 50 most common words
    first50 = collected_words.most_common(50)
    # create a DataFrame from the list of tuples
    word_freq = pd.DataFrame(first50, columns=['words', 'count'])
    # create a figure and axes
    fig, ax = plt.subplots(figsize=(15, 8))
    # Plot horizontal bar graph
    word_freq.sort_values(by='count').plot.barh(x='words',
                        y='count',
                        ax=ax,
                        color="brown")
    # set title
    ax.set_title(f"Common Words Found written by {writer}")
    plt.show() # show the graph

# call the functions
#barGraph(estraiParole(name_contact, writer, other_user))

if __name__ == '__main__':
    # ask the user to input the informations needed
    name_contact = input('Name of the contact: ')
    writer = input('Name of the person who wrote the message: ')
    other_user = input('Name of the person who received the message: ')
    # call the functions
    barGraph(estraiParole(name_contact, writer, other_user))