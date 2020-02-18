import networkx as nx
import matplotlib.pylab as plot
from tkinter import *
from tkinter.ttk import *
from time import strftime

index = 0

M = nx.Graph()

C = []

City = ['Narathiwat','Yala','Pattani','Songkhla','Satun','Trang','Phatthalung','Nakhon Si Thammarat',
        'Krabi','Phuket','Phang Nga','Surat Thani','Ranong','Chumphon','Prachuap Khiri Khan','Phetchaburi',
        'Samut Songkhram','Samut Sakhon','Nonthaburi','Bangkok','Samut Prakan','Ratchaburi','Trat','Chanthaburi',
        'Rayong','Chonburi','Chachoengsao','Sa Kaew','PrachinBuri','NakhonPathom','PathhumThani','NakhonNayok',
        'Kanchanaburi','Suphanburi','Ayutthaya','AngThong','Saraburi','NakonRatchasima','Buriram','Surin',
        'Sisaket','Ubon Ratchathani','Uthaithani','Chainat','Singburi','Lopburi','Nakon Sawan','Chaiyaphum',
        'Maha Sarakam','Roi Et','Yasothon','AmnatCharoen','Tak','KamphaengPhet','Phichit','Phetchabun',
        'Khon Kean','Kalasin','Mukdahan','Nakhon Phanom','Sakon Nakhon','Udon Thani',
        'Nong BuaLamphu','Loei','Phitsanulok','Sukhothai','Nong Khai','Bueng Kan','Uttaradit','Phrae',
        'Nan','Lampang','Lamphun','Mae Hong Son','Chiang Mai','Phayao','Chiang Rai']


M.add_weighted_edges_from([('Loei','Nong Khai',234),('Loei','Nong BuaLamphu',99),('Loei','Khon Kean',207),('Loei','Chaiyaphum',227),
                           ('Nong Khai','Bueng Kan',135),('Nong Khai','Udon Thani',52),('Nong BuaLamphu','Udon Thani',51),('Udon Thani','Bueng Kan',207),
                           ('Nong BuaLamphu','Khon Kean',118),('Chaiyaphum','Khon Kean',141),('Khon Kean','Udon Thani',121),('Chaiyaphum','NakonRatchasima',121),
                           ('Khon Kean','NakonRatchasima',192),('Bueng Kan','Nakhon Phanom',181),('Udon Thani','Sakon Nakhon',166),('Bueng Kan','Sakon Nakhon',196),
                           ('Udon Thani','Kalasin',149),('Kalasin','Sakon Nakhon',129),('Sakon Nakhon','Nakhon Phanom',94),('Kalasin','Khon Kean',100),
                           ('Khon Kean','Maha Sarakam',72),('Maha Sarakam','NakonRatchasima',214),('Maha Sarakam','Kalasin',48),('Sakon Nakhon','Mukdahan',114),
                           ('Kalasin','Mukdahan',164),('Mukdahan','Nakhon Phanom',110),('Kalasin','Roi Et',49),('Roi Et','Maha Sarakam',44),
                           ('Maha Sarakam','Buriram',149),('Buriram','NakonRatchasima',127),('Buriram','Roi Et',149),('Roi Et','Mukdahan',149),
                           ('Mukdahan','AmnatCharoen',99),('AmnatCharoen','Yasothon',57),('Yasothon','Mukdahan',115),('Yasothon','Roi Et',68),
                           ('Yasothon','AmnatCharoen',57),('Buriram','Surin',55),('Surin','Roi Et',145),('Roi Et','Sisaket',146),
                           ('Sisaket','Surin',106),('Sisaket','Yasothon',103),('Sisaket','Ubon Ratchathani',65),('Ubon Ratchathani','Yasothon',103),
                           ('Ubon Ratchathani','AmnatCharoen',77),('Kanchanaburi','Suphanburi',98),('Kanchanaburi','NakhonPathom',67),
                           ('Kanchanaburi','Ratchaburi',81),('Ratchaburi','NakhonPathom',48),('NakhonPathom','Suphanburi',97),('Phetchaburi','Ratchaburi',58),
                           ('Phetchaburi','Samut Songkhram',57),('Samut Songkhram','Ratchaburi',35),('NakhonPathom','Samut Sakhon',67),
                           ('Samut Sakhon','Ratchaburi',67),('Samut Sakhon','Samut Songkhram',38),('Suphanburi','Chainat',101),('Chainat','Uthaithani',26),
                           ('Uthaithani','Nakon Sawan',43),('Nakon Sawan','Chainat',62),('Singburi','Chainat',57),('Chainat','Nakon Sawan',100),
                           ('AngThong','Singburi',40),('AngThong','Suphanburi',77),('Suphanburi','Ayutthaya',64),('AngThong','Ayutthaya',39),
                           ('Ayutthaya','NakhonPathom',32),('Nonthaburi','NakhonPathom',64),('Bangkok','Nonthaburi',22),('NakhonPathom','Bangkok',57),
                           ('Samut Sakhon','Bangkok',36),('Nonthaburi','Ayutthaya',75),('Lopburi','Nakon Sawan',151),('Lopburi','Singburi',32),
                           ('Lopburi','AngThong',42),('Saraburi','Ayutthaya',69),('Lopburi','Saraburi',47),('Saraburi','PathhumThani',85),
                           ('PathhumThani','Ayutthaya',60),('PathhumThani','Nonthaburi',27),('PathhumThani','Bangkok',42),('NakhonNayok','Saraburi',58),
                           ('PathhumThani','NakhonNayok',117),('PrachinBuri','NakhonNayok',20),('PrachinBuri','Bangkok',145),('Chachoengsao','Bangkok',85),
                           ('Chachoengsao','NakhonNayok',75),('Chachoengsao','PrachinBuri',74),('Samut Prakan','Bangkok',26),('Samut Prakan','Chonburi',70),
                           ('Chonburi','Chachoengsao',50),('Prachuap Khiri Khan','Chumphon',189),('Ranong','Chumphon',126),('Chumphon','Surat Thani',184),
                           ('Surat Thani','Ranong',218),('Phang Nga','Ranong',231),('Phang Nga','Surat Thani',159)])


TH = [('1.กระบี่'),('2.กรุงเทพมหานคร'),('3.กาญจนบุรี'),('4.กาฬสินธุ์'),('5.กำแพงเพชร'),('6.ขอนแก่น'),('7.จันทบุรี'),('8.ฉะเชิงเทรา'),
        ('9.ชลบุรี'),('10.ชัยนาท'),('11.ชัยภูมิ'),('12.ชุมพร'),('13.เชียงราย'),('14.เชียงใหม่'),('15.ตรัง'),('16.ตราด'),
        ('17.ตาก'),('18.นครนายก'),('19.นครปฐม'),('20.นครพนม'),('21.นครราชสีมา'),('22.นครศรีธรรมราช'),('23.นครสวรรค์'),
        ('24.นนทบุรี'),('25.นราธิวาส'),('26.น่าน'),('27.บึงกาฬ'),('28.บุรีรัมย์'),('29.ปทุมธานี'),('30.ประจวบคีรีขันธ์'),
        ('31.ปราจีนบุรี'),('32.ปัตตานี'),('33.พระนครศรีอยุธยา'),('34.พะเยา'),('35.พังงา'),('36.พัทลุง'),('37.พิจิตร'),
        ('38.พิษณุโลก'),('39.เพชรบุรี'),('40.เพชรบูรณ์'),('41.แพร่'),('42.ภูเก็ต'),('43.มหาสารคาม'),('44.มุกดาหาร'),
        ('45.แม่ฮ่องสอน'),('46.ยโสธร'),('47.ยะลา'),('48.ร้อยเอ็ด'),('49.ระนอง'),('50.ระยอง'),('51.ราชบุรี'),
        ('52.ลพบุรี'),('53.ลำปาง'),('54.ลำพูน'),('55.เลย'),('56.ศรีสะเกษ'),('57.สกลนคร'),('58.สงขลา'),('59.สตูล'),
        ('60.สมุทรปราการ'),('61.สมุทรสงคราม'),('62.สมุทรสาคร'),('63.สระแก้ว'),('64.สระบุรี'),('65.สิงห์บุรี'),('66.สุโขทัย'),
        ('67.สุพรรณบุรี'),('68.สุราษฎร์ธานี'),('69.สุรินทร์'),('70.หนองคาย'),('71.หนองบัวลำภู'),('72.อ่างทอง'),
        ('73.อำนาจเจริญ'),('74.อุดรธานี'),('75.อุตรดิตถ์'),('76.อุทัยธานี'),('77.อุบลราชธานี')]

ENG = [('1.Krabi'),('2.Bangkok'),('3.Kanchanaburi'),('4.Kalasin'),('5.Kamphaeng Phet'),('6.Khon Kaen '),('7.Chanthaburi'),('8.Chachoengsao'),
        ('9.Chonburi'),('10.Chainat'),('11.Chaiyaphum'),('12.Chumphon'),('13.Chiang Mai '),('14.Chiang Rai'),('15.Trang'),('16.Trat'),
        ('17.Tak'),('18.Nakhon Nayok'),('19.Nakhon Pathom'),('20.Nakhon Phanom'),('21.Nakhon Ratchasima'),('22.Nakhon Si Thammarat'),('23.Nakhon Sawan'),
        ('24.Nonthaburi'),('25.Narathiwat'),('26.Nan'),('27.Bueng Kan'),('28.Buriram'),('29.Pathum Thani'),('30.Prachuap Khiri Khan'),
        ('31.Prachinburi'),('32.Pattani'),('33.Phra Nakhon Si Ayutthaya'),('34.Phayao'),('35.Phang Nga'),('36.Phatthalung'),('37.Phichit'),
        ('38.Phitsanulok'),('39.Phetchaburi'),('40.Phetchabun'),('41.Phrae'),('42.Phuket'),('43.Maha Sarakham'),('44.Mukdahan'),
        ('45.Mae Hong Son'),('46.Yasothon'),('47.Yala'),('48.Roi Et'),('49.Ranong'),('50.Rayong'),('51.Rayong'),
        ('52.Lopburi'),('53.Lampang'),('54.Lamphun'),('55.Loei'),('56.Sisaket'),('57.Sakon Nakhon'),('58.Songkhla'),('59.Satun'),
        ('60.Samut Prakan'),('61.Samut Songkhram'),('62.Samut Sakhon'),('63.Sa Kaeo'),('64.Saraburi'),('65.Sing Buri'),('66.Sukhothai'),
        ('67.Suphan Buri'),('68.Surat Thani'),('69.Surin'),('70.Nong Khai'),('71.Nong Bua Lamphu'),('72.Ang Thong'),
        ('73.Amnat Charoen'),('74.Udon Thani'),('75.Uttaradit'),('76.Uthai Thani'),('77.Ubon Ratchathani')]

def THMeun() :
        print('===| เลือกจุดแวะ |===')
        for i in TH :
                print(i)
        Start = int(input('เลือกต้นทาง : '))
        First = int(input('เลือกจุดที่ 1 แต่ถ้าไม่ต้องการให้เลือก 0 : '))
        
        if 77 >= First >= 1 :
                index = 1
                Second = int(input('เลือกจุดที่ 2 แต่ถ้าไม่ต้องการให้เลือก 0 : '))
                
                if 77 >= Second >= 1 :
                        index = 2
                        pass
                else :
                        pass
        else :
                Second = 0
                pass
        Place = int(input('เลือกปลายทาง : '))
        Count(Start,First,Second,Place)

def Count(Start,First,Second,Place) :
        edge_labels = nx.get_edge_attributes(M, 'weight')

        S_1 = ENG[Start-1]
        if index == 1 :
                F_1 = ENG[First-1]
        if index == 2 :
                S_2 = ENG[Second-1]
        P_1 = ENG[Place-1]

        if index == 0 :
                P = nx.shortest_path(M,source=S_1,target=P_1,weight='weight')
                C = nx.shortest_path_length(M,source=S_1,target=P_1,weight='weight')
                print(f'Shortest from {S_1} to {P_1} : {P} ')
                print(f'Shortest length from {S_1} to {P_1} : {C}')
        if index == 1 :
                F = nx.shortest_path(M,source=S_1,target=F_1,weight='weight')
                P = nx.shortest_path(M,source=F_1,target=P_1,weight='weight')
                C = nx.shortest_path_length(M,source=S_1,target=F_1,weight='weight') + nx.shortest_path_length(M,source=F_1,target=P_1,weight='weight')
                print(f'Shortest from {S_1} to {F_1} : {F} ')
                print(f'Shortest from {F_1} to {P_1} : {F} ')
                print(f'Shortest length from {S_1} to {P_1} : {C}')
        if index == 2 :
                F = nx.shortest_path(M,source=S_1,target=F_1,weight='weight')
                S = nx.shortest_path(M,source=F_1,target=S_2,weight='weight')
                P = nx.shortest_path(M,source=S_2,target=P_1,weight='weight')
                C = nx.shortest_path_length(M,source=S_1,target=F_1,weight='weight') + nx.shortest_path_length(M,source=F_1,target=S_2,weight='weight') + nx.shortest_path_length(M,source=S_2,target=P_1,weight='weight')
                print(f'Shortest from {S_1} to {F_1} : {F} ')
                print(f'Shortest from {F_1} to {S_2} : {F} ')
                print(f'Shortest from {S_2} to {P_1} : {F} ')
                print(f'Shortest length from {S_1} to {P_1} : {C}')
                
        pos = nx.spring_layout(M)
        
        nx.draw(M, pos, with_labels=True, font_color = 'black', node_size=200,font_size=5)
        nx.draw_networkx_edge_labels(M, pos, edge_labels=edge_labels)
        plot.show()

def ENMeun() :
        print('===| Choose |===')

def main() :
        correct = 'uncorrect'
        L = input('Enter TH/EN : ')
        while correct != 'correct' :
                if L == 'TH' :
                        correct = 'correct'
                        THMeun()
                elif L == 'EN' :
                        correct = 'correct'
                        ENMeun()
                else :
                        print(']----------[')
                        print('Error Choose')
                        print(']----------[')
                        correct = 'uncorrect'
                        L = input('Enter TH/EN : ')

main()