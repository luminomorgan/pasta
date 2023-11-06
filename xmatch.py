import os
import sys
from astropy.io import fits

def stiltsquery(tapurl, adqlquery, out='tmp'):
    stiltsCommand = '~/stilts tapquery '+tapurl+" adql='"+adqlquery+"' out="+out+'.fits'
    print(stiltsCommand)
    os.system(stiltsCommand)

### Gaia-ESO queries via VizieR

tapurl = 'tapurl=http://TAPVizieR.u-strasbg.fr/TAPVizieR/tap/'

adqlquery = 'SELECT "I/345/gaia2".phot_g_mean_mag,  "J/A+A/676/A129/catalog".Object,  "J/A+A/676/A129/catalog".RAJ2000,  "J/A+A/676/A129/catalog".DEJ2000,  "J/A+A/676/A129/catalog".Teff,  "J/A+A/676/A129/catalog".logg,  "J/A+A/676/A129/catalog"."[Fe/H]",  "I/345/gaia2".dec_epoch2000,  "I/345/gaia2".ra,  "I/345/gaia2".source_id FROM "I/345/gaia2","J/A+A/676/A129/catalog" WHERE 1=CONTAINS(POINT("ICRS","J/A+A/676/A129/catalog".RAJ2000,"J/A+A/676/A129/catalog".DEJ2000),CIRCLE("ICRS","I/345/gaia2".ra,"I/345/gaia2".dec, 0.1/3600.))'

stiltsquery(tapurl,adqlquery, 'xgaiaeso')
