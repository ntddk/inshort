#!/bin/sh
if [ $# -ne 1 ]; then
    echo "Input PDF file path."
    exit 1
fi

python pdf2txt.py \-V $1 | sed -r -e ':loop;N;$!b loop;s/\n/ /g' -e 's/ +/ /g' -e 's/-//g' -e 's/\./\.\n/g' -e 's/\f/ /g' | python summary.py
