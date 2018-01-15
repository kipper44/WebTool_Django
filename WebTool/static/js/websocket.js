
g_WebSocket = null;
g_WebSocketOnOpen = null;
g_WebSocketOnClose = null;
g_WebSocketOnOnError = null;
g_WebSocketMonitorViewOnMessage = null;


function WebSocketInit(strUrl)
{
    if (g_WebSocket != null) {
        console.log("websocket not null");
        return;
    }
    console.log(strUrl);

    try
    {
        g_WebSocket = new WebSocket(strUrl);
    }
    catch(e)
    {
        console.log(e);
        if (g_WebSocketOnOnError != null) g_WebSocketOnOnError();
        return;
    }
    g_WebSocket.onopen = function (e) {
        if (g_WebSocketOnOpen != null) g_WebSocketOnOpen();
    };

    g_WebSocket.onmessage = function (e) {
        //console.log(e.data);
        var cPacket = JSON.parse(e.data);

        switch(cPacket.protocol)
        {
            case 9:
            case 10:
                if (g_WebSocketMonitorViewOnMessage != null) g_WebSocketMonitorViewOnMessage(cPacket);
                break;
            default:
                console.log("INVAILD PACKET :" + e.data);
        }

    };

    g_WebSocket.onerror = function (e) {
        //console.log("disconnect111111");
        if (g_WebSocketOnOnError != null) g_WebSocketOnOnError();
    };

    g_WebSocket.onclose = function (e) {
        //console.log(g_WebSocketOnClose);
        if (g_WebSocketOnClose != null) g_WebSocketOnClose();
    };
}
function WebSocketTryReConnect() {
    if (g_WebSocket != null && g_WebSocket.readyState == WebSocket.CLOSED)
    {
        var strUrl = g_WebSocket.url;
        g_WebSocket = null;
        WebSocketInit(strUrl);
    }
}


function WebSocketSetOpen( funcOpen)
{
    g_WebSocketOnOpen = funcOpen;
}

function WebSocketSetError(funcError) {
    g_WebSocketOnOnError = funcError;
}
function WebSocketSetClose(funcOnClose) {
    g_WebSocketOnClose = funcOnClose;
}
function WebSocketSend(strMessage) {
    if (g_WebSocket == null || WebSocket.OPEN != g_WebSocket.readyState)
    {
        console.log(strMessage);
        return false;
    }
    g_WebSocket.send(strMessage);
    return true;
}

function WebSocketClose()
{
    if (g_WebSocket != null) g_WebSocket.close();
}

function WebSocketSetOnMessageMonitor(funcOnMessage) {
    g_WebSocketMonitorViewOnMessage = funcOnMessage;
}

function SendUpdateServerData(nDataFlag)
{
    var cSend = {
        protocol: 11,
        udpate_flag: nDataFlag
    };
    var msg = JSON.stringify(cSend);
    WebSocketSend(msg);
}