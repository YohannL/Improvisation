
var API="http://192.168.1.34:5001/";
var ID;
var PUBLIC_REDTIME_TOADD;
var PUBLIC_BLUETIME_TOADD;
var PUBLIC_GREENTIME_TOADD;
var PUBLIC_YELLOWTIME_TOADD;

class player {
    constructor(color, isPlaying, time, timeMax){
        this.color = color;
        this.isPlaying = isPlaying;
        this.time = time;
        this.timeMax = timeMax;
    }

};
let playerList = [];

function connect(){
    isConnected = requestToApi_Connect();
    if ( isConnected == true){
        
        document.querySelector('#ButtonConnect').innerText = 'Connected';
        // document.querySelector('#Row1').hei = 'Connected';

        const elRed = document.getElementById("Red");
        elRed.addEventListener("click", redHandler, false);

        const elBlue = document.getElementById("Blue");
        elBlue.addEventListener("click", blueHandler, false);

        const elGreen = document.getElementById("Green");
        elGreen.addEventListener("click", greenHandler, false);

        const elYellow = document.getElementById("Yellow");
        elYellow.addEventListener("click", yellowHandler, false);

        getPublicInfo();
        // launch the loop
        loop();
    }
}
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function loop() {
    while(true){ //add a better confition
        // getPublicInfo();
        getPlayerInfo();
        await sleep(1000);
    }
}

function requestToApi_Connect(){
    // Verification if we can connect to the API and get the ID of the public
    data = sendToApi('POST', API+"api/v1/public/", false)
    if ( data == false )
        return false;

    ID = data.id;
    return true;
}

async function redHandler(){
    // Send time to RED player and get info the public
    useTime("RED");
    await sleep(100);
    getPublicInfo();
}
async function blueHandler(){
    // Send time to BLUE player and get info the public
    useTime("BLUE");
    await sleep(100);
    getPublicInfo();
}
async function greenHandler(){
    // Send time to GREEN player and get info the public
    useTime("GREEN");
    await sleep(100);
    getPublicInfo();
}
async function yellowHandler(){
    // Send time to YELLOW player and get info the public
    useTime("YELLOW");
    await sleep(100);
    getPublicInfo();
}

 

function useTime(color){
    return sendToApi('POST',API+"api/v1/public/"+ID+"/time/use/"+color);
}

function getPublicInfo(){
    response = sendToApi('GET', API+"api/v1/public/"+ID)
    if(response.status === 200){
        response= JSON.parse(response.response)
        PUBLIC_BLUETIME_TOADD = response._ColorTimeList.BLUE
        PUBLIC_REDTIME_TOADD = response._ColorTimeList.RED
        PUBLIC_YELLOWTIME_TOADD = response._ColorTimeList.YELLOW
        PUBLIC_GREENTIME_TOADD = response._ColorTimeList.GREEN
        document.querySelector('#Red').innerText = PUBLIC_REDTIME_TOADD;
        document.querySelector('#Green').innerText = PUBLIC_GREENTIME_TOADD;
        document.querySelector('#Blue').innerText = PUBLIC_BLUETIME_TOADD;
        document.querySelector('#Yellow').innerText = PUBLIC_YELLOWTIME_TOADD;

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
