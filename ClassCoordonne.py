class ClassCoordonne:
    def __init__(self):
        self.graph = {
            'Kinshasa':{
                'Bandundu':75,
                'Matadi':118,
                'Kananga':140,
            },
            'Bandundu':{
                'Mbandaka':71,
                'Kinshasa':75
            },
            'Mbandaka':{
                'Bandundu':71,
                'Kananga':151
            },
            'Kananga':{
                'Tshikapa':80,
                'Mbuji-Mayi':99,
                'Mbandaka':151,
                'Kinshasa':140,
                
            },
            'Mbuji-Mayi':{
                'Kananga':99,
                'Kolwezi':211,
            },
            'Tshikapa':{
                'Kamina':97,
                'Kananga':80,
                'Mwene-Ditu':146
            },
            'Kolwezi':{
                'Likasi':85,
                'Kundelungu':90,
                'Mbuji-Mayi':211,
                'Kamina':101
            },
            'Kundelungu':{
                'Kolwezi':90,
            },
            'Kamina':{
                'Kolwezi':101,
                'Tshikapa':97,
                'Mwene-Ditu':138
            },
        
            'Mwene-Ditu':{
                'Kamina':138,
                'Tshikapa':146,
                'Idiofa':120
            },
            'Likasi':{
                'Kolwezi':85,
                'Bukavu':142,
                'Lubumbashi':98
            },
            'Bukavu':{
                'Likasi':142,
                'Goma':92
            },
            'Goma':{
                'Bukavu':92,
                'Kisangani':87
            },
            'Kisangani':{
                'Goma':87
            },
            'Lubumbashi':{
                'Likasi':98,
                'Kasumbalesa':86
            },
            'Kasumbalesa':{
                'Lubumbashi':86
            },
            'Idiofa':{
                'Mwene-Ditu':120,
                'Kikwit':75,
            },
            'Kikwit':{
                'Idiofa':75,
                'Boma':70
            },
            'Boma':{
                'Kikwit':70,
                'Matadi':111
            },
            'Matadi':{
                'Boma':111,
                'Kinshasa':118
            }
        }
        self.coordinates = {
        'Kinshasa':(15.342, -4.319),
        'Bandundu':(17.377, -3.320),
        'Mbandaka':(18.256, 0.047),
        'Kananga':(22.408, -5.895),
        'Mbuji-Mayi':(23.599, -6.125),
        'Tshikapa':(20.788, -6.423),
        'Kolwezi':(25.466, -10.716),
        'Kundelungu':(27.486, -11.701),
        'Kamina':(25.003, -8.735),
        'Mwene-Ditu':(23.448, -7.006),
        'Likasi':(26.739, -10.989),
        'Bukavu':(28.859, -2.505),
        'Goma':(29.225, -1.666),
        'Kisangani':(25.205, 0.518),
        'Lubumbashi':(27.482, -11.664),
        'Kasumbalesa':(27.796, -12.202),
        'Idiofa':(19.588, -4.969),
        'Kikwit':(18.817, -5.038),
        'Boma':(13.050, -5.850),
        'Matadi':(13.460,-5.825), 
    }