import os, shutil, sys, re, urllib.request, pytest
from math import ceil
from bs4 import BeautifulSoup
from typing import Union
from tqdm import tqdm
import requests

def GetSCP(scpid,):
  if scpid < 1000:
    url = "http://scp-wiki.wikidot.com/scp-series"
  elif scpid % 1000 == 0:
      url = f"http://scp-wiki.wikidot.com/scp-series-{int(scpid/1000+1)}"
  else:
    url = f"http://scp-wiki.wikidot.com/scp-series-{ceil(scpid/1000, 0)}"
    
  

