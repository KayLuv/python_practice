# coding: utf-8
"""
write vim configure file.
"""

def vimconfig():
    '''
    create or replace .vimrc file in ~
    '''
	#config contents
    con = '''syntax on
    set number
	filetype on
	set nocompatible
	set history=1000
	set autoindent
	set smartindent
	set tabstop=4
	set shiftwidth=4
	set showmatch
	set incsearch'''

    with open("~/.vimrc", "w") as code:
        code.write(con)

vimconfig()
