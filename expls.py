import numpy as np

def getLeaf(i):
    if i == 1: 
        return [ (17, -4), (20, 7), (-10, 15), (-5, 20), (-8, -20), (20, 0), (5, 10), (22, 4), (-30, 5), (-35, -6)]

    elif i == 2:
        return [ (17, -4), (20, 7), (-10, 15), (-5, 20), (-8, -20)]
    
    elif i == 3:
        return [ (10, 0), (10, 10), (0, 9), (15, 8.2), (10, 3.6), (3.66, 10.13)]
    
    elif i == 4:
        return [ (10, 0), (10, 10), (0, 9), (15, 8.2), (10, 3.6), (17, 4.1)]
    
    elif i == 5:
        return [(110.60289476284164, 0.0),
 (172.66269590402504, 38.00593334790393),
 (160.04780458535853, 74.04599928279603),
 (91.28819245356952, 69.39547975534474),
 (84.53031269794627, 99.51677748032657),
 (60.82883221325307, 114.73534898240658),
 (44.21192450783797, 159.23696070102386),
 (9.237648714392932, 170.37840524965335),
 (-16.7481641066041, 102.15928160389913),
 (-46.50537127325378, 116.71968057336491),
 (-77.27938662754069, 113.97856801033778),
 (-102.55266333593273, 97.14304271129762),
 (-114.95662921751178, 69.16710888299222),
 (-120.8788321280685, 40.72882066269916),
 (-178.2827001181997, 19.38941210325078),
 (-154.36600909848062, -16.788315204785544),
 (-140.3941738848047, -47.30430489420864),
 (-108.0101151223719, -64.98753002750344),
 (-79.36277598624645, -75.17641460041725),
 (-94.59789671726276, -139.5214594105088),
 (-56.48931447500145, -141.77748850964534),
 (-25.11407890334805, -153.18910434475615),
 (7.280803914360199, -134.28652660620753),
 (27.132268556261472, -97.72159954396669),
 (89.91828075688638, -169.60386953296788),
 (72.24816247650075, -85.05711240212986),
 (122.04465697419597, -92.77593623741028),
 (108.45855133932353, -50.1782691458383),
 (140.47334670755347, -30.92052179639243)]

    elif i == 6:
        bias = np.array((193.980769230769, -195.706730769231))
        leaves = []
        l_prep = [(244.461538461538,-50.7259615384615),
        (168.134615384615, -40.2259615384615),
        (141.884615384615, -81.4182692307691),
        (76.0576923076923, -37.3990384615384),
        (216.899038461538, -111.605769230769),
        (304.129807692308, -88.8894230769231),
        (322.201923076923, -130.6875),
        (283.9375, -184.701923076923),
        (301.302884615385, -202.471153846154),
        (304.9375, -254.971153846154),
        (210.841346153846, -279.605769230769),
        (185.197115384616, -244.471153846154),
        (172.879807692308, -314.538461538462),
        (109.879807692308, -310.096153846154),
        (46.4759615384617, -278.596153846154),
        (59.3990384615386, -214.990384615385),
        (114.927884615385, -204.692307692308),
        (21.8413461538463, -177.432692307692),
        (36.5817307692309, -130.586538461539),
        (56.3701923076924, -102.317307692308)]
        for i in l_prep:
            leaves.append(list(np.array(i) - bias))
        return leaves
    elif i == 7:
        leaves = []
        r = 100
        phi = np.linspace(0, np.pi*2, 180)
        noise = np.random.rand(len(phi))*100
        r = r+noise
        x = r*np.cos(phi)
        y = r*np.sin(phi)
        for i in range(len(phi)-1):
            leaves.append((x[i], y[i]))
        return leaves
    
    elif i == 8:
        return [(382232.19612568984, 1669699.5022962443),
        (-793850.3363108455, 1774076.9858557906),
        (-100570.35646826492, 1776254.1359321831),
        (-1220641.8204228252, 1539821.0049460274),
        (-1579507.508434653, 1961715.0071746744),
        (-1135738.0101247514, 387515.7788613965),
        (-1786697.9520706413, 845462.1951430056),
        (-543549.3561942923, 851455.761190787),
        (-1485682.5802975388, 1017561.3099198448),
        (-624207.0481840938, 347250.31807524664),
        (-1686786.9928033967, 1591924.821825396),
        (-1064949.4274241629, 942491.6371049358),
        (-677197.5472906884, 1311329.2285473822),
        (626242.1752286307, 413934.47676894814),
        (471233.0662309636, 1199303.0034674988),
        (77088.23095617101, 779420.9903135517),
        (591425.7126862309, 796154.0118430099),
        (-48744.03914481909, 1116010.257654382),
        (162303.5590977808, 459557.24823862186),
        (-82265.61026772165, 1440789.5493917174),
        (706415.9564142299, -9269.15908840904),
        (2151719.0211879234, 1499245.8027622122),
        (2205860.986376081, 1594421.813129084),
        (2164335.9205720956, 1753826.148565951),
        (2242243.223393609, 1541128.609757172),
        (2068464.0723548122, 1764460.4962562916),
        (1168412.988447556, 240624.60196588282),
        (1647323.1974522723, -140407.93928191415),
        (1482345.5920262202, 282398.0699358247),
        (905081.5386275313, 203326.08147657267),
        (1690139.2257012606, 468842.53908063134),
        (855648.3383591378, 1020188.0306285706),
        (1100155.0311186516, 1033631.5245906294),
        (1228870.759231691, 784745.727511052),
        (1796326.9055929969, 681977.2816323288),
        (1387757.9110602825, 1144489.1428100008),
        (1166051.412357807, 584886.1139379513),
        (1784336.3145900138, 906172.0474786261),
        (745576.119841513, 1514885.7018670046),
        (1603557.3432459275, 991884.442011311),
        (2018204.8620746166, 1145785.7467117482),
        (1896262.866891583, 1098112.1183013287),
        (1912663.6755449201, 1118933.9326595617),
        (2046998.9863101859, 1297760.56194222),
        (1880201.452209886, 1569744.994203125),
        (1771136.145663433, 1295850.5605714275),
        (2269031.6329678837, 1994677.39647615),
        (1053273.977768733, 1586185.0104757904)]