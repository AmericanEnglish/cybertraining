#!/bin/bash

# This function writes a HEG Parameter script 
# for converting HDF regional files (h11v05) to GeoTIFF files

DIR_NAME=$(cd "$(dirname "$0")";pwd)

echo $DIR_NAME
mkdir -p $STUDY_NAME

files=$(ls ${DIR_NAME}/heg.h11v05/)

for filename in $files
do
    length=${#filename}
    outname=${filename:0:${length}-4}
    cat << _EOF_ > MyParameter.prm

NUM_RUNS = 1

BEGIN
INPUT_FILENAME = ${DIR_NAME}/heg.h11v05/${filename}
OBJECT_NAME = MOD_Grid_BRDF|
FIELD_NAME = Albedo_BSA_shortwave
BAND_NUMBER = 1
SPATIAL_SUBSET_UL_CORNER = ( 39.999999996 -80.000000000 )
SPATIAL_SUBSET_LR_CORNER = ( 37.000000000 -76.000000000 )
RESAMPLING_TYPE = BI
OUTPUT_PROJECTION_TYPE = GEO
ELLIPSOID_CODE = WGS84
OUTPUT_PROJECTION_PARAMETERS = ( 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0  )
OUTPUT_PIXEL_SIZE = 15.000023890652672
OUTPUT_FILENAME = ${DIR_NAME}/tif_files/heg.h11v05/${outname}.tif
OUTPUT_TYPE = GEO
END

_EOF_
    resample -p MyParameter.prm
    rm -f MyParameter.prm
done

