# What's this?

Repository with daemon to send Telegram notifies when ISS passes by your location (with sane deviation).

# How to run

### Manual

```
export ISS_PASS_LOCATION=<lat>,<lon>
export ISS_PASS_TG_TOKEN=<token>
export ISS_PASS_TG_ID=<ID1>,<ID2>

python3 daemon.py
```

### Docker

```
docker run -d --name isspass \
  -e ISS_PASS_LOCATION="<lat>,<lon>" \
  -e ISS_PASS_TG_TOKEN="<token>" \
  -e ISS_PASS_TG_ID=<ID1>,<ID2> \
  agrrh/isspass:latest
docker logs -f isspass
```
