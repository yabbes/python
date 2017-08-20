#! /usr/bin/env python3

import ephem

mars = ephem.Mars()
mars.compute()

dortmund = ephem.Observer()
dortmund.lat = '51.5135872'
dortmund.lon = '7.465298100000041'
