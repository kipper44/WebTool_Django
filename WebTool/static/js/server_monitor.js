    var myVar = setInterval(function () { RefreshTimer(); }, 4000);

    function OnMessage(cPacket)
    {
    console.log("socket message");
        switch( cPacket.protocol)
        {
            case 9:
                {
                    vServerMonitor.servers = cPacket.monitor_servers;
                }
                break;
            case 10:
                if (cPacket.ret == false) alert(cPacket.msg);
                break;
            default:
                console.log("INVAILD PACKET :" + cPacket);
        }
    }
   $(window).load(function () {
        WebSocketSetOnMessageMonitor(OnMessage);
      });
    $(window).unload(function () {
    });

    function RefreshTimer() {
        var cSend = {
            protocol: 8
        };
        var msg = JSON.stringify(cSend);
        WebSocketSend(msg);
     }

    function SendAction(ActionNum)
    {
        var cSend = {
            protocol: ActionNum
        };
        var msg = JSON.stringify(cSend);
        WebSocketSend(msg);
    }