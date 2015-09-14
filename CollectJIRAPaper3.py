import re
import os
import subprocess
import commands
from datetime import datetime
import Levenshtein


file1 = open('AllFiles','r')

for l in file1:

	