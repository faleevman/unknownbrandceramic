from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# импортируем классы Book и Base из файла database_setup.py
from database_setup import Users, NFT
from database_setup import Base
from pymongo import MongoClient
import pymongo
CONNECTION_STRING = "mongodb+srv://dbUser:dbPassword@cluster0.erlmt.mongodb.net"
engine = engine = create_engine("sqlite:///db.sqlite")
client = MongoClient(CONNECTION_STRING)
db = client['mydb']
collection = db['nft']
#rint(collection)

# чтобы декларативы могли получить доступ через экземпляр DBSession
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
def get_all_ads():
    return collection.find()
def add_user(uid, role,username): #++
    bookOne = Users(uid=uid, role=role, balance=0, username=username)
    session.add(bookOne)
    session.commit()

def add_balance_curr(uid,sum):
    u = session.query(Users).filter_by(uid=uid).first()
    print("Current balance", u.balance)
    newBalance = u.balance + sum
    u1 = engine.execute("UPDATE users SET balance={} WHERE uid={}".format(newBalance,uid))
    return u

def del_balance(uid,sum):
    u = session.query(Users).filter_by(uid=uid).first()
    print("-Current balance", u.balance)
    newBalance = u.balance - sum
    u1 = engine.execute("UPDATE users SET balance={} WHERE uid={}".format(newBalance,uid))
    return u


def add_balance(user_id,sum): #+
    u = engine.execute("UPDATE users SET balance={} WHERE uid={}".format(sum,user_id))
    #print(u)
    return u
def set_deal_status(deal_id,status): #+
    u = engine.execute("UPDATE deals SET status={} WHERE id={}".format(status,user_id))
    #print(u)
    return u


def set_role(uid,role): #+
    u = engine.execute("UPDATE users SET role={} WHERE uid={}".format(role,uid))
    #print(u)
    return u

def set_req(uid,req): #+
    u = engine.execute("UPDATE users SET req={} WHERE uid={}".format(req,uid))
    #print(u)
    return u

def add_cat(name): #++
    session.add(Cats(name=name))
    session.commit()

def add_service(cat,name,description,sellerID,sellerNickname): #++
    session.add(Services(name=name,cat=cat,description=description,sellerID=sellerID,sellerNickname=sellerNickname))
    session.commit()

def add_bill(sellerID,buyerID,amount,dataTime): #++
    a = session.add(Services(sellerID=sellerID,buyerID=buyerID,amount=amount,status=0,dataTime=dataTime))
    session.commit()
    u = engine.execute("SELECT * FROM bills WHERE sellerID={} AND buyerID={} AND amount={} AND dataTime={}".format(sellerID,buyerID,amount,dataTime))
    return u
# def add_subcat(catID, name): #++
#     session.add(Subcats(catID=catID, name=name))
#     session.commit()

def get_user(uid):
    print("All users")
    u = session.query(Users).filter_by(uid=uid).first()
    if u is not None:
        print(u.uid)
    return u

def get_service(name):
    print("Name is: {}".format(name))
    u = session.query(Services).filter_by(name=name).first()
    return u

def get_all_users(): #+
    print("All users")
    for us in session.query(Users).all():
        print(vars(us)['role'])
    return session.query(Users).all()

def get_services(cat):
    u = session.query(Services).filter_by(cat=cat).all()
    return u

def get_all_services():
    u = session.query(Services).all()
    return u


def get_cat(name):
    print("Cat")
    u = session.query(Cats).filter_by(name=name).first()
    return u.id

def get_all_cats(): #+
    return session.query(Cats).all()


def get_all_pictures(): #+
    print("All pictures")
    for us in session.query(Pictures).all():
        print(vars(us))
    return session.query(Pictures).all()



def move_user(user_id, picture_id): #+
    engine.execute("INSERT INTO movings(user_id, action_date, picture_id) VALUES ({}, NULL, {})".format(user_id,picture_id))
    session.commit()

def del_cat(name):
    #get all pictures objects in specifified exposition
    u = engine.execute("DELETE FROM cats WHERE name='{}'".format(name))
    return u

def del_service(name):
    #get all pictures objects in specifified exposition
    u = engine.execute("DELETE FROM services WHERE name='{}'".format(name))
    return u

def get_usr_count():
    u = engine.execute("SELECT COUNT(*) from users")
    return u.first()[0]

def get_admin_count():
    u = engine.execute("SELECT COUNT(*) from users WHERE role=1")
    return u.first()[0]

def get_deals_count():
    u = engine.execute("SELECT COUNT(*) from deals")
    return u.first()[0]

def get_refs_count(uid):
    u = engine.execute("SELECT COUNT(*) from users where whoMaster={}".format(uid))
    return u.first()[0]
