from Queue import Queue


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.arrs = [v1, v2]
        self.next_pointers = Queue()
        if v1:
            self.next_pointers.put((0, 0))
        if v2:
            self.next_pointers.put((1, 0))

    def next(self):
        """
        :rtype: int
        """
        arr_index, ele_index = self.next_pointers.get()
        if ele_index + 1 < len(self.arrs[arr_index]):
            self.next_pointers.put((arr_index, ele_index + 1))
        return self.arrs[arr_index][ele_index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_pointers.qsize() > 0


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
true = True
false = False
null = None
d = {
    "server-maxThreads": 100,
    "server-applicationConnectors[0]-type": "http",
    "server-applicationConnectors[0]-port": 25290,
    "server-adminConnectors[0]-type": "http",
    "server-adminConnectors[0]-port": 25291,
    "server-requestLog-appenders[0]-type": "file",
    "server-requestLog-appenders[0]-currentLogFilename": "/tmp/access.log",
    "server-requestLog-appenders[0]-threshold": "ALL",
    "server-requestLog-appenders[0]-archive": true,
    "server-requestLog-appenders[0]-archivedLogFilenamePattern": "/tmp/access.%d.log.gz",
    "server-requestLog-appenders[0]-archivedFileCount": 7,
    "server-requestLog-appenders[0]-logFormat": "%h %t %r %i{X-Web-Host} %i{X-Request-ID} %I %s %b %D",
    "logging-level": "INFO",
    "logging-loggers-org.hibernate.engine.internal.StatisticalLoggingSessionEventListener": "OFF",
    "logging-appenders[0]-type": "console",
    "logging-appenders[0]-threshold": "INFO",
    "logging-appenders[1]-type": "file",
    "logging-appenders[1]-threshold": "INFO",
    "logging-appenders[1]-currentLogFilename": "/tmp/service.log",
    "logging-appenders[1]-archivedLogFilenamePattern": "/tmp/service-%i.log.gz",
    "logging-appenders[1]-archivedFileCount": 40,
    "logging-appenders[1]-timeZone": "Asia/Kolkata",
    "logging-appenders[1]-maxFileSize": "500MB",
    "database-driverClass": "com.mysql.jdbc.Driver",
    "database-user": "root",
    "database-password": null,
    "database-url": "jdbc:mysql://_MYSQL_HOST_/final_hudson?zeroDateTimeBehavior=convertToNull&autoReconnect=true",
    "database-properties-charSet": "UTF-8",
    "database-properties-hibernate.generate_statistics": false,
    "database-properties-hibernate.session.events.log": false,
    "database-properties-hibernate.show_sql": false,
    "database-properties-hibernate.format_sql": false,
    "database-maxWaitForConnection": "1s",
    "database-validationQuery": "/* MyService Health Check */ SELECT 1",
    "database-initialSize": 2,
    "database-minSize": 2,
    "database-maxSize": 10,
    "database-checkConnectionWhileIdle": true,
    "database-validationInterval": "10s",
    "database-minIdleTime": "1 minute",
    "mysqlHosts": "localhost",
    "bucketName": "hudson-development",
    "rateLimitCount": 2000,
    "deepPageHardCount": 2000,
    "cbOpsTimeOut": 10000,
    "falconConfiguration-falconCorePoolSize": 50,
    "falconConfiguration-falconMaxPoolSize": 200,
    "falconConfiguration-falconKeepAliveTime": 20000,
    "gapServiceConfiguration-host": "10.47.1.125",
    "gapServiceConfiguration-port": 80,
    "gapServiceConfiguration-whitelistedGapTopStores[0]": "2oq",
    "gapServiceConfiguration-whitelistedGapTopStores[1]": "search.flipkart.com",
    "pinCodeServiceConfiguration-host": "10.47.1.31",
    "pinCodeServiceConfiguration-port": 80,
    "pinCodeServiceConfiguration-maximumCacheSize": 30000,
    "pinCodeServiceConfiguration-cacheTtlInSecs": 86400,
    "bzServiceConfiguration-host": "10.47.6.191",
    "bzServiceConfiguration-port": 80,
    "bzServiceConfiguration-guavaCacheRefreshAfterWrite": 10,
    "bzServiceConfiguration-guavaCacheExpireAfterWrite": 15,
    "bzServiceConfiguration-guavaCacheReloadThreadPoolSize": 2,
    "abServiceConfiguration-endPoint": "10.47.0.146",
    "abServiceConfiguration-clientName": "Mapi.sherlock",
    "abServiceConfiguration-continueWithoutABOnFailure": false,
    "abServiceConfiguration-configuredLayers[0]": "search-ranking",
    "abServiceConfiguration-configuredLayers[1]": "sherlock-matching",
    "abServiceConfiguration-configuredLayers[2]": "sherlock-autosuggest",
    "abServiceConfiguration-configuredLayers[3]": "sherlock-experience",
    "redirectionServiceConfiguration-host": "10.47.7.117",
    "redirectionServiceConfiguration-port": 80
}

d1 = {}
for k, v in d.items():
    if '[' in k:
        major = k.split('[', 1)[0]
        # print k, k.split('[', 1)[1].split(']', 1)
        if k.split('[', 1)[1].split(']', 1)[1]:

            d1.setdefault(major, [])
            #     .append(k.split('[', 1)[1].split(']', 1)[1][1:], v)
            pos = int(k.split('[', 1)[1].split(']', 1)[0])
            while len(d1[major]) < pos + 1:
                d1[major].append({})
            print major, pos, d1[major][pos], k.split('[', 1)[1].split(']', 1)[1][1:], v
            d1[major][pos][k.split('[', 1)[1].split(']', 1)[1][1:]] = v

        else:
            print 'list', major
            d1.setdefault(major, []).append(v)
    else:
        d1.setdefault(k, v)
