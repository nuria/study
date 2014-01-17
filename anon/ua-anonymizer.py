#!/usr/local/bin/python
import md5
import re
# gets a file with IP UA
# anonymizes ua
# calculates md5
# prints md5, as to establish how good of a unique identifier is that

def anonymize(ua):
     # from 1.1.2 ->1.1
    processed  = re.sub(r'(\d+\.\d+)(\.(\d|\w)+)+', r'\1', ua)

    # remove language headers en-EN
    processed  = re.sub(r'\s\w\w-\w\w(;|\s|\)){1}', r'\1', processed)

    # blackberry language headers are: BlackBerry 9300; en)
    processed  = re.sub(r'(BlackBerry\s\d{4,};)\s\w\w\)', r'\1)', processed)

    # AppleWebKit/537.17 -> AppleWebKit/537.17
    processed  = re.sub(r'(AppleWebKit|Safari)/?(\d+)(\.\d*\+?)+', r'\1/\2', processed)

    # Apple also has some bizarre versions for firmware:Mobile/10B329 -> Mobile/10
    # removing those as are not needed for device/os/browser id
    # it is questionable whether these should be maintanined
    processed  = re.sub(r'Mobile/((\d|\w){2})(\w|\d)+ ', r'Mobile ', processed)

    # remove apple versions 1_2_3 ->1_2
    processed  = re.sub(r'(\d+_\d+)(_\d+)+', r'\1', processed)

    # ignore everything after .NET,SV1,MSN,SIMBAR... in MS UA
    processed  = re.sub(r'\s(\.NET|BTR|GTB|SV1|MSN|SIMBAR|SLCC|MR(A|S)).*\)?', r')', processed)

    # remove version of gecko, hardly relevant
    processed  = re.sub(r'rv:\d+\.\d+(\.\d+)?', r'', processed)

    #remove Build/JZO54K Build/1.A_3 from android
    processed  = re.sub(r'\sBuild/(\w|\.|\d|-)+(\s|;)?', r'', processed)

    # round dates to year 20100101 becomes 2010
    processed  = re.sub(r'(\d\d\d\d)\d\d\d\d\s', r'\1 ', processed)

    # remove stuff like (65FAA2DA-9457-4993-B310-98228E704BBE)
    processed  = re.sub(r'\(((\w|\d)-?)+\)', r'', processed)



    return processed;



def main():
    f = open('./80k-moduleStorage.txt')
    lines = f.readlines();
    f.close()

    for l in lines:
        # ua chuncks
        l = l.strip();

        items = l.split();

        ip = items[1];

        ua = " ".join(items[2:]);

        #print ua;

        aua = anonymize(ua)

        #print ">"+aua;

        fingerprint = md5.new(aua+ip)
        #print aua;

        print fingerprint.hexdigest()
        #print aua


if __name__ == "__main__":
    main();
