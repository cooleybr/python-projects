## GUI Based CVE Search 

Application connects to the NIST CVE Database and queries for a given term. A JSON Object is returned.

https://services.nvd.nist.gov/rest/json/cves/1.0/

### Python 3.8.10
 - Uses Virtual Environment

Inital Research Sources
https://build-system.fman.io/pyqt5-tutorial
https://build-system.fman.io/

### Clone, and...
RUN apt install python3-venv (if not installed)
RUN python3 -m venv <environment name> (setup virtual environment)
RUN source <environment name>/bin/activate (start virtual environment)
RUN pip install -r requirements.txt (install requirements)
RUN python src/main/python/main.py

TODO:
 - Currently only prints object to stdout. Do something 
