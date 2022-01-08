# A simple example of using S3MPython to retrieve information about the library
import os
from S3MPython.settings import VERSION, RMVERSION, DM_LIB, ACSFILE, get_acs, XMLDIR, RDFDIR

print("\n  S3MPython version:", VERSION)
print("  S3M RM version:", RMVERSION)

print("\nYou may change the following settings in the conf/S3MPython.conf file.")
print("\nData Model Library location: ", DM_LIB)
print("The XML catalog directory: ", os.environ["XML_CATALOG_FILES"])


print("\n\nUsing Access Control System file: ", ACSFILE)
print("\nACS Content: ")
ACS = get_acs(ACSFILE)
for s in ACS:
    print(s)

print("\n\nXML data files will be in: ", XMLDIR)
print("\nRDF data files will be in: ", RDFDIR)

print("\n\n     That is all!\n\n")
