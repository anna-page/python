
"""
create a function that called load_json() which loads data/json_data.json, extracts the sentences
and puts them into a pandas.DataFrame with three columns [sentence_id, word_id, word], where a row
is a one word.

NOTE! the json file is corrupt so you have to manually correct the errors in it to make it load.


DataFrame Example:

dataframe ->    | sentence_id | word_id | word   |
                -----------------------------------
                | 0           | 0       | "hello"|
                | 1           | 0       | "bye"  |

"""

import pandas as pd
import re
import json

def load_json(file):
    """Reads JSON from file and corrects incorrect usage of '.
    
    file: File path to JSON file.
    returns: Pandas dataframe based on provided JSON file.
    """
    
    # Temporary holder for raw data.
    data = None
    
    # Read file.
    with open(file, 'r') as f:
        data_raw = f.read()
    
    # Clean corrupted JSON.
    data_raw = re.sub(' \'', ' \"', data_raw)  # Remove leading ' with ".
    data_raw = re.sub('\'\n', '\"\n', data_raw)  # Replace trailing ' with ".
    data_raw = re.sub('}\s*{', '},{', data_raw)  # Replace }{ with },{.
    
    # Temporary holder for processed data.
    data = []
    
    # Iterate sentences and load to JSON from string.
    for sentence in json.loads(data_raw):
        sentence_id = sentence.get('id')  # Extract value for 'id'.
        
        # Iterate words in sentence.
        for word in sentence.get('words'):
            
            word_id = word.get('idx')  # Extract value for 'idx'.
            word = word.get('text')  # Extract value for 'text'.

            # Append sentence_id, word_id, and word.
            data.append({'sentence_id': sentence_id, 'word_id': word_id, 'word': word})

    # Create Pandas DataFrame from JSON.
    dataframe = pd.DataFrame.from_records(data)
    
    return dataframe

dataframe = load_json('data/json_data.json')
