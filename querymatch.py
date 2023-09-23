import os
import sys
from astropy.io import fits

def stiltsquery(tapurl, adqlquery, out='tmp'):
    stiltsCommand = 'stilts tapquery '+tapurl+" adql='"+adqlquery+"' out="+out+'.fits'
    print(stiltsCommand)
    os.system(stiltsCommand)

### Gaia Benchmark queries via VizieR

tapurl = 'tapurl=http://TAPVizieR.u-strasbg.fr/TAPVizieR/tap/'

adqlquery = 'SELECT "III/281/gbs".StarID4 as id,  "III/281/gbs".RAJ2000 as RA,  "III/281/gbs".DEJ2000 as dec,  "III/281/gbs".Teff,  "III/281/gbs".logg,  "III/281/gbs"."[Fe/H]", "III/281/gbs".SimbadName, "I/345/gaia2".phot_g_mean_mag as Gmag FROM "III/281/gbs" JOIN "I/345/gaia2" ON "III/281/gbs".StarID4 = "I/345/gaia2".source_id'

stiltsquery(tapurl,adqlquery, 'benchmark')

### Gaia-ESO queries via Gaia-ESO 
'''

tapurl = 'tapurl=XXX'

adqlquery = 'adql="SELECT OBJECT, RA, DECLINATION, TEFF, E_TEFF, LOGG, E_LOGG, FEH, E_FEH FROM XXX '
'''



### Gaia-ESO queries via VizieR

tapurl = 'tapurl=http://TAPVizieR.u-strasbg.fr/TAPVizieR/tap/'

adqlquery = 'SELECT "J/A+A/676/A129/catalog".Object,  "J/A+A/676/A129/catalog".RAJ2000,  "J/A+A/676/A129/catalog".DEJ2000,  "J/A+A/676/A129/catalog".Teff,  "J/A+A/676/A129/catalog".logg,  "J/A+A/676/A129/catalog"."[Fe/H]" FROM "J/A+A/676/A129/catalog"'

stiltsquery(tapurl,adqlquery, 'gaiaeso')
