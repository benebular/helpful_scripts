## Using regex to extract relevant information from text files
# Author: Ben Lang, bcl267@nyu.edu

# import packages
import re
import csv
import pandas as pd
from pathlib import Path
dir = '/Users/(accountname)/(wherever)' # your default path with the text files that you saved from the HTML inspection
url = 'https://nyu.ca1.qualtrics.com/WRQualtricsControlPanel_rel/File.php?F=' # here you will want to insert the front part of the URL that is the same for every sound
string = Path('the_doc_nonnative_tc.txt').read_text() # the text file from the HTML inspection

# for trials
id_pattern = r'id=["](.*?)["] ui-tree-' # template to pull out anything that matches what is inside r'': in this case all items between id and ui-tree- that are inside double quotes
id_matches = re.findall(id_pattern,string) # execute the function to extract data
print(len(re.findall(id_pattern,string))) # sanity check the length (helpful if you know about how many files you have per page from the website)
print(id_matches) # print the matches to double check you grabb the right strings

phon_pattern = r'[~](.*?)\.wav' # template to find all of the information between the ~ symbol and the .wav extension
phon_matches = re.findall(phon_pattern,string) # execute the function to extract data
print(len(re.findall(phon_pattern,string))) # sanity check the length (helpful if you know about how many files you have per page from the website)
print(phon_matches) # print the matches to double check you grabb the right strings

phon_entry = [] # instatiate a blank list to fill with entries
for i in phon_matches: # for each item in the phon_matches list you made above
  if i not in phon_entry: # if the item is not in the new list already
    phon_entry.append(i) # append the item to the list

df_matches = pd.DataFrame({'phon': phon_entry, 'url': url, 'id': id_matches}) # create a pandas DataFrame with an index for each list
df_matches['finalurl'] = df_matches['url'] + df_matches['id'] # concatenate the urls so they are all one big string in the same column
print(df_matches) # sanity check to view the data

df_matches.to_excel(excel_writer=dir+'matches_nonnative_tc_round4.xls') # send the df to an excel file and then change to whatever format you may need from there
