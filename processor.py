#!/usr/bin/env python3

import sys
import mido

def multiply_time(m,multiple):
    newtime = float(multiple) * m.time
    return mido.Message(m.type,channel=m.channel,note=m.note,velocity=m.velocity,time=(int(newtime)))

if __name__ == "__main__":
    try:
        #likely to give error if these are not supplied
        file = sys.argv[1]
        output = sys.argv[2]
        multiple = sys.argv[3]

        mid = mido.MidiFile(file,clip=True)

        #add track
        mid.add_track()
        newtrack = mid.tracks[1]

        for m in mid.tracks[0]:
            #append MetaMessages unaltered
            if isinstance(m,mido.midifiles.meta.MetaMessage):
                newtrack.append(m)
            
            #change time of messages
            if isinstance(m,mido.messages.messages.Message) :
                newtrack.append(multiply_time(m,multiple))
        
        #type 0 files can only have one track - so remove original track
        mid.tracks.remove(mid.tracks[0])
        mid.save(output)


        
    except IndexError:
        # one of the ncessary parameters was not supplied
        print("Supply an input file name, an output file name and a number as a multiple")
        print("multiple can be a whole number - 4 for four times as slow or a decimal 0.5 for twice as fast")
        print("E.g. - for a file twice as slow:-")
        print("./processor.py inputfile.mid outputfile.mid 2")