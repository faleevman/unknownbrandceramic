from aiogram import types
import db
start_b = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_b.add(types.KeyboardButton(text="My info"),
                                types.KeyboardButton(text="Buy ADS"),
                                types.KeyboardButton(text="Help"))

start_s = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_s.add(types.KeyboardButton(text="My info"),
                                types.KeyboardButton(text="Add NFT"),
                                types.KeyboardButton(text="Help"))

role_select = types.ReplyKeyboardMarkup(resize_keyboard=True)
role_select.add(types.KeyboardButton(text="Buyer"),
                                types.KeyboardButton(text="Seller"))

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(types.KeyboardButton(text="Назад"))


def get_nft(nid):
    buy = types.InlineKeyboardMarkup()
    buy.add(types.InlineKeyboardButton('🤑Buy here!', callback_data='buy_{}'.format(nid)))
    print(nid)
    return buy

def rent(nid):
    buy = types.InlineKeyboardMarkup()
    buy.add(types.InlineKeyboardButton('🗓1 day', callback_data='rent_1_{}'.format(nid)))
    buy.add(types.InlineKeyboardButton('📆2 days', callback_data='rent_2_{}'.format(nid)))
    buy.add(types.InlineKeyboardButton('🗓3 days', callback_data='rent_3_{}'.format(nid)))
    buy.add(types.InlineKeyboardButton('🗓7 days', callback_data='rent_7_{}'.format(nid)))
    buy.add(types.InlineKeyboardButton('🗓1 month', callback_data='rent_30_{}'.format(nid)))
    buy.add(types.InlineKeyboardButton('🍁1 year', callback_data='rent_365_{}'.format(nid)))
    return buy
