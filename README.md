The files listed in NZBs generated from sites such as binsearch and 
nzbindex are typically unordered. Newsreaders such as nzbget download 
files in the order they are listed within the NZB file and there is no
ability to sort these within the newsreader client itself. If you want to 
check the files within a RAR prior to downloading the entire archive,
having the files you are fetching is critical. This script will parse the 
XML in an NZB file passed as an argument and sort based on filename,
overwriting the original NZB file. 

Usage: python nzb_sorter.py test.nzb 

