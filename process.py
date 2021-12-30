from datetime import datetime  # get timestamp for filename
from pylatex import Document, NoEscape, escape_latex, Package, Command
from re import sub

from pylatex.base_classes.command import UnsafeCommand


def make_dict(text: str) -> dict:
    return dict()


def handle_comments(text: str, comments: bool) -> str:
    if comments:
        if "<div id=\"comments\">" in text:
            text, commentspart = text.split("<div id=\"comments\">", 1)
            commentsdict = make_dict(commentspart)
            raise NotImplementedError
    else:
        text = sub("<span class=\"comment [^\"]*\">", "", text)
        text = sub("<sup><a href=[^*]*\\*</a></sup></span>", "", text)
        text = sub("<div id=\"comments\">.*", "", text)
    return text


def saveTex(text: str, style: int, numbers: bool, contenttable: bool, comments: bool) -> str:
    # Preprocessing text
    _, text = text.split("<body>\n")
    text, _ = text.split("</body>")
    # escape
    text = escape_latex(text)
    text = handle_comments(text, comments)
    # rewrite to latex
    text = text.replace("<br>", "\\\\\n")
    text = text.replace("<br/>", "\\\\\n")  # escaped slashes -> python docs
    text = text.replace("<strong>", "\\textbf{").replace("</strong>", "}")
    text = text.replace("<em>", "\\textit{").replace("</em>", "}")
    text = text.replace("<u>", "\\underline{").replace("</u>", "}")
    text = text.replace("<s>", "\\sout{").replace("</s>", "}")
    text = text.replace("\\\\\n<code>", "\\begin{lstlisting}\n").replace("</code>\\\\", "\n\\end{lstlisting}")
    if contenttable:
        text = text.replace("<h1>", "\\date{}\n\\title{").replace("</h1>\\\\", "}\n\\maketitle\n\\renewcommand*\\contentsname{Inhalt}\n\\tableofcontents")  # FIXME: Multiple tableofcontents
    else:
        text = text.replace("\\\\<h1>", "\\date{}\n\\title{").replace("</h1>\\\\", "}\n\\maketitle")
    if numbers:
        text = text.replace("\\\\<h2>", "\\section{").replace("</h2>\\\\", "}")
        text = text.replace("\\\\<h3>", "\\subsection{").replace("</h3>\\\\", "}")
        text = text.replace("\\\\<h4>", "\\subsubsection{").replace("</h4>\\\\", "}")
    else:
        text = text.replace("\\\\<h2>", "\\section*{").replace("</h2>\\\\", "}")
        text = text.replace("\\\\<h3>", "\\subsection*{").replace("</h3>\\\\", "}")
        text = text.replace("\\\\<h4>", "\\subsubsection*{").replace("</h4>\\\\", "}")
    text = text.replace("\\\\<ol start=\"1\" class=\"number\">", "\\begin{enumerate}").replace("</ol>\\\\", "\\end{enumerate}")
    text = text.replace("\\\\<ul class=\"bullet\">", "\\begin{itemize}").replace("\\\\<ul class=\"indent\">", "\\begin{itemize}").replace("</ul>\\\\", "\n\\end{itemize}")
    text = text.replace("<li>", "\n\\item ").replace("</li>", "")
    # Fallback replacement without \\ or \n required
    text = text.replace("<code>", "\\begin{lstlisting}\n").replace("</code>", "\n\\end{lstlisting}")
    if contenttable:
        text = text.replace("<h1>", "\\date{}\n\\title{").replace("</h1>", "}\n\\maketitle\n\\renewcommand*\\contentsname{Inhalt}\n\\tableofcontents")
    else:
        text = text.replace("<h1>", "\\date{}\n\\title{").replace("</h1>", "}\n\\maketitle")
    if numbers:
        text = text.replace("<h2>", "\\section{").replace("</h2>", "}")
        text = text.replace("<h3>", "\\subsection{").replace("</h3>", "}")
        text = text.replace("<h4>", "\\subsubsection{").replace("</h4>", "}")
    else:
        text = text.replace("<h2>", "\\section*{").replace("</h2>", "}")
        text = text.replace("<h3>", "\\subsection*{").replace("</h3>", "}")
        text = text.replace("<h4>", "\\subsubsection*{").replace("</h4>", "}")
    text = text.replace("<ol start=\"1\" class=\"number\">", "\\begin{enumerate}").replace("</ol>", "\\end{enumerate}")
    text = text.replace("<ul class=\"bullet\">", "\\begin{itemize}").replace("<ul class=\"indent\">", "\\begin{itemize}").replace("</ul>", "\n\\end{itemize}")
    text = text.replace("<li>", "\n\\item ").replace("</li>", "")
    return text


def getFileName(workingdir, title) -> str:
    """Generates the file name for a downloaded pad dump"""
    # build timestamp which is appended to the file to avoid overwriting an existing dump
    dt = datetime.now()
    timestamp = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day) + "-" + str(dt.hour) + "-" + str(dt.minute) + "-" + str(dt.second)
    # return filename
    return workingdir + "/" + title + "-" + timestamp


def TexToPDF(filename: str, tex: str) -> None:
    doc = Document()
    doc.packages.append(Package('listings'))
    doc.packages.append(Package('ulem'))
    doc.packages.append(Package('emoji'))
    # FIXME: DIsplay emojis
    #doc.append(Command("directlua", """luaotfload.add_fallback   ("emojifallback",    {      "Noto Emoji:mode=harf;"    })"""))
    #doc.append(Command("setmainfont", "texgyretermes-regular", """  BoldFont       = texgyretermes-bold,  ItalicFont     = texgyretermes-italic,  BoldItalicFont = texgyretermes-bolditalic,  RawFeature={fallback=emojifallback}    """))
    doc.append(NoEscape(tex))
    # print(doc)
    doc.generate_pdf(filepath=filename, clean_tex=False, compiler="lualatex")