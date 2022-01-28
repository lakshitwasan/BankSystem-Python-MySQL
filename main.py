import PySimpleGUI as sg
import mysql.connector
import yaml

server_config_yaml_file = open('ServerInfo.yaml', 'r')
server_config = yaml.load(server_config_yaml_file, Loader = yaml.FullLoader)

mysql_connect = mysql.connector.connect(user = server_config['user'],
                                       password = server_config['password'],
                                       host = server_config['host'])
