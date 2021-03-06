import time
import sys
import os
from isspass import ISSPass


if __name__ == '__main__':
    try:
        loc = os.environ['ISS_PASS_LOCATION'].split(',')
        tg_token = os.environ['ISS_PASS_TG_TOKEN']
        tg_id = os.environ['ISS_PASS_TG_ID']
    except KeyError:
        print('Specify location of interest as ISS_PASS_LOCATION env variable in "lat,lon" format and Telegram Token/recipient ID as ISS_PASS_TG_TOKEN/_ID variables.')
        sys.exit(1)

    i = 0
    ISS = ISSPass(loc[0], loc[1])

    while True:
        loc = ISS._get_iss_location()

        if i % 100 == 0:
            print(ISS.location, loc)
        i += 1

        above = ISS.is_above(loc)

        if above:
            for recipient in tg_id.split(','):
                requests.post(
                    URI = 'https://api.telegram.org/bot' + tg_token + '/sendMessage',
                    json={
                        'chat_id': int(recipient),
                        'text': '🚀 ISS is passing over you!',
                        'parse_mode': 'Markdown'
                    })
            print('Notify sent, sleeping a little to prevent spam.')
            time.sleep(30)
            continue
        time.sleep(1)
