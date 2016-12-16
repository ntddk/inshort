#!/bin/sh
if [ ! -d ./pdfminer ]; then
    git clone https://github.com/euske/pdfminer
    cd pdfminer
    make cmap
    python setup.py install
    cd ..
fi

pip install -r requirements.txt