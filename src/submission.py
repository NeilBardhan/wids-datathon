import os
import kaggle

def publish_submission(competition, message, path):
    """[summary]

    Args:
        competition ([type]): [description]
        path ([type]): [description]
    """
    kaggle.api.authenticate()
    kaggle.api.competition_submit(file_name=path, message=message, competition=competition, quiet=False)