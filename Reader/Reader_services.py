import sys

class serviceInstances:
    serviceInstanceId = " "
    userName = ""
    partner = ""
    applicationName = ""
    type = ""
    status = ""
    servicePlan = ""
    spaceName = ""
    spaceGuid = ""
    serviceInstanceName = ""

    def __init__(self, serviceInstanceId, userName, partner, applicationName, type, status, servicePlan, spaceName, spaceGuid, serviceInstanceName):
        self.serviceInstanceId = serviceInstanceId
        self.userName = userName
        self.partner = partner
        self.applicationName = applicationName
        self.type = type
        self.status = status
        self.servicePlan = servicePlan
        self.spaceName = spaceName
        self.spaceGuid = spaceGuid
        self.serviceInstanceName = serviceInstanceName

    def toString(self):
        print ("%s %s %s %s %s") % (self.serviceInstanceId, self.userName, self.applicationName, self.type, self.status)


list_pivotal = []
fp = open('pivotal_active_services_lite.csv', 'r')
for line in fp:
    list_pivotal.append(line.strip().split(','))

serviceInstanceListPivotal = []
for element in list_pivotal:
    serviceInstance = serviceInstances(element[5],'','',element[0], '', '', element[1],element[2],element[3],element[4])
    serviceInstanceListPivotal.append(serviceInstance)


list_appdirect = []
fad = open('appdirect_active_services_lite.csv','r')
for line in fad:
    list_appdirect.append(line.strip().split(','))

serviceInstanceListAppdirect = []
for element in list_appdirect:
    serviceInstance = serviceInstances(element[0],element[1],element[2],element[3], element[4], element[5], '','','','')
    serviceInstanceListAppdirect.append(serviceInstance)

reportOutput = []

sys.stdout.write("Start Job: ")
sys.stdout.flush()

for servInstancePivotal in serviceInstanceListPivotal:
    for i, servInstanceAppdirect in enumerate(serviceInstanceListAppdirect):
        if servInstancePivotal.serviceInstanceId == servInstanceAppdirect.serviceInstanceId:
            reportOutput.append(("Space: %s,"
                                 "Service name in Pivotal: %s,"
                                 "Service name in Appdirect: %s,"
                                 "Service/Plan: %s,"
                                 "Type: %s,"
                                 "Service Instance: %s,"
                                 "Status on AD: %s")
                                % (servInstancePivotal.spaceGuid,
                                   servInstancePivotal.applicationName,
                                   servInstanceAppdirect.applicationName,
                                   servInstancePivotal.servicePlan,
                                   servInstanceAppdirect.type,
                                   servInstancePivotal.serviceInstanceId,
                                   servInstanceAppdirect.status))
            break
    else:
        reportOutput.append(("Space: %s,"
                             "Service name in Pivotal: %s,"
                             "Service name in Appdirect: %s,"
                             "Service/Plan: %s,"
                             "Type: %s,"
                             "Service Instance: %s,"
                             "Status on AD: %s,")
                            % (servInstancePivotal.spaceGuid,
                               servInstancePivotal.applicationName,
                               '',
                               servInstancePivotal.servicePlan,
                               '',
                               servInstancePivotal.serviceInstanceId,
                               'NOT PRESENT IN APPDIRECT'))
sys.stdout.write("DONE"+"\n")
sys.stdout.flush()

thefile = open('example_output.csv', 'w')
for item in reportOutput:
  thefile.write("%s\n" % item)
thefile.close();
