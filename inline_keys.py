from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def calamity_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Rain", callback_data="rain"),
        InlineKeyboardButton("Flooding", callback_data="flooding"),
        InlineKeyboardButton("Storm", callback_data="storm"),
        InlineKeyboardButton("Lightning", callback_data="lightning"),
        InlineKeyboardButton("Visibility", callback_data="visibility"),
        InlineKeyboardButton("Landslide", callback_data="landslide"),
        InlineKeyboardButton("Earthquake", callback_data="earthquake")
    )
    return markup

def rain_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("No Rain", callback_data="a1_No Rain"),
        InlineKeyboardButton("Light Rain (Drizzle)", callback_data="a2_Light Rain (Drizzle)"),
        InlineKeyboardButton("Heavy Rain", callback_data="a3_Heavy Rain"),
        InlineKeyboardButton("Freezing Rain", callback_data="a4_Freezing Rain"),
        InlineKeyboardButton("Freezing Drizzle", callback_data="a5_Freezing Drizzle"),
        InlineKeyboardButton("Snow", callback_data="a6_Snow"),
        InlineKeyboardButton("Mixed Rain and Snow", callback_data="a7_Mixed Rain and Snow")
    )
    return markup

def flooding_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("SEVERE - Large Scale evacuation of people. Permananent houses and vahicles swept away", callback_data="b1_SEVERE"),
        InlineKeyboardButton("MAJOR - Affecting communities. Flooded roads, stranded vehicles, and inundated houses.", callback_data="b2_MAJOR"),
        InlineKeyboardButton("MODERATE - Flooded roads, Disruption of travel to flooding sites.", callback_data="b3_MODERATE"),
        InlineKeyboardButton("MINOR - Flooding in low-lying areas, some inconviences to the public.", callback_data="b4_MINOR"),
        InlineKeyboardButton("NONE - No flooding observed", callback_data="b5_NONE")
    )
    return markup

def storm_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Catastrophic - Damage to doors and windows, building failures with massive evacuation.", callback_data="c1_Catastrophic"),
        InlineKeyboardButton("Extreme - Failure of roofs, major erosion, evacuation near the sea-shore", callback_data="c2_Extreme"),
        InlineKeyboardButton("Extensive - Large trees blown down, some structural damage to buildings", callback_data="c3_Extensive"),
        InlineKeyboardButton("Moderate - Small trees down, damage to temporary structure.", callback_data="c4_Moderate"),
        InlineKeyboardButton("Monir - Damage to trees and foliage, low-lying roads flooded.", callback_data="c5_Monir")
    )
    return markup

def lightning_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Cloud-to-Ground", callback_data="d1_Cloud-to-Ground"),
        InlineKeyboardButton("Cloud-to-Cloud", callback_data="d2_Cloud-to-Cloud"),
        InlineKeyboardButton("Cloud-to-Air", callback_data="d3_Cloud-to-Air"),
        InlineKeyboardButton("Spider", callback_data="d4_Spider")
    )
    return markup

def visibility_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Light Fog", callback_data="e1_Light Fog"),
        InlineKeyboardButton("Dense Fog", callback_data="e2_Dense Fog"),
        InlineKeyboardButton("Smog/Air Pollution", callback_data="e3_Smog/Air Pollution"),
        InlineKeyboardButton("Blowing Dust", callback_data="e4_Blowing Dust"),
        InlineKeyboardButton("Blowing Snow", callback_data="e5_Blowing Snow")
    )
    return markup

def landslide_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Landslide", callback_data="f1_Landslide"),
        InlineKeyboardButton("Mudslide", callback_data="f2_Mudslide"),
        InlineKeyboardButton("Debris flow", callback_data="f3_Debris flow"),
        InlineKeyboardButton("Rock fall", callback_data="f4_Rock fall"),
        InlineKeyboardButton("Translational slide", callback_data="f5_Translational slide"),
        InlineKeyboardButton("Rotational slide", callback_data="f6_Rotational slide"),
        InlineKeyboardButton("Complex", callback_data="f7_Complex"),
        InlineKeyboardButton("Topple", callback_data="f8_Topple"),
        InlineKeyboardButton("Riverbank collapse", callback_data="f9_Riverbank collapse"),
        InlineKeyboardButton("Lahar", callback_data="f10_Lahar"),
        InlineKeyboardButton("Earth flow", callback_data="f11_Earth flow"),
        InlineKeyboardButton("Snow avalanche", callback_data="f12_Snow avalanche"),
        InlineKeyboardButton("Creep", callback_data="f13_Creep")
    )
    return markup

def confirm_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Confirm", callback_data="confirm")
    )
    return markup