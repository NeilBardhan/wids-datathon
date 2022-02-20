import os
import kaggle
from zipfile import ZipFile

def get_kaggle_competition_data(competition, path):
    """
    """
    kaggle.api.authenticate()
    f = kaggle.api.competition_list_files(competition)
    if f:
        kaggle.api.competition_download_files(competition, path=path, force=True, quiet=False)
        zf = ZipFile('{p}{c}.zip'.format(p=path, c=competition))
        zf.extractall(path)
        zf.close()

get_kaggle_competition_data('widsdatathon2022', os.getcwd() + '/data/')

def create_validation_data(path):
    """[summary]

    Args:
        path ([type]): [description]
    """
    pass
