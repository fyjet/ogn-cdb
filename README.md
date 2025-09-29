# Python virtual env creation
Create virtual environment and install pure-cdb and requests python modules
```shell
python -m venv .
./bin/pip install pure-cdb requests
```

# Run utility
```shell
./bin/python3 ogn_cdb.py
```
The tool will download OGN data in JSON format from http://ddb.glidernet.org/download/?j=1 and create ogn.cdb file.

File ogn.cdb must be copied to SoftRF drive, into Aircraft directory (see https://github.com/lyusupov/SoftRF/wiki/Badge-Edition.-Aircrafts-database)
