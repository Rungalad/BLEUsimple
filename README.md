# BLEUsimple
BLEU simplified for json cv parsed
Func launcing

import json

ff0 = open(r'origin.json', 'r')

origign = json.load(ff0)

ff0.close()

ff1 = open(r'bad_var.json', 'r')

origign_bad = json.load(ff1)

ff1.close()


ParseMetric(origign, origign_bad)
