#!/bin/bash
set -x

datFileAbsPath="${1}"
outdir="results/final"

if [[ -z ${datFileAbsPath} ]]; then
    curl "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data" > auto-mpg.data
    datFileAbsPath="$(pwd)/auto-mpg.data"
fi

mkdir -p "${outdir}"

for i in {1..100}; do
    python3 main.py "${datFileAbsPath}" > "${outdir}/out${i}-by_script.txt"
done
