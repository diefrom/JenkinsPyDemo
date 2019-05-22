import jenkins

class ControlJenkins(object):

    def __init__(self):
        self.server = jenkins.Jenkins("http://localhost:8080",
                                      username="diefrom",
                                      password="diefrom")

    def get_version(self):
        return self.server.get_version()

    def build_job(self, jobname):
        return self.server.build_job(jobname)

if __name__ == '__main__':
    control_jenkins = ControlJenkins()
    control_jenkins.build_job("demo")
