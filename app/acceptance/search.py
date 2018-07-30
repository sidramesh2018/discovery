

def generate_search_tests():
    return {
        'actions': {
            'naics_bmo': {
                'params': {'naics': '238220'},
                'action': ('#naics-code', 'select[238220]'),
                'naics': ('238220', 78, True),
                'vehicle': ('all', 4, True),
                'pool': ('all', 8, 7, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (35, 'results/csv/?naics=238220'),
                'vendor_table': (35, 'h_naics_results', 'desc')
            },
            'naics_bmo_sb': {
                'params': {'naics': '561730'},
                'action': ('#naics-code', 'select[561730]'),
                'naics': ('561730', 78, True),
                'vehicle': ('all', 3, True),
                'pool': ('all', 5, 4, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (17, 'results/csv/?naics=561730'),
                'vendor_table': (17, 'h_naics_results', 'desc')
            },
            'naics_hcats': {
                'params': {'naics': '611710'},
                'action': ('#naics-code', 'select[611710]'),
                'naics': ('611710', 78, True),
                'vehicle': ('all', 4, True),
                'pool': ('all', 4, 3, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (28, 'results/csv/?naics=611710'),
                'vendor_table': (28, 'h_naics_results', 'desc')
            },
            'naics_hcats_sb': {
                'params': {'naics': '541618'},
                'action': ('#naics-code', 'select[541618]'),
                'naics': ('541618', 78, True),
                'vehicle': ('all', 5, True),
                'pool': ('all', 5, 4, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (37, 'results/csv/?naics=541618'),
                'vendor_table': (37, 'h_naics_results', 'desc')
            },
            'naics_oasis': {
                'params': {'naics': '541712'},
                'action': ('#naics-code', 'select[541712]'),
                'naics': ('541712', 78, True),
                'vehicle': ('all', 4, True),
                'pool': ('all', 10, 9, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (50, 'results/csv/?naics=541712'),
                'vendor_table': (50, 'h_naics_results', 'desc')
            },
            'naics_oasis_sb': {
                'params': {'naics': '541810'},
                'action': ('#naics-code', 'select[541810]'),
                'naics': ('541810', 78, True),
                'vehicle': ('all', 4, True),
                'pool': ('all', 4, 3, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (30, 'results/csv/?naics=541810'),
                'vendor_table': (30, 'h_naics_results', 'desc')
            },
            'naics_pss': {
                'params': {'naics': '236220'},
                'action': ('#naics-code', 'select[236220]'),
                'naics': ('236220', 78, True),
                'vehicle': ('all', 4, True),
                'pool': ('all', 4, 3, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (28, 'results/csv/?naics=236220'),
                'vendor_table': (28, 'h_naics_results', 'desc')
            },
            
            'vehicle_bmo': {
                'params': {'vehicle': 'BMO'},
                'action': ('#vehicle-id', 'select[BMO]'),
                'naics': ('all', 15, True),
                'vehicle': ('BMO', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('', 6, True, True),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (14, 'results/csv/?vehicle=BMO'),
                'vendor_table': (14, 'h_naics_results', 'desc')
            },
            'vehicle_bmo_sb': {
                'params': {'vehicle': 'BMO_SB'},
                'action': ('#vehicle-id', 'select[BMO_SB]'),
                'naics': ('all', 15, True),
                'vehicle': ('BMO_SB', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('', 6, True, True),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (23, 'results/csv/?vehicle=BMO_SB'),
                'vendor_table': (23, 'h_naics_results', 'desc')
            },
            'vehicle_hcats': {
                'params': {'vehicle': 'HCATS'},
                'action': ('#vehicle-id', 'select[HCATS]'),
                'naics': ('all', 9, True),
                'vehicle': ('HCATS', 8, True),
                'pool': ('', 2, 2, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (12, 'results/csv/?vehicle=HCATS'),
                'vendor_table': (12, 'h_naics_results', 'desc')
            },
            'vehicle_hcats_sb': {
                'params': {'vehicle': 'HCATS_SB'},
                'action': ('#vehicle-id', 'select[HCATS_SB]'),
                'naics': ('all', 9, True),
                'vehicle': ('HCATS_SB', 8, True),
                'pool': ('', 2, 2, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (17, 'results/csv/?vehicle=HCATS_SB'),
                'vendor_table': (17, 'h_naics_results', 'desc')
            },
            'vehicle_oasis': {
                'params': {'vehicle': 'OASIS'},
                'action': ('#vehicle-id', 'select[OASIS]'),
                'naics': ('all', 29, True),
                'vehicle': ('OASIS', 8, True),
                'pool': ('', 7, 7, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (29, 'results/csv/?vehicle=OASIS'),
                'vendor_table': (29, 'h_naics_results', 'desc')
            },
            'vehicle_oasis_sb': {
                'params': {'vehicle': 'OASIS_SB'},
                'action': ('#vehicle-id', 'select[OASIS_SB]'),
                'naics': ('all', 29, True),
                'vehicle': ('OASIS_SB', 8, True),
                'pool': ('', 7, 7, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (46, 'results/csv/?vehicle=OASIS_SB'),
                'vendor_table': (46, 'h_naics_results', 'desc')
            },
            'vehicle_pss': {
                'params': {'vehicle': 'PSS'},
                'action': ('#vehicle-id', 'select[PSS]'),
                'naics': ('all', 58, True),
                'vehicle': ('PSS', 8, True),
                'pool': ('', 7, 7, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (66, 'results/csv/?vehicle=PSS'),
                'vendor_table': (50, 'h_naics_results', 'desc', ('Prev', '1'), '2')
            },
            
            'pool_bmo_1': {
                'params': {'pools': 'BMO_1'},
                'action': ('#pool-id', 'select[BMO_1]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_1', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_1'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_2': {
                'params': {'pools': 'BMO_2'},
                'action': ('#pool-id', 'select[BMO_2]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_2', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_2'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_3': {
                'params': {'pools': 'BMO_3'},
                'action': ('#pool-id', 'select[BMO_3]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_3', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_3'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_4': {
                'params': {'pools': 'BMO_4'},
                'action': ('#pool-id', 'select[BMO_4]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_4', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_4'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_5': {
                'params': {'pools': 'BMO_5'},
                'action': ('#pool-id', 'select[BMO_5]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_5', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (9, 'results/csv/?pools=BMO_5'),
                'vendor_table': (9, 'h_naics_results', 'desc')
            },
            'pool_bmo_6': {
                'params': {'pools': 'BMO_6'},
                'action': ('#pool-id', 'select[BMO_6]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_6', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (9, 'results/csv/?pools=BMO_6'),
                'vendor_table': (9, 'h_naics_results', 'desc')
            },
            'pool_bmo_7': {
                'params': {'pools': 'BMO_7'},
                'action': ('#pool-id', 'select[BMO_7]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_7', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_7'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_8': {
                'params': {'pools': 'BMO_8'},
                'action': ('#pool-id', 'select[BMO_8]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_8', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_8'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_9': {
                'params': {'pools': 'BMO_9'},
                'action': ('#pool-id', 'select[BMO_9]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_9', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (8, 'results/csv/?pools=BMO_9'),
                'vendor_table': (8, 'h_naics_results', 'desc')
            },
            'pool_bmo_10': {
                'params': {'pools': 'BMO_10'},
                'action': ('#pool-id', 'select[BMO_10]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_10', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (8, 'results/csv/?pools=BMO_10'),
                'vendor_table': (8, 'h_naics_results', 'desc')
            },
            'pool_bmo_11': {
                'params': {'pools': 'BMO_11'},
                'action': ('#pool-id', 'select[BMO_11]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_11', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (8, 'results/csv/?pools=BMO_11'),
                'vendor_table': (8, 'h_naics_results', 'desc')
            },
            'pool_bmo_12': {
                'params': {'pools': 'BMO_12'},
                'action': ('#pool-id', 'select[BMO_12]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_12', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (8, 'results/csv/?pools=BMO_12'),
                'vendor_table': (8, 'h_naics_results', 'desc')
            },
            'pool_bmo_13': {
                'params': {'pools': 'BMO_13'},
                'action': ('#pool-id', 'select[BMO_13]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_13', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (9, 'results/csv/?pools=BMO_13'),
                'vendor_table': (9, 'h_naics_results', 'desc')
            },
            'pool_bmo_14': {
                'params': {'pools': 'BMO_14'},
                'action': ('#pool-id', 'select[BMO_14]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_14', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (9, 'results/csv/?pools=BMO_14'),
                'vendor_table': (9, 'h_naics_results', 'desc')
            },
            'pool_bmo_15': {
                'params': {'pools': 'BMO_15'},
                'action': ('#pool-id', 'select[BMO_15]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_15', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (9, 'results/csv/?pools=BMO_15'),
                'vendor_table': (9, 'h_naics_results', 'desc')
            },
            'pool_bmo_16': {
                'params': {'pools': 'BMO_16'},
                'action': ('#pool-id', 'select[BMO_16]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_16', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (9, 'results/csv/?pools=BMO_16'),
                'vendor_table': (9, 'h_naics_results', 'desc')
            },
            'pool_bmo_17': {
                'params': {'pools': 'BMO_17'},
                'action': ('#pool-id', 'select[BMO_17]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_17', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (3, 'results/csv/?pools=BMO_17'),
                'vendor_table': (3, 'h_naics_results', 'desc')
            },
            'pool_bmo_mix_1': {
                'params': {'vehicle': 'BMO', 'pools': 'BMO_1,BMO_5,BMO_17'},
                'action': (
                    ('#vehicle-id', 'select[BMO]'),
                    ('#pool-id', 'select[BMO_1]'),
                    ('#pool-id', 'select[BMO_17]'),
                    ('#pool-id', 'select[BMO_5]')
                ),
                'naics': ('all', 4, True),
                'vehicle': ('BMO', 8, True),
                'pool': (('BMO_1', 'BMO_5', 'BMO_17'), 17, 3, True),
                'zone': ('', 6, True, True),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (2, 'results/csv/?vehicle=BMO&pools=BMO_1,BMO_5,BMO_17'),
                'vendor_table': (2, 'h_naics_results', 'desc')
            },
                    
            'pool_bmo_sb_1': {
                'params': {'pools': 'BMO_SB_1'},
                'action': ('#pool-id', 'select[BMO_SB_1]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_1', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_1'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_2': {
                'params': {'pools': 'BMO_SB_2'},
                'action': ('#pool-id', 'select[BMO_SB_2]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_2', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_2'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_3': {
                'params': {'pools': 'BMO_SB_3'},
                'action': ('#pool-id', 'select[BMO_SB_3]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_3', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_3'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_4': {
                'params': {'pools': 'BMO_SB_4'},
                'action': ('#pool-id', 'select[BMO_SB_4]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_4', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (6, 'results/csv/?pools=BMO_SB_4'),
                'vendor_table': (6, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_5': {
                'params': {'pools': 'BMO_SB_5'},
                'action': ('#pool-id', 'select[BMO_SB_5]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_5', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_5'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_6': {
                'params': {'pools': 'BMO_SB_6'},
                'action': ('#pool-id', 'select[BMO_SB_6]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_6', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_6'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_7': {
                'params': {'pools': 'BMO_SB_7'},
                'action': ('#pool-id', 'select[BMO_SB_7]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_7', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_7'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_8': {
                'params': {'pools': 'BMO_SB_8'},
                'action': ('#pool-id', 'select[BMO_SB_8]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_8', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_8'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_9': {
                'params': {'pools': 'BMO_SB_9'},
                'action': ('#pool-id', 'select[BMO_SB_9]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_9', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_9'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_10': {
                'params': {'pools': 'BMO_SB_10'},
                'action': ('#pool-id', 'select[BMO_SB_10]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_10', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_10'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_11': {
                'params': {'pools': 'BMO_SB_11'},
                'action': ('#pool-id', 'select[BMO_SB_11]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_11', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_11'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_12': {
                'params': {'pools': 'BMO_SB_12'},
                'action': ('#pool-id', 'select[BMO_SB_12]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_12', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_12'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_13': {
                'params': {'pools': 'BMO_SB_13'},
                'action': ('#pool-id', 'select[BMO_SB_13]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_13', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_13'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_14': {
                'params': {'pools': 'BMO_SB_14'},
                'action': ('#pool-id', 'select[BMO_SB_14]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_14', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_14'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_15': {
                'params': {'pools': 'BMO_SB_15'},
                'action': ('#pool-id', 'select[BMO_SB_15]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_15', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_15'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_16': {
                'params': {'pools': 'BMO_SB_16'},
                'action': ('#pool-id', 'select[BMO_SB_16]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_16', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=BMO_SB_16'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_17': {
                'params': {'pools': 'BMO_SB_17'},
                'action': ('#pool-id', 'select[BMO_SB_17]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('BMO_SB_17', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (1, 'results/csv/?pools=BMO_SB_17'),
                'vendor_table': (1, 'h_naics_results', 'desc')
            },
            'pool_bmo_sb_mix_1': {
                'params': {'vehicle': 'BMO_SB', 'pools': 'BMO_SB_1,BMO_SB_5,BMO_SB_17'},
                'action': (
                    ('#vehicle-id', 'select[BMO_SB]'),
                    ('#pool-id', 'select[BMO_SB_1]'),
                    ('#pool-id', 'select[BMO_SB_5]'),
                    ('#pool-id', 'select[BMO_SB_17]')
                ),
                'naics': ('all', 4, True),
                'vehicle': ('BMO_SB', 8, True),
                'pool': (('BMO_SB_1', 'BMO_SB_5', 'BMO_SB_17'), 17, 3, True),
                'zone': ('', 6, True, True),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (1, 'results/csv/?vehicle=BMO_SB&pools=BMO_SB_1,BMO_SB_5,BMO_SB_17'),
                'vendor_table': (1, 'h_naics_results', 'desc')
            },
            
            'pool_hcats_1': {
                'params': {'pools': 'HCATS_1'},
                'action': ('#pool-id', 'select[HCATS_1]'),
                'naics': ('all', 4, True),
                'vehicle': ('all', 8, True),
                'pool': ('HCATS_1', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=HCATS_1'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_hcats_2': {
                'params': {'pools': 'HCATS_2'},
                'action': ('#pool-id', 'select[HCATS_2]'),
                'naics': ('all', 6, True),
                'vehicle': ('all', 8, True),
                'pool': ('HCATS_2', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=HCATS_2'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_hcats_mix_1': {
                'params': {'vehicle': 'HCATS', 'pools': 'HCATS_1,HCATS_2'},
                'action': (
                    ('#vehicle-id', 'select[HCATS]'),
                    ('#pool-id', 'select[HCATS_2]'),
                    ('#pool-id', 'select[HCATS_1]')
                ),
                'naics': ('all', 9, True),
                'vehicle': ('HCATS', 8, True),
                'pool': (('HCATS_1', 'HCATS_2'), 2, 2, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (8, 'results/csv/?vehicle=HCATS&pools=HCATS_1,HCATS_2'),
                'vendor_table': (8, 'h_naics_results', 'desc')
            },
            
            'pool_hcats_sb_1': {
                'params': {'pools': 'HCATS_SB_1'},
                'action': ('#pool-id', 'select[HCATS_SB_1]'),
                'naics': ('all', 4, True),
                'vehicle': ('all', 8, True),
                'pool': ('HCATS_SB_1', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=HCATS_SB_1'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_hcats_sb_2': {
                'params': {'pools': 'HCATS_SB_2'},
                'action': ('#pool-id', 'select[HCATS_SB_2]'),
                'naics': ('all', 6, True),
                'vehicle': ('all', 8, True),
                'pool': ('HCATS_SB_2', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=HCATS_SB_2'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_hcats_sb_mix_1': {
                'params': {'vehicle': 'HCATS_SB', 'pools': 'HCATS_SB_1,HCATS_SB_2'},
                'action': (
                    ('#vehicle-id', 'select[HCATS_SB]'),
                    ('#pool-id', 'select[HCATS_SB_1]'),
                    ('#pool-id', 'select[HCATS_SB_2]')
                ),
                'naics': ('all', 9, True),
                'vehicle': ('HCATS_SB', 8, True),
                'pool': (('HCATS_SB_1', 'HCATS_SB_2'), 2, 2, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (3, 'results/csv/?vehicle=HCATS_SB&pools=HCATS_SB_1,HCATS_SB_2'),
                'vendor_table': (3, 'h_naics_results', 'desc')
            },
            
            'pool_oasis_1': {
                'params': {'pools': 'OASIS_1'},
                'action': ('#pool-id', 'select[OASIS_1]'),
                'naics': ('all', 22, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_1', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_1'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_2': {
                'params': {'pools': 'OASIS_2'},
                'action': ('#pool-id', 'select[OASIS_2]'),
                'naics': ('all', 6, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_2', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_2'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_3': {
                'params': {'pools': 'OASIS_3'},
                'action': ('#pool-id', 'select[OASIS_3]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_3', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_3'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_4': {
                'params': {'pools': 'OASIS_4'},
                'action': ('#pool-id', 'select[OASIS_4]'),
                'naics': ('all', 3, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_4', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_4'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_5a': {
                'params': {'pools': 'OASIS_5A'},
                'action': ('#pool-id', 'select[OASIS_5A]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_5A', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_5A'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_5b': {
                'params': {'pools': 'OASIS_5B'},
                'action': ('#pool-id', 'select[OASIS_5B]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_5B', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_5B'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_6': {
                'params': {'pools': 'OASIS_6'},
                'action': ('#pool-id', 'select[OASIS_6]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_6', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_6'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_mix_1': {
                'params': {'vehicle': 'OASIS', 'pools': 'OASIS_1,OASIS_2,OASIS_5B,OASIS_6'},
                'action': (
                    ('#vehicle-id', 'select[OASIS]'),
                    ('#pool-id', 'select[OASIS_6]'),
                    ('#pool-id', 'select[OASIS_1]'),
                    ('#pool-id', 'select[OASIS_5B]'),
                    ('#pool-id', 'select[OASIS_2]')
                ),
                'naics': ('all', 28, True),
                'vehicle': ('OASIS', 8, True),
                'pool': (('OASIS_1', 'OASIS_2', 'OASIS_5B', 'OASIS_6'), 7, 4, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (2, 'results/csv/?vehicle=OASIS&pools=OASIS_1,OASIS_2,OASIS_5B,OASIS_6'),
                'vendor_table': (2, 'h_naics_results', 'desc')
            },
            
            'pool_oasis_sb_1': {
                'params': {'pools': 'OASIS_SB_1'},
                'action': ('#pool-id', 'select[OASIS_SB_1]'),
                'naics': ('all', 22, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_SB_1', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_SB_1'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_sb_2': {
                'params': {'pools': 'OASIS_SB_2'},
                'action': ('#pool-id', 'select[OASIS_SB_2]'),
                'naics': ('all', 6, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_SB_2', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_SB_2'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_sb_3': {
                'params': {'pools': 'OASIS_SB_3'},
                'action': ('#pool-id', 'select[OASIS_SB_3]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_SB_3', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_SB_3'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_sb_4': {
                'params': {'pools': 'OASIS_SB_4'},
                'action': ('#pool-id', 'select[OASIS_SB_4]'),
                'naics': ('all', 3, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_SB_4', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_SB_4'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_sb_5a': {
                'params': {'pools': 'OASIS_SB_5A'},
                'action': ('#pool-id', 'select[OASIS_SB_5A]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_SB_5A', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_SB_5A'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_sb_5b': {
                'params': {'pools': 'OASIS_SB_5B'},
                'action': ('#pool-id', 'select[OASIS_SB_5B]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_SB_5B', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_SB_5B'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_sb_6': {
                'params': {'pools': 'OASIS_SB_6'},
                'action': ('#pool-id', 'select[OASIS_SB_6]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('OASIS_SB_6', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=OASIS_SB_6'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_oasis_sb_mix_1': {
                'params': {'vehicle': 'OASIS_SB', 'pools': 'OASIS_SB_2,OASIS_SB_5A,OASIS_SB_5B'},
                'action': (
                    ('#vehicle-id', 'select[OASIS_SB]'),
                    ('#pool-id', 'select[OASIS_SB_2]'),
                    ('#pool-id', 'select[OASIS_SB_5A]'),
                    ('#pool-id', 'select[OASIS_SB_5B]')
                ),
                'naics': ('all', 7, True),
                'vehicle': ('OASIS_SB', 8, True),
                'pool': (('OASIS_SB_2', 'OASIS_SB_5A', 'OASIS_SB_5B'), 7, 3, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (0, 'results/csv/?vehicle=OASIS_SB&pools=OASIS_SB_2,OASIS_SB_5A,OASIS_SB_5B'),
                'vendor_table': (0, 'h_naics_results', 'desc')
            },
            
            'pool_pss_382': {
                'params': {'pools': 'PSS_382'},
                'action': ('#pool-id', 'select[PSS_382]'),
                'naics': ('all', 2, True),
                'vehicle': ('all', 8, True),
                'pool': ('PSS_382', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=PSS_382'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_pss_520': {
                'params': {'pools': 'PSS_520'},
                'action': ('#pool-id', 'select[PSS_520]'),
                'naics': ('all', 13, True),
                'vehicle': ('all', 8, True),
                'pool': ('PSS_520', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=PSS_520'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_pss_541': {
                'params': {'pools': 'PSS_541'},
                'action': ('#pool-id', 'select[PSS_541]'),
                'naics': ('all', 11, True),
                'vehicle': ('all', 8, True),
                'pool': ('PSS_541', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=PSS_541'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_pss_871': {
                'params': {'pools': 'PSS_871'},
                'action': ('#pool-id', 'select[PSS_871]'),
                'naics': ('all', 5, True),
                'vehicle': ('all', 8, True),
                'pool': ('PSS_871', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=PSS_871'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_pss_874': {
                'params': {'pools': 'PSS_874'},
                'action': ('#pool-id', 'select[PSS_874]'),
                'naics': ('all', 16, True),
                'vehicle': ('all', 8, True),
                'pool': ('PSS_874', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=PSS_874'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_pss_874500': {
                'params': {'pools': 'PSS_874500'},
                'action': ('#pool-id', 'select[PSS_874500]'),
                'naics': ('all', 11, True),
                'vehicle': ('all', 8, True),
                'pool': ('PSS_874500', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=PSS_874500'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_pss_899': {
                'params': {'pools': 'PSS_899'},
                'action': ('#pool-id', 'select[PSS_899]'),
                'naics': ('all', 7, True),
                'vehicle': ('all', 8, True),
                'pool': ('PSS_899', 60, 1, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (10, 'results/csv/?pools=PSS_899'),
                'vendor_table': (10, 'h_naics_results', 'desc')
            },
            'pool_pss_mix_1': {
                'params': {'vehicle': 'PSS', 'pools': 'PSS_382,PSS_541,PSS_874'},
                'action': (
                    ('#vehicle-id', 'select[PSS]'),
                    ('#pool-id', 'select[PSS_541]'),
                    ('#pool-id', 'select[PSS_382]'),
                    ('#pool-id', 'select[PSS_874]')
                ),
                'naics': ('all', 27, True),
                'vehicle': ('PSS', 8, True),
                'pool': (('PSS_382', 'PSS_541', 'PSS_874'), 7, 3, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (0, 'results/csv/?vehicle=PSS&pools=PSS_382,PSS_541,PSS_874'),
                'vendor_table': (0, 'h_naics_results', 'desc')
            },
            
            'pool_remove_1': {
                'params': {
                    'test': 'true',
                    'vehicle': 'OASIS'
                },
                'action': (
                    ('#vehicle-id', 'select[OASIS]'),
                    ('#pool-id', 'select[OASIS_2]'),
                    ('.select2-selection__choice__remove', 'click')
                ),
                'naics': ('all', 29, True),
                'vehicle': ('OASIS', 8, True),
                'pool': ('', 7, 7, True),
                'zone': ('', 6, False, False),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (29, 'results/csv/?vehicle=OASIS'),
                'vendor_table': (5, 'h_naics_results', 'desc', ('Prev', '1'), '6')
            },
            'pool_clear_1': {
                'params': {
                    'test': 'true',
                    'vehicle': 'BMO_SB'
                },
                'action': (
                    ('#vehicle-id', 'select[BMO_SB]'),
                    ('#pool-id', 'select[BMO_SB_2]'),
                    ('#pool-id', 'select[BMO_SB_11]'),
                    ('#pool-id', 'select[BMO_SB_7]'),
                    ('.select2-selection__clear', 'click')
                ),
                'naics': ('all', 15, True),
                'vehicle': ('BMO_SB', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('', 6, True, True),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (23, 'results/csv/?vehicle=BMO_SB'),
                'vendor_table': (5, 'h_naics_results', 'desc', ('Prev', '1'), '5')
            },
            
            'bmo_zone_1': {
                'params': {'vehicle': 'BMO', 'zones': '1'},
                'action': (('#vehicle-id', 'select[BMO]'), ('#zone-id', 'select[1]')),
                'naics': ('all', 15, True),
                'vehicle': ('BMO', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('1', 6, True, True),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (9, 'results/csv/?vehicle=BMO&zones=1'),
                'vendor_table': (9, 'h_naics_results', 'desc')
            },
            'bmo_sb_zone_2': {
                'params': {'vehicle': 'BMO_SB', 'zones': '2'},
                'action': (('#vehicle-id', 'select[BMO_SB]'), ('#zone-id', 'select[2]')),
                'naics': ('all', 15, True),
                'vehicle': ('BMO_SB', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('2', 6, True, True),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (13, 'results/csv/?vehicle=BMO_SB&zones=2'),
                'vendor_table': (13, 'h_naics_results', 'desc')
            },
            'bmo_zone_3': {
                'params': {'vehicle': 'BMO', 'zones': '3'},
                'action': (('#vehicle-id', 'select[BMO]'), ('#zone-id', 'select[3]')),
                'naics': ('all', 15, True),
                'vehicle': ('BMO', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('3', 6, True, True),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (8, 'results/csv/?vehicle=BMO&zones=3'),
                'vendor_table': (8, 'h_naics_results', 'desc')
            },
            'bmo_sb_zone_4': {
                'params': {'vehicle': 'BMO_SB', 'zones': '4'},
                'action': (('#vehicle-id', 'select[BMO_SB]'), ('#zone-id', 'select[4]')),
                'naics': ('all', 15, True),
                'vehicle': ('BMO_SB', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('4', 6, True, True),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (15, 'results/csv/?vehicle=BMO_SB&zones=4'),
                'vendor_table': (15, 'h_naics_results', 'desc')
            },
            'bmo_zone_5': {
                'params': {'vehicle': 'BMO', 'zones': '5'},
                'action': (('#vehicle-id', 'select[BMO]'), ('#zone-id', 'select[5]')),
                'naics': ('all', 15, True),
                'vehicle': ('BMO', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('5', 6, True, True),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (8, 'results/csv/?vehicle=BMO&zones=5'),
                'vendor_table': (8, 'h_naics_results', 'desc')
            },
            'bmo_sb_zone_6': {
                'params': {'vehicle': 'BMO_SB', 'zones': '6'},
                'action': (('#vehicle-id', 'select[BMO_SB]'), ('#zone-id', 'select[6]')),
                'naics': ('all', 15, True),
                'vehicle': ('BMO_SB', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('6', 6, True, True),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (13, 'results/csv/?vehicle=BMO_SB&zones=6'),
                'vendor_table': (13, 'h_naics_results', 'desc')
            },
                    
            'bmo_zone_mix_1': {
                'params': {'vehicle': 'BMO', 'zones': '1,3,6'},
                'action': (
                    ('#vehicle-id', 'select[BMO]'),
                    ('#zone-id', 'select[6]'),
                    ('#zone-id', 'select[1]'),
                    ('#zone-id', 'select[3]')
                ),
                'naics': ('all', 15, True),
                'vehicle': ('BMO', 8, True),
                'pool': ('', 17, 17, True),
                'zone': (('1', '3', '6'), 6, True, True),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (3, 'results/csv/?vehicle=BMO&zones=1,3,6'),
                'vendor_table': (3, 'h_naics_results', 'desc')
            },
            'bmo_sb_zone_mix_1': {
                'params': {'vehicle': 'BMO_SB', 'zones': '1,2,4'},
                'action': (
                    ('#vehicle-id', 'select[BMO_SB]'),
                    ('#zone-id', 'select[4]'),
                    ('#zone-id', 'select[2]'),
                    ('#zone-id', 'select[1]')
                ),
                'naics': ('all', 15, True),
                'vehicle': ('BMO_SB', 8, True),
                'pool': ('', 17, 17, True),
                'zone': (('1', '2', '4'), 6, True, True),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (4, 'results/csv/?vehicle=BMO_SB&zones=1,2,4'),
                'vendor_table': (4, 'h_naics_results', 'desc')
            },
            
            'bmo_zone_remove_1': {
                'params': {
                    'test': 'true',
                    'vehicle': 'BMO'
                },
                'action': (
                    ('#vehicle-id', 'select[BMO]'),
                    ('#zone-id', 'select[2]'),
                    ('.select2-selection__choice__remove', 'click')
                ),
                'naics': ('all', 15, True),
                'vehicle': ('BMO', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('', 6, True, True),
                'setaside_filters': (None, 0, False),
                'vendor_result_info': (14, 'results/csv/?vehicle=BMO'),
                'vendor_table': (5, 'h_naics_results', 'desc', ('Prev', '1'), '3')
            },
            'bmo_sb_zone_clear_1': {
                'params': {
                    'test': 'true',
                    'vehicle': 'BMO_SB'
                },
                'action': (
                    ('#vehicle-id', 'select[BMO_SB]'),
                    ('#zone-id', 'select[5]'),
                    ('#zone-id', 'select[1]'),
                    ('#zone-id', 'select[6]'),
                    ('.select2-selection__clear', 'click')
                ),
                'naics': ('all', 15, True),
                'vehicle': ('BMO_SB', 8, True),
                'pool': ('', 17, 17, True),
                'zone': ('', 6, True, True),
                'setaside_filters': (None, 0, True),
                'vendor_result_info': (23, 'results/csv/?vehicle=BMO_SB'),
                'vendor_table': (5, 'h_naics_results', 'desc', ('Prev', '1'), '5')
            },
            
            'setasides_8a': {
                'params': {'setasides': 'A6'},
                'action': ('#eight_a', 'click'),
                'naics': ('all', 78, True),
                'vehicle': ('all', 5, True),
                'pool': ('all', 34, 33, True),
                'zone': ('', 6, False, False),
                'setaside_filters': ('A6', 1, True),
                'vendor_result_info': (29, 'results/csv/?setasides=A6'),
                'vendor_table': (29, 'h_naics_results', 'desc'),
                'i1|xpath://*[@id="pool_vendors"]/tbody/tr[2]/td[6]/img': 'exists',
                'i2|xpath://*[@id="pool_vendors"]/tbody/tr[10]/td[6]/img': 'exists',
                'i3|xpath://*[@id="pool_vendors"]/tbody/tr[20]/td[6]/img': 'exists',
                'i4|xpath://*[@id="pool_vendors"]/tbody/tr[29]/td[6]/img': 'exists'
            },
            'setasides_hubz': {
                'params': {'setasides': 'XX'},
                'action': ('#Hubz', 'click'),
                'naics': ('all', 78, True),
                'vehicle': ('all', 5, True),
                'pool': ('all', 34, 33, True),
                'zone': ('', 6, False, False),
                'setaside_filters': ('XX', 1, True),
                'vendor_result_info': (3, 'results/csv/?setasides=XX'),
                'vendor_table': (3, 'h_naics_results', 'desc'),
                'i1|xpath://*[@id="pool_vendors"]/tbody/tr[2]/td[7]/img': 'exists',
                'i2|xpath://*[@id="pool_vendors"]/tbody/tr[3]/td[7]/img': 'exists'
            },
            'setasides_sdvo': {
                'params': {'setasides': 'QF'},
                'action': ('#disvet', 'click'),
                'naics': ('all', 78, True),
                'vehicle': ('all', 5, True),
                'pool': ('all', 34, 33, True),
                'zone': ('', 6, False, False),
                'setaside_filters': ('QF', 1, True),
                'vendor_result_info': (25, 'results/csv/?setasides=QF'),
                'vendor_table': (25, 'h_naics_results', 'desc'),
                'i1|xpath://*[@id="pool_vendors"]/tbody/tr[2]/td[10]/img': 'exists',
                'i2|xpath://*[@id="pool_vendors"]/tbody/tr[10]/td[10]/img': 'exists',
                'i3|xpath://*[@id="pool_vendors"]/tbody/tr[24]/td[10]/img': 'exists'
            },
            'setasides_wo': {
                'params': {'setasides': 'A2'},
                'action': ('#woman', 'click'),
                'naics': ('all', 78, True),
                'vehicle': ('all', 5, True),
                'pool': ('all', 34, 33, True),
                'zone': ('', 6, False, False),
                'setaside_filters': ('A2', 1, True),
                'vendor_result_info': (20, 'results/csv/?setasides=A2'),
                'vendor_table': (20, 'h_naics_results', 'desc'),
                'i1|xpath://*[@id="pool_vendors"]/tbody/tr[2]/td[8]/img': 'exists',
                'i2|xpath://*[@id="pool_vendors"]/tbody/tr[10]/td[8]/img': 'exists',
                'i3|xpath://*[@id="pool_vendors"]/tbody/tr[20]/td[8]/img': 'exists'
            },
            'setasides_vo': {
                'params': {'setasides': 'A5'},
                'action': ('#vet', 'click'),
                'naics': ('all', 78, True),
                'vehicle': ('all', 5, True),
                'pool': ('all', 34, 33, True),
                'zone': ('', 6, False, False),
                'setaside_filters': ('A5', 1, True),
                'vendor_result_info': (20, 'results/csv/?setasides=A5'),
                'vendor_table': (20, 'h_naics_results', 'desc'),
                'i1|xpath://*[@id="pool_vendors"]/tbody/tr[2]/td[9]/img': 'exists',
                'i2|xpath://*[@id="pool_vendors"]/tbody/tr[10]/td[9]/img': 'exists',
                'i3|xpath://*[@id="pool_vendors"]/tbody/tr[20]/td[9]/img': 'exists'
            },
            'setasides_sdb': {
                'params': {'setasides': '27'},
                'action': ('#smalldis', 'click'),
                'naics': ('all', 78, True),
                'vehicle': ('all', 5, True),
                'pool': ('all', 34, 33, True),
                'zone': ('', 6, False, False),
                'setaside_filters': ('27', 1, True),
                'vendor_result_info': (35, 'results/csv/?setasides=27'),
                'vendor_table': (35, 'h_naics_results', 'desc'),
                'i1|xpath://*[@id="pool_vendors"]/tbody/tr[2]/td[5]/img': 'exists',
                'i2|xpath://*[@id="pool_vendors"]/tbody/tr[10]/td[5]/img': 'exists',
                'i3|xpath://*[@id="pool_vendors"]/tbody/tr[20]/td[5]/img': 'exists',
                'i4|xpath://*[@id="pool_vendors"]/tbody/tr[35]/td[5]/img': 'exists'
            },
            
            'mixed_1': {
                'params': {
                    'naics': '561720', 
                    'vehicle': 'BMO_SB',
                    'pools': 'BMO_SB_5',
                    'zones': '1,5',
                    'setasides': '27,A2'
                },
                'action': (
                    ('#naics-code', 'select[561720]'),
                    ('#vehicle-id', 'select[BMO_SB]'),
                    ('#pool-id', 'select[BMO_SB_5]'),
                    ('#zone-id', 'select[1]'),
                    ('#zone-id', 'select[5]'),
                    ('#woman', 'click'),
                    ('#smalldis', 'click')
                ),
                'naics': ('561720', 2, True),
                'vehicle': ('BMO_SB', 2, True),
                'pool': ('BMO_SB_5', 1, 1, True),
                'zone': (('1', '5'), 6, True, True),
                'setaside_filters': (('27', 'A2'), 2, True),
                'vendor_result_info': (1, 'results/csv/?naics=561720&vehicle=BMO_SB&pools=BMO_SB_5&zones=1,5&setasides=27,A2'),
                'vendor_table': (1, 'h_naics_results', 'desc')
            }
        }
    }