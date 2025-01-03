# About

Acrostiquery empowers users to mechanically search for acrostics (words made from the first letters of consecutive lines of poetry or prose) and telestichs (words made from the last letters of consecutive lines), primarily in Greek and Latin literature. Users can search any author or text in the [Tesserae project](https://tesserae.caset.buffalo.edu/blog/about-tesserae/)'s corpus (see the available [Latin](https://github.com/ndh4/acrostiquery/tree/main/texts/la), [Greek](https://github.com/ndh4/acrostiquery/tree/main/texts/grc), and [English](https://github.com/ndh4/acrostiquery/tree/main/texts/en) texts here).

# Instructions

### Install python

1. Go to [python.org/downloads/](https://www.python.org/downloads/) and download the latest version.
2. Open the downloaded `pkg` or `exe` file and follow the installer's instructions to complete installation. On Windows, make sure that "Add python.exe to PATH" is selected. ![Make sure that Add python.exe to PATH has a check mark next to it.](images/add_python_to_path.png)

### Run acrostiquery

1. Go to [github.com/ndh4/acrostiquery](https://github.com/ndh4/acrostiquery) and click on the green box that says `<> Code`. Then click `Download ZIP`.
![Code | Download ZIP](images/download_zip.png)
2. Unzip and open the downloaded folder.
3. Open a terminal inside `scripts`:
   1. Here's how to do that on Mac:
      1. Right-click on `scripts`.
      2. Select "New Terminal at Folder" ![Right-click on `scripts` and select "New Terminal at Folder"](images/open_terminal_mac.png)
   2. Here's how to do it on Windows:
      1. Open the `scripts` folder.
      2. Click on the address bar at the top of the window. This should highlight the entire address of the `scripts` folder. ![Click on the space after the address.](images/scripts_folder.png) ![The entire address should be highlighted after you do so.](images/address_highlighted.png)
      3. Use <kbd>CTRL</kbd> + <kbd>c</kbd> to copy the contents of the address bar.
      4. Open the Start Menu and search for `cmd`. Open the first thing that comes up (probably called `Command Prompt`). ![Search for cmd and open the first program that comes up.](images/windows_search.png)
      5. Type `pushd` and hit the <kbd>Space</kbd> bar, then use <kbd>CTRL</kbd> + <kbd>v</kbd> to paste the address you copied earlier. ![pushd paste](images/pushd.png)
      6. Hit the <kbd>Enter</kbd> key 3 or 4 times. ![Hit enter 3 or 4 times to make sure that the command took.](images/enter3.png)
4. Type `python3 main.py` and hit <kbd>Enter</kbd>.
   1. If that doesn't work ("Python was not found/recognized"), try `py main.py`.
   2. If that doesn't work, try `python main.py`.
   3. If that doesn't work, try `py3 main.py`.
5. Answer the prompts that follow. The first prompt should be the question shown below.
![The first question should be, "Do you want to search for an acrostic or telestich?"](images/mac_success.png)
6. After you've answered all the questions, and the program gives you a search result, you can repeat step 4 to start another search.

# Acknowledgements

Big thanks to Neil Coffee and the [Tesserae team](https://tesserae.caset.buffalo.edu/blog/people/) for the use of their corpus and specialized `.tess` file format. Also, thanks to Joseph Dexter and the [Quantitative Criticism Lab](https://www.qcrit.org/people) for their advice and direction.

If you run into problems using this tool or have suggestions for improvement, contact Nathaniel Hejduk at [nhejduk4@gmail.com](mailto:nhejduk4@gmail.com).