#
# Demonstration-tqdm
#
# https://github.com/MegaGigaAsbl/Demonstration-tqdm/tree/main
#

from time import sleep
from tqdm import tqdm

for i in tqdm( range(5) , desc="MegaGiga" ):
    sleep(1)
