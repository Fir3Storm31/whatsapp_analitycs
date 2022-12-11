import pandas as pd
import re
import json

# path to the directory that contains the folder with the chats
path = 'C:/Users/franc/Desktop/Portfolio coding/Whatsapp'
# name of the person who is using the program
me = 'Francesco Catalanotti' 
# name of the contact
name_contact = 'Elena Zanchi' 
# list of stopwords
stopwords = [r'\s+ei\s', r'\s+oi\s', 'come stai', 'come va', 'tutto bene?', 'che succede']
# tag
tag = 'hello'

def estrapolaSaluti(name_contact, tag, stopwords):
    # read csv file and drop first row and rows with NaN values
    ds = pd.read_csv(f'{path}/Elaborazioni/csv/WhatsApp Chat with {name_contact}.csv').drop(0).dropna()
    # reset index
    ds.reset_index(drop=True, inplace=True)
    patterns = [""]
    responses = [""]
    # iterate over rows
    for i in range(len(ds.index)-1):
        # iterate over stopwords
        for stopword in stopwords:
            # check if row contains the stopword
            if re.search(stopword, ds['input'][i+1]):
                # check if the previous row is the same as the current row
                if responses[-1] == ds.iloc[i+1].tolist()[1]:
                    pass
                else:
                    # append the current row to patterns and responses
                    patterns.append(ds.iloc[i+1].tolist()[0])
                    responses.append(ds.iloc[i+1].tolist()[1])
    # remove first element of patterns and responses
    patterns.pop(0)
    responses.pop(0)
    # create/open json file
    with open(f'{path}/Elaborazioni/json/WhatsApp Chat with {name_contact}.json') as json_file:
        # load json file
        data = json.load(json_file)
        # append the new data to the json file
        data['intents'].append({
        'tag': tag,
        'patterns': patterns,
        'responses': responses,
        })
        # open json file and write the new data
        with open(f'{path}/Elaborazioni/json/WhatsApp Chat with {name_contact}.json', 'w') as outfile:
            json.dump(data, outfile)

#estrapolaSaluti(name_contact, 'notte', ['buonanotte', 'notte'])

if __name__ == '__main__':
    # ask the user to input the informations needed
    name_contact = input('Name of the contact: ')
    tag = input('Tag: ')
    stopwords = input('Stopwords: ')
    # call the function
    estrapolaSaluti(name_contact, tag, stopwords)