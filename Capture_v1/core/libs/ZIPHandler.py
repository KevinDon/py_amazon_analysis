import os
import zipfile
import zlib


def zip_str(str=''):
    return zlib.compress(str)


def unzip_str(str=''):
    return zlib.decompress(str)


def zip_files(file_list, zip_name, out_path='.\\'):
    zip_handler = zipfile.ZipFile(os.path.abspath(os.path.join(out_path, zip_name)), 'w', zipfile.ZIP_DEFLATED)
    for file in file_list:
        print('Compressing zip ', file)
        zip_handler.write(file)
    zip_handler.close()
    print('Compressing Finished')


def unzip_file(file_path, out_path='.\\'):
    if os.path.exists(out_path) is False:
        os.makedirs(os.path.abspath(out_path), 644)
    zip_handler = zipfile.ZipFile(file_path, 'r')
    for file in zip_handler.namelist():
        zip_handler.extract(file, os.path.abspath(out_path))

