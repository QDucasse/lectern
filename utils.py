import glob
import os
import bibtexparser

bib_name = "biblio.bib"
bib_name_no_comments = "biblio_nocomments.bib"

def find_entry(year, author, title, database):
    unwanted_characters = [",", ".", ":", "{", "}", '"', "'", "+", "`", "^", "&", "*", "?", "!", "\\", "/", "™"]
    for entry in database.entries:
        # Process unwanted characters
        try:
            modified_title = entry['title'].strip()
            modified_author = entry['author'].strip()
        except KeyError:
            print(entry)
            print("Error when processing: " +title)
        for char in unwanted_characters:
            modified_title =   modified_title.replace(char, "")
            modified_author = modified_author.replace(char, " ")
        # Compare Title
        # print("Comparing '" + modified_title + "' with '" + title + "'")
        if title.lower() in modified_title.lower():
            return entry
        # Compare year and author
        elif year == entry['year'] and author.lower() in modified_author.lower():
            return entry
    return "Entry not found!"


def propagate_notes():
    '''
    Appends the modifications added to notes.md files to the comment entry in the bibliography
    '''
    # List the md files
    notes = glob.glob("**/*.md", recursive=True)
    # Filter out the md files other than notes
    notes = [note for note in notes if note.endswith("notes.md")]
    # Open the bibliography
    with open("Bibliography/" + bib_name) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    for note in notes:
        # Process file name
        year, author, title = note.split("/")[1].split("_")

        # Get the content of the notes file
        content = ""
        with open(note, "r") as f:
             content = f.read()

        # Add notes to the correct article
        entry = find_entry(year, author, title, bib_database)
        if entry != "Entry not found!":
            entry['comment'] = str(content)

        # Write down the bibliography
    with open('Bibliography/' + bib_name, 'w') as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)

def compare_bib_physical():
    '''
    Compare the physical bibliography with the contents of the bib file and show the differences
    '''
    # Articles list
    articles = os.listdir("Articles/")
    articles.remove("TO_PROCESS")
    # Open the bibliography
    with open("Bibliography/biblio.bib") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    for entry in bib_database.entries:
        entry['found'] = 'false'

    # Check that articles are in the bib
    not_found_in_bib = []
    for article in articles:
        # Process filename
        # print(article)
        year, author, title = article.split("_")
        entry = find_entry(year, author, title, bib_database)
        if entry == "Entry not found!":
            # Article not found
            not_found_in_bib.append(article)
        else:
            # Article found
            entry['found'] = 'true'

    # Print missing article
    if len(not_found_in_bib) > 1:
        print("The following articles are present in physical but not in the bib file:")
        for article in not_found_in_bib:
            print(article.replace("_"," "))
    else:
        print("All physical articles in the bib!")

    # Check for articles in the bib file but not in physical
    not_found_in_phys = [(entry['year'] + " " + entry['author'] + " " + entry['title']) for entry in bib_database.entries if entry['found'] != 'true']

    if len(not_found_in_bib) > 1:
        print("\n\n\nThe following articles are present in the bib file but not in physical form:")
        for article in not_found_in_phys:
            print(article)
    else:
        print("All bib articles in physical!")

def extract_bib_without_comments():
    '''
    Creates a bibliography version with no comments
    '''
    # Open initial bibtex file
    with open("Bibliography/"+bib_name) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Remove the comment entry
    for entry in bib_database.entries:
        # Remove comments
        try:
            del entry['comment']
        except KeyError:
            print(entry['title'] + ": No comment found for that entry, skipping.")
        # Remove groups
        try:
            del entry['groups']
        except KeyError:
            print(entry['title'] + ": No group found for that entry, skipping.")

    with open('Bibliography/'+bib_name_no_comments, 'w') as bibtex_file:
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
        # Add bib file
        with open("Articles/" + article_name + "/biblio.bib", "w") as f:
            f.write(" ")
        # Add notes file
        with open("Articles/"+ article_name + "/notes.md", "w") as f:
            f.write("<!-- Please prefix the notes with the date as in [22/12/2020] -->")
        os.rename("Articles/TO_PROCESS/" + article, "Articles/"+ article_name + "/" + article_name + ".pdf")
        print("Article processed: " + article_name)

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
        actual_paragraph = "### {0} - {1}, {2}".format(article_year, article_author, article_name) + "\n" + content + "\n\n---\n\n"
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
            f.write(item[1][1] + "\n")

if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser(description="Helper for Bibliography handling")
    parser.add_argument("-n","--nocomments", action="store_true",  help="Flag to output a bibliography without comments.")
    parser.add_argument("-p","--propagate", action="store_true", help="Propagate the markdown notes to the comment field of the corresponding bib entry")
    parser.add_argument("-P","--process", action="store_true", help="Create a folder and a blank note file for each pdf article in TO_PROCESS")
    parser.add_argument("-g","--generate", action="store_true", help="Modify the README with the different notes from the articles")
    parser.add_argument("-c","--compare", action="store_true", help="Compare the physical bibliography structure with the bib file and notes the differences")
    args = parser.parse_args(sys.argv[1:])
    no_args = True
    if args.propagate:
        no_args = False
        propagate_notes()
        print("Notes propagated into the bibliography!")
    if args.nocomments:
        no_args = False
        extract_bib_without_comments()
        print("Bibliography with no comments generated!")
    if args.process:
        no_args = False
        process_pdf_articles()
        print("Articles in TO_PROCESS have their dedicated folder!")
    if args.generate:
        no_args = False
        generate_readme()
        print("Notes propagated into the main README!")
    if args.compare:
        no_args = False
        compare_bib_physical()
        print("Differences checked between physical resources and the bibliography!")
    if no_args:
        parser.print_help()
