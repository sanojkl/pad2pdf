from datetime import datetime  # get timestamp for filename
from pylatex import Document, NoEscape, escape_latex, Package


def saveTex(text: str, style: int) -> str:
    # Preprocessing text
    _, text = text.split("<body>\n")
    text, _ = text.split("</body>")
    # TODO: remove comments (optional)
    # escape
    text = escape_latex(text)
    print(text)
    # rewrite to latex
    text = text.replace("<br>", "\\\\")
    text = text.replace("<br/>", "\\\\")  # escaped slashes -> python docs
    text = text.replace("<strong>", "\\textbf{").replace("</strong>", "}")
    text = text.replace("<em>", "\\textit{").replace("</em>", "}")
    text = text.replace("<u>", "\\underline{").replace("</u>", "}")
    text = text.replace("<code>", "\\begin{lstlisting}").replace("</code>", "\\end{lstlisting}")
    return text


def getFileName(workingdir, title):
    """Generates the file name for a downloaded pad dump"""
    # build timestamp which is appended to the file to avoid overwriting an existing dump
    dt = datetime.now()
    timestamp = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day) + "-" + str(dt.hour) + "-" + str(dt.minute) + "-" + str(dt.second)
    # return filename
    return workingdir + "/" + title + "-" + timestamp


def TexToPDF(filename: str, tex: str) -> None:
    doc = Document(data=NoEscape(tex),)
    doc.packages.append()
    print(doc.data)
    doc.generate_pdf(filepath=filename, clean_tex=False)