"""
This module handles the email.message.Message list. For each element 
in the list contains several parts (header, body, attachments) 
"""

def not_multipart_parser(msg):
    body = ""
    payload = msg.get_payload(decode=True)
    if payload:
        body += payload.decode(errors="ignore")
    return body


def multipart_parser(msg):
    pass


"""
bu mesajin header kismi ascii disi karakter iceriyor ise mime 
encode eder ve bunu decode etmem lazim ama nasil yaparim bilmiyorum
"""
def parse_message_list(msg_list):

    messages_as_dict_list = []
    for msg in msg_list:   
        subject = msg["subject"] or "Empty"
        fromwho = msg["from"] or "Empty"
        date = msg["date"] or "Empty"
        to = msg["to"] or "Empty"

        if not msg.is_multipart():
            body = not_multipart_parser(msg)
        else:
            body = multipart_parser(msg)
        
        messages_as_dict_list.append({
            "subject": subject,
            "from": fromwho,
            "date": date,
            "to" : to,
            "body": body
        })
    
    return messages_as_dict_list
