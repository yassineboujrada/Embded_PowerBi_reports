from pyrebase import pyrebase

config_db={
    'apiKey': "AIzaSyCPeLozDHk6Sn2_KGlqZA_YWdrQQBTNNnc",
    'authDomain': "db-awelk.firebaseapp.com",
    'databaseURL': "https://db-awelk-default-rtdb.firebaseio.com",
    'projectId': "db-awelk",
    'storageBucket': "db-awelk.appspot.com",
    'messagingSenderId': "37231178359",
    'appId': "1:37231178359:web:b4e5fae6e61555dce7cc72",
    'measurementId': "G-VX1NF3YBG7"
}

firebase=pyrebase.initialize_app(config_db)

db=firebase.database()
first_collection = {
    "gp2": {
        "emails": 'yassine.boujrada@gmail.com',
        "time": '9:35',
        "perids": '4 Day',
        "subject":"simple2_test",
        "file_path":"./files/US Sales Analysis.pdf",
        "name_of_reportBI":"US Sales Analysis"
    }
}
db.child('send_email_informations').push(first_collection)

user_collection={
    "user1":{
        "full_name":"yassine boujrada",
        "age":19,
        "email":'yassine.boujrada@gmail.com',
        "password":"yassine@2002"
    },
    "user2":{
        "full_name":"EL Mehdi Aich",
        "age":None,
        "email":'aich.mehdi@gmail.com',
        "password":"mehdi@2022"
    }
}
# db.child('User').push(user_collection)


#.order_by_child("email").equal_to("yassine.boujrada@gmail.com").limit_to_first(1).get()
# print(all_users.val())

# def search_about(collection,ref,indice):
#     all_data=db.child(collection).child(ref).get()
#     for data in all_data.each():
#         if data.val()['email'].lower()==indice.lower():
#             return data.val()
        
#         else:
#             return f'aucun resultat'