
var API="http://192.168.1.34:5000/";

class player {
    constructor(color, isPlaying, time, timeMax){
        this.color = color;
        this.isPlaying = isPlaying;
        this.time = time;
        this.timeMax = timeMax;
    }

};
let playerList = [];

window.onload = async function(){
    loop();
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function loop() {
    while(true){ //add a better confition
        // getPublicInfo();
        getPlayerInfo();
        await sleep(200);
    }
}

async function getPlayerInfo(){
    response = sendToApi('GET', API+"api/v1/player", false)
    if(response.status === 200){
        response= JSON.parse(response.response)
        console.log(response);
        
        playerList = []
        playerList.push(new player(response.playerList[0].color, response.playerList[0].isPlaying, response.playerList[0].time, response.playerList[0].timeMax))
        playerList.push(new player(response.playerList[1].color, response.playerList[1].isPlaying, response.playerList[1].time, response.playerList[1].timeMax))
        playerList.push(new player(response.playerList[2].color, response.playerList[2].isPlaying, response.playerList[2].time, response.playerList[2].timeMax))
        playerList.push(new player(response.playerList[3].color, response.playerList[3].isPlaying, response.playerList[3].time, response.playerList[3].timeMax))
        document.querySelector('#Red').innerText = playerList[0].time;
        document.querySelector('#Green').innerText = playerList[1].time;
        document.querySelector('#Blue').innerText = playerList[2].time;
        document.querySelector('#Yellow').innerText = playerList[3].time;
        console.log(playerList)

        // give to a manager
    }
}

function sendToApi(method,url){
    var request = new XMLHttpRequest();
    request.open(method, url , false);  // `false` makes the request synchronous
    try{
        request.send(null);
    }catch(error){
        return false;
    }

    if (request.status === 200) {
        return JSON.parse(request.responseText);
    }else{
        return false;
    }
    return request.responseText;
}
