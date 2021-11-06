
var API="http://192.168.1.34:5001/";
var ID;
var REDTIME;
var BLUETIME;
var GREENTIME;
var YELLOWTIME;

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
    // Verification if we can connect to the API and get the ID of the public
    data = sendToApi('POST', API+"api/v1/public/", false)
    if ( data == false )
        return false;

    ID = data.id;
    return true;
}

function redHandler(){
    // Send time to RED player and get info the public
    useTime("RED");
    getPublicInfo();
}
function blueHandler(){
    // Send time to BLUE player and get info the public
    useTime("BLUE");
    getPublicInfo();
}
function greenHandler(){
    // Send time to GREEN player and get info the public
    useTime("GREEN");
    getPublicInfo();
}
function yellowHandler(){
    // Send time to YELLOW player and get info the public
    useTime("YELLOW");
    getPublicInfo();
}

 

function useTime(color){
    return sendToApi('POST',API+"api/v1/public/"+ID+"/time/use/"+color);
}

function getPublicInfo(){
    sendToApi('GET', API+"api/v1/public/"+ID)
    //JSON.parse(response.response)
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


function loop(){
    alert("loop");
}