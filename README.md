# lufft-python
A Python API/driver for communication to Weatherstations made by the German company Lufft (e.g. WS600-UMB) via Serial-Port
It implements their Lufft UMB-Protocol. You just need a USB-to-RS485 dongle and connect it to your PWS according to the wiring diagram you find in the manual.

This class does not replace the UMB-config-tool, because its not able to set the config values in your PWS at the moment.

### In your python-script

## Usage single channel

```python
from WS_UMB import WS_UMB

with WS_UMB() as umb:
    value, status = umb.onlineDataQuery(SomeChannelNumber)
    if status != 0:
        print(umb.checkStatus(status))
    else:
        print(value)
```

## Usage multiple channels

```python
from WS_UMB import WS_UMB

with WS_UMB() as umb:
    channels = [113, 4630]
    values, statuses = umb.onlineDataQueryMulti(channels)
    print(values)
```

## Usage multiple channels one query

```python
from WS_UMB import WS_UMB

with WS_UMB() as umb:
    channels = [113, 4630]
    values, statuses = umb.onlineDataQueryMultiOneCall(channels)
    print(values)
```