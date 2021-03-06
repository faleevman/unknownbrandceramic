#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
import config as cfg
import strings as strs
import keyboards as kb
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import db
import ipfs
import uuid
from PIL import Image

#Unknown brand hackathon
class Start(StatesGroup):
    mainMenu = State()
    setRole = State()
    sendBanner = State()

bot = Bot(token=cfg.token)
dp = Dispatcher(bot,storage=MemoryStorage())


@dp.message_handler(state=Start.setRole)
async def user_set_role(message: types.Message):
    print(message.text)
    if message.text in ["Seller", "Buyer"]:
        if message.text == "Seller":
            print("Seller")
            db.add_user(message.chat.id, 0,message.from_user.username)
            await message.reply("Main menu",reply_markup=kb.start_s)
            await Start.mainMenu.set()
        elif message.text == "Buyer":
            db.add_user(message.chat.id, 1,message.from_user.username)
            await message.reply("Main menu",reply_markup=kb.start_b)
            await Start.mainMenu.set()
    else:
        await message.reply("Error!", reply_markup=kb.set_role)
        await Start.setRole.set()

@dp.message_handler(content_types='photo')
async def receive_banner(message: types.Message,state: FSMContext):
    state = dp.current_state(user=message.from_user.id)
    name = uuid.uuid4().hex
    await message.photo[-1].download(name + '.jpg')
    await state.update_data(name=name)
    user_data = await state.get_data()
    print(user_data)
    await bot.send_photo(chat_id=message.chat.id,photo=open(name + '.jpg', 'rb'), caption="Here is your banner👆")
    await message.reply("Processing banner...")
    imgName = uuid.uuid4().hex + ".png"
    im1 = Image.open('12345.png')
    im2 = Image.open(name + '.jpg')
    im1.paste(im2, (200, 70))
    im1.save(imgName, quality=95)
    h = open(imgName, 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=h, caption="final banner:")

@dp.callback_query_handler(lambda call: call.data and call.data.startswith('rent'))
async def set_rent_time(call: types.CallbackQuery,state: FSMContext):
    spt = call.data.split("_")
    await bot.send_message(call.message.chat.id, "Order for: {} days".format(spt[1]))
    await state.update_data(days=spt[1])
    await bot.send_message(call.message.chat.id, "Please send banner in reply message. ")

@dp.callback_query_handler(lambda call: call.data and call.data.startswith('buy'))
async def process_callback_kb1btn1(call: types.CallbackQuery,state: FSMContext):
    print(call.data)
    await bot.send_message(call.message.chat.id, "Processing query...")
    await state.update_data(nftID=call.data.split("_")[1])
    await bot.send_message(call.message.chat.id, "Enter rent period: ",reply_markup=kb.rent(call.data.split("_")[1]))

@dp.message_handler(state=Start.mainMenu)
async def main_menu(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    if message.text == "My info":
        await bot.send_photo(message.chat.id, photo=ipfs.get_ipfs("bafkreignwi7echwfdoo4t3okpv54fb7vy4pipteby3n5c3c2nh73ith25a"))
        usr = db.get_user(message.from_user.id)
        await message.answer("⌨️")
        if int(usr.role) == 0:
            print(usr.balance)
            await message.answer("""")
My info:
Role: {}
Balance: {} ETH
            """.format("Buyer", float(usr.balamce)))
        elif int(usr.role) == 1:
            await message.answer(""""
My info:
Role: {}
Balance: {} ETH
            """.format("Seller",float(usr.balance)))
            await message.reply("--------")
            await message.reply("Here, you can view your AD campaigns")

        #await message.answer(strs.invite_link.format(cfg.percent, cfg.botLink, message.chat.id))
    elif message.text == "Add NFT":
        await message.answer("Here you can add NFT")
    elif message.text == "Buy ADS":
        await message.answer("👇Here is a list of NFTs, where u can place your ads:👇")
        for i in db.get_all_ads():
            photo = ipfs.get_ipfs(i["image"].split("ipfs://")[1])
            hhh = open(photo, 'rb')
            await bot.send_photo(message.from_user.id,photo=hhh, caption=strs.nftPage.format(i["name"],i["author"],i["description"],i["pricePerDay"],i["pricePerPlace"]),reply_markup=kb.get_nft(i["nid"]))
        await state.reset_state()

        #now need to get nfts
    elif message.text == "Help":
        print("Help")
        await message.reply("Here will be a help page")


# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def parse_start(message: types.Message):
    try:
        usr = db.get_user(message.from_user.id)
        print(usr)
        if usr == None:
            await message.reply(strs.start)
            await message.answer(strs.select_role, reply_markup=kb.role_select)
            await Start.setRole.set()
        else:
            usr = db.get_user(message.from_user.id)
            if usr.role == 0:
                await message.reply("Seller menu",reply_markup=kb.start_s)
                await Start.mainMenu.set()
            elif usr.role == 1:
                await message.reply("Buyer menu",reply_markup=kb.start_b)
                await Start.mainMenu.set()

    except:
        usr = db.get_user(message.from_user.id)
        print("err")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
