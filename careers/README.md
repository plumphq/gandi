### Folder name conventions
- Company folder name should be lowercase and contain only letters, numbers, and dashes. 

For example, "Goldman Sachs" should be named as "goldman-sachs".

### Initial company folder structure
Acceptable company folder at the beginning should contain 2, and only 2, files:
- `company.yaml` – company description
- `careers.yaml` – simple list of open positions

Things to consider: 
- You don't need to keep `careers.yaml` up-to-date. We handle it for you.
- Don't try to add more files to the company folder, they will be ignored.
- We strictly support `.yaml` extension only. Other formats like `.yml` will be ignored.

### Files content
Take a look at the `example` folder for the good reference.

### Quick start
There is `./init.sh` script that will create a company folder based on the latest template for you. 

Alternatively, just copy-paste and rename the `template` folder by yourself (remember folder name conventions).

### Complete company folder structure
Once the first PR is merged, your company folder will be updated with the following sub-folders and files:
- /schema
  - /<job-position-1-name>.json
  - /<job-position-2-name>.json
  - /<job-position-n-name>.json
- /data
  - /<job-position-1-name>.json
  - /<job-position-2-name>.json
  - /<job-position-n-name>.json

To make it simple: 
- `schema` is an _intermediate folder_ that is used by Gandi AI Worker to aggregate a job listing json structure from a raw .html format into
- `data` is a _final folder_ that contains a job listing json structure that is ready to be used by consumers. 