import requests
import json
import os.path
import config
from datetime import datetime, date

paths = ['C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/consumercyc/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/energy/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/tech/']

consumercyc = ['ASNA', 'BBW', 'DLTH', 'EFOI', 'FAT', 'JILL', 'JMIA', 'KIRK', 'LUB', 'EVK', 'BGI', 'MFH', 'MKGI', 'MYT', 'LITB', 'VOXX', 'WBAI', 'DLTH', 'LE', 'FOSL']
energy = ['CRC', 'EXTN', 'GPP', 'MR', 'MTR', 'MVO', 'QES', 'SBOW', 'SAEX', 'SMPL', 'SND', 'TAT', 'TUSK', 'MCEP', 'DLNG', 'RCON', 'ROSE', 'ASC', 'MR', 'SDPI']
tech = ['MYSZ', 'MRIN', 'NSYS', 'MICT', 'SPI', 'WSTL', 'VVPR', 'CPAH', 'CPSH', 'MIND', 'OSS', 'CIH', 'CREX', 'MTC', 'CLRO', 'PHUN', 'LPTH', 'IEC', 'PRTH']

all_comps = [consumercyc, energy, tech]

con = ['APEX', 'SQBG', 'DXLG', 'GMBL']
ene = ['VTNR', 'IO']
tec = ['BOXL', 'NETE', 'MOGO', 'NNDM', 'AKTS']

new_ene = ['AMTX', 'BRN', 'CEI', 'CNXM', 'DWSN', 'FTX', 'ICD', 'KLX', 'LONE', 'NINE', 'PFIE', 'PVAC', 'RNET', 'RNGR', 'TALO', 'TDW', 'TNK', 'TH', 'USAC', 'USWS']
new_ene_two = ['CCLP', 'GEOS', 'KLXE']

class stocknews():
    def __init__(self):
        self.url = 'https://stocknewsapi.com/api/v1?tickers='
        self.secondurl = '&items=50&sortby=rank&token=' + config.api_token

        self.savepath = 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/'

    def curr_date(self):
        """ Returns the current date

        Parameters:

        Returns:
        date-time in ISO 8601 format

        """

        today = datetime.now()

        return date(today.year, today.month, today.day).isoformat()

    def search(self, company, path):
        """ writes a json file to some path containing information from an api call

        Parameters:
        company (str) : ticker of company

        Returns:

        """
        comp_url =  self.url + company + self.secondurl
        responses = requests.get(comp_url).json()

        title = company + '.json'
        completepath = os.path.join(path, title)

        with open(completepath, 'w+') as curr_file:
            json.dump(responses, curr_file, indent=4)

        curr_file.close()

# martin_broker = stocknews()
#
# for i in range(len(con)):
#     martin_broker.search(con[i], paths[0])
#
# for u in range(len(energy)):
#     martin_broker.search(energy[u], paths[1])
#
# for y in range(len(tech)):
#     martin_broker.search(tech[y], paths[2])
#
# for y in range(len(ene)):
#     martin_broker.search(ene[y], paths[1])
#
# for y in range(len(tec)):
#     martin_broker.search(tec[y], paths[2])

# for u in range(len(new_ene)):
#     martin_broker.search(new_ene[u], paths[1])
#
# for u in range(len(new_ene_two)):
#     martin_broker.search(new_ene_two[u], paths[1])
