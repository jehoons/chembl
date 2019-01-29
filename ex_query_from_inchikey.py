import os
import sys 
import json
import pandas as _pandas 
from os.path import join as _join
from matplotlib_venn import venn2
from tqdm import tqdm
from chembl_webresource_client.unichem import unichem_client as unichem
import requests 


def test_this(): 
    ret = unichem.get('AAOVKJBEBIDNHE-UHFFFAOYSA-N')
    filename = 'test.json'
    with open(filename, 'w') as f: 
        json.dump(ret, f, indent=4)


if __name__ == '__main__': 

    infile = sys.argv[1] 
    outfile = sys.argv[2]

    # import ipdb; ipdb.set_trace()
    
    with open(infile) as data_file:    
        data = json.load(data_file)

    inputkey = data['inchi-key']
    
    try: 
        ret = unichem.get(inputkey)
    except requests.exceptions.RetryError: 
        ret = {} 

    with open(outfile, 'w') as f: 
        json.dump(ret, f, indent=4)

