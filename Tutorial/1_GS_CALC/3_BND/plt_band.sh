#!/bin/bash

################################################################################
# pyband can be download from: https://github.com/QijingZheng/pyband
################################################################################

# --occ '1 2 6' \                          # the atom index of WS2
# --occL \                                 # use the color stripes to plot the band
# --occLC_cmap seismic \                   # choose the colormap "seismic"
# --occLC_cbar_ticks '0 1' \               # set the color range from 0 to 1
# --occLC_cbar_vmin 0 \                    #
# --occLC_cbar_vmax 1 \                    #
# --occLC_cbar_ticklabels 'MoS$_2$ WS$_2$' # 0 corresponds to MoS2, 1 corresponds to WS2
# -k mgkm                                  # the name of the high-symmetry k-point

pyband  --occ '1 2 6' \
        --occL \
        --occLC_cmap seismic \
        --occLC_cbar_ticks '0 1' \
        --occLC_cbar_vmin 0 \
        --occLC_cbar_vmax 1 \
        --occLC_cbar_ticklabels 'MoS$_2$ WS$_2$'
        -k mgkm
