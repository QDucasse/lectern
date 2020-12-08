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

if __name__ == "__main__":
    # propagate_notes()
    extract_bib_without_comments()
