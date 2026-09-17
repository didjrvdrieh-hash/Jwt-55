from flask import Flask, request, jsonify
import requests
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import urllib3

import MajoRLoGinrEq_pb2

urllib3.disable_warnings()

app = Flask(__name__)

AES_KEY = b'Yg&tc%DEuh6%Zc^8'
AES_IV = b'6oyZDr22E3ychjM%'

Hr = {
    'User-Agent': "UnityPlayer/2018.4.12f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "deflate, gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-GA-SV': "1789535859",
    'X-Unity-Version': "2018.4.12f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB55",
    'Host': "loginbp.ppmainecoonghj.com",
}


def encrypted_proto(data_bytes):
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
    return cipher.encrypt(pad(data_bytes, AES.block_size))


def EncRypTMajoRLoGin(open_id, access_token, platform_id):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = platform_id
    major_login.client_version = "1.132.3"
    major_login.system_software = "Android OS 15 / API-35 (AP3A.240905.015.A2/180019)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1600
    major_login.screen_height = 720
    major_login.screen_dpi = "247"
    major_login.processor_details = "ARM64 FP ASIMD AES | 1820 | 8"
    major_login.memory = 2798
    major_login.gpu_renderer = "Mali-G57"
    major_login.gpu_version = "OpenGL ES 3.2"
    major_login.unique_device_id = "Google|f744e396-5694-4e65-995d-97a958f2bd1f"
    major_login.client_ip = "102.156.188.156"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "3"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 49973
    major_login.external_storage_available = 3720
    major_login.internal_storage_total = 854
    major_login.internal_storage_available = 3848
    major_login.game_disk_storage_available = 49973
    major_login.game_disk_storage_total = 3848
    major_login.external_sdcard_avail_storage = 49973
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 2
    major_login.library_path = "/data/app/~~eSPQu--bhSQDx0qVSCantw==/com.dts.freefireth-vZx-FXAnMdmzzvXGsuWZyw==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "1f74b435e72dfb267bce75a21d10074a|/data/app/~~eSPQu--bhSQDx0qVSCantw==/com.dts.freefireth-vZx-FXAnMdmzzvXGsuWZyw==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019121040"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 8191
    major_login.login_open_id_type = 3
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 14877
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTw/Pu89bWLI8IrlnJmIiCY6YqpSbCBdWNnQDYxboZ7JeQcOVP5M6uEbk+DUIl9ktJRhEFg6NjoW9Tvl1ZAh6R/8="
    major_login.android_engine_init_flag = 111207
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return encrypted_proto(string)


def MajorLogin(payload):
    url = "https://loginbp.ppmainecoonghj.com/MajorLogin"
    r = requests.post(url, data=payload, headers=Hr, verify=False, timeout=10)
    if r.status_code == 200:
        return r.content
    return None


@app.route('/token', methods=['GET'])
def get_token():
    uid = request.args.get('uid')
    password = request.args.get('password')

    if not uid or not password:
        return jsonify({"error": "uid and password"}), 400

    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": "UnityPlayer/2018.4.12f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "deflate, gzip",
        "Connection": "Keep-Alive",
        "X-GA-SV": "1789535859",
        "X-Unity-Version": "2018.4.12f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB55"
    }

    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }

    try:
        r = requests.post(url, headers=headers, data=data, verify=False, timeout=10)
        if r.status_code != 200:
            return jsonify({"error": f"fuck you server"}), 500

        result = r.json()
        open_id = result.get('open_id', '')
        access_token = result.get('access_token', '')

        if not open_id or not access_token:
            return jsonify({"error": "token: null"}), 500

        platform_id = 2
        payload = EncRypTMajoRLoGin(open_id, access_token, platform_id)
        r2 = MajorLogin(payload)

        if not r2 or len(r2) < 10:
            platform_id = 4
            payload = EncRypTMajoRLoGin(open_id, access_token, platform_id)
            r2 = MajorLogin(payload)

        if not r2 or len(r2) < 10:
            return jsonify({"error": "MajorLogin failed"}), 500

        text = r2.decode('utf-8', errors='ignore')
        start = text.find("eyJhbGciOiJIUzI1NiIsInN2ciI6IjEiLCJ0eXAiOiJKV1QifQ")
        if start != -1:
            token = text[start:]
            second_dot = token.find(".", token.find(".") + 1)
            jwt = token[:second_dot + 44]
            return jsonify({
                "token": jwt
            })

        return jsonify({"error": "token: null"}), 500

    except Exception as e:
        return jsonify({"error": f"mistake: {str(e)}"}), 500


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "usage": "GET /token?uid={uid}&password={password}"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2020)