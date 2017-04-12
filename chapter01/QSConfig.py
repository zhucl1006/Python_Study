import urllib
import urllib2
import json


class QSConfig(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        self.tokenIdStr = QSConfig.logIn_To_QS("http://192.168.10.132:12821/ecp","adm/apply","user","111111");
        self.logger.debug("getTokenID %s", self.tokenId)
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
    
    def logIn_To_QS(QSIPUrl,ConfigPath,UserNmae,UserPass):
        url = QSIPUrl.rstrip('/').rstrip('\\') + '/openapi/' + ConfigPath
        data = {};
        data["loginName"] = UserNmae
        data["password"] = UserPass
        data["language"] ="en"
     
        # values = {"auth":{"passwordCredentials":{"username":"alan","password":"admin"},"tenantName":"swifttenant1"}}
        params = json.dumps(data)
        print params
        print url
        headers = {"Content-type":"application/json","Accept": "application/json"}
        req = urllib2.Request(url, params, headers)
        response = urllib2.urlopen(req)
        returnStr = response.read()
        print returnStr ,type(returnStr)
        rData = json.loads(returnStr)
        return rData["tokenId"];