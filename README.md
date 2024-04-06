# lethal_downloader
Downloads lethal mods from thunderstore

## How to install
git clone the repo and then pip install

### Getting started
After pip installing, the first thing we need to do is create a text file. This text file will contain mod names that we'd like to search for, separated by a new line. For the purposes of this we'll act like we have a file, with one mod in it
<p> Run the script lethal_md generate.jsons FILE and a file will be generated</p>

> lethal_md generate.jsons test.txt

<p> Afterwards, in order to install the mods, you must use lethal_md download.mods and point to the created json from the previous script. This allows for mod configurations that can be saved over time and have an ease of downloading different variations. </p>

> lethal_md download.mods test.json
