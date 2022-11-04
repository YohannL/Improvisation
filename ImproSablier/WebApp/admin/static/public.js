
var API="http://192.168.1.34:5000/";
var LOOP= true;

let loopCond = true

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
