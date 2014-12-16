SPRITES =  {'c1' : '1_corner.gif',
			'c2' : '2_corner.gif',
			'c3' : '3_corner.gif',
			'c4' : '4_corner.gif',
			'hw' : 'H_wall.gif',
			'vw' : 'V_wall.gif',
			'hb' : 'H_barricade.gif', 
			'vb' : 'V_barricade.gif',
			'bu' : 'bush.gif',
			'tr' : 'tree.gif',
			'fl' : 'smaller_flower.gif',
			'pa' : 'path.gif'
			}

UNWALKABLES = ['c1','c2','c3','c4','hw','vw','bu','hb','vb','tr']

LEVELS = [['tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 'tr', 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 'bu', 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 'tr',
		   'bu', 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000,
		   0000, 0000, 'tr', 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000,
		   'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu',
		   0000, 'bu', 0000, 'c1', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'c2', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 'fl', 0000, 0000,
		   0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 'tr', 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 'bu', 0000,
		   0000, 'fl', 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000,
		   'bu', 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 'pa', 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 'bu', 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 'fl', 'c4', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'c3', 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000,
		   'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr',
		   0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 'tr', 0000,
		   0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr',
		   0000, 0000, 'tr', 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 'fl', 0000, 'bu', 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 'tr', 0000, 0000, 'fl', 'tr', 0000, 0000, 'tr', 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 'pa', 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 'pa', 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000,
		   0000, 'fl', 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 'pa', 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 'tr',
		   0000, 0000, 0000, 'fl', 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 'pa', 'pa', 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 'bu', 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 'pa', 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 'pa', 'pa', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vb', 'hb', 'hb', 'hb', 'hb', 'hb', 'hb', 'hb', 'hb', 'hb',
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 'vb', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 'vb', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vb', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   'tr', 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 'tr', 0000, 0000, 0000, 'vb', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 'bu', 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vb', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 'vb', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 'vb', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vb', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 'vb', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   'bu', 0000, 0000, 0000, 'fl', 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'tr', 0000, 'vb', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000]]