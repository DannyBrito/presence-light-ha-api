import os
from typing import Optional
from requests import post
from fastapi import FastAPI

app = FastAPI()

ha_ip = os.environ['HA_IP']
ha_port = os.environ['HA_PORT']
ha_entity = os.environ['HA_ENTITY']
ha_token = os.environ['HA_TOKEN']
ha_domain = ha_entity.split('.')[0]


base_url = str("http://" + ha_ip + ":" + ha_port + "/api/services/" + ha_domain + "/")
headers = {
    "Authorization": str("Bearer " + ha_token),
    "Content-Type": "application/json"
}

def payload(option):
    payload = {
        "option": option,
        "entity_id": ha_entity
    }
    return payload

@app.post("/available")
def available():
    url = base_url + "select_option"
    post(url, headers=headers, json=payload("available"))
    
@app.post("/busy")
def busy():
    url = base_url + "select_option"
    post(url, headers=headers, json=payload("busy"))

@app.post("/away")
def away():
    url = base_url + "select_option"
    post(url, headers=headers, json=payload("away"))

@app.post("/offline")
def offline():
    url = base_url + "select_option"
    post(url, headers=headers, json=payload("offline"))

@app.post("/active_available")
def active_available():
    url = base_url + "select_option"
    post(url, headers=headers, json=payload("active_available"))