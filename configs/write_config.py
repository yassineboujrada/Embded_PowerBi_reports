import configparser

config = configparser.ConfigParser()

# Add the structure to the file we will create
config.add_section('power_bi_config')

config.set('power_bi_config', 'client_id', "fd664596-cbb4-4445-a416-f4fa587146de")
config.set('power_bi_config', 'client_secret', 'VCF8Q~v~a.eXt1v3hr_~_nnTyqsXY2Jwy.Ryyb9l')
config.set('power_bi_config', 'redirect_uri', 'https://localhost/redirect')

# Write the new structure to the new file
with open('configs/config.ini', 'w') as configfile:
    config.write(configfile)