# external imports
import argparse  # Parse CLI arguments
import os  # get filenames for duplicity check

# internal imports
from download import dl, getTitleFromBaseUrl, baseURLcleanup
from process import saveTex, TexToPDF, getFileName


def pad2pdf(padurl: str, style: int, workingdir: str) -> None:
    """ generates a pdf from a etherpad link
    Params:

    padurl: Url to the pad. Example 'htttps://pad.example/p/test/'
    style: int of the style for the pdf
    workingdir: dir to save the final file
    """
    padurl = baseURLcleanup(padurl)
    title = getTitleFromBaseUrl(padurl)
    filename = getFileName(workingdir, title)
    content = dl(padurl)
    if __debug__:
        print(content, "\n\n")
    content = saveTex(content, style)
    if __debug__:
        print(content)
    TexToPDF(filename, content)

# TODO: set invalid file names


# for execute file directly
if __name__ == "__main__":
    # Parse cli arguments
    parser = argparse.ArgumentParser(description="Save your Etherpads styled as PDF's")
    parser.add_argument('-b', '--baseurl', dest='baseurl', help='BaseURL of the pad you like to save')
    parser.add_argument('-w', '--workingdir', dest='workingdir', default=".", help='Path to the directory the pad(s) are saved into; Default: .')
    parser.add_argument('-s', '--style', dest='style', default='0', help="the style for the final document; Default:0")
    args = parser.parse_args()
    workingdir = os.path.abspath(args.workingdir)
    # executes the main function
    pad2pdf(args.baseurl, int(args.style), workingdir)
