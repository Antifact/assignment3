
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

# Item Creation Form
class ItemForm(FlaskForm):

    # Basic and Important Information
    itemName=StringField("Item Name", validators=[InputRequired('Enter item name')])
    itemType=StringField("Item Type", validators=[InputRequired('Enter item type')])
    itemBrand=StringField("Brand", validators=[InputRequired('Enter brand')])
    itemYear=StringField("Year", validators=[InputRequired('Enter year')])
    itemSize=StringField("Size", validators=[InputRequired('Enter size')])
    itemWeight=StringField("Weight", validators=[InputRequired('Enter weight')])
    itemAmount=StringField("Item Amount", validators=[InputRequired('Enter amount')])
    itemCondition=StringField("Condition", validators=[InputRequired('Enter condition')])
    itemGemstones=StringField("Variety of Gemstones")
    itemMetals=StringField("Variety of Metals")

    # Optional Gemstones
    itemGemType=StringField("Gemstone Type")
    itemGemAmount=StringField("Gemstone Amount")
    itemGemColour=StringField("Colour")
    itemGemClarity=StringField("Clarity")
    itemGemCTW=StringField("CTW")
    itemGemCut=StringField("Cut Type")
    itemGemHeight=StringField("Height")
    itemGemWidth=StringField("Width")
    itemGemDepth=StringField("Depth")

    # Optional Metal
    itemMetalType=StringField("Metal Type")
    itemMetalMaterial=StringField("Plating Material")
    itemMetalKarat=StringField("Karat")
    itemMetalLength=StringField("Length")
    itemMetalWeight=StringField("Weight")

    # The rest 
    itemStartingPrice=StringField("Starting Price", validators=[InputRequired('Enter starting price')])
    itemValuePrice=StringField("Value Price", validators=[InputRequired('Enter value price')])
    itemDescription=StringField("Description", validators=[InputRequired('Enter description')])
    itemPicture=StringField("Picture", validators=[InputRequired('Upload picture')])
    itemAuth=StringField("Jewellery Authentication", validators=[InputRequired('Upload authentication')])

    # Submit
    submit = SubmitField("Submit")


#creates the login information
class LoginForm(FlaskForm):
    username=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    username=StringField("User Name", validators=[InputRequired()])
    email = StringField("Email ID", validators=[InputRequired(),Email("Please enter a valid email")])
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired()])            
    confirm = PasswordField("Confirm Password" , validators=[ EqualTo('confirm', message="Passwords should match")])
    #submit button
    submit = SubmitField("Register")