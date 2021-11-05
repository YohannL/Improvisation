
var API="http://192.168.1.34:5001/";
var ID;


function connect(){
    isConnected = requestToApi_Connect();
    if ( isConnected == true){
        
        document.querySelector('#ButtonConnect').innerText = 'Connected';

        const elRed = document.getElementById("Red");
        elRed.addEventListener("click", redHandler, false);

        const elBlue = document.getElementById("Blue");
        elBlue.addEventListener("click", blueHandler, false);

        const elGreen = document.getElementById("Green");
        elGreen.addEventListener("click", greenHandler, false);

        const elYellow = document.getElementById("Yellow");
        elYellow.addEventListener("click", yellowHandler, false);
    }
}

function requestToApi_Connect(){
    
    var request = new XMLHttpRequest();
    request.open('POST', API+"api/v1/public/", false);  // `false` makes the request synchronous
    try{
        request.send(null);
    }catch(error){
        return false;
    }

    if (request.status === 200) {
        const data = JSON.parse(request.responseText);
        console.log(data.id);
        ID = data.id;
    }else{
        return false;
    }
    return true;
}

function redHandler(){
    // useTime("RED");
    response = getPlayerInfo();
    console.log("Reponse",JSON.parse(response.response));
}
function blueHandler(){
    useTime("BLUE");
}
function greenHandler(){
    useTime("GREEN");
}
function yellowHandler(){
    useTime("YELLOW");
}

 

function useTime(color){
    return sendToApi('POST',API+"api/v1/public/"+ID+"/time/use/"+color);
}

function getPlayerInfo(){
    return sendToApi('GET', API+"api/v1/player")
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
        console.log(200);
        return JSON.parse(request.responseText);
    }else{
        return false;
    }
    return request.responseText;
}


function loop(){
    alert("loop");
}