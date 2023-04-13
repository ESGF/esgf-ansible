Log4J 1 to 2 Bridge Installation for esg-search
===============================================

This page documents the procedure for patching an instance of the latest esg-search webapp to use an up-to-date version of the Log4J library with the Log4J bridge.

1. Locate the JAR files for esg-search
--------------------------------------

The JAR files for the esg-search webapps are stored at a standard location on an ESGF index node. In preparation for the rest of the steps below, you will need to set the below environment variable to the webapp `lib` path::

    export LIB_PATH=/usr/local/tomcat/webapps/esg-search/WEB-INF/lib

2. Remove all Log4j jars and classes
------------------------------------

Log4J libraries are packaged into 3 different JARs in the esg-search `lib` directory. Before installation of new JARs, the old ones need to be removed::

    rm -f $LIB_PATH/log4j-1.2.17.jar
    zip $LIB_PATH/esgf-node-manager-accesslog-client-1.0.5.jar -d org/apache/log4j/\*
    zip $LIB_PATH/esgf-node-manager-connector-1.0.5.jar -d org/apache/log4j/\*

3. Install Log4j 1.x to 2.x jars
--------------------------------

Next, install the new Log4J libraries (api and core), as well as the 1 to 2 bridge, into the same `lib` folder::

    export JAR=log4j-1.2-api-2.20.0.jar && \
    curl https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-1.2-api/2.20.0/$JAR --output $LIB_PATH/$JAR && \
    echo "689151374756cb809cb029f2501015bdc7733179 *$LIB_PATH/$JAR" | sha1sum --strict --check

    export JAR=log4j-core-2.20.0.jar && \
    curl https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-core/2.20.0/$JAR --output $LIB_PATH/$JAR && \
    echo "eb2a9a47b1396e00b5eee1264296729a70565cc0 *$LIB_PATH/$JAR" | sha1sum --strict --check

    export JAR=log4j-api-2.20.0.jar && \
    curl https://repo1.maven.org/maven2/org/apache/logging/log4j/log4j-api/2.20.0/$JAR --output $LIB_PATH/$JAR && \
    echo "1fe6082e660daf07c689a89c94dc0f49c26b44bb *$LIB_PATH/$JAR" | sha1sum --strict --check

At this point, you can restart the node to ensure changes are being used::

    ansible-playbook -v -i hosts.test stop.yml start.yml status.yml
