from os import environ
from flask import Flask
from flask import render_template, request
import json
import requests

app=Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/pushBack", methods=['GET','POST'])
def pushBack():
    Id = request.args.get('Id')
    postData = {
        'D_B_DUNS_Number__c':'00000000000'
    }
    data = get_user_access_token()
    Headers = {
    'Authorization': 'Bearer '+ data['access_token'],
    'Content-Type': 'application/json',
    }
    url = data['instance_url']+'/services/data/v44.0/sobjects/Contact/'+Id
    res = requests.patch(url=url, headers=Headers, data=json.dumps(postData))
    print(res.text)
    return 'Success'

@app.route("/returnContactDataset", methods=['GET','POST'])
def returnContactDataset():
    data    = get_user_access_token()
    query   = '{"operation":"query", "object":"Contact", "contentType": "CSV"}'
    url     = data['instance_url']+'/services/data/v44.0/query/?q=SELECT+Id,+Name,+Account.Name,+email+FROM+Contact'
    headers = {
    'Authorization': 'Bearer '+ data['access_token'],
    'Content-Type': 'application/json',
    } 

    res = requests.get(url=url,headers=headers)
    jdata = json.loads(res.text) 
    print(jdata)
    return render_template('index.html', data=jdata['records'])



@app.route("/get_connected_app_url", methods=['GET', 'POST'])
def get_connected_app_url():
    baseUrl         = 'https://login.salesforce.com/services/oauth2/authorize?response_type=code&client_id='
    client_id       = '3MVG9Nk1FpUrSQHdvT4riecoT54Pk47hzzVP.WtBJaJ.8tZopDWsIuk12p45lTdtLfB8WaBIt_BTA4g78kvjS&client_secret='
    client_secret   = '8C059382F620317BE631CFE64E7B5598B927801A04C0F105686351BFE882832A'
    params          = '&scope=full refresh_token&redirect_uri=http://localhost:5000/getRefreshToken&prompt=login consent'
    url = baseUrl+client_id+client_secret+params
    return render_template('welcome_page.html', url=url)



@app.route("/getRefreshToken", methods=['GET', 'POST'])
def getRefreshToken():
    code =request.args.get('code')
    print(code)
    URL = 'https://login.salesforce.com/services/oauth2/token'
    PARAMS = {
    'client_id':'3MVG9Nk1FpUrSQHdvT4riecoT54Pk47hzzVP.WtBJaJ.8tZopDWsIuk12p45lTdtLfB8WaBIt_BTA4g78kvjS',
    'client_secret':'8C059382F620317BE631CFE64E7B5598B927801A04C0F105686351BFE882832A',
    'redirect_uri':'http://localhost:5000/getRefreshToken',
    'grant_type':'authorization_code',
    'code':code,
    }
    res = requests.post(url=URL, data=PARAMS)
    data= json.loads(res.text)
    print(data)
    return render_template('org_info.html')

def get_user_access_token():
    refresh_token = '5Aep861NT6Ju45T6F0B2wnoaRiqCqYAEh5omdrQnpwbKpvS_U2w58K4gznqoqkS_PGCL78c.i3IUEs7x0JjCInH'
    #Retrieve User Access Token
    URL = 'https://login.salesforce.com/services/oauth2/token'
    PARAMS = {
        'client_id':'3MVG9Nk1FpUrSQHdvT4riecoT54Pk47hzzVP.WtBJaJ.8tZopDWsIuk12p45lTdtLfB8WaBIt_BTA4g78kvjS',
        'client_secret':'8C059382F620317BE631CFE64E7B5598B927801A04C0F105686351BFE882832A',
        'grant_type':'refresh_token',
        'refresh_token':refresh_token
    }
    r = requests.post(url = URL, params = PARAMS)
    data = json.loads(r.text)
    return data