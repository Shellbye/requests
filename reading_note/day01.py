# -*- coding:utf-8 -*-
# Created by shellbye on 2017/7/26.
import requests


if __name__ == '__main__':
    """
    requests require 
        urllib3 https://pypi.python.org/pypi/urllib3 
            'HTTP library with thread-safe connection pooling, file post, and more.'
        chardet https://pypi.python.org/pypi/chardet
            'Universal encoding detector for Python 2 and 3'
        certifi https://pypi.python.org/pypi/certifi
            'Python package for providing Mozilla's CA Bundle.'
        idna    https://pypi.python.org/pypi/idna
            'Internationalized Domain Names in Applications (IDNA)'
    
    mark: shellbye_day01
    """

    r = requests.get('https://github.com')
    print(r.status_code)
