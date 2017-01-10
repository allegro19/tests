import os
def rename_files():
    #1 get files from the folder
    files=os.listdir(r'/run/media/amelie/E854-187C/prank')
    print(files)


    #2 for each file rename the filename
    for new_files in files:
        os.rename(new_files,new_files.translate(None, '0123456789'))
rename_files()

