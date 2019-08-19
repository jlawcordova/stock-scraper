from requests import get, post, Response, Session
from bs4 import BeautifulSoup
import sched, time
from win10toast import ToastNotifier
from datetime import datetime
import random

s = sched.scheduler(time.time, time.sleep)

session = Session()

def login():
    loginres: Response = session.post("http://www.neopets.com/login.phtml",
        # {
        #     'username': 'netzon_jlaw',
        #     'password': 'aMsn21!dks@'
        # })
        {
            'username': 'jlawcordova',
            'password': '7zsxPj3S'
        })
    print("[{}] Logged in with status {}.".format(datetime.now(), loginres.status_code))
    toaster = ToastNotifier()
    toaster.show_toast("Store Checker","Successfully logged in.")

def check_store(sc): 
    print("[{}] Checking store.".format(datetime. now()))
    response: Response = session.get(
    "http://www.neopets.com/objects.phtml?obj_type=108&type=shop"
    # ,
    # cookies=dict(
    #     __utmt="1",
    #     _tz="-480",
    #     fq="1",
    #     vq="11673,11682,11682,11673,11682,11682,11682,11673,11682,11682,11673,11682,11673,11682,11682,11673,11682,11682,11673,11682,11673,11682,11673,11682,11682,11673,11682,11682,11673,11682,11682,11673,11682,11682,11673,11682,11682,11673,11682,11682,11682,11673,11682,11673,11681,11673,11673,11673,11673,11673,11673",
    #     session_depth="12",
    #     vl="1:5:00|2:PH|3:BULACAN|4:|5:BULACAN/|6:BULACAN/SAN JOSE DEL MONTE|7:1479|!0",
    #     PHPSESSID="1bp6q1hg1rdo2qf554j7d68hv1",
    #     np_uniq_="2019-08-17",
    #     np_uniq_jlawcordova="2019-08-18",
    #     np_randseed="21917855492942605",
    #     __utmv="258639253.|5=altador-cup-team-member=no=1",
    #     __utmb="258639253.65.10.1566184058",
    #     __utma="258639253.1877533537.1566054550.1566179371.1566184058.7",
    #     __utmz="258639253.1566140011.5.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
    #     __utmc="258639253",
    #     vg="54e4cbc5-9a46-4c91-842d-779c760f47da",
    #     xt6Yr4e33D="752079179778",
    #     pwUID="820083090675487",
    #     country="PH",
    #     m2session="be99ce3b-9cc3-4ba2-b499-6dd43e1d2396",
    #     npuid="d50000003e6070470007Y600063000000060a6001000c0f72646f76610000000",
    #     m2hb="enabled",
    #     vd="globe.com.ph",
    #     neoremember="jlawcordova",
    #     neologin="jlawcordova%2B55e735da4820ff254859bc32900a537cc8ed9dcf",
    #     np_uniq="pending",
    #     pg_variant="prod",
    #     OX_plg="swf|shk|pm",
    #     df_active="true",
    #     toolbar="jlawcordova%2BC%2B55e735da4820ff254859bc32900a537cc8ed9dcf",
    # )
    )
    soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
    table: BeautifulSoup = soup.find_all("table", {
        "class": "contentModuleTable"
    })
    if len(table) == 0:
        login()
        print("[{}] Session timed out. Logging back in.".format(datetime. now()))
        check_again = 0
        toaster = ToastNotifier()
        toaster.show_toast("Store Checker","Session timed out. Logging back in.")
    elif len(table) != 2:
        print("[{}] Sold out!".format(datetime. now()))
        check_again = random.randint(25, 75)
    else:
        content: BeautifulSoup = table[1].find_all("b")

        rares = [
            'Usukicon Y11 Background', 'Wheel of Excitement Background', 'Faerie City Balcony Background', 'Faerie Caverns Background', '10 Year Celebration Shield Background',
            'Faerieland Gazebo Background', 'Faerielands Destruction Background', 'Ultimate Battlefield Background', 'Usuki Dream Castle Background', 'Entrance to Haunted Woods Background',
            'View of Krawk Island from Ship Background', 'Haunted House Porch Background', 'Inside a Toy Claw Machine Background', 'House in Neopia Central Background', 'Lost Desert Silhouette Background',
            'Meridell Castle Silhouette Background', 'Classy Minimal Boudoir', 'Krawk Island Silhouette Background', 'Mystery Island Huts Background', 'Meridell Entrance Background',
            'Shenkuu Silhouette Background', 'Space Station Silhouette Background', 'Classy Minimal Dresser', 'Creepy Darigan Citadel Background', 'Entrance to Altador Background',
            'Lost Desert Game Board Background', 'Saskias Cart Silhouette Background', 'Underwater Shipwreck Background', 'Soup Faerie Kitchen Background', 'Tyrannia Concert Hall Background',
            'Shenkuu Game Board Background', 'Mystery Island Silhouette Background', 'Deserted Fairground Silhouette Background', 'Double Rainbow Background', 'Neovia Shop Silhouette Background',
            'Neopies After-Party Background', 'Mystery Island Game Board Background', 'Lovely Spring Morning Background', 'Moltara Silhouette Background', 'Beautiful Desert Oasis Background',
            'Terror Mountain Snowy Path Background', 'Shooting Star Background', 'Ultimate Fan Room Background', 'Shenkuu Mansion Background', 'Question Mark Background', 'Kreludor Cave Door Background',
            'Nox Castle Silhouette Background', 'Spaceship Interior Background', 'Governors Mansion Silhouette Background', 'Seasonal Maraquan Background', 'Wheel of Misfortune Silhouette Background',
            'Games Graveyard Silhouette Background', 'Evil Garden Gnome Background', 'Ice Volcano Background', 'Faerieland Mansion Background', 'Doughnut Explosion Background',
            'Resistance Headquarters Background', 'Super Ice Cream Machine Background', 'Outside Desert Arms Background', 'Underwater Background', 'Crisis Courier Craze Background',
            'Tarlas Underground Workshop Background', 'Starry Night in Neopia', 'Dark Cave Background', 'Sophies Hut Background', 'Neopies Carpet Background', 'Tyrannian Concert Hall Background',
            'Dreamy Pink Hearts Background', 'Altador Mansion Background', 'Day and Night Garland', 'Terror Mountain Mansion Background', 'Fancy Kitchen Background',
            'Perilous Catacombs Sentient Door Background', 'Spooky Background', 'Faerieland Cloud Background', 'Spring Topiary Garden Background', 'Shoppe of Neggs Background',
            'Haunted Weapon Silhouette Background', 'Neopies Dressing Room Background', 'Roo Island Pier Background', 'Chocolate Paradise Background', 'Negg Hunt Foreground',
            'Tyrannian Cliffs Background', 'Destroyed Faerie Festival Background', 'Melting Test Station Background', 'I Love Pie Background', 'Negg Museum', 'Meepit Vs Feepit Background',
            'Spring Courtyard Background', 'Festive Fireworks',
            # 'Xandras Library Background', 
            # 'Nightfall Background',
            'Noxs Mansion Background', 'Moltaran Workshop Background',
            'Spooky Forest Path Background', 'Meepit Juice Break Background',
            # 'Mystical Little House Background',
            'Hollowed Negg Tree Background', 'Idyllic Nature Scene', 'Ednas Shadow Background',
            'Terror Mountain Igloo Background', 'Virtupets Space Dock 010 Background', 'Exploring Kreludor Background'
            # 'Shop Inventory',
            # 'Grassy Meadow Background',
            # 'Moon and Stars Background',
            # 'Buzzer Hive Background',
            # 'Rubbish Dump Background',
            # 'Raining Doughnuts Background',
            # 'Raspberry Patch Background',
            # 'Gross Food Buffet Background',
            # 'Citrus Background',
            # 'Waffle Paradise Background',
            # 'Birthday in the Park Background',
            # 'Mystery Island Training School Background',
            # 'Winter Landscape Background',
            # 'Perfectly Flat Rock Quarry Background',
            # 'Mystery Island Heads Background',
            # 'Rocky Ocean Background',
            # 'Brightvale Books Background',
            # 'Swashbuckling Academy Background',
            # 'Cornucopia Background',
            # 'Visiting the Advent Calendar Background',
            # 'Jhudoras Bluff Background',
            # 'Lily Pad Background',
            # 'Tropical Island Paradise Background',
            # 'Holiday Decorated Money Tree',
            # 'Altadorian Pasture Background',
            # 'Snowy Mountain Background',
            # 'Scenic Tyrannian Background',
            # 'Magma Falls Background',
            # 'Fyoras Room Background',
            # 'Transmogrification Lab Background',
            # 'Mystical Little House Background',
            # 'Bubbled Background',
            # 'Snowfall in the Night Background',
            # 'Snowy Mansion Background',
            # 'Tree of Petals Background',
            # 'Ice Caves Background',
            # 'Game Room Background',
            # 'Cloudy Sky Background',
            # '8th Birthday Celebration Background',
            # 'Shearing Room Background',
            # 'A Grey Day Background',
            # 'Courgette Field Background',
            # 'Lunar Temple Background',
            # 'Neopia Central Background',
            # 'Fungus Cave Background',
            # 'Spooky Tower Entrance',
            # 'Scenic Mountain Top Background',
            # 'Spring Path Background',
            # 'Neopia Central Background',
            # 'Snowed In - errr - Out Background',
            # 'Zen Garden Background',
            # 'Glitter and Sparkle Background',
            # 'Colourful Towel Background',
            # 'Gourmet Club Bowls Background',
            # 'Meridell Countryside Background',
            # 'Relaxing Kiko Lake Background',
            # 'Road to the Deserted Tomb Background',
            # 'Bone Vault Background',
            # 'Neopia Central Neohome Background',
            # 'Keyring Case Background',
            # 'Soft Rain Background',
            # 'Haunted Laboratory Background',
            # 'Square Mania Ba Background',
            # 'Giant Omelette Background',
            # 'Field of Grass Background',
            # 'Malicious Dark Faeries Background',
            # 'Maractite Cavern Background',
            # 'River Overlook',
            # 'Nostalgic Faerieland Background',
            # 'Kiko Lake Carpentry Background',
            # 'Square Mania Background',
            # 'Mystery Swirl Background',
            # 'Chocolate Ballroom Background',
            # 'Kau Kau Farms Background',
            # 'Ye Olde Petpets Stall Background',
            # 'Mystical Little House Background',
            # 'Secluded Bench Background',
            # 'Fyoras Balcony',
            # 'Lawyerbots Number One Fan Background',
            # 'Ileres Tree Background',
            # 'Forest Glade Background',
            # 'Underwater Net Background',
            # 'Autumn Country Road Background',
            # 'Dark Secret Background',
            # 'Xandras Library Background',
            # 'Neogarden Background',
            # 'Nightfall Background',
            # '8-Bit Mystery Island Background',
            # 'Altador Sun Background',
            # 'Brightvale Prison Cell Background',
            # 'Crumbling Ancient Castle Background',
            # 'Moltara City Background',
            # ''
        ]

        items = [element.text for element in content]
        uncommons = [uncommon for uncommon in items if uncommon in rares]

        # print("[{}] Found!\n{}".format(datetime.now(), str(items)))
        if len(uncommons) != 0:
            print("[{}] Uncommons found!\n{}".format(datetime.now(), str(uncommons)))
            toaster = ToastNotifier()
            toaster.show_toast("Store Checker","Uncommons found!\n{}".format(str(uncommons)))
            check_again = random.randint(120, 180)
        else:
            print("[{}] Nothing special.".format(datetime.now()))
            check_again = random.randint(8, 28)

    print("[{}] Checking again in {} seconds.".format(datetime.now(), check_again))
    s.enter(check_again, 1, check_store, (sc,))

toaster = ToastNotifier()
toaster.show_toast("Store Checker", str("Starting store checker."))
print("[{}] Starting checker.".format(datetime.now()))
login()

s.enter(0, 1, check_store, (s,))
s.run()


