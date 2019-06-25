import json

import jenkins

class ControlJenkins(object):

    def __init__(self):
        self.server = jenkins.Jenkins("http://localhost:8080",
                                      username="diefrom",
                                      password="diefrom")

    def get_version(self):
        return self.server.get_version()

    def build_job(self, jobname, param=None):
        return self.server.build_job(jobname, param)

if __name__ == '__main__':
    data = {"countryCode": {"value": "86", "type": "string"},
            "email": {"value": "2508487675@qq.com", "type": "string"}}
    strdata = json.dumps(data, separators=(',', ':'))
    control_jenkins = ControlJenkins()
    param = {"env": "daily", "region": "daily", "user": "2508487675@qq.com",
             "api": "tuya.m.user.email.token.create", "v": "1.0", "data": strdata,
             "log": "info"}
    control_jenkins.build_job("tuya_type_check", param)
