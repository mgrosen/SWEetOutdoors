import requests
from models import db, Event

# use ramboho virtual enviornment which is in top level directory
# current page = offset
# per_page = rows per page


per_page = 1200
#set current page to 1
current_page = 1

url = "http://api.amp.active.com/v2/search?per_page=1&current_page=0&start_date=2016-08-01..2017-12-31&category=trail%20heads&api_key=kww96xbnrt8a3dj6ndfkdyzx"
response = requests.get(url)

data = response.json()

zipset = set(['55616', '55614', '55612', '61517', '81403', '26378', '02109', '60914', '66777', '92651', '24715', '32507', '92305', '82190', '19711', '50644', '32656', '32303', '32653', '32309', '55613', '74010', '96150', '13607', '10960', '56123', '98648', '51640', '98310', '98642', '61943', '98640', '52003', '19971', '25443', '22485', '81330', '02351', '43056', '96796', '96790', '11730', '63020', '63021', '49768', '49765', '98520', '97444', '63845', '93923', '93920', '95555', '36442', '98261', '53026', '45663', '05733', '33476', '44241', '54880', '04350', '45669', '01020', '17729', '15860', '83876', '62466', '63448', '24084', '16922', '98862', '55760', '41230', '62863', '84050', '15834', '15861', '71822', '49947', '49417', '53510', '53517', '58214', '68770', '49781', '58763', '66779', '45068', '02645', '13057', '33852', '59929', '71753', '59922', '95018', '14716', '95010', '62080', '59101', '62241', '92549', '87105', '40744', '83611', '01201', '44429', '83616', '54873', '39355', '24522', '95303', '27617', '67749', '94941', '61348', '61341', '73655', '12831', '87571', '87575', '55111', '7457', '59324', '97846', '97848', '66502', '93430', '55332', '93434', '04981', '50675', '50672', '74955', '66763', '55026', '32310', '01590', '32643', '32641', '16668', '16669', '13618', '97141', '10976', '46120', '06037', '32226', '19701', '98675', '57260', '32008', '65466', '97321', '11754', '98585', '98584', '97326', '88034', '97329', '88030', '75844', '43046', '43512', '49436', '49779', '52101', '49770', '97450', '94015', '94010', '75661', '95542', '94019', '47250', '84116', '46304', '97210', '97630', '12134', '52038', '45651', '98502', '04348', '85602', '83860', '04605', '36542', '37010', '33043', '14891', '33040', '36830', '42156', '54981', '62656', '78382', '59620', '49950', '62897', '49953', '38635', '14092', '34949', '13066', '68760', '98926', '98925', '67025', '13069', '59825', '06335', '15677', '40311', '04769', '27546', '28512', '26812', '38748', '79015', '53588', '44432', '37762', '88029', '83604', '83605', '02835', '23040', '95374', '77963', '26705', '47516', '72135', '66970', '72396', '97850', '66086', '87743', '87740', '15050', '97859', '25951', '06488', '74728', '06482', '06484', '72401', '97523', '04974', '04970', '26554', '50065', '61350', '55037', '51047', '55033', '55921', '16657', '16655', '16652', '06002', '35452', '13669', '10989', '97137', '43456', '10986', '10980', '99653', '24589', '24954', '98110', '74451', '65692', '06443', '83638', '42032', '11743', '98595', '42038', '11580', '43521', '43035', '97040', '79834', '94005', '25550', '95571', '95570', '56073', '43140', '43143', '98282', '98283', '05201', '45317', '45865', '98843', '98844', '98846', '27976', '17740', '83851', '17745', '16901', '33050', '84078', '14886', '97467', '97466', '97465', '03820', '54401', '59639', '15849', '15840', '70358', '14081', '49431', '99156', '99403', '99402', '99401', '62311', '53574', '24171', '18947', '13078', '33455', '59834', '97913', '97102', '76372', '48059', '45889', '41144', '01267', '68801', '89705', '89704', '67301', '02806', '18456', '97914', '95366', '18360', '59016', '50273', '39576', '58545', '97131', '14464', '78644', '67764', '94965', '79734', '27705', '12580', '03222', '98382', '97865', '15021', '98380', '59301', '61031', '74735', '15337', '48848', '92332', '93206', '27016', '61322', '74937', '16648', '65202', '65203', '32321', '98611', '97123', '13679', '98614', '43338', '43440', '56686', '02066', '93117', '65336', '06043', '25411', '24946', '57790', '57247', '74447', '74441', '32060', '16226', '43534', '23927', '96056', '98051', '98547', '98546', '98541', '46216', '98548', '16354', '17518', '65536', '63670', '90277', '90272', '26056', '64484', '70586', '49887', '52761', '49337', '05764', '41164', '52565', '02780', '22827', '16915', '45387', '97471', '53965', '54629', '58220', '14850', '84624', '54212', '99143', '49424', '62305', '10516', '14072', '18951', '44231', '18426', '84718', '59808', '84713', '84712', '84536', '84531', '84532', '76692', '58318', '86403', '41557', '86406', '83623', '99709', '62231', '62234', '15857', '72084', '34432', '68813', '33955', '50265', '25882', '97907', '79720', '58554', '32038', '40330', '83716', '32561', '77340', '40119', '87722', '89008', '03251', '89004', '03255', '12845', '28714', '95223', '25979', '28086', '35124', '73842', '66554', '02818', '77833', '66049', '06795', '06794', '06791', '51023', '55012', '89131', '50049', '28668', '50511', '74056', '19335', '61244', '96778', '13640', '55781', '55782', '98604', '11702', '56470', '51331', '19020', '16217', '16740', '69339', '32720', '43944', '69337', '19939', '97420', '43015', '06371', '43830', '56273', '56278', '98550', '99323', '52175', '19803', '19802', '19807', '19809', '19808', '90265', '26260', '56096', '27954', '62939', '62938', '27959', '52577', '53081', '49636', '48328', '46996', '97487', '80025', '63080', '98952', '37355', '33592', '89042', '84525', '15627', '15623', '33547', '12901', '62205', '04426', '58495', '49854', '01247', '78028', '37738', '01085', '83541', '33946', '54024', '97121', '54022', '45502', '99603', '79756', '39553', '24363', '34997', '33898', '04548', '28694', '66949', '87732', '97838', '15557', '43331', '66549', '02865', '72855', '06810', '06812', '66543', '35111', '72455', '72450', '72458', '89452', '34606', '04949', '19106', '87935', '35801', '50520', '50036', '91709', '13650', '73038', '02043', '23832', '22520', '98635', '97103', '98631', '65047', '19034', '56649', '56319', '02919', '74464', '32446', '11793', '11792', '37029', '61270', '93001', '81146', '98563', '60051', '98569', '98092', '71241', '32136', '32137', '36343', '63656', '57220', '57227', '56085', '27928', '38804', '52540', '38555', '38556', '52544', '95437', '17406', '95432', '94129', '84028', '60450', '84021', '85008', '97498', '03870', '80526', '97624', '62324', '62326', '48467', '53549', '33711', '85737', '54235', '63501', '49449', '99166', '49441', '99161', '49445', '37341', '83429', '24104', '06756', '03905', '84738', '45612', '33408', '84733', '84737', '03908', '54521', '43438', '84511', '54651', '54301', '12910', '40046', '38703', '48001', '27587', '49841', '17324', '78584', '50008', '84601', '83555', '44108', '53533', '76033', '14303', '54016', '14305', '52042', '49128', '99613', '17963', '24354', '03275', '12866', '67010', '79562', '03278', '16720', '87701', '14541', '50441', '34450', '32459', '13796', '78837', '32456', '32455', '06777', '06770', '55072', '87419', '51558', '51555', '66441', '38230', '50020', '44102', '73559', '61469', '06518', '47112', '47111', '61111', '44065', '47118', '04848', '98620', '98624', '04843', '50156', '61001', '44060', '22191', '32703', '98392', '75418', '97883', '65366', '06357', '06424', '38948', '17814', '97394', '06351', '06422', '12071', '88240', '77473', '19317', '13685', '33036', '52205', '66064', '65560', '98577', '98571', '95531', '97626', '74525', '16301', '45426', '17365', '94020', '57239', '62919', '17776', '99576', '27938', '46554', '62914', '16947', '95409', '05089', '99371', '49616', '52552', '16948', '80517', '90293', '13309', '12095', '43616', '52157', '53934', '05156', '42211', '62354', '85743', '45772', '99111', '99115', '84726', '84721', '45601', '33149', '36919', '04441', '71429', '18214', '99026', '99021', '99752', '99022', '27842', '71950', '71956', '95662', '83672', '84340', '71226', '71220', '72058', '78572', '71040', '67637', '48706', '39530', '04069', '76043', '94920', '37663', '03260', '40475', '87718', '97823', '66219', '68845', '34448', '47906', '72834', '02840', '66075', '66070', '34668', '89315', '55047', '50548', '51544', '13614', '50833', '72946', '38222', '97026', '04562', '34714', '48442', '47129', '12526', '39063', '12520', '04854', '59725', '76801', '65020', '61074', '73946', '55987', '56628', '98368', '98365', '98366', '32712', '98362', '06340', '97385', '42519', '06438', '97013', '97010', '89301', '97014', '97019', '23966', '92004', '32625', '32626', '56241', '96013', '93535', '03086', '96017', '93536', '95528', '96720', '56751', '17224', '96729', '96728', '75686', '17222', '10512', '16313', '64683', '61858', '06239', '42420', '27306', '96120', '93442', '43113', '49423', '63628', '57201', '97701', '97525', '69101', '49601', '64429', '70094', '99566', '45162', '61920', '36726', '74331', '53147', '62341', '45701', '52635', '37416', '49265', '99103', '52639', '01748', '78838', '85119', '40069', '41040', '04107', '33605', '13162', '59759', '46017', '63361', '59752', '59754', '49868', '37090', '78368', '37096', '13118', '71232', '84401', '47460', '48730', '28448', '04074', '33924', '28444', '04072', '94938', '94937', '56342', '33598', '51103', '79786', '89043', '89040', '26651', '59405', '50313', '85936', '03458', '50531', '24244', '77879', '95060', '38109', '03581', '38041', '40241', '29061', '03588', '47265', '34470', '47042', '49670', '97458', '50482', '27043', '06759', '04915', '06757', '39189', '06754', '50557', '51573', '55053', '35010', '32541', '61443', '01983', '86052', '72554', '19063', '19067', '87505', '87501', '61061', '24460', '38922', '32763', '32096', '98370', '38852', '89310', '89311', '88220', '97023', '92036', '16145', '54732', '63623', '98512', '17237', '60081', '96737', '96730', '46714', '06248', '88130', '01566', '65344', '56345', '52314', '26222', '97735', '97734', '64437', '95466', '45177', '70085', '38581', '63755', '98198', '03842', '53913', '03848', '74340', '74343', '74346', '35652', '85344', '99826', '92060', '99133', '48653', '53597', '45714', '52623', '49707', '49701', '84740', '33160', '14456', '80403', '98292', '54646', '45003', '33952', '04462', '18235', '99006', '63379', '04660', '49814', '04261', '37066', '62626', '28450', '48725', '05846', '49920', '47859', '67054', '83211', '03287', '03280', '03281', '17844', '17847', '17841', '14779', '03592', '28584', '88416', '88415', '67871', '67878', '89415', '92154', '61610', '50569', '44843', '44842', '25813', '25812', '47631', '06423', '13693', '55731', '86028', '34731', '12502', '51360', '32951', '61727', '61054', '98349', '61546', '74425', '74426', '61542', '06418', '06419', '96143', '13746', '43755', '97031', '86336', '50619', '16882', '32174', '32177', '16833', '63967', '96744', '96746', '56289', '57730', '55959', '56283', '42408', '43135', '43138', '96103', '56601', '32086', '32080', '10913', '56359', '17331', '24927', '99344', '99345', '49660', '98230', '57004', '98239', '97502', '54661', '60410', '16424', '36093', '01612', '42717', '36258', '74350', '36701', '42718', '11735', '97342', '46701', '97341', '60099', '98528', '99123', '48625', '48624', '99128', '84083', '14012', '17063', '49718', '49715', '49712', '62563', '79847', '01760', '62960', '62966', '54618', '05474', '45036', '71929', '05478', '96718', '39648', '98837', '95613', '84319', '04274', '37076', '44141', '44632', '53589', '18644', '33931', '83332', '54729', '38053', '15765', '04015', '40823', '49930', '87045', '40004', '67042', '78636', '78633', '19044', '33809', '15501', '72802', '95043', '62037', '95045', '47446', '47448', '06880', '88426', '34108', '73772', '15437', '67864', '89403', '59066', '67464', '50801', '28337', '78946', '78945', '22551', '32564', '72774', '87529', '51358', '12517', '51351', '61048', '66026', '17241', '32413', '50115', '38901', '88203', '43720', '43724', '56566', '86326', '26337', '50606', '63601', '32181', '32346', '12188', '12186', '32348', '97750', '06067', '97754', '26201', '06062', '97759', '90401', '88119', '06069', '06068', '98351', '52333', '98358', '43920', '38873', '98229', '49125', '98221', '98222', '74366', '74365', '56381', '74361', '42259', '98532', '49012', '97376', '85546', '20144', '85544', '17074', '49721', '49720', '49725', '94060', '13646', '84764', '84766', '80428', '02809', '03741', '62958', '53801', '70538', '37769', '53806', '14174', '27889', '05468', '71667', '71913', '70447', '94037', '45806', '49349', '98826', '69165', '02779', '45732', '37043', '33037', '33920', '33921', '41653', '33928', '40701', '99664', '48740', '72142', '76667', '49908', '87036', '44041', '18255', '83012', '78629', '39401', '71486', '62040', '85621', '34223', '34241', '47438', '06896', '34114', '88435', '51501', '59070', '59071', '19706', '55718', '06095', '78957', '72742', '72740', '47362', '12569', '50125', '32408', '35976', '04357', '06385', '06382', '73439', '32059', '74756', '06473', '56572', '65283', '02748', '32578', '56713', '19520', '98033', '74578', '32358', '06277', '06076', '06070', '98320', '98325', '96161', '93402', '43420', '56007', '56001', '95450', '98250', '95452', '49643', '95456', '34229', '03894', '96766', '97369', '97365', '97366', '97361', '49735', '97415', '05676', '54452', '70611', '49738', '62549', '97419', '64062', '17006', '38585', '95589', '16841', '38464', '48823', '54850', '04654', '41008', '59868', '04652', '71901', '59860', '59711', '05253', '98813', '13156', '75020', '98816', '98819', '83821', '71958', '10598', '36502', '04032', '95459', '18661', '71953', '38079', '14612', '83226', '87025', '98251', '70471', '95451', '99328', '78611', '98252', '59911', '59910', '76430', '47552', '95023', '17870', '18064', '94515', '28001', '83316', '67669', '35180', '34698', '66538', '51537', '67801', '14437', '91321', '67481', '23883', '74966', '74960', '72753', '50135', '35967', '38326', '25918', '73401', '55362', '06441', '16505', '16051', '65635', '56144', '26351', '26354', '59937', '59936', '32693', '56547', '43701', '39120', '19426', '50627', '93271', '00830', '98028', '15222', '98027', '98022', '98023', '64651', '32328', '54169', '55964', '32320', '55960', '32324', '32327', '13625', '13624', '18328', '98331', '98335', '17760', '98249', '52069', '52065', '52060', '98245', '32034', '03886', '19956', '17764', '75706', '19958', '13367', '88007', '81089', '97411', '64098', '63956', '11704', '93308', '05661', '57452', '49749', '41256', '63005', '32428', '75638', '17015', '36467', '45133', '05060', '97220', '45822', '04628', '44266', '59870', '74423', '62448', '62441', '13142', '13148', '83810', '98801', '98802', '95460', '19607', '18616', '58271', '48162', '04285', '99683', '83250', '38666', '70462', '33304', '13035', '13036', '23942', '37807', '97880', '59452', '76429', '97885', '97884', '59901', '78606', '44319', '78602', '95033', '95037', '33872', '54153', '95039', '41745', '01226', '76049', '71023', '67654', '76557', '72619', '97868', '57013', '06877', '47989', '66523', '66520', '97135', '03576', '14427', '95329', '95324', '97138', '77554', '61361', '43452', '87551', '23188', '95926', '28166', '50435', '35776', '50436', '73749', '38333', '06457', '55604', '55603', '81415', '72432', '23451', '23456', '43718', '95630', '39117', '50651', '71403', '22079', '55910', '75551', '32336', '01821', '96145', '06058', '96142', '97760', '93428', '65625', '56156', '56157', '56150', '98304', '10956', '98812', '99301', '19943', '60103', '18801', '02366', '42048', '56734', '98950', '97304', '42044', '62521', '97439', '97436', '17028', '93933', '01721', '46703', '16866', '42629', '45690', '98277', '97541', '98275', '57042', '98273', '45106', '98279', '98592', '04631', '58645', '18466', '11954', '11957', '83801', '33001', '18414', '37034', '68410', '49686', '01030', '01035', '84049', '62854', '84044', '59602', '44410', '87002', '05343', '62675', '98907', '67005', '71651', '71653', '37814', '40376', '33513', '71722', '41759', '42339', '84528', '44090', '95006', '62277', '28578', '40977', '12410', '34212', '66514', '99347', '28684', '15470', '91302', '59025', '72112', '72110', '25831', '66605', '73647', '54210', '59337', '59330', '73737', '38340'])
zipregionset = set(['010', '012', '015', '016', '017', '018', '019', '344', '346', '347', '341', '342', '810', '811', '813', '814', '349', '737', '719', '718', '717', '716', '714', '712', '710', '423', '913', '195', '290', '591', '590', '593', '199', '198', '597', '596', '599', '598', '197', '196', '191', '190', '193', '270', '273', '275', '276', '277', '278', '279', '525', '526', '527', '520', '521', '522', '523', '448', '443', '442', '441', '440', '446', '444', '109', '105', '902', '904', '640', '644', '438', '439', '436', '437', '434', '435', '433', '430', '431', '339', '338', '335', '334', '337', '336', '331', '330', '333', '058', '054', '559', '056', '057', '050', '051', '052', '053', '855', '856', '857', '850', '851', '853', '859', '740', '743', '744', '745', '747', '749', '557', '556', '551', '550', '553', '238', '239', '234', '230', '231', '614', '146', '147', '144', '619', '143', '140', '141', '612', '613', '610', '611', '616', '617', '148', '615', '154', '949', '945', '940', '941', '688', '684', '687', '458', '133', '131', '130', '498', '499', '494', '496', '497', '490', '491', '492', '493', '407', '939', '404', '403', '402', '401', '400', '933', '932', '931', '930', '935', '934', '628', '027', '026', '021', '020', '023', '029', '028', '378', '370', '373', '821', '374', '377', '376', '704', '705', '706', '700', '618', '703', '393', '391', '145', '396', '395', '394', '797', '795', '790', '798', '170', '586', '587', '584', '585', '582', '583', '245', '244', '247', '241', '240', '243', '242', '249', '511', '510', '513', '515', '516', '623', '622', '620', '626', '625', '624', '450', '451', '629', '453', '454', '455', '456', '457', '179', '178', '177', '175', '174', '173', '172', '594', '977', '976', '975', '974', '973', '972', '971', '970', '180', '979', '978', '656', '183', '654', '655', '652', '653', '650', '194', '186', '188', '189', '060', '063', '062', '065', '184', '067', '068', '860', '863', '864', '882', '881', '880', '884', '064', '322', '323', '320', '321', '326', '327', '324', '325', '329', '201', '774', '563', '773', '779', '778', '359', '804', '669', '667', '666', '665', '664', '662', '660', '693', '691', '542', '543', '540', '541', '546', '547', '544', '545', '548', '549', '995', '994', '997', '996', '991', '990', '993', '998', '120', '121', '124', '125', '128', '129', '415', '416', '417', '410', '411', '412', '920', '137', '923', '925', '926', '136', '038', '039', '921', '032', '030', '037', '034', '035', '832', '833', '830', '836', '837', '834', '835', '838', '725', '368', '369', '367', '364', '365', '362', '363', '360', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '785', '786', '780', '783', '788', '789', '150', '572', '570', '577', '574', '182', '258', '259', '601', '254', '255', '730', '735', '734', '508', '736', '506', '738', '504', '505', '502', '503', '500', '501', '630', '633', '634', '635', '636', '637', '638', '639', '467', '461', '460', '463', '462', '168', '169', '164', '165', '166', '167', '160', '161', '162', '163', '967', '960', '961', '409', '408', '879', '877', '874', '875', '870', '871', '890', '891', '893', '894', '897', '646', '008', '357', '356', '354', '351', '350', '800', '805', '358', '768', '763', '760', '766', '764', '765', '281', '280', '283', '285', '284', '287', '286', '678', '674', '676', '677', '670', '673', '263', '262', '260', '267', '266', '265', '268', '535', '531', '530', '539', '538', '775', '988', '989', '982', '983', '980', '981', '986', '985', '115', '117', '119', '421', '420', '917', '422', '425', '424', '427', '426', '049', '048', '047', '046', '045', '044', '043', '042', '041', '040', '847', '846', '845', '844', '843', '841', '840', '750', '757', '756', '755', '754', '560', '561', '562', '758', '564', '565', '566', '567', '739', '228', '225', '224', '221', '220', '726', '727', '724', '390', '723', '720', '721', '728', '729', '604', '153', '152', '155', '600', '157', '156', '158', '609', '469', '959', '950', '953', '952', '955', '954', '956', '465', '488', '487', '486', '484', '483', '481', '480', '472', '473', '470', '471', '476', '474', '475', '478', '479'])
foundset = set()

numResponses = 0
numResponses = int(data["total_results"])
print(numResponses)
numPages = numResponses // per_page + 1
print(numPages)
# categories = set()
# topics = set()

# print(results)
count = 0
summ = 0
while current_page < numPages:
	url = "http://api.amp.active.com/v2/search?per_page=" + str(per_page) + "&current_page="+str(current_page)+"&start_date=2016-08-01..2017-12-31&category=trail%20heads&api_key=kww96xbnrt8a3dj6ndfkdyzx"
	response = requests.get(url)
	# print(url)

	data = response.json()

	# numResponses = data["total_results"]
	# numPages = numResponses // per_page + 1
	# leftover = numResponses % per_page

	results = data["results"]		#dictionary
	for event in results:
		# print(event)
		count += 1

		invalidEvent = False
		state = ""
		zipcode = ""
		try:
			longitude = event["place"]["geoPoint"]["lon"]
			latitude = event["place"]["geoPoint"]["lat"]
			# location_json = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+latitude+","+longitude+"&key=AIzaSyD6F3rB8GtFapIpn9YG-GmqW_aGisnY5s8").json()
			# for comp in location_json["results"][0]["address_components"]:
			# 	if(comp["types"][0] == "administrative_area_level_1"):
			# 		state = comp["long_name"]
			# 	elif(comp["types"][0] == "postal_code"):
			# 		zipcode = comp["long_name"]
			orgName = event["organization"]["organizationName"]
			zipcode = event["organization"]["addressPostalCd"]

			if orgName == "" or zipcode == "":
				invalidEvent = True
		except KeyError:
			invalidEvent = True
			# print("KeyError: {0}".format(err))
			# print("nothing works")

		if not invalidEvent:
			# Topics
			first = True
			topics = "" 
			for topic in event["assetTopics"]:
				if first:
					topics += topic["topic"]["topicName"]
					first = False
				else:
					topics += ", "+topic["topic"]["topicName"]
			# print(topics)

			endDate = event["activityEndDate"]
			startDate = event["activityStartDate"]
			picUrl = event["logoUrlAdr"]
			eventUrl = event["urlAdr"]
			contactPhoneNum = event["organization"]["primaryContactPhone"]
			orgUrl = event["homePageUrlAdr"]
			city = event["place"]["cityName"]

			if endDate == "":
				print("FUCKALI--1")
			if startDate == "":
				print("FUCKALI--2")
			if picUrl == "":
				print("FUCKALI--3")
			#if eventUrl == "":
				#print("FUCKALI--4")
			if orgName == "":
				print("FUCKALI--5")
			if zipcode == "":
				print("FUCKALI--6")
			if contactPhoneNum == "":
				print("FUCKALI--7")
			if city == "":
				print("FUCKALI--9")

			if zipcode[0:3] in zipregionset:
				summ += 1
				#foundset.add(zipcode[0:3])
			#add to database <---------
			#eventInstance = Event(latitude, longitude, topics, startDate, endDate, picUrl, eventUrl, orgName, 
            #     contactPhoneNum, orgUrl, zipcode, city)
			#print(eventInstance)
			#print("***********************did it print?")
			#db.session.add(eventInstance)
			# print("begin commit")
			#db.session.commit()
			# print("  end commit")
	print(summ)
	current_page += 1
print(foundset)
#db.session.close()

# print(topics)
# print(categories)