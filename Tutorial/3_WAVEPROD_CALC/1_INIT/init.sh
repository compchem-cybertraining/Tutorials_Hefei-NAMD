#!/bin/bash

sed -i 's/^\s*$/Direct configuration=/' ../../2_MD_CALC/3_NVE_MD/XDATCAR  
python extract_positions_from_nve.py

if [ $? -eq 0 ]; then

    inp_dir=$(pwd)

    for xx in ../2_RUN/*/
    do
        cd ${xx}
        ln -sf ../../1_INIT/INCAR
        ln -sf ../../1_INIT/KPOINTS
        ln -sf ../../1_INIT/POTCAR
        cd ${inp_dir}
    done

fi
