## VM-related Articles

This repository contains the different articles and the bibliography (in BibTeX format) related to the VM world (to a LARGE extent). The `VM.bib` file in `Bibliography` is best used with  [JabRef]. The notes in each of the folders, namely `notes.md` are integrated in the bibliography using a Python script in `utils.py`.  This script contains several useful helpers:

```bash
$ python utils.py --propagate  # Adds the contents of the notes.md files to their respective entry
$ python utils.py --nocomments # Generates a comment-free bibliography
$ python utils.py --process    # Creates a repository and empty notes.md file for each pdf in 
							   # Articles/TO_PROCESS
$ python utils.py --genreadme  # Adds the notes to the present README.md file
```





[JabRef]: https://www.jabref.org/

