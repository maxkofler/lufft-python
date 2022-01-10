from WS_UMB import WS_UMB # fork from https://github.com/Tasm-Devil/lufft-python

def query_one_channel(umb, channel):
    '''query one channel'''

    value, status = umb.onlineDataQuery(channel)
    if status != 0:
        print(umb.checkStatus(status))
    else:
        print(value)
   
def query_multiple_channels(umb, channels):
    '''Query multiple channels by providing list of channels'''

    values, statuses = umb.onlineDataQueryMulti(channels)
    print("per channel query list: " + str(values))

def query_multiple_channels_one_call(umb, channels):
    '''Query multiple channels in one call by proving list of channels'''

    values, statuses = umb.onlineDataQueryMultiOneCall(channels)
    print("one call query list:    " + str(values))

def main():

    single_request = 113                        # single channel request
    channels = [113, 4630, 113, 113, 4630, 113] # channels to request

    with WS_UMB() as umb:
        query_one_channel(umb, single_request)
        query_multiple_channels(umb, channels)
        query_multiple_channels_one_call(umb, channels)

if __name__ == "__main__":
    main()