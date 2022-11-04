
var API="http://192.168.1.34:5000/";
var LOOP= true;

let loopCond = true
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
        if(loopCond){
            getPublicSize()
            getPlayerInfo()
            await sleep(500)
        }else{
            await sleep(1000)
        }
    }
}

async function getPublicSize(){
    response = sendToApi('GET', API+"api/v1/admin/publicsize", false)    
    newTxt= [ 'Nombre de personnes connectées: ', JSON.parse(response.response)]
    document.querySelector('#Public_Size').innerText = "".concat(...newTxt);
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
        console.log(playerList)
        // give to a manager

        for (let i = 0; i < 4; i++) {
            switch(playerList[i].color){
                case "BLUE":
                    if(!playerList[i].isPlaying){
                        document.querySelector('#ButtonBlueOn').style.background = "#000088";
                        document.querySelector('#ButtonBlueOff').style.background = "#0000ff";
                    }else{
                        document.querySelector('#ButtonBlueOn').style.background = "#0000ff";
                        document.querySelector('#ButtonBlueOff').style.background = "#000088";
                    }
                    break;
                case "RED":
                    if(!playerList[i].isPlaying){
                        document.querySelector('#ButtonRedOn').style.background = "#880000";
                        document.querySelector('#ButtonRedOff').style.background = "#ff0000";
                    }else{
                        document.querySelector('#ButtonRedOn').style.background = "#ff0000";
                        document.querySelector('#ButtonRedOff').style.background = "#880000";
                    }
                    break;
                case "GREEN":
                    if(!playerList[i].isPlaying){
                        document.querySelector('#ButtonGreenOn').style.background = "#008800";
                        document.querySelector('#ButtonGreenOff').style.background = "#00ff00";
                    }else{
                        document.querySelector('#ButtonGreenOn').style.background = "#00ff00";
                        document.querySelector('#ButtonGreenOff').style.background = "#008800";
                    }
                    break;
                case "YELLOW":
                    if(!playerList[i].isPlaying){
                        document.querySelector('#ButtonYellowOn').style.background = "#b37400";
                        document.querySelector('#ButtonYellowOff').style.background = "#ffa500";
                    }else{
                        document.querySelector('#ButtonYellowOn').style.background = "#ffa500";
                        document.querySelector('#ButtonYellowOff').style.background = "#b37400";
                    }
                    break;
            }
      }

    }
}

async function start(){
    response = sendToApi('POST', API+"api/v1/admin/status/RUN", false)
    loopCond = false
}

async function pause(){
    response = sendToApi('POST', API+"api/v1/admin/status/PAUSE", false)
    loopCond = true
}

async function reset(){
    response = sendToApi('POST', API+"api/v1/admin/reset", false)
    loopCond = true
}

async function fullreset(){
    response = sendToApi('POST', API+"api/v1/admin/fullreset", false)
    loopCond = true
}

async function onRed(){
    response = sendToApi('POST', API+"api/v1/admin/timer/on/RED", false)
}
async function offRed(){
    response = sendToApi('POST', API+"api/v1/admin/timer/off/RED", false)
}
async function addRed(){
    response = sendToApi('POST', API+"api/v1/admin/timer/add/RED", false)
}
async function removeRed(){
    response = sendToApi('POST', API+"api/v1/admin/timer/remove/RED", false)
}

async function onGreen(){
    response = sendToApi('POST', API+"api/v1/admin/timer/on/GREEN", false)
}
async function offGreen(){
    response = sendToApi('POST', API+"api/v1/admin/timer/off/GREEN", false)
}
async function addGreen(){
    response = sendToApi('POST', API+"api/v1/admin/timer/add/GREEN", false)
}
async function removeGreen(){
    response = sendToApi('POST', API+"api/v1/admin/timer/remove/GREEN", false)
}

async function onBlue(){
    response = sendToApi('POST', API+"api/v1/admin/timer/on/BLUE", false)
}
async function offBlue(){
    response = sendToApi('POST', API+"api/v1/admin/timer/off/BLUE", false)
}
async function addBlue(){
    response = sendToApi('POST', API+"api/v1/admin/timer/add/BLUE", false)
}
async function removeBlue(){
    response = sendToApi('POST', API+"api/v1/admin/timer/remove/BLUE", false)
}

async function onYellow(){
    response = sendToApi('POST', API+"api/v1/admin/timer/on/YELLOW", false)
}
async function offYellow(){
    response = sendToApi('POST', API+"api/v1/admin/timer/off/YELLOW", false)
}
async function addYellow(){
    response = sendToApi('POST', API+"api/v1/admin/timer/add/YELLOW", false)
}
async function removeYellow(){
    response = sendToApi('POST', API+"api/v1/admin/timer/remove/YELLOW", false)
}

//  response = sendToApi('GET', API+"api/v1/player", false)
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
