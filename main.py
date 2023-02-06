import subprocess
import re
import requests
import json
import database
from sqlalchemy.orm import sessionmaker
import co2_concentrate
import os
from os.path import join, dirname
from dotenv import load_dotenv
out = subprocess.check_output(
    ['sudo', 'python3', '-m', 'mh_z19']).decode('utf-8')


re_out = re.match(r'{\"co2\": (?P<conc>\d+)}', out)
CO2_conce = int(re_out.group('conc'))
print(CO2_conce)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
WEB_HOOK_URL = os.environ.get("WEBHOOK_URL")
requests.post(WEB_HOOK_URL, data=json.dumps({
    'text': u'CO2の濃度は' + str(CO2_conce) + u' ppmです',
    'username': 'Mr. CO2 monitor',
    'icon_emoji': u':smile_cat:',
    'link_names': 1,
}))

maker = sessionmaker(bind=database.ENGINE)
session = maker()
co2 = co2_concentrate.Co2Concentrate()
co2.concentrate = CO2_conce
session.add(co2)
session.commit()
