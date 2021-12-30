# external imports
import argparse  # Parse CLI arguments
import os  # get filenames for duplicity check

# internal imports
from download import dl, getTitleFromBaseUrl, baseURLcleanup
from process import saveTex, TexToPDF, getFileName


def pad2pdf(padurl: str, style: int, workingdir: str, numbers: bool, contenttable: bool, comments: bool) -> None:
    """ generates a pdf from a etherpad link
    Params:

    padurl: str\tUrl to the pad. Example 'htttps://pad.example.com/p/test/'
    style:int \t int of the style for the pdf
    workingdir:str \tdir to save the final file
    numbers:bool \twhether to nummerate the headings
    contenttable:bool \t whether to add a content table after the first headline
    comments:bool \t whether turn comments into foodnotes
    """
    padurl = baseURLcleanup(padurl)
    title = getTitleFromBaseUrl(padurl)
    filename = getFileName(workingdir, title)
    content = dl(padurl)
    # print(content, "\n\n")
    content = saveTex(content, style, numbers, contenttable, comments)
    # print(content)
    TexToPDF(filename, content)


# for execute file directly
if __name__ == "__main__":
    # Parse cli arguments
    parser = argparse.ArgumentParser(description="Save your Etherpads styled as PDF's")
    parser.add_argument('-u', '--url', dest='baseurl', help='URL of the pad you like to save')
    parser.add_argument('-w', '--workingdir', dest='workingdir', default=".", help='Path to the directory the pad(s) are saved into; Default: .')
    parser.add_argument('-s', '--style', dest='style', default='0', help="the style for the final document; Default:0")
    parser.add_argument('-n', '--numberparagraphs', dest='numbers', default=True, help="whether to nummerate the headings")
    parser.add_argument('-c', "--contenttable", dest="contenttable", default=True, help='whether to add a content table after the first headline')
    parser.add_argument('-f', '--footnote', dest="comments", default=False, help="whether comments in pad should turn into foodnotes")
    args = parser.parse_args()
    workingdir = os.path.abspath(args.workingdir)
    # executes the main function
    pad2pdf(args.baseurl, int(args.style), workingdir, bool(args.numbers), bool(args.contenttable), bool(args.comments))
