from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
markup = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🚘 Online sotish")],
    [KeyboardButton(text="📞 Kanal Admini bilan bog'lanish"), KeyboardButton(text="🎆 Kanalga o'tish ")],
    [KeyboardButton(text="🚗 Chevralet avto haqida malumot"), KeyboardButton(text="🟢 Youtubedan tamosha qilish")],
], resize_keyboard=True)


moshinalar=["🚗damas🚗","🚗Labo🚗","🚗spark🚗","🚗nexia3🚗", "🚗cobalt🚗","🚗gentra🚗", "🚗onix🚗","🚗trecker🚗", "🚗malibu🚗","🚗equinox🚗", "🚗tahoe🚗","🚗trailblazer🚗", "🚗traverse🚗"]
markup3=ReplyKeyboardMarkup(resize_keyboard=True)
for moshina in moshinalar:
    markup3.insert(moshina)
markup3.add(KeyboardButton(text="🏠 Bosh sahifa 🏛"))

order=ReplyKeyboardMarkup(resize_keyboard=True)
order.add(KeyboardButton(text="☎️ Bog'lanish uchun raqamingizni jo'natinhg", request_contact=True))
order.add(KeyboardButton(text="📍Joylashuvingizni jo'nating", request_location=True))
order.add(KeyboardButton(text="ORQAGA↩️"))

colors=InlineKeyboardMarkup(row_width=1)
colors_lst = [("🔴 QIZIL 🔴","qizil"), ("⚫️ QORA ⚫️", "qora"), ("🟢 YASHIL 🟢", "yashil"), ("🔵 KO'K 🔵", "ko'k"), ("⚪️ OQ ⚪", "oq"), ("🟤 CHOKKO 🟤", "chokko")]
for color in colors_lst:
    colors.insert(InlineKeyboardButton(text=color[0], callback_data=color[1]))
contact = ReplyKeyboardMarkup(resize_keyboard=True)
contact.add(KeyboardButton(text="☎️ Bog'lanish uchun raqamingizni jo'natinhg", request_contact=True))

m_markup=InlineKeyboardMarkup(row_width=2)
m_markup.row(InlineKeyboardButton(text="✅ HA", callback_data="YES"), InlineKeyboardButton(text="❌ YO'Q", callback_data="NO"))

restart=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="🔁 Botni qayta ishga tushirish")]
])


