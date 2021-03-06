from flask import Blueprint, render_template, request, session
from .models import Item, Gemstone, Metal, Bid
from .forms import ItemForm
from . import db


def get_item():
    item = Item("Gold Amber Ring", "https://i.pinimg.com/474x/b0/dc/40/b0dc40f5a5bc0ae02e2ba0dafe7926de.jpg",
                "Talisa", "Ring", "MaryP", 1, 2, 1992, "$120.00", "$230.35", "3.5cm", "15g", "Good", "Worn twice to parties")
    gem = Gemstone("Amber", "Gold Amber Ring", 1, "Rectangle",
                   "Orange", "2cm", "1cm", "0.5cm", "5g")
    gem2 = Gemstone("Amber", "Gold Amber Ring", 2, "Teardrop",
                    "Orange", "0.5cm", "0.8cm", "0.5cm", "3g")
    metal = Metal("Gold", "Gold Amber Ring", "Gold",
                  "14k", "copper", "3.5cm", "1cm", "4g")
    bid = Bid("nyne03", "Amber Pendant", "$144", "5/10/2020")
    bid1 = Bid("Starlight28", "Amber Pendant", "$150", "8/10/2020")
    bid2 = Bid("nyne03", "Amber Pendant", "$145", "12/10/2020")
    item.set_items(item)
    item.set_gems(gem)
    item.set_gems(gem2)
    item.set_metals(metal)
    item.set_bids(bid)
    item.set_bids(bid1)
    item.set_bids(bid2)
    item1 = Item("Round Diamond Earrings", "https://dl.airtable.com/.attachments/c408c402b19d6d876560736bd9b85f68/2dd7dd7f/RoundDiamondEarrings.jpg",
                 "Cartier", "Earrings", "cookieMonster789", 1, 2, "2016", "$330", "$299.00", "24mm", "12g", "Excellent", "Never worn. Perfect for functions.")
    gem3 = Gemstone("Diamond", "Round Diamond Earrings", 2,
                    "White", "Circle", "0.4cm", "0.4cm", "0.25cm", "4g")
    metal1 = Metal("Sterling silver", "Round Diamond Earrings",
                   "Silver", 0, "Silver", "12cm", "44mm", "10g")
    item.set_items(item1)
    item1.set_gems(gem3)
    item1.set_metals(metal1)
    item2 = Item("Sapphire Crystal Ring", "https://dl.airtable.com/.attachments/5ed715bb5470acaf07fa8c3439c3de3d/949ebaab/SilverSapphireRing.jpg",
                 "Wallace Bishop", "Ring", "cookieMonster789", 1, 2, 2009, "$287", "$311.50", "3cm", "50g", "Very Good", "Super sparkly, real crystals")
    gem4 = Gemstone("Sapphire", "Sapphire Crystal Ring", 1,
                    "Dark Blue", "Circle", "0.5cm", "0.5cm", "0.5cm", "4.5g")
    gem5 = Gemstone("Crystal", "Sapphire Crystal Ring", 24,
                    "White", "Circle", "1.5mm", "1.5mm", "1.5mm", "1g")
    item.set_items(item2)
    item2.set_gems(gem4)
    item2.set_gems(gem5)
    item2.set_metals(metal1)
    item3 = Item("Silver Diamond Ring", "https://dl.airtable.com/.attachments/6548906181af2d117a18ce634b5d69df/d86a2199/SilverDiamondRing.jpg",
                 "Tiffany & Co", "Ring",	"Starlight28", 1, 1, 2000, "$239", "$264.00", "2.5cm", "32g", "Good", "Thin metal, small diamond")
    gem6 = Gemstone("Diamond", "Silver Diamond Ring", 1,
                    "White", "Circle", "2cm", "2cm", "1cm", "6g")
    item.set_items(item3)
    item3.set_gems(gem6)
    item3.set_metals(metal1)
    item4 = Item("Gold Crystal Joint Bracelet",	"https://dl.airtable.com/.attachments/e2656e7e37902f2ba1c0615544db0893/0a779932/GoldJointBracelet.jpg",
                 "Cartier", "Bracelet", "CaseyLM", 1, 2, 2014, "$345", "$299.00", "7.8cm", "18g", "Very Good", "Worn 3 times")
    gem7 = Gemstone("Amber", "Gold Crystal Joint Bracelet",	8,
                    "Orange", "Square", "1cm", "1cm", "0.5cm", "3g")
    gem8 = Gemstone("Crystal", "Gold Crystal Joint Bracelet", 5,
                    "White", "Circle", "4mm", "4mm", "4mm", "1g")
    item.set_items(item4)
    item4.set_gems(gem7)
    item4.set_gems(gem8)
    item4.set_metals(metal)
    item5 = Item("Gold Drop Earrings", "https://dl.airtable.com/.attachments/85c26a6c8caf1e3a78d2fa59b0cc7b7b/db06debd/GoldDropEarrings.jpg",
                 "Prouds",	"Earrings",	"MaryP", 1, 0, 1998, "$98", "$75.90", "2.4cm", "9g", "Good", "Long and dangly")
    item.set_items(item5)
    item5.set_metals(metal)
    item6 = Item("Silver Rose Quartz Earrings",	"https://dl.airtable.com/.attachments/dc5cfb44aa36648ceecc9135670cd926/c13c2be6/SilverRoseEarrings.jpg",
                 "Michael Hill", "Earrings", "nyne03", 1, 1, 2003, "$120", "$94.50", "1.4cm", "5g",	"Fair", "Very pretty, shines in the light")
    gem9 = Gemstone("Rose Quartz", "Silver Rose Quartz Earrings",
                    2, "Pink", "Other Shape", "2cm", "2.4cm", "3mm", "2.2g")
    item.set_items(item6)
    item6.set_gems(gem9)
    item6.set_metals(metal1)
    item7 = Item("Silver Geometric Pendant", "https://dl.airtable.com/.attachments/136d02d4e0500cd257838351dc9927e0/855cc15a/SilverGeometricPendant.jpg",
                 "Pandora", "Pendant", "yyr84", 1, 0, 1996, "$99", "$108.95", "30cm", "14g", "Fair", "Very light to wear")
    item.set_items(item7)
    item7.set_metals(metal1)
    item8 = Item("Amber Flower Earrings", "https://dl.airtable.com/.attachments/199e360752c5b82fddffff00e23e9645/0cc685a5/AmberFlowerEarrings.jpg",
                 "Bvlgari", "Earrings", "Starlight28", 1, 2, 1994, "$124", "$102.00", "2cm", "15g", "Very Good", "Amazing!! 10/10. My daughter loved it")
    gem10 = Gemstone("Amber", "Amber Flower Earrings", 2,
                     "Orange", "Circle", "1.5cm", "1.5cm", "1cm", "4g")
    gem11 = Gemstone("Amber", "Amber Flower Earrings", 10,
                     "Orange", "Other Shape", "2.15cm", "1cm", "1cm", "4.5g")
    item.set_items(item8)
    item8.set_gems(gem10)
    item8.set_gems(gem11)
    item8.set_metals(metal1)
    item9 = Item("Amethyst Flower Ring", "https://dl.airtable.com/.attachments/d1854ca617034993922ffc327a3f55b5/6a9934bf/GoldAmethystFlowerRing.jpg",
                 "Dior", "Ring", "JamTam", 1, 2, 2008, "$420", "$250.90", "3.2cm", "27g", "Excellent", "Worn once, slightly heavy")
    gem12 = Gemstone("Amethyst", "Amethyst Flower Ring", 6,
                     "Purple", "Circle", "1.5cm", "1.5cm", "1cm", "4g")
    gem13 = Gemstone("Pink Topaz", "Amethyst Flower Ring", 4,
                     "Dark Pink", "Circle", "1cm", "1cm", "1cm", "3g")
    item.set_items(item9)
    item9.set_gems(gem12)
    item9.set_gems(gem13)
    item9.set_metals(metal)
    item10 = Item("Rose Gold Butterfly Bracelet", "https://dl.airtable.com/.attachments/ace4cc960edd1bbb3ceddf54e8a0a080/17c5feb3/RoseGoldButterfly.jpg", "Tiffany & Co",
                  "Bracelet", "LucyGooseyy", 1,	2, 2012, "$225", "$294.50",	"6.8cm", "19g",	"Good", "Many of my friends complimented this bracelet whenever I wore it")
    gem14 = Gemstone("Crystal", "Rose Gold Butterfly Bracelet",
                     36, "White", "Circle", "2mm", "2mm", "2mm", "0.5g")
    gem15 = Gemstone("Peach Sapphire", "Rose Gold Butterfly Bracelet",
                     1, "Light Peach", "Oval", "2.5cm", "1cm", "1cm", "3.5g")
    metal2 = Metal("Rose Gold", "Rose Gold Butterfly Bracelet",
                   "Rose gold", "8k", "Copper", "12cm", "3mm", "22g")
    item.set_items(item10)
    item10.set_gems(gem14)
    item10.set_gems(gem15)
    item10.set_metals(metal2)
    item11 = Item("Gold Triangular Earrings", "https://dl.airtable.com/.attachments/b9d21ac9445a677618d71f0a42efad56/c67d86ad/GoldTriangularEarrings.jpg",
                  "Goldmark", "Earrings", "cookieMonster789", 1, 0, 2017, "$87", "$84.99", "0.7cm", "8g", "Fair", "Simple, but makes a statement")
    item.set_items(item11)
    item11.set_metals(metal)
    return item


bp = Blueprint('main', __name__)


@bp.route('/')
def show():
    item = get_item()
    # item = Item.query.filter_by(ItemNo=id).first()
    return render_template('index/show.html', item=item)


@bp.route('/watchlist/<id>')
def watchlist(id):
    item = get_item()
    return render_template('watchlist/show.html', item=item)


@bp.route('/item_details/<id>')
def item_details(id):
    item = Item.query.filter_by(ItemNo=id).first()
    # item = get_item()
    return render_template('item_details/show.html', item=item)


@bp.route('/list_item', methods=['GET', 'POST'])
def list_item():
    print('Method Type: ', request.method)
    form = ItemForm()
    if form.validate_on_submit():
        print('Item submitted')

        name = form.itemName.data
        pic = form.itemPicture.data
        brand = form.itemBrand.data
        itemtype = form.itemType.data
        metalamount = form.itemMetals.data
        gemamount = form.itemGemAmount.data
        year = form.itemYear.data
        starting = form.itemStartingPrice.data
        original = form.itemValuePrice.data
        size = form.itemSize.data
        weight = form.itemWeight.data
        cond = form.itemCondition.data
        desc = form.itemDescription.data

        # create new item in session
        new_item = Item(ItemName=name, Picture=pic, Brand=brand, ItemType=itemtype, MetalAmount=metalamount, GemAmount=gemamount, YrCreated=year, StartingPrice=starting, OriginalPrice=original, Size=size, Weight=weight, Condition=cond, Description=desc)
        db.session.add(new_item)

        # commit to db
        db.session.commit()
        return ''

    return render_template('list_item/show.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    session['email'] = request.values.get('email')
    return render_template('login.html')


@bp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
