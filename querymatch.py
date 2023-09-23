import os
import sys
from astropy.io import fits

def stiltsquery(tapurl, adqlquery, out='tmp'):
    stiltsCommand = 'stilts tapquery '+tapurl+" adql='"+adqlquery+"' out="+out+'.fits'
    print(stiltsCommand)
    os.system(stiltsCommand)
    
### Gaia-ESO queries via Gaia-ESO 
'''

tapurl = 'tapurl=XXX'

adqlquery = 'adql="SELECT OBJECT, RA, DECLINATION, TEFF, E_TEFF, LOGG, E_LOGG, FEH, E_FEH FROM XXX '
'''



### Gaia-ESO queries via VizieR

tapurl = 'tapurl=http://TAPVizieR.u-strasbg.fr/TAPVizieR/tap/'

adqlquery = 'SELECT "J/A+A/676/A129/catalog".Object,  "J/A+A/676/A129/catalog".RAJ2000,  "J/A+A/676/A129/catalog".DEJ2000,  "J/A+A/676/A129/catalog".Teff,  "J/A+A/676/A129/catalog".logg,  "J/A+A/676/A129/catalog"."[Fe/H]" FROM "J/A+A/676/A129/catalog"'

stiltsquery(tapurl,adqlquery, 'gaiaeso')
