import subprocess
import re

# define the format of data
cellNumberRe = re.compile(r"^Cell\s+(?P<cellnumber>.+)\s+-\s+Address:\s(?P<mac>.+)$")
regexps = [
    re.compile(r"^ESSID:\"(?P<essid>.*)\"$"),
    re.compile(r"^Quality=(?P<signal_quality>\d+)/(?P<signal_total>\d+)\s+Signal level=(?P<signal_level_dBm>.+) d.+$"),
    re.compile(r"^Signal level=(?P<signal_quality>\d+)/(?P<signal_total>\d+).*$"),
]

#d define the encription
wpaRe = re.compile(r"IE:\ WPA\ Version\ 1$")
wpa2Re = re.compile(r"IE:\ IEEE\ 802\.11i/WPA2\ Version\ 1$")

# run the command in linux interface
def scan(interface='wlo1'):
    cmd = ["iwlist", interface, "scan"]
    detected = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    newtorks = detected.stdout.read().decode('utf-8')
    return newtorks

# to parse the information
def parse(content):
    cells = []
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        cellNumber = cellNumberRe.search(line)
        if cellNumber is not None:
            cells.append(cellNumber.groupdict())
            continue
        wpa = wpaRe.search(line)
        if wpa is not None :
            cells[-1].update({'encryption':'wpa'})
        wpa2 = wpa2Re.search(line)
        if wpa2 is not None :
            cells[-1].update({'encryption':'wpa2'}) 
        for expression in regexps:
            result = expression.search(line)
            if result is not None:
                if 'encryption' in result.groupdict() :
                    if result.groupdict()['encryption'] == 'on' :
                        cells[-1].update({'encryption': 'wep'})
                    else :
                        cells[-1].update({'encryption': 'off'})
                else :
                    cells[-1].update(result.groupdict())
                continue
    return cells