
var API="http://192.168.1.34:5001/";
var IP;


function connect(){
    isConnected = getMyIp();
    console.error(isConnected);
    if ( isConnected == true){
        requestToApi_Connect();
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

function getMyIp(){
    isConnected = true;
    var request = new XMLHttpRequest();
    request.open('GET', API+"get_my_ip", false);  // `false` makes the request synchronous
    try{
        request.send(null);
    }catch(error){
        return false;
    }

    if (request.status === 200) {
        const data = JSON.parse(request.responseText);
        console.log(data.ip);
        IP = data.ip;
    }else{
        isConnected = false;
    }
    return isConnected;
}

function requestToApi_Connect(){
    // const params = {
    //     "ip": "127.0.0.1",
    // };
    // const options = {
    //     method: 'POST',
    //     body: JSON.stringify( params )  
    // };
    // fetch( API+"api/v1/public/"+IP, options )
    // .then( response => response.json() )
    // .then( response => {
    //     alert(response);
    // } );
    
    var request = new XMLHttpRequest();
    request.open('POST', API+"api/v1/public/"+IP, false);  // `false` makes the request synchronous
    try{
        request.send(null);
    }catch(error){
        return false;
    }
    return true;
}

function redHandler(){
    alert("redHandler");
}
function blueHandler(){
    alert("blueHandler");
}
function greenHandler(){
    alert("greenHandler");
}
function yellowHandler(){
    alert("yellowHandler");
}
function loop(){
    alert("loop");
}