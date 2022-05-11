# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:37:35 2022

@author: bruno.andriolli
"""

def tel(msg):
    import requests
    
    token = '5381545226:AAGaJoY06wOxLe7B4qnZell8FP6mz9caAR8'
    msg = msg
    # mostra o id do último grupo adicionado
    def last_chat_id(token):
        try:
            url = "https://api.telegram.org/bot{}/getUpdates".format(token)
            response = requests.get(url)
            if response.status_code == 200:
                json_msg = response.json()
                for json_result in reversed(json_msg['result']):
                    message_keys = json_result['message'].keys()
                    if ('new_chat_member' in message_keys) or ('group_chat_created' in message_keys):
                        return json_result['message']['chat']['id']
                print('Nenhum grupo encontrado')
            else:
                print('A resposta falhou, código de status: {}'.format(response.status_code))
        except Exception as e:
            print("Erro no getUpdates:", e)
            
    
    chat_id = last_chat_id(token)
    
    
    def send_message(token, chat_id, message):
        try:
            data = {"chat_id": chat_id, "text": msg}
            url = "https://api.telegram.org/bot{}/sendMessage".format(token)
            requests.post(url, data)
        except Exception as e:
            print("Erro no sendMessage:", e)
    
    send_message(token, chat_id, msg)