from django.http import JsonResponse
from django.shortcuts import render
from . import AES as aes
import json


def index(request):
    body = json.loads(request.body)
    KEYS = [body["key"]]
    TEXTS = [body["message"]]
    for i in range(1):
        main_key = aes.translate_string_into_hex_str(KEYS[i])
        main_text = aes.translate_string_into_hex_str(TEXTS[i])
        round_keys = aes.find_all_round_keys(main_key)
        encrypt_text = aes.encrypt(main_text, round_keys)
        encrypt_text_str = aes.translate_hex_into_str(encrypt_text)
        decrypt_text = aes.decryption(encrypt_text, round_keys)
        resolved_text = aes.translate_hex_into_str(decrypt_text)

        print("Key : \'{}\'".format(KEYS[i]))
        print("Message Text : \'{}\'".format(TEXTS[i]))
        print("Length of Text :", len(TEXTS[i]))
        print("Encrypted Text :", encrypt_text)
        print("Encrypted Text :", encrypt_text_str)
        print("Length of Encrypted Text :", len(encrypt_text_str))
        print("decrypt text", decrypt_text)
        print("Resolved Text : \'{}\'".format(resolved_text))
        print("Length of Resolved Text :", len(resolved_text))
        dictionary = {
            "mainKey": main_key,
            "roundKey": round_keys,
            "encryptText": encrypt_text,
            "decryptText": decrypt_text,
            "resolveText": resolved_text
        }

    return JsonResponse({'result': dictionary})
