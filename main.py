import subprocess
import re

out = subprocess.check_output(['sudo', 'python3', '-m', 'mh_z19']).decode('utf-8')


re_out = re.match(r'{\"co2\": (?P<conc>\d+)}',out)
CO2_conce = int(re_out.group('conc'))
print(CO2_conce)

