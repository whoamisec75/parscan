import json
from parscan.core.args import with_subs, host, output, concurrency
from parscan.core.scanner import wayback, scan
from parscan.core.path import compatible_path
import parscan.core.config as mem 
from concurrent.futures import ThreadPoolExecutor
from parscan.core.colors import red, reset, green

print(green + '''                                      
   ___  ___ _ ____ ___ ____ ___ _ ___ 
  / _ \/ _ `// __/(_-</ __// _ `// _ \ 
 / .__/\_,_//_/  /___/\__/ \_,_//_//_/
/_/                                   ''' + reset)
print('                         @whoamisec' + '\n')
    
Qscan_dir = compatible_path(mem.__file__.replace(compatible_path('/core/config.py'), ''))

with open (Qscan_dir+'/db/db.json') as file:
    r3 = json.load(file)

def main():
    wayback(host, with_subs, output)
    with open(output) as URLs:
        read_URLs = URLs.readlines()
        f_url = list(set(read_URLs))
    with ThreadPoolExecutor(max_workers=concurrency) as exec:
        for u2 in f_url:
            exec.submit(scan(r3, u2))

    
    
