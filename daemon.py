import time
import sys
import os
from isspass import ISSPass


if __name__ == '__main__':
    try:
        loc = os.environ['ISS_PASS_LOCATION'].split(',')
        url = os.environ['ISS_PASS_URL']
    except KeyError:
        print('Specify location of interest as ISS_PASS_LOCATION env variable in "lat,lon" format and notification URL as ISS_PASS_URL variable.')
        sys.exit(1)

    ISS = ISSPass(loc[0], loc[1])

    while True:
        above = ISS.is_above()
        if above:
            try:
                requests.put(url)
            except:
                print('Error occured while calling notify URL.')
                continue
            print('Notify sent, sleeping a little to prevent spam.')
            time.sleep(30)
            continue
        time.sleep(1)
