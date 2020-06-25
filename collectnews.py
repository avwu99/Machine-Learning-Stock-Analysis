import requests
import json
import os.path
import config
from datetime import datetime, date

paths = ['C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/consumercyc/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/energy/', 'C:/Users/PC/Documents/github_projects/Machine-Learning-Stock-Analysis/data/tech/']

consumercyc = ['ASNA', 'BBW', 'DLTH', 'EFOI', 'FAT', 'JILL', 'JMIA', 'KIRK', 'LUB', 'EVK', 'BGI', 'MFH', 'MKGI', 'MYT', 'LITB', 'VOXX', 'WBAI', 'DLTH', 'LE', 'FOSL', 'APEX', 'SQBG', 'DXLG', 'GMBL', 'APRN', 'BXG', 'BZH', 'CNTY', 'CVGI', 'ELA', 'FLL', 'GES', 'GRIL', 'HOME', 'HUD', 'JAKK', 'LAZY', 'LMPX', 'OSW', 'RGS', 'RRGB', 'VOXX', 'YJ', 'YTRA']
energy      = ['CRC', 'EXTN', 'GPP', 'MR', 'MTR', 'MVO', 'QES', 'SBOW', 'SAEX', 'SMPL', 'SND', 'TAT', 'TUSK', 'MCEP', 'DLNG', 'RCON', 'ROSE', 'ASC', 'MR', 'SDPI', 'AMTX', 'BRN', 'CEI', 'CNXM', 'DWSN', 'FTX', 'ICD', 'KLX', 'LONE', 'NINE', 'PFIE', 'PVAC', 'RNET', 'RNGR', 'TALO', 'TDW', 'TNK', 'TH', 'USAC', 'USWS', 'CCLP', 'GEOS', 'KLXE']
tech        = ['MYSZ', 'MRIN', 'NSYS', 'MICT', 'SPI', 'WSTL', 'VVPR', 'CPAH', 'CPSH', 'MIND', 'OSS', 'CIH', 'CREX', 'MTC', 'CLRO', 'PHUN', 'LPTH', 'IEC', 'PRTH', 'BOXL', 'NETE', 'MOGO', 'NNDM', 'AKTS', 'ADTN', 'AEYE', 'ALOT', 'AOSL', 'ATOM', 'AXTI', 'BDR', 'BLIN', 'CLSK', 'CMCM', 'DZSI', 'GILT', 'PXLW', 'QMCO', 'SFET', 'TACT', 'VERI', 'WATT']

all_comps = [consumercyc, energy, tech]

new_con = ['BLBD', 'BSET', 'CAAS', 'CATO', 'CONN', 'CPS', 'FFHL', 'FRAN', 'FRGI', 'FUV', 'MYE', 'PLAY', 'RMBL', 'SUP', 'TUP', 'XELB', 'XSPA', 'ZAGG']
new_ene = ['CHAP', 'CHK', 'CVIA', 'DSSI', 'ESTE', 'FTSI', 'GASS', 'GLP', 'ICD', 'KRP', 'LEU', 'LPI', 'MNRL', 'NBLX', 'NESR', 'NVGS', 'OMP', 'PBFX', 'PVAC', 'TRMD']
new_tec = ['AAOI', 'BNFT', 'CAMP', 'CMBM', 'EMAN', 'GNSS', 'IDN', 'INPX', 'LYTS', 'NEON', 'PLT', 'QUIK', 'RIOT', 'SNCR', 'SONM', 'SQNS', 'TUFN', 'VECO', 'VUZI', 'WRTC']

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
