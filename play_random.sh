#!/bin/bash

CLIP_PATH=/Users/davidyerrington/soundclips/

afplay $CLIP_PATH`ls $CLIP_PATH | /usr/local/bin/gshuf -n 1`
