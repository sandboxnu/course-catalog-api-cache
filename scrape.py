#!/usr/bin/env python3

import requests
import json

BANNER_URL="https://nubanner.neu.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?offset=1&max=200&searchTerm="
# The "academic year" is the year of the SPRING semester.
# For example, in the 2022-2023 academic year, the SPRING semester will be in 2023
# 	Therefore, this counts as the 2023 year, not 2022
ACADEMIC_YEAR="2023"

r = requests.get((BANNER_URL))
res = json.loads(r.content.decode('utf-8'))

parsed_res = [term['code'] for term in res if term['code'].startswith(ACADEMIC_YEAR)]
print(f"TERMS_TO_SCRAPE={','.join(parsed_res)}")
print(f'\n\nCopy and paste the above string to scrape the terms for the {int(ACADEMIC_YEAR)-1}-{ACADEMIC_YEAR} academic year')
