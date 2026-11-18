[SoftRF](https://github.com/lyusupov/SoftRF) aircrafts file, generated twice a day from Openglider network registred aircrafts database, can usually be downloaded from http://soaringweather.no-ip.info/ADB/data/ogn.cdb . You can generate your own with ogn-cdb.py python script, without waiting for extract from previous site.

Daily built [ogn.cdb](https://github.com/fyjet/ogn-cdb/releases/download/latest/ogn.cdb) is available in [Release pages](https://github.com/fyjet/ogn-cdb/releases) (Thanks to @yasiupl for git-hub action)

# Run your own
## Installation
In your home directory, clone this repository and change to ogn-cdb directory
```shell
$ git clone https://github.com/fyjet/ogn-cdb.git
$ cd ogn-cdb
```

Create virtual environment and install pure-cdb and requests python modules
```shell
$ python -m venv .
$ ./bin/pip install pure-cdb requests
```

## Run utility
```shell
$ ./bin/python3 ogn_cdb.py
```
The tool will download OGN data in JSON format from http://ddb.glidernet.org/download/?j=1 and create ogn.cdb file.

File ogn.cdb must be copied to SoftRF drive, into Aircraft directory (see https://github.com/lyusupov/SoftRF/wiki/Badge-Edition.-Aircrafts-database)
