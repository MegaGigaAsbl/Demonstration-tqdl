#
# Demonstration-tqdl
#
# https://github.com/MegaGigaAsbl/Demonstration-tqdl/tree/main
#

from time import sleep
from tqdm import tqdm

for i in tqdm( range(5) , ncols=60 ):
    sleep(1)
