import configparser
parser = configparser.ConfigParser()
# parser.add_section('DB_CONFIGURATION')


# parser.set('DB_CONFIGURATION','apiKey', "AIzaSyCPeLozDHk6Sn2_KGlqZA_YWdrQQBTNNnc")
# parser.set('DB_CONFIGURATION','authDomain', "db-awelk.firebaseapp.com")
# parser.set('DB_CONFIGURATION','databaseURL', "https://db-awelk-default-rtdb.firebaseio.com")
# parser.set('DB_CONFIGURATION','projectId', "db-awelk")
# parser.set('DB_CONFIGURATION','storageBucket', "db-awelk.appspot.com")
# parser.set('DB_CONFIGURATION','messagingSenderId', "37231178359")
# parser.set('DB_CONFIGURATION','appId', "1:37231178359:web:b4e5fae6e61555dce7cc72")
# parser.set('DB_CONFIGURATION','measurementId', "G-VX1NF3YBG7")

# fp=open('DB.ini','w')
# parser.write(fp)
# fp.close()

section=parser.sections()
print(section)