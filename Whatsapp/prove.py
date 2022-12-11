import csv
from collections import Counter
import os
import pandas as pd
import re
import json

path = 'C:/Users/franc/Desktop/Portfolio coding/Whatsapp'

me = 'Francesco Catalanotti'
nome_contatto = 'Elena Zanchi'

with open(f'{path}/Elaborazioni/json/WhatsApp Chat with {nome_contatto}.json') as json_file:
    data = json.load(json_file)
    data['intents'][1]['patterns'].append('ciao')
    with open(f'{path}/Elaborazioni/json/WhatsApp Chat with {nome_contatto}.json', 'w') as outfile:
        json.dump(data, outfile)
