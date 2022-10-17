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
            f.write("")
        # Add notes file
        with open(path + "/notes.md", "w") as f:
            f.write("<!-- Please prefix the notes with the date as in [22/12/2020] -->\n\n##### tags: unread")
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



def add_files_in_folder(parent, dirname, ignored_files):
    # Base64 versions of images of a file. PNG files (may not work with PySimpleGUI27, swap with GIFs)
    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'
    files = sorted(os.listdir(dirname))
    for ifile in ignored_files:
        files.remove(ifile)
    treedata = sg.TreeData()
    for f in files:
        fullname = os.path.join(dirname, f)
        treedata.Insert(parent, fullname, f, values=[os.stat(fullname).st_size], icon=file_icon)
    return treedata


def open_bib_gui():
    '''
    Opens a simple gui to select articles to include in a bib. The generated bib is called bibgen.bib.
    '''
    sg.theme('light brown 8')
    starting_path = "./articles"

    treedata = add_files_in_folder('', starting_path, ["TO_PROCESS", ".gitignore"])
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


# =================================
#        Check missing bibs
# =================================

def check_missing_bibs():
    articles = os.listdir("articles/")
    articles.remove("TO_PROCESS")
    missing_bibs = []
    for article in articles:
        bib_path = "articles/" + article + "/biblio.bib"
        bib_file_filled = os.path.exists(bib_path) and os.path.getsize(bib_path) > 0
        # Check if it consists of a single space character
        if bib_file_filled:
            with open(bib_path, "r") as f:
                if f.readline() == " ":
                    bib_file_filled = False
        if not bib_file_filled:
            missing_bibs.append(article)
    if len(missing_bibs) > 0:
        print("Missing bibs:")
        for bib in missing_bibs:
            print(" - " + bib)
    else:
        print("No missing bibs!")


# =================================
#              Tags
# =================================

def collect_tags():
    articles = os.listdir("articles/")
    articles.remove("TO_PROCESS")
    tags = {}
    for article in articles:
        # Extract the last line
        with open("articles/" + article + "/notes.md", 'r') as f:
            last_line = f.readlines()[-1]
        # Process the last line
        if last_line.startswith("##### tags:"):
            # Extract tags
            article_tags = last_line.split("##### tags:")[1].split(",")
            article_tags = [tag.strip() for tag in article_tags]
            # Add the article to the corresponding entry in the dict
            for tag in article_tags:
                if tag in tags:
                    tags[tag].append(article)
                else:
                    tags[tag] = [article]
    return dict(sorted(tags.items()))


def display_tags(tags):
    nb_digits = len(str(len(tags.keys())))
    print("Available tags:\n")
    for i, tag in enumerate(tags):
        sub_str = str(i+1) + "."
        print("{0:>{padding}}{1}".format(sub_str, tag, padding=(nb_digits + 1)))
    selection = int(input("\nSelect the tag you want:\n_______________________\n> "))
    return list(tags.items())[selection - 1]


def create_tagged_directory(tag_result):
    tag_name, tagged_articles = tag_result
    tag_dir_path = "tags/" + tag_name
    if not os.path.exists(tag_dir_path):
        os.makedirs(tag_dir_path)
    for article in tagged_articles:
        sym_src_dir = "../../articles/{}".format(article)
        sym_dst_dir = "tags/{}/{}".format(tag_name, article)
        temp_link = sym_dst_dir + ".new"
        os.symlink(sym_src_dir, temp_link)
        os.rename(temp_link, sym_dst_dir)


def handle_tag():
    tag_dict = collect_tags()
    tag_selection = display_tags(tag_dict)
    create_tagged_directory(tag_selection)


# =================================
#          Main and CLI
# =================================

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
    parser.add_argument(
        "-t", "--tags", action="store_true",
        help="Display tags to choose from and get corresponding articles"
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
    elif args.tags:
        handle_tag()
        print("________________________________\n\nTag directory created!")
    else:
        parser.print_help()
