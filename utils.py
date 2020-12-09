import glob
import os
import bibtexparser

def propagate_notes():
    '''
    Appends the modifications added to notes.md files to the comment entry in the bibliography
    '''
    # List the md files
    notes = glob.glob("**/*.md", recursive=True)
    # Filter out the md files other than notes
    notes = [note for note in notes if note.endswith("notes.md")]
    # Open the bibliography
    with open("Bibliography/VM.bib") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    for note in notes:
        # Process file name
        year, author_name, article_name = note.split("/")[1].split("_")

        # Get the content of the notes file
        content = ""
        with open(note, "r") as f:
             content = f.read()

        # Add notes to the correct article
        for entry in bib_database.entries:
            if article_name == entry['title']:
                print("Title matched!")
                entry['comment'] = str(content)
                break
            elif author_name in entry['author'] and year == entry['year']:
                print("Author and year matched!")
                entry['comment'] = str(content)
                break


        # Write down the bibliography
        with open('Bibliography/VM.bib', 'w') as bibtex_file:
            bibtexparser.dump(bib_database, bibtex_file)


def extract_bib_without_comments():
    '''
    Creates a bibliography version with no comments
    '''
    # Open initial bibtex file
    with open("Bibliography/VM.bib") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Remove the comment entry
    for entry in bib_database.entries:
        try:
            del entry['comment']
        except KeyError:
            print("No comment found for that entry, skipping.")

    with open('Bibliography/VM_NoComments.bib', 'w') as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)

def process_pdf_articles():
    '''
    Create a folder, moves the pdf and add a notes.md file
    '''
    # List articles
    articles_to_process = os.listdir("Articles/TO_PROCESS/")
    if len(articles_to_process)==0:
        print("No article to process.")
        return
    for article in articles_to_process:
        # Extract name
        article_name = article.split(".")[0]
        # Create directory
        os.mkdir("Articles/"+article_name)
        # Add notes file
        with open("Articles/"+ article_name + "/notes.md", "w") as f:
            f.write("<!-- Please prefix the notes with the date as in [22/12/2020] -->")
        os.rename("Articles/TO_PROCESS/" + article, "Articles/"+ article_name + "/" + article_name + ".pdf")

def generate_readme():
    '''
    Appends the content of each note file to the README
    '''
    # Process all files
    articles = os.listdir("Articles/")
    articles = [article for article in articles if article != "TO_PROCESS"]
    article_dict = {}
    for article in articles:
        article_year   = article.split("_")[0]
        article_author = article.split("_")[1]
        article_name   = article.split("_")[2]
        dash_separated_header = article_year + "---" + article_author + "-" + article_name.replace(" ","-")
        paragraph_link = "[{0} - {1}, {2}](#{3})".format(article_year, article_author, article_name, dash_separated_header)
        content = ""
        with open("Articles/" + article + "/notes.md", "r") as f:
            content = f.read()
        actual_paragraph = "### {0} - {1}, {2}".format(article_year, article_author, article_name) + "\n" + content + "\n\n"
        article_dict[article_year + article_author] = (paragraph_link, actual_paragraph)

    items = article_dict.items()
    sorted_items = sorted(items)

    with open("README.md", "w") as f:
        f.write(''' ## VM-related Articles

This repository contains the different articles and the bibliography (in BibTeX format) related to the VM world (to a LARGE extent). The `VM.bib` file in `Bibliography` is best used with  [JabRef]. The notes in each of the folders, namely `notes.md` are integrated in the bibliography using a Python script in `utils.py`.  This script contains several useful helpers:

```bash
$ python utils.py --propagate  # Adds the contents of the notes.md files to their respective entry
$ python utils.py --nocomments # Generates a comment-free bibliography
$ python utils.py --process    # Creates a repository and empty notes.md file for each pdf in
							   # Articles/TO_PROCESS
$ python utils.py --genreadme  # Adds the notes to the present README.md file
```
[JabRef]: https://www.jabref.org/



## Article notes
### Summary
''')
        for item in sorted_items:
            f.write(item[1][0] + "\n\n")

        f.write("\n\n\n")

        for item in sorted_items:
            f.write(item[1][1] + "\n\n")

if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser(description="Helper for Bibliography handling")
    parser.add_argument("--nocomments", action="store_true",  help="Flag to output a bibliography without comments.")
    parser.add_argument("--propagate", action="store_true", help="Propagate the markdown notes to the comment field of the corresponding bib entry")
    parser.add_argument("--process", action="store_true", help="Create a folder and a blank note file for each pdf article in TO_PROCESS")
    parser.add_argument("--generate", action="store_true", help="Modify the README with the different notes from the articles")
    args = parser.parse_args(sys.argv[1:])

    if args.propagate:
        propagate_notes()
    if args.nocomments:
        extract_bib_without_comments()
    if args.process:
        process_pdf_articles()
    if args.generate:
        generate_readme()
