# weather_stn_data.py - Used by extract_numbers.py, get_info_from_mshr.py, get_past_observations_cdo.py, get_daily_normals_cdo.py
#    Location of each of the following numbers in the image corresponds to a city (or weather station) in the continental U.S.
#    Location of (lower-left pixel of) first character of number in image when the number is 2 characters and positive, e.g. 12 or 63, not 1, 101, -1, -23
#    Number in image is "weather number", e.g. max temperature prediction.
#    0-based row=y, column=x (origin=lower-left); character is 13 rows x 9 columns pixel array
# Data Science class project - General Assembly - Seattle - SEA-DAT1 (10/27/15 - 1/21/16)
# Developed by Bruce Aker   1/11/16 - 1/21/16
[{'icao_code':'KABE','row':494,'col':739,'stn_id_cdo':'GHCND:USW00014737','state':'PA','weather_station':'ALLENTOWN INTL AP'},
 {'icao_code':'KABQ','row':275,'col':299,'stn_id_cdo':'GHCND:USW00023050','state':'NM','weather_station':'ALBUQUERQUE INTL AP'},
 {'icao_code':'KACV','row':437,'col': 54,'stn_id_cdo':'GHCND:USW00024283','state':'CA','weather_station':'ARCATA EUREKA AP'},
 {'icao_code':'KACY','row':480,'col':762,'stn_id_cdo':'GHCND:USW00093730','state':'NJ','weather_station':'ATLANTIC CITY INTL AP'},
 {'icao_code':'KALB','row':540,'col':739,'stn_id_cdo':'GHCND:USW00014735','state':'NY','weather_station':'ALBANY AP'},
 {'icao_code':'KANJ','row':541,'col':582,'stn_id_cdo':'GHCND:USW00014847','state':'MI','weather_station':'SAULT STE MARIE SANDERSON FLD'},
 {'icao_code':'KATL','row':308,'col':669,'stn_id_cdo':'GHCND:USW00013874','state':'GA','weather_station':'ATLANTA HARTSFIELD INTL AP'},
 {'icao_code':'KBCE','row':335,'col':215,'stn_id_cdo':'GHCND:USW00023159','state':'UT','weather_station':'BRYCE CANYON AP'},
 {'icao_code':'KBGR','row':610,'col':774,'stn_id_cdo':'GHCND:USW00014606','state':'ME','weather_station':'BANGOR INTL AP'},
 {'icao_code':'KBHM','row':294,'col':632,'stn_id_cdo':'GHCND:USW00013876','state':'AL','weather_station':'BIRMINGHAM AP'},
 {'icao_code':'KBIL','row':484,'col':281,'stn_id_cdo':'GHCND:USW00024033','state':'MT','weather_station':'BILLINGS INTL AP'}, #wfo=byz
 {'icao_code':'KBIS','row':502,'col':380,'stn_id_cdo':'GHCND:USW00024011','state':'ND','weather_station':'BISMARCK MUNI AP'},
 {'icao_code':'KBNA','row':343,'col':617,'stn_id_cdo':'GHCND:USW00013897','state':'TN','weather_station':'NASHVILLE INTL AP'},
 {'icao_code':'KBNO','row':464,'col':138,'stn_id_cdo':'GHCND:USW00094185','state':'OR','weather_station':'BURNS MUNI AP'},
 {'icao_code':'KBOI','row':456,'col':174,'stn_id_cdo':'GHCND:USW00024131','state':'ID','weather_station':'BOISE AIR TERMINAL'}, #wfo=boi
 {'icao_code':'KBOS','row':555,'col':775,'stn_id_cdo':'GHCND:USW00014739','state':'MA','weather_station':'BOSTON LOGAN INTL AP'},
 {'icao_code':'KBPI','row':425,'col':255,'stn_id_cdo':'GHCND:USW00024164','state':'WY','weather_station':'BIG PINEY MARBLETON AP'},
 {'icao_code':'KBTV','row':573,'col':729,'stn_id_cdo':'GHCND:USW00014742','state':'VT','weather_station':'BURLINGTON INTL AP'},
 {'icao_code':'KBUF','row':510,'col':677,'stn_id_cdo':'GHCND:USW00014733','state':'NY','weather_station':'BUFFALO NIAGARA INTL AP'},
 {'icao_code':'KCAE','row':335,'col':719,'stn_id_cdo':'GHCND:USW00013883','state':'SC','weather_station':'COLUMBIA METRO AP'},
 {'icao_code':'KCLE','row':466,'col':649,'stn_id_cdo':'GHCND:USW00014820','state':'OH','weather_station':'CLEVELAND HOPKINS INTL AP'},
 {'icao_code':'KCMH','row':435,'col':646,'stn_id_cdo':'GHCND:USW00014821','state':'OH','weather_station':'COLUMBUS PORT COLUMBUS INTL AP'},
 {'icao_code':'KCOS','row':350,'col':330,'stn_id_cdo':'GHCND:USW00093037','state':'CO','weather_station':'COLORADO SPRINGS MUNI AP'}, #wfo=pub
 {'icao_code':'KCOU','row':356,'col':517,'stn_id_cdo':'GHCND:USW00003945','state':'MO','weather_station':'COLUMBIA RGNL AP'},
 {'icao_code':'KCPR','row':429,'col':306,'stn_id_cdo':'GHCND:USW00024089','state':'WY','weather_station':'Casper, Natrona County International Airport'},
 {'icao_code':'KCRE','row':350,'col':756,'stn_id_cdo':'GHCND:USW00093718','state':'SC','weather_station':'N MYRTLE BCH AP'},
 {'icao_code':'KCRP','row':132,'col':470,'stn_id_cdo':'GHCND:USW00012924','state':'TX','weather_station':'CORPUS CHRISTI INTL AP'},
 {'icao_code':'KCRW','row':413,'col':676,'stn_id_cdo':'GHCND:USW00013866','state':'WV','weather_station':'CHARLESTON YEAGER AP'},
 {'icao_code':'KDCA','row':452,'col':735,'stn_id_cdo':'GHCND:USW00013743','state':'VA','weather_station':'WASHINGTON REAGAN AP'},
 {'icao_code':'KDFW','row':240,'col':463,'stn_id_cdo':'GHCND:USW00003927','state':'TX','weather_station':'Dallas-Fort Worth WSCMO AP'}, 
 {'icao_code':'KDSM','row':418,'col':487,'stn_id_cdo':'GHCND:USW00014933','state':'IA','weather_station':'DES MOINES INTL AP'},
 {'icao_code':'KEYW','row':146,'col':788,'stn_id_cdo':'GHCND:USW00012836','state':'FL','weather_station':'KEY WEST INTL AP'},
 {'icao_code':'KFAR','row':510,'col':429,'stn_id_cdo':'GHCND:USW00014914','state':'ND','weather_station':'Fargo, Hector International Airport'}, #WFO=FGF, Grand Forks, ND
 {'icao_code':'KFAT','row':339,'col': 94,'stn_id_cdo':'GHCND:USW00093193','state':'CA','weather_station':'Fresno Air Terminal'}, #wfo=hnx
 {'icao_code':'KFLG','row':283,'col':216,'stn_id_cdo':'GHCND:USW00003103','state':'AZ','weather_station':'FLAGSTAFF PULLIAM AP'},
 {'icao_code':'KFMY','row':187,'col':768,'stn_id_cdo':'GHCND:USW00012835','state':'FL','weather_station':'FT MYERS PAGE FLD AP'},
 {'icao_code':'KFSD','row':449,'col':438,'stn_id_cdo':'GHCND:USW00014944','state':'SD','weather_station':'SIOUX FALLS FOSS FLD'},
 {'icao_code':'KFST','row':190,'col':364,'stn_id_cdo':'GHCND:USW00023091','state':'TX','weather_station':'FT STOCKTON PECOS AP'},
 {'icao_code':'KGEG','row':533,'col':173,'stn_id_cdo':'GHCND:USW00024157','state':'WA','weather_station':'SPOKANE INTL AP'}, #wfo=otx
 {'icao_code':'KGGW','row':527,'col':306,'stn_id_cdo':'GHCND:USW00094008','state':'MT','weather_station':'GLASGOW INTL AP'},
 {'icao_code':'KGRB','row':491,'col':548,'stn_id_cdo':'GHCND:USW00014898','state':'WI','weather_station':'GREEN BAY A S INTL AP'},
 {'icao_code':'KGRR','row':473,'col':591,'stn_id_cdo':'GHCND:USW00094860','state':'MI','weather_station':'GRAND RAPIDS INTL AP'},
 {'icao_code':'KGSO','row':383,'col':718,'stn_id_cdo':'GHCND:USW00013723','state':'NC','weather_station':'PIEDMONT TRIAD INTL AP'},
 {'icao_code':'KHLN','row':502,'col':238,'stn_id_cdo':'GHCND:USW00024144','state':'MT','weather_station':'HELENA RGNL AP'}, #wfo=tfx
 {'icao_code':'KIAH','row':185,'col':502,'stn_id_cdo':'GHCND:USW00012960','state':'TX','weather_station':'HOUSTON INTERCONT AP'},
 {'icao_code':'KICT','row':334,'col':444,'stn_id_cdo':'GHCND:USW00003928','state':'KS','weather_station':'WICHITA DWIGHT D EISENHOWER NA'},
 {'icao_code':'KINL','row':547,'col':465,'stn_id_cdo':'GHCND:USW00014918','state':'MN','weather_station':'International Falls Airport'},
 {'icao_code':'KJAN','row':253,'col':584,'stn_id_cdo':'GHCND:USW00003940','state':'MS','weather_station':'JACKSON INTL AP'},
 {'icao_code':'KJAX','row':266,'col':738,'stn_id_cdo':'GHCND:USW00013889','state':'FL','weather_station':'JACKSONVILLE INTL AP'},
 {'icao_code':'KLAS','row':310,'col':163,'stn_id_cdo':'GHCND:USW00023169','state':'NV','weather_station':'LAS VEGAS MCCARRAN AP'},
 {'icao_code':'KLAX','row':278,'col':101,'stn_id_cdo':'GHCND:USW00023174','state':'CA','weather_station':'Los Angeles International Airport'}, #wfo=lox
 {'icao_code':'KLBB','row':248,'col':380,'stn_id_cdo':'GHCND:USW00023042','state':'TX','weather_station':'LUBBOCK INTL AP'},
 {'icao_code':'KLBF','row':397,'col':388,'stn_id_cdo':'GHCND:USW00024023','state':'NE','weather_station':'N PLATTE RGNL AP'},
 {'icao_code':'KLEX','row':390,'col':636,'stn_id_cdo':'GHCND:USW00093820','state':'KY','weather_station':'LEXINGTON BLUEGRASS AP'},
 {'icao_code':'KLIT','row':292,'col':537,'stn_id_cdo':'GHCND:USW00013963','state':'AR','weather_station':'LITTLE ROCK AP ADAMS FLD'},
 {'icao_code':'KMCI','row':373,'col':480,'stn_id_cdo':'GHCND:USW00003947','state':'MO','weather_station':'KANSAS CITY INTL AP'},
 {'icao_code':'KMCO','row':228,'col':762,'stn_id_cdo':'GHCND:USW00012815','state':'FL','weather_station':'ORLANDO INTL AP'},
 {'icao_code':'KMEM','row':307,'col':571,'stn_id_cdo':'GHCND:USW00013893','state':'TN','weather_station':'MEMPHIS INTL AP'},
 {'icao_code':'KMIA','row':184,'col':804,'stn_id_cdo':'GHCND:USW00012839','state':'FL','weather_station':'MIAMI INTL AP'},
 {'icao_code':'KMIE','row':426,'col':610,'stn_id_cdo':'GHCND:USW00094895','state':'IN','weather_station':'MUNCIE DELAWARE CO AP'},
 {'icao_code':'KMLI','row':427,'col':531,'stn_id_cdo':'GHCND:USW00014923','state':'IL','weather_station':'MOLINE QUAD CITY INTL AP'},
 {'icao_code':'KMOB','row':229,'col':625,'stn_id_cdo':'GHCND:USW00013894','state':'AL','weather_station':'MOBILE RGNL AP'},
 {'icao_code':'KMSY','row':205,'col':594,'stn_id_cdo':'GHCND:USW00012916','state':'LA','weather_station':'NEW ORLEANS INTL AP'},
 {'icao_code':'KOKC','row':290,'col':447,'stn_id_cdo':'GHCND:USW00013967','state':'OK','weather_station':'OKLAHOMA CITY WILL ROGERS AP'},
 {'icao_code':'KORF','row':424,'col':765,'stn_id_cdo':'GHCND:USW00013737','state':'VA','weather_station':'NORFOLK INTL AP'},
 {'icao_code':'KP60','row':462,'col':254,'stn_id_cdo':'GHCND:USW00094173','state':'WY','weather_station':'Yellowstone Lake'},
 {'icao_code':'KPDX','row':513,'col':101,'stn_id_cdo':'GHCND:USW00024229','state':'OR','weather_station':'Portland International Airport'},
 {'icao_code':'KPHX','row':249,'col':206,'stn_id_cdo':'GHCND:USW00023183','state':'AZ','weather_station':'Phoenix Sky Harbor International Airport'}, #wfo=psr
 {'icao_code':'KPOU','row':521,'col':749,'stn_id_cdo':'GHCND:USW00014757','state':'NY','weather_station':'POUGHKEEPSIE DUTCHESS CO AP'},
 {'icao_code':'KPWM','row':581,'col':770,'stn_id_cdo':'GHCND:USW00014764','state':'ME','weather_station':'PORTLAND INTL JETPORT'},
 {'icao_code':'KRAP','row':450,'col':352,'stn_id_cdo':'GHCND:USW00024090','state':'SD','weather_station':'RAPID CITY REGIONAL AP'},
 {'icao_code':'KRDD','row':420,'col': 76,'stn_id_cdo':'GHCND:USW00024257','state':'CA','weather_station':'REDDING MUNI AP'}, #wfo=sto
 {'icao_code':'KRNO','row':391,'col':107,'stn_id_cdo':'GHCND:USW00023185','state':'NV','weather_station':'RENO TAHOE INTL AP'}, #wfo=rev
 {'icao_code':'KROA','row':405,'col':708,'stn_id_cdo':'GHCND:USW00013741','state':'VA','weather_station':'ROANOKE RGNL AP'},
 {'icao_code':'KRST','row':466,'col':494,'stn_id_cdo':'GHCND:USW00014925','state':'MN','weather_station':'ROCHESTER INTL AP'},
 {'icao_code':'KSAN','row':250,'col':116,'stn_id_cdo':'GHCND:USW00023188','state':'CA','weather_station':'SAN DIEGO LINDBERGH FLD'}, #wfo=sgx
 {'icao_code':'KSAT','row':167,'col':447,'stn_id_cdo':'GHCND:USW00012921','state':'TX','weather_station':'SAN ANTONIO INTL AP'},
 {'icao_code':'KSAV','row':301,'col':732,'stn_id_cdo':'GHCND:USW00003822','state':'GA','weather_station':'SAVANNAH INTL AP'},
 {'icao_code':'KSEA','row':545,'col':115,'stn_id_cdo':'GHCND:USW00024233','state':'WA','weather_station':'Seattle Tacoma Airport'}, #WFO=SEW, Sandpoint, Seattle, WA
 {'icao_code':'KSHV','row':241,'col':520,'stn_id_cdo':'GHCND:USW00013957','state':'LA','weather_station':'SHREVEPORT RGNL AP'},
 {'icao_code':'KSLC','row':394,'col':225,'stn_id_cdo':'GHCND:USW00024127','state':'UT','weather_station':'SALT LAKE CITY INTL AP'}, #wfo=slc
 {'icao_code':'KSPI','row':400,'col':551,'stn_id_cdo':'GHCND:USW00093822','state':'IL','weather_station':'SPRINGFIELD CAPITAL AP'},
 {'icao_code':'KTAD','row':319,'col':337,'stn_id_cdo':'GHCND:USW00023070','state':'CO','weather_station':'TRINIDAD PERRY STOKES AP'},
 {'icao_code':'KTPA','row':210,'col':745,'stn_id_cdo':'GHCND:USW00012842','state':'FL','weather_station':'TAMPA INTL AP'},
 {'icao_code':'KTUS','row':220,'col':222,'stn_id_cdo':'GHCND:USW00023160','state':'AZ','weather_station':'TUCSON INTL AP'},
 {'icao_code':'KUIL','row':562,'col': 92,'stn_id_cdo':'GHCND:USW00094240','state':'WA','weather_station':'Quillayute State Airport'}, #WFO=SEW
 {'icao_code':'KWMC','row':411,'col':142,'stn_id_cdo':'GHCND:USW00024128','state':'NV','weather_station':'WINNEMUCCA MUNI AP'}, #wfo=lkn
 {'icao_code':'KYKM','row':523,'col':132,'stn_id_cdo':'GHCND:USW00024243','state':'WA','weather_station':'Yakima Air Terminal'}] #WFO=PDT, Pendleton, OR
# {'icao_code':'K','row':000,'col':000,'stn_id_cdo':'GHCND:USW000','state':'','weather_station':''},
