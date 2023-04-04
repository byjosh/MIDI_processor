# Install notes

## Assumptions
 * You have Python3 installed and can use a terminal (commandline) 
 * This works with type 0 MIDI files - i.e. those that have a single track
 * you give different names for the output and input file (otherwise you will overwrite your input file)
 * to play MIDI files you have a sound font installed (if you are generating the MIDI files this is likely true - if not then [https://archive.org/details/fluidr3-gm-gs](https://archive.org/details/fluidr3-gm-gs) or [https://launchpad.net/ubuntu/+source/fluid-soundfont](https://launchpad.net/ubuntu/+source/fluid-soundfont) may, at your own risk, provide the necessary file (the FluidR3 soundfont file by Frank Wen which seems to be a widely available soundfont used in open-source projects).
 


## Steps to use this in Mac or Linux environment

If you have not got Python3 installed - [download and install it](https://www.python.org/downloads/)

Run following commands in terminal

Make folder that is a Python 3 virtual environment to copy the script into

` python3 -m venv name_of_folder_for_virtual_enviroment`

change to folder

`cd name_of_folder_for_virtual_enviroment`

activate virtual enviroment

`source bin/activate`

Install [mido](https://mido.readthedocs.io/) 

`pip install mido`

At this point download the processor.py file into the folder you have create
and make the processor.py file executable using the following command in terminal

`chmod +x processory.py`


# Running the script

Having done all the above you are now ready to use the processor.py script. Here is an example - having created a simple midi file (a sample midi file  is provided just in case - and you can download it into the same folder you created the virtual environment in) this example command would output the scales file at double speed - including twice the silence at the beginning.

`./processor.py scales.mid doublespeed.mid 2`
