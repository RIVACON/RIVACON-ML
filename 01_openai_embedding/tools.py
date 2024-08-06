# Just an additional function to load our local openai key
import os
import openai
from openai import OpenAI

def init_openai():
    '''
    Return an OpenAI instance started with our licence key.
    '''
    # Configure the OpenAI API Licence key
    keypath = "extra" + os.sep + "openai_key.txt"
    tmp_file = open(keypath, "r")
    tmp = tmp_file.readline()
    # The licence key ist stored in the second line
    the_key = tmp_file.readline().strip()
    tmp_file.close()
    openai.api_key = the_key
    return OpenAI(api_key=the_key)
#---
