

import fitz
from unidecode import unidecode

from os import DirEntry, curdir, getcwd, chdir, rename
from glob import glob as glob

directory = 'arquivos'
chdir(directory)

pdf_list = glob('*.pdf')

for pdf in pdf_list:
    with fitz.open(pdf) as pdf_obj:
        text = pdf_obj[0].get_text()
    new_file_name = text.split("\n", 1)[1].strip().title().replace(':', '-')
    new_file_name = new_file_name.split(',')[0].replace('\n \n', ',').replace('\n', '').split(',')[0]

    u = unidecode(new_file_name, "utf-8")
    # print(u)
    rename(pdf, u + '.pdf')