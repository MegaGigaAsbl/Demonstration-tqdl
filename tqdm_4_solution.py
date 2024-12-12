#
# Demonstration-tqdm
#
# https://github.com/MegaGigaAsbl/Demonstration-tqdm/tree/main
#

from time import sleep
from tqdm import tqdm

for i in tqdm( range(5) , ncols=60 ):
    sleep(1)
