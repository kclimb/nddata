# Unofficial times:
# DAN: (76,17) by C (no proof)
# SPY: (42,22) by C (no proof)
# LIE: (32,1) by C (no proof)

games = ["SCK", "STFD", "MHM", "TRT", "FIN", "SSH", "DOG", "CAR", "DDI", "SHA", "CUR", "CLK", "TRN", "DAN",
        "CRE", "ICE", "CRY", "VEN", "HAU", "RAN", "WAC", "TOT", "SCKR", "SAW", "CAP", "ASH", "TMB", "DED",
        "GTH", "SPY", "MED", "LIE", "SEA"]

times = [(4, 14), (11, 54), (9, 56),	# SCK STFD MHM
         (24, 23), (17, 12), (56, 14),	# TRT FIN SSH
         (35, 1), (43, 52), (54, 3),	# DOG CAR DDI
         (57, 30), (44, 36), (53, 41),	# SHA CUR CLK
         (63, 15), (77, 51), (78, 14),	# TRN DAN CRE
         (58, 52), (59, 17), (79, 18),	# ICE CRY VEN
         (64, 27), (66, 22), (53, 56),	# HAU RAN WAC
         (69, 19), (11, 53), (89, 13),	# TOT SCKR SAW
         (53, 4), (52, 45), (35, 33),	# CAP ASH TMB
         (45, 50), (24, 52), (44, 15),	# DED GTH SPY
         (38, 44), (32, 23), (33, 50)]	# MED LIE SEA

sub1 = [guy[0] < 60 for guy in times]
peeps = ['toburr', 'toburr', 'toburr', 'rpgg', 'rpgg', 'toburr', 'eca',
         'toburr', 'toburr', 'toburr', 'toburr', 'toburr',
         'corrine', 'nancyjilk', 'arglefumph', 'eca', 'yandema',
         'yandema', 'karen', 'yandema', 'toburr', 'yandema',
         'eca', 'yandema', 'rpgg', 'bluetooth', 'yandema',
         'rpgg', 'yandema', 'yandema', 'corrine', 'corrine',
         'arglefumph']
countries = {'toburr': 'USA', 'yandema': 'USA', 'eca': 'USA', 'arglefumph': 'USA', 'lisa': 'CAN',
            'rpgg': 'CAN', 'nancyjilk': 'CAN', 'tkd': 'USA', 'corrine': 'USA', 'ttc': 'AUS',
             'may': 'RUS', 'bluetooth': 'USA', 'karen': 'USA'} #don't actually know Karen's country, but she's implied Minnesota

print 'Game\tTime (min, sec)\tSub 1?\tRecord Holder'
print '-------------------------------------'
for i in xrange(len(times)):
    print games[i], '\t', times[i], '\t', sub1[i], '\t', peeps[i]

seconds = sum([guy[1] for guy in times])
minutes = sum([guy[0] for guy in times]) + seconds / 60
seconds = seconds % 60
hours = minutes / 60
minutes = minutes % 60
print hours, minutes, seconds
print 24 * 60. * 60 / (hours * 60. * 60 + minutes * 60 + seconds)

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
print sorted(reccounts.items(), key=lambda tup: tup[1])
print sorted(nations.items(), key=lambda tup: tup[1])
print ''

timesort = sorted(times, key=lambda x: 60*x[0] + x[1])
for i in xrange(len(timesort)):
    print timesort[i]
