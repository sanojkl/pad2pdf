from datetime import datetime  # get timestamp for filename


def saveTex(filename: str, text: str, style) -> None:
    raise NotImplementedError


def getFileName(workingdir, title):
    """Generates the file name for a downloaded pad dump"""
    # build timestamp which is appended to the file to avoid overwriting an existing dump
    dt = datetime.now()
    timestamp = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day) + "-" + str(dt.hour) + "-" + str(dt.minute) + "-" + str(dt.second)
    # return filename
    return workingdir + "/" + title + "-" + timestamp + ".tex"


def TexToPDF(filename) -> None:
    raise NotImplementedError