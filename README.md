# pad2pdf
a simple styled pdf export for etherpads

## Usage
usage: main.py [-h] [-b BASEURL] [-w WORKINGDIR] [-s STYLE]

Save your Etherpads styled as PDF's

options:
options:
  -h, --help            show this help message and exit
  -u BASEURL, --url BASEURL
                        URL of the pad you like to save
  -w WORKINGDIR, --workingdir WORKINGDIR
                        Path to the directory the pad(s) are saved into; Default: .
  -s STYLE, --style STYLE
                        the style for the final document; Default:0
  -n NUMBERS, --numberparagraphs NUMBERS
                        whether to nummerate the headings
  -c CONTENTTABLE, --contenttable CONTENTTABLE
                        whether to add a content table after the first headline
  -f COMMENTS, --footnote COMMENTS
                        whether comments in pad should turn into foodnotes
## dependencies
python 3.10
pylatex module
- Lualatex
- noto color emoji
## Roadmap
TODO: comment handeling
TODO: create templates
TODO: generate webfrontend
TODO: Error handling if no pad link provided


### Thanks to 
https://github.com/importantchoice/epad-saver for the basics of pad downloading.