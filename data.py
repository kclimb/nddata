# Unofficial times:
# SPY: (42,22) by C (no proof)

games = ["SCK", "STFD", "MHM", "TRT", "FIN", "SSH", "DOG", "CAR", "DDI", "SHA", "CUR", "CLK", "TRN", "DAN",
        "CRE", "ICE", "CRY", "VEN", "HAU", "RAN", "WAC", "TOT", "SCKR", "SAW", "CAP", "ASH", "TMB", "DED",
        "GTH", "SPY", "MED", "LIE", "SEA"]

times = [(4, 10), (11, 34), (9, 56),	# SCK STFD MHM
         (23, 26), (17, 2), (55, 55),	# TRT FIN SSH
         (31, 10), (42, 51), (48, 49),	# DOG CAR DDI
         (56, 9), (44, 33), (52, 51),	# SHA CUR CLK
         (51, 57), (65, 40), (68, 20),	# TRN DAN CRE
         (58, 52), (56, 48), (77, 1),	# ICE CRY VEN
         (59, 49), (66, 23), (52, 39),	# HAU RAN WAC
         (65, 24), (11, 53), (73, 17),	# TOT SCKR SAW
         (53, 4), (48, 37), (33, 55),	# CAP ASH TMB
         (45, 50), (24, 31), (44, 15),	# DED GTH SPY
         (35, 20), (28, 1), (33, 30)]	# MED LIE SEA

sub1 = [guy[0] < 60 for guy in times]
peeps = ['toasterberry', 'toburr', 'toburr', 'rpgg', 'rpgg', 'rpgg', 'yandema', #1-7
         'yandema', 'toburr', 'yandema', 'toburr', 'yandema', #8-12
         'eca', 'toburr', 'marenkae', 'eca', 'smileyz', #13-17
         'smileyz', 'smileyz', 'yandema', 'marenkae', 'yandema', #18-22
         'eca', 'yandema', 'rpgg', 'rpgg', 'nancyjilk', #sckr-26
         'rpgg', 'nancyjilk', 'yandema', 'nancyjilk', 'nancyjilk', 'brekkieboo'] #27-32
countries = {'toburr': 'USA', 'yandema': 'USA', 'eca': 'USA', 'arglefumph': 'USA', 'lisa': 'CAN',
            'rpgg': 'CAN', 'nancyjilk': 'CAN', 'tkd': 'USA', 'corrine': 'USA', 'ttc': 'AUS',
             'may': 'RUS', 'bluetooth': 'USA', 'marenkae': 'USA', 'toasterberry': 'unknown',
             'brekkieboo': 'unknown','v_neptune': 'USA', 'smileyz': 'USA', 'steveus':'USA'}

print 'Game\tTime (min, sec)\tSub 1?\tRecord Holder'
print '-------------------------------------'
for i in xrange(len(times)):
    print games[i], '\t', times[i], '\t', sub1[i], '\t', peeps[i]

seconds = sum([guy[1] for guy in times])
minutes = sum([guy[0] for guy in times]) + seconds / 60
seconds = seconds % 60
hours = minutes / 60
minutes = minutes % 60
if minutes < 10:
    minstr = '0'+str(minutes)
else:
    minstr = str(minutes)
if seconds < 10:
    secstr = '0'+str(seconds)
else:
    secstr = str(seconds)
print "Sum of WRs:", str(hours)+':'+minstr+':'+secstr
print "Percentage to sub-24:", 100*24 * 60. * 60 / (hours * 60. * 60 + minutes * 60 + seconds)

print ''
reccounts = {}
nations = {}
for guy in peeps:
    if guy not in reccounts:
        reccounts[guy] = 1
        if countries[guy] not in nations:
            nations[countries[guy]] = 1
        else:
            nations[countries[guy]] += 1
    else:
        reccounts[guy] += 1
        nations[countries[guy]] += 1
holderlist = sorted(reccounts.items(), key=lambda tup: tup[1])
holderlist.reverse()
for tup in holderlist:
    tabs = '\t'
    if len(tup[0]) < 7:
        tabs += '\t' #very lazy way to make columns consistent til somebody has a 15+ username lmao
    print tup[0],tabs,tup[1]
print ''
nationslist = sorted(nations.items(), key=lambda tup: tup[1])
nationslist.reverse()
for tup in nationslist:
    print tup[0],'\t',tup[1]
print ''

timesort = sorted(times, key=lambda x: 60*x[0] + x[1])
for i in xrange(len(timesort)):
    print i+1, games[times.index(timesort[i])], timesort[i]
