import numpy as np
from obspy import UTCDateTime


def catalognpy2pha():
    catalog = np.load('./catalog.npy', allow_pickle=True).item()
    nms = []
    #sort catalog
    for evn in catalog['head']:
        nms.append(evn)
    nms.sort()
    pha = open('XFJ.pha', 'w')
    evid = 0
    for evn in nms:
        evid += 1
        lat = catalog['head'][evn]['lat']
        lon = catalog['head'][evn]['lon']
        starttime = catalog['head'][evn]['starttime']
        ML = catalog['head'][evn]['ML']
        depth = catalog['head'][evn]['depth']
        strt = starttime.strftime(
            '# %Y %m %d %H %M %S.%f')[:-4]
        line = (strt + '%9.4f' % lat + '%10.4f' % lon
                + '%8.2f' % depth + '%5.2f' % ML + '  0.00  0.00  0.00' + '%11i' % evid + '\n')
        pha.write(line)
        for st in catalog['phase'][evn]:
            if 'P' in catalog['phase'][evn][st]:
                tp = catalog['phase'][evn][st]['P']
                ttp = catalog['phase'][evn][st]['P']-starttime
                pha.write('{:<5}{}{:6.3f}  {:6.3f}   P\n'.format(st, ' ' * 6, ttp, 1.0))
            if 'S' in catalog['phase'][evn][st]:
                ts = catalog['phase'][evn][st]['S']
                tts = catalog['phase'][evn][st]['S']-starttime
                pha.write('{:<5}{}{:6.3f}  {:6.3f}   S\n'.format(st, ' ' * 6, tts, 1.0))
            # breakpoint()
    pha.close()


def catalognpy2station():
    catalog = np.load('./catalog.npy', allow_pickle=True).item()
    nms = []
    # sort catalog
    for evn in catalog['head']:
        nms.append(evn)
    nms.sort()
    station = open('station.dat', 'w')
    station.close()


if __name__ == '__main__':
    catalognpy2pha()
