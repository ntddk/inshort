#!/bin/sh
if [ ! -d ./pdfminer ]; then
    git clone https://github.com/euske/pdfminer
    cd pdfminer
    make cmap
    python setup.py install
    cd ..
fi

if [ $# -ne 1 ]; then
    echo "[inshort] Enter PDF file path."
    exit 1
fi

echo "[inshort] Processing..."
python pdf2txt.py \-V $1 | sed -r -e ':loop;N;$!b loop;s/\n/ /g' -e 's/ +/ /g' -e 's/-//g' -e 's/\./\.\n/g' -e 's/\f/ /g' | python summary.py

