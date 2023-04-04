# Install notes

## Assumptions
 * This works with type 0 MIDI files - i.e. those that have a single track
 * you give different names for the output and input file (otherwise you will overwrite your input file)


## Steps to use this in Mac or Linux environment
Run following commands in terminal

Make folder that is a Python 3 virtual environment to copy the script into
` python3 -m venv name_of_folder_for_virtual_enviroment`
change to folder
`cd name_of_folder_for_virtual_enviroment`
activate virtual enviroment
`source bin/activate`
Install mido 
`pip install mido`
make the script executable
`chmod +x processory.py`


# Running the script

This would output the scales file at double speed - including twice the silence at the beginning.
`./processor.py scales.mid doublespeed.mid 2`
