import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboard import markup, markup3, order, colors, contact, m_markup
from states import AUTOINFO
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from confrig import API_TOKEN,ADMINS
from aiogram.dispatcher import FSMContext

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    full_name = message.from_user.full_name
    await message.reply(f"<i>Salom! {full_name}\nMen Online Moshina sotishga yordam beraman!\nMa'lumot kiritsangiz kifoya.</i>",parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗 Chevralet avto haqida malumot")
async def get_auto_info(message: types.Message):
    await message.answer("<b>Moshinalarimizni qaysi biri qiziqtirsa shuni tanlang.</b>", parse_mode="html")
    await message.answer("<i>Ro'yxatdan kerakli moshinani tanlang</i>",parse_mode="html",reply_markup=markup3)
@dp.message_handler(content_types=["contact"])
async def save_contact(message: types.Message):
    phone=message.contact.phone_number
    await message.answer(f"{phone} raqami saqlandi")
    reply_murkub=ReplyKeyboardRemove()
@dp.message_handler(text="🚗Labo🚗")
async def get_labo_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/SdR1SQ0")
    await message.answer("<b>🚚Yuk xona sig'imi (550l)\n🕹 Uzatish qutisi (MT5)\n⚒🛠 Xavfsizlik(-)\n🛢 Yoqilg'i istemoli (7.8/8.6)\n🛏 Xavfsizlik yostiqchasi (-)</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗damas🚗")
async def get_damas_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/SspkrZq")
    await message.answer("<b>🚚Yuk xona sig'imi (450l)\n🕹 Uzatish qutisi (MT5)\n⚒🛠 Xavfsizlik(-)\n🛢 Yoqilg'i istemoli (7.8/8.6)\n🛏 Xavfsizlik yostiqchasi (-)</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗spark🚗")
async def get_damas_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/j3fD5Md")
    await message.answer("<b>🚚Yuk xona sig'imi (170/568 L.)\n🕹 Uzatish qutisi (MT5/AT4)\n⚒🛠 Xavfsizlik(ABS)\n🛢 Yoqilg'i istemoli (6.2/8.2 L.)\n🛏 Xavfsizlik yostiqchasi (1)</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗nexia🚗")
async def get_nexia_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/VwDWLrV")
    await message.answer("<b>🚚Yuk xona sig'imi (400l)\n🕹 Uzatish qutisi (MT5/AT6)\n⚒🛠 Xavfsizlik(ABS)\n🛢 Yoqilg'i istemoli (8/9.3 L.)\n🛏 Xavfsizlik yostiqchasi (2)</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗cobalt🚗")
async def get_cobalt_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/Bw4nmQF")
    await message.answer("<b>🚚Yuk xona sig'imi (563 L.)\n🕹 Uzatish qutisi (MT5/AT6)\n⚒🛠 Xavfsizlik(ABS)\n🛢 Yoqilg'i istemoli (8.5/9.0 L.)\n🛏 Xavfsizlik yostiqchasi (2)</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗gentra🚗")
async def get_gentra_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/P1ZCmy3")
    await message.answer("<b>🚚Yuk xona sig'imi (405 L.)\n🕹 Uzatish qutisi (MT5/AT6)\n⚒🛠 Xavfsizlik(ABS)\n🛢 Yoqilg'i istemoli (8.5/9.5 L.)\n🛏 Xavfsizlik yostiqchasi (2)</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗onix🚗")
async def get_onix_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/Vt6CcVG")
    await message.answer("<b>🚚Yuk xona sig'imi (469l)\n🕹 Uzatish qutisi (MT5/6AT)\n⚒🛠 Xavfsizlik(ABS (ABS и ESC - электронная система курсовой устойчивости))\n🛢 Yoqilg'i istemoli (АИ - 92 L.)\n🛏 Xavfsizlik yostiqchasi (Все автомобили Chevrolet Onix оснащены минимум 2 подушками безопасности и системами ABS и ESC (электронная система курсовой устойчивости).)</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗trecker🚗")
async def get_trecker_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/LvkXf1P")
    await message.answer("<b>🚚Yuk xona sig'imi (235l)\n🕹 Uzatish qutisi (MT5/6AT)\n⚒🛠 Xavfsizlik(ABS и ESC - электронная система курсовой устойчивости)\n🛢 Yoqilg'i istemoli (АИ - 92 L\n🛏 Xavfsizlik yostiqchasi (Все автомобили Chevrolet Trecker оснащены минимум 2 подушками безопасности и системами ABS и ESC (электронная система курсовой устойчивости).))</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗malibu🚗")
async def get_damas_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/J2cKFYr")
    await message.answer("<b>🚚Yuk xona sig'imi (447l)\n🕹 Uzatish qutisi (AT6)\n⚒🛠 Xavfsizlik(ABS)\n🛢 Yoqilg'i istemoli (T8,5/8.1)\n🛏 Xavfsizlik yostiqchasi (Все автомобили Chevrolet Malibu оснащены минимум 2 подушками безопасности и системами ABS и ESC (электронная система курсовой устойчивости).))</b>", parse_mode="html", reply_markup=markup)


@dp.message_handler(text="🚗equinox🚗")
async def get_damas_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/sjBghVQ")
    await message.answer("<b>🚚Yuk xona sig'imi (1627l)\n🕹 Uzatish qutisi (AT9)\n⚒🛠 Xavfsizlik(ABS)\n🛢 Yoqilg'i istemoli (8.2)\n🛏 Xavfsizlik yostiqchasi (Все автомобили Chevrolet equinox оснащены минимум 2 подушками безопасности и системами ABS и ESC (электронная система курсовой устойчивости).))</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗tahoe🚗")
async def get_damas_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/FHgh6pn")
    await message.answer("<b>🚚Yuk xona sig'imi (722 / 3480 L.)\n🕹 Uzatish qutisi (AT10)\n⚒🛠 Xavfsizlik(ABS)\n🛢 Yoqilg'i istemoli (17.9 / 9.6 L.)\n🛏 Xavfsizlik yostiqchasi (7)</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗trailblazer🚗")
async def get_damas_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/9htPTQP")
    await message.answer("<b>🚚Yuk xona sig'imi (1830l)\n🕹 Uzatish qutisi (AT6)\n⚒🛠 Xavfsizlik(ABS)\n🛢 Yoqilg'i istemoli (9.7L)\n🛏 Xavfsizlik yostiqchasi (6)</b>", parse_mode="html", reply_markup=markup)

@dp.message_handler(text="🚗traverse🚗")
async def get_damas_info(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/ZTyCvy2")
    await message.answer("<b>🚚Yuk xona sig'imi (651 / 2781 L.)\n🕹 Uzatish qutisi (AT9)\n⚒🛠 Xavfsizlik(ABS)\n🛢 Yoqilg'i istemoli (13.6/7.8)\n🛏 Xavfsizlik yostiqchasi (6)</b>", parse_mode="html", reply_markup=markup)
@dp.message_handler(text="📞 Kanal Admini bilan bog'lanish")
async  def get_admin_info(message: types.Message):
    await message.answer("<i>📞 Telefon raqam va 📍 Joylashuvni jo'nating</i>",parse_mode="html", reply_markup=order)
# @dp.message_handler()

@dp.message_handler(text="🚘 Online sotish")
async def get_sotish(message: types.Message):
    await message.answer("<b>🚗Moshinangizni nomini kiriting!</b>", parse_mode="html")
    await AUTOINFO.title.set()

@dp.message_handler(state=AUTOINFO.title)
async def get_auto_title(message: types.Message, state: FSMContext):
    title = message.text
    await state.update_data({"title": title})
    await message.answer("<i>🚗Moshinangizni ishlab chiqarilgan yilini kiriting (Masalan: 2020)</i>", parse_mode="html")
    await AUTOINFO.next()

@dp.message_handler(lambda message: message.text.isdigit(),state=AUTOINFO.year)
async def get_auto_year(message: types.Message, state: FSMContext):
    year = message.text
    await state.update_data({"year": year})
    await message.answer("<i>🚗Moshinangizni rangini kiriting</i>", parse_mode="html", reply_markup=colors)
    await AUTOINFO.next()

@dp.callback_query_handler(state=AUTOINFO.color)
async def get_auto_color(call: types.CallbackQuery, state: FSMContext):
    color=call.data
    await state.update_data({"color": color})
    await call.answer(text=f"🌈{color.title()} rangini tanladingiz!")
    await call.message.delete()
    await call.message.answer("🚗 Moshinangizni bosib o'tgan masofasini kiriting!(km)")
    await AUTOINFO.probeg.set()

@dp.message_handler(lambda message: message.text.isdigit(),state=AUTOINFO.probeg)
async def get_auto_probeg(message: types.Message, state: FSMContext):
    probeg = message.text
    await state.update_data({"probeg": probeg} )
    await message.answer("<i>🚗Moshinangizni rasmini jo'nating kiriting</i>", parse_mode="html",)
    await AUTOINFO.image.set()
@dp.message_handler(content_types=["photo"], state=AUTOINFO.image)
async def get_auto_photo(message: types.Message, state: FSMContext):
    photo_id=message.photo[-1].file_id
    await state.update_data({"photo": photo_id})
    await message.answer("📞 Bog'lanish uchun raqamni jo'nating!", reply_markup=contact)
    await AUTOINFO.next()

@dp.message_handler(state=AUTOINFO.phone)
@dp.message_handler(content_types=["contact"], state=AUTOINFO.phone)
async def get_auto_info(message: types.Message, state: FSMContext):
    if message.text:
        phone = message.text
    else:
        phone = message.contact.phone_number
    await state.update_data({"phone": phone})
    await message.answer("🚗 Moshinangizni narxini kiriting ($)", reply_markup = ReplyKeyboardRemove())
    await AUTOINFO.price.set()
@dp.message_handler(lambda message: message.text.isdigit(), state=AUTOINFO.price)
async def get_auto_price(message: types.Message, state: FSMContext):
    price = message.text
    await state.update_data({"price": price})
    data = await state.get_data()
    msg = f"<b>🚗 Moshinangiz ma'lumotlari</b>\n\n{data.get('title')}\n🚗<b>Yili:</b> {data.get('year')}\n🌈<b>Rangi:</b> {data.get('color')}\n<b>🏇Probeg:</b> {data.get('probeg')}\n☎️<b>Telefon raqam:</b>{data.get('phone')}\n🟢<b>Telegram:</b> @{message.from_user.username}\n\n💵<b> Moshina narxi:</b> {data.get('price')}$"
    await message.answer_photo(photo=data.get('photo'),caption=msg, parse_mode='html', reply_markup=m_markup)
    await AUTOINFO.confrim.set()

@dp.callback_query_handler(state=AUTOINFO.confrim, text="NO")
async  def delete_data(call: types.callback_query, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Menyulardan birini tanlang", reply_markup= markup)
    await state.finish()
@dp.callback_query_handler(state=AUTOINFO.confrim, text="YES")
async  def send_to_admin(call: types.callback_query, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer("📧 Adminga xabar jo'natildi.", show_alert=True)
    await call.message.send_copy(chat_id=ADMINS[0])
    await state.finish()
    await call.message.answer("Menyulardan birini tanlang", reply_markup=markup)









if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
