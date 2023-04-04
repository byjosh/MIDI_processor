# Install notes

## Assumptions
 * You have Python3 installed and can use a terminal (commandline) 
 * This works with type 0 MIDI files - i.e. those that have a single track
 * you give different names for the output and input file (otherwise you will overwrite your input file)
 * to play MIDI files you have a sound font installed (if you are generating the MIDI files this is likely true - if not then [https://archive.org/details/fluidr3-gm-gs](https://archive.org/details/fluidr3-gm-gs) or [https://launchpad.net/ubuntu/+source/fluid-soundfont](https://launchpad.net/ubuntu/+source/fluid-soundfont) may, at your own risk, provide the necessary file - the FluidR3 soundfont file by Frank Wen which seems to be a widely available soundfont used in open-source projects).
 


## Steps to use this in Mac or Linux environment

If you have not got Python3 installed - [download and install it](https://www.python.org/downloads/)

Run following commands in terminal

Make folder that is a Python 3 [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) to copy the script into

` python3 -m venv name_of_folder_for_virtual_environment`

change current directory to folder you just created

`cd name_of_folder_for_virtual_environment`

now inside the folder you created activate virtual environment you created

`source bin/activate`

Install [mido](https://mido.readthedocs.io/) 

`pip install mido`

At this point download the processor.py file in this Github repository into the folder you have created
and make the processor.py file executable using the following command in terminal

`chmod +x processory.py`


# Running the script

Having done all the above you are now ready to use the processor.py script. 

An example use is:

`./processor.py scales.mid twiceaslong.mid 2`

This script takes 3 parameters

1. the input MIDI file (here in the same directory and called `scales.mid`)
2. the output MIDI filename (here in the same directory and called `twiceaslong.mid`)
3. a multiple - integer or decimal - used to multiple the time of the MIDI messages - here this is `2` so the file will play at approximately halfspeed taking twice as long (hence output file name of `twiceaslong.mid` used as example - though it could be called anything ending `.mid`)

If you fail to provide these oarameters the script should print a reminder and then exit.

Use your own input MIDI file (provided it is a type 0 MIDI file with a single track) but in case you need a test MIDI file one called scales.mid is provided in this repository - it just goes up and down the keys on a piano).
