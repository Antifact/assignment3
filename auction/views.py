from flask import Blueprint, render_template, request, session
from .models import Item, Gemstone, Metal


def get_item():
    item = Item("Gold Amber Ring", "https://i.pinimg.com/474x/b0/dc/40/b0dc40f5a5bc0ae02e2ba0dafe7926de.jpg", "Talisa", "Ring", "MaryP", 1, 2, 1992, "$120.00", "$230.35", "3.5cm", "15g", "Good", "Worn twice to parties")
    gem = Gemstone("Amber", "Gold Amber Ring", 1,"Rectangle", "Orange","n/a",  "2cm", "1cm", "0.5cm", "5g", "Rare quality")
    gem2 = Gemstone("Amber", "Gold Amber Ring", 2,"Teardrop", "Orange","n/a",  "1cm", "0.8cm", "0.5cm", "3g", "Rare quality")
    metal = Metal("Gold", "Gold Amber Ring", "gold", "14k", "copper", "3.5cm", "1cm", "4g")
    item1 = Item("Round Diamond Earrings", "https://dl.airtable.com/.attachments/c408c402b19d6d876560736bd9b85f68/2dd7dd7f/RoundDiamondEarrings.jpg", "Cartier", "Earrings", "cookieMonster789", 1, 2, "2016", "$330", "$299.00", "24mm", "12g", "Excellent", "Never worn. Perfect for functions.")
    item2 = Item("Sapphire Crystal Ring", "https://dl.airtable.com/.attachments/5ed715bb5470acaf07fa8c3439c3de3d/949ebaab/SilverSapphireRing.jpg", "Wallace Bishop", "Ring", "cookieMonster789", 1, 2, 2009, "$287", "$311.50", "3cm", "50g", "Very Good", "Super sparkly, real crystals")
    item3 = Item("Silver Diamond Ring", "https://dl.airtable.com/.attachments/6548906181af2d117a18ce634b5d69df/d86a2199/SilverDiamondRing.jpg", "Tiffany & Co", "Ring",	"Starlight28", 1, 1, 2000, "$239", "$264.00", "2.5cm", "32g", "Good", "Thin metal, small diamond")
    item4 = Item("Gold Crystal Joint Bracelet",	"https://dl.airtable.com/.attachments/e2656e7e37902f2ba1c0615544db0893/0a779932/GoldJointBracelet.jpg",	"Cartier", "Bracelet", "CaseyLM", 1, 2, 2014, "$345", "$299.00", "7.8cm", "18g", "Very Good", "Worn 3 times")
    item5 = Item("Gold Drop Earrings", "https://dl.airtable.com/.attachments/85c26a6c8caf1e3a78d2fa59b0cc7b7b/db06debd/GoldDropEarrings.jpg", "Prouds",	"Earrings",	"MaryP", 1, 0, 1998, "$98", "$75.90", "2.4cm", "9g", "Good", "Long and dangly")
    item6 = Item("Silver Rose Quartz Earrings",	"https://dl.airtable.com/.attachments/dc5cfb44aa36648ceecc9135670cd926/c13c2be6/SilverRoseEarrings.jpg", "Michael Hill", "Earrings", "nyne03", 1, 1, 2003, "$120", "$94.50", "1.4cm", "5g",	"Fair", "Very pretty, shines in the light")
    item7 = Item("Silver Geometric Pendant", "https://dl.airtable.com/.attachments/136d02d4e0500cd257838351dc9927e0/855cc15a/SilverGeometricPendant.jpg", "Pandora", "Pendant", "yyr84", 1, 0, 1996, "$99", "$108.95", "30cm", "14g", "Fair", "Very light to wear")
    item8 = Item("Amber Flower Earrings", "https://dl.airtable.com/.attachments/199e360752c5b82fddffff00e23e9645/0cc685a5/AmberFlowerEarrings.jpg", "Bvlgari", "Earrings", "Starlight28", 1, 2, 1994, "$124", "$102.00", "2cm", "15g", "Very Good", "Amazing!! 10/10. My daughter loved it")
    item9 = Item("Amethyst Flower Ring", "https://dl.airtable.com/.attachments/d1854ca617034993922ffc327a3f55b5/6a9934bf/GoldAmethystFlowerRing.jpg", "Dior", "Ring", "JamTam", 1, 2, 2008, "$420", "$250.90", "3.2cm", "27g", "Excellent", "Worn once, slightly heavy")
    item10 = Item("Rose Gold Butterfly Bracelet", "https://dl.airtable.com/.attachments/ace4cc960edd1bbb3ceddf54e8a0a080/17c5feb3/RoseGoldButterfly.jpg", "Tiffany & Co", "Bracelet", "LucyGooseyy", 1,	2, 2012, "$225", "$294.50",	"6.8cm", "19g",	"Good", "Many of my friends complimented this bracelet whenever I wore it")
    item11 = Item("Gold Triangular Earrings", "https://dl.airtable.com/.attachments/b9d21ac9445a677618d71f0a42efad56/c67d86ad/GoldTriangularEarrings.jpg", "Goldmark", "Earrings", "cookieMonster789", 1, 0, 2017, "$87", "$84.99", "0.7cm", "8g", "Fair", "Simple, but makes a statement")
    item.set_items(item)
    item.set_items(item1)
    item.set_items(item2)
    item.set_items(item3)
    item.set_items(item4)
    item.set_items(item5)
    item.set_items(item6)
    item.set_items(item7)
    item.set_items(item8)
    item.set_items(item9)
    item.set_items(item10)
    item.set_items(item11)
    item.set_gems(gem)
    item.set_gems(gem2)
    item.set_metals(metal)
    return item

bp = Blueprint('main', __name__)

@bp.route('/')
def show():
    item = get_item()
    return render_template('index/show.html', item=item)

@bp.route('/watchlist/<id>')
def watchlist(id):
    item = get_item()
    return render_template('watchlist/show.html', item=item)

@bp.route('/item_details/<id>')
def item_details(id):
    item = get_item()
    return render_template('item_details/show.html', item=item)

@bp.route('/list_item')
def list_item():
    return render_template('list_item/show.html')

@bp.route('/login', methods=['GET' , 'POST'])
def login():
    session['email']=request.values.get('email')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)