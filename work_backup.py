# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:23:28 2015

@author: Dominik
"""

import datetime
import shutil
import errno


SOURCE_DIRECTORY = 'C:/Users/Dominik/Work'
EXTERNAL_DRIVE_DIRECTORY = 'E:/md_backup_{0}'

def get_backup_directory(base_directory):
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    return base_directory.format(date)
 
def copy_files_to(src, dstdir):
    try:
        shutil.copytree(src, dstdir)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dstdir)
        else:
            print('Directory not copied. Error: %s' % e)
            
def copy_files(dstdir):
    copy_files_to(SOURCE_DIRECTORY, dstdir)
    
def perform_backup(base_directory):
    backup_directory = get_backup_directory(base_directory)
    copy_files(backup_directory)

def main():
    perform_backup(EXTERNAL_DRIVE_DIRECTORY)

if __name__ == '__main__':
    main()