import sys
import os
import PySimpleGUI as sg

# $ python lectern.py --process
# or -p. Creates a repository and empty notes.md file for each pdf in
# $ python lectern.py --genreadme
# or -g. Adds the notes to the present README.md file
# $ python lectern.py --bibgui
# or -b. Opens the GUI to generate a bibgen.bib file with selected articles.


# =================================
#            Process
# =================================

def process_pdf_articles():
    '''
    Create a folder, moves the pdf and add a notes.md file
    '''
    # List articles
    articles_to_process = os.listdir("articles/TO_PROCESS/")
    articles_to_process.remove("README.md")
    if len(articles_to_process)==0:
        print("No article to process.")
        return
    for article in articles_to_process:
        # Extract name
        article_name = article.split(".")[0]
        # Create directory
        path = "articles/"+article_name
        if os.path.exists(path):
            print(" - " + article_name + "\n ↳ Article directory already present, continuing...")
            continue
        os.mkdir(path)
        # Add bib file
        with open(path + "/biblio.bib", "w") as f:
            f.write(" ")
        # Add notes file
        with open(path + "/notes.md", "w") as f:
            f.write("<!-- Please prefix the notes with the date as in [22/12/2020] -->")
        os.rename("articles/TO_PROCESS/" + article, "articles/"+ article_name + "/" + article_name + ".pdf")
        print(" - " + article_name + "\n ↳ Article processed in its corresponding directory!")


# =================================
#         README generation
# =================================

def generate_readme():
    '''
    Appends the content of each note file to the README
    '''
    # Process all files
    articles = os.listdir("articles/")
    articles.remove("TO_PROCESS")
    article_dict = {}
    for article in articles:
        print(article)
        article_year = article.split("_")[0]
        article_author = article.split("_")[1]
        article_name = article.split("_")[2]
        dash_separated_header = article_year + "---" + article_author + "-" + article_name.replace(" ","-")
        paragraph_link = "[{0} - {1}, {2}](#{3})".format(article_year, article_author, article_name, dash_separated_header)
        content = ""
        with open("articles/" + article + "/notes.md", "r") as f:
            content = f.read()
        actual_paragraph = "### {0} - {1}, {2}".format(article_year, article_author, article_name) + "\n" + content + "\n\n---\n\n"
        article_dict[article_year + article_author] = (paragraph_link, actual_paragraph)

    items = article_dict.items()
    sorted_items = sorted(items)

    with open("README.md", "w") as f:
        f.write(''' ## VM-related articles

This repository contains the different articles and the bibliography (in BibTeX format) related to the VM world (to a LARGE extent). The notes in each of the folders, namely `notes.md` are integrated in the bibliography using a Python script in `utils.py`.  This script contains several useful helpers:

```bash
$ python lectern.py --process
# or -p. Creates a repository and empty notes.md file for each pdf in

$ python lectern.py --genreadme
# or -g. Adds the notes to the present README.md file

$ python lectern.py --bibgui
# or -b. Opens the GUI to generate a bibgen.bib file with selected articles.

$ python lectern.py --missbib
# or -m. Checks for missing or empty biblio files.
```

## Article notes
### Summary
''')
        for item in sorted_items:
            f.write(item[1][0] + "\n\n")

        f.write("\n\n\n")

        for item in sorted_items:
            f.write(item[1][1] + "\n")


# =================================
#        GUI bib generation
# =================================


def open_bib_gui():
    '''
    Opens a simple gui to select articles to include in a bib. The generated bib is called bibgen.bib.
    '''
    sg.theme('light brown 8')
    starting_path = "./articles"

    treedata = add_files_in_folder('', starting_path)
    layout = [[sg.Tree(
        data=treedata,
        headings=[],
        auto_size_columns=True,
        select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
        num_rows=20,
        col0_width=40,
        key='-TREE-',
        show_expanded=False,
        enable_events=True
    )]]

    window = sg.Window('Select articles to add to the bib', layout, resizable=True, finalize=True)
    window['-TREE-'].expand(True, True)  # Resize with the window (Full support for Tree element being released in 4.44.0)

    while True:     # Event Loop
        event, values = window.read()

        bib = []
        for folder in values['-TREE-']:
            with open(folder + "/biblio.bib","r") as f:
                bib += f.readlines()

        with open("bibgen.bib", "w") as f:
            f.writelines(bib)

        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
    window.close()


def add_files_in_folder(parent, dirname):
    # Base64 versions of images of a file. PNG files (may not work with PySimpleGUI27, swap with GIFs)
    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'
    files = sorted(os.listdir(dirname))
    treedata = sg.TreeData()
    for f in files:
        fullname = os.path.join(dirname, f)
        treedata.Insert(parent, fullname, f, values=[os.stat(fullname).st_size], icon=file_icon)
    return treedata


# =================================
#        Check missing bibs
# =================================

def check_missing_bibs():
    articles = os.listdir("articles/")
    articles.remove("TO_PROCESS")
    missing_bibs = []
    for article in articles:
        bib_path = "articles/" + article + "/biblio.bib"
        bib_file_exists = os.path.exists(bib_path) and os.path.getsize(bib_path) > 0
        if not bib_file_exists:
            missing_bibs.append(article)
    if len(missing_bibs) > 0:
        print("Missing bibs:")
        for bib in missing_bibs:
            print(" - " + bib)
    else:
        print("No missing bibs!")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Helper for Bibliography handling")
    parser.add_argument(
        "-p", "--process", action="store_true",
        help="Create a folder and a blank note file for each pdf article in TO_PROCESS"
    )
    parser.add_argument(
        "-g", "--generate", action="store_true",
        help="Modify the README with the different notes from the articles"
    )
    parser.add_argument(
        "-b", "--bibgui", action="store_true",
        help="Open the GUI to create a new biblio file"
    )
    parser.add_argument(
        "-m", "--missbib", action="store_true",
        help="Checks for missing bibliographic references"
    )

    args = parser.parse_args(sys.argv[1:])
    if args.process:
        process_pdf_articles()
        print("________________________________\n\nArticles in TO_PROCESS have their dedicated folder!")
    elif args.generate:
        generate_readme()
        print("________________________________\n\nNotes propagated into the main README!")
    elif args.bibgui:
        open_bib_gui()
        print("________________________________\n\nBiblio generated in bibgen.bib!")
    elif args.missbib:
        check_missing_bibs()
        print("________________________________\n\nBibliographic references checked!")
    else:
        parser.print_help()
