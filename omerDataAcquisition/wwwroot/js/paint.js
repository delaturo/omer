var canvas, ctx, flag = false,
    prevX = 0,
    currX = 0,
    prevY = 0,
    currY = 0,
    dot_flag = false;

var x = "black",
    y = 2;

document.addEventListener("DOMContentLoaded", function () {
    canvas = document.getElementById('can');
    canvasContainer = document.getElementById('canvasContainer');
    ctx = canvas.getContext("2d");    

    addLiseteners();

    outputsize()
    new ResizeObserver(outputsize).observe(canvasContainer)
});

function addLiseteners(){

    window.ontouchstart = function(event) {
        if (event.touches.length>1) { //If there is more than one touch
            event.preventDefault();
        }
    }

    // Click Events
    canvas.addEventListener("mousemove", function (e) {
        findxy('move', e)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        findxy('down', e)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        findxy('up', e)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        findxy('out', e)
    }, false);

    // Tap Events (a.k.a Touch)
    canvas.addEventListener("touchstart", function (e) {
        findxy('down', e.touches[0])
        // dispatchMouseEvent("mouseDown",e);
    }, false);
    canvas.addEventListener("touchend", function (e) {
        findxy('up', e.touches[0])
        // dispatchMouseEvent("mouseup",e);
    }, false);
    canvas.addEventListener("touchmove", function (e) {
        findxy('move', e.touches[0])
        // dispatchMouseEvent("mousemove",e);
    }, false);
    
}

function draw() {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = x;
    ctx.lineWidth = y;
    ctx.stroke();
    ctx.closePath();
}

function findxy(res, e) {
    if (res == 'down') {
        prevX = currX;
        prevY = currY;
        currX = getCurrentX(e);
        currY = getCurrentY(e);
        // currX = e.clientX;
        // currY = e.clientY;

        flag = true;
        dot_flag = true;
        if (dot_flag) {
            ctx.beginPath();
            ctx.fillStyle = x;
            ctx.fillRect(currX, currY, 2, 2);
            ctx.closePath();
            dot_flag = false;
        }
    }
    if (res == 'up' || res == "out") {
        flag = false;
    }
    if (res == 'move') {
        if (flag) {
            prevX = currX;
            prevY = currY;
            currX = getCurrentX(e);
            currY = getCurrentY(e);
            draw();
        }
    }
}

function getCurrentX(e) {
    var rect = canvas.getBoundingClientRect();
    return (e.clientX - rect.left) / (rect.right - rect.left) * canvas.width;
}

function getCurrentY(e) {
    var rect = canvas.getBoundingClientRect();
    return (e.clientY - rect.top) / (rect.bottom - rect.top) * canvas.height;
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function send(){
    var image = canvas.toDataURL("image/png");
    buffer = image.replace('data:image/png;base64,', '');
    
    var data = new FormData();
    data.append("charId",document.getElementById("charId").value);
    data.append("imgCaptured", buffer);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/Home/SaveCapture");
    xhr.onload = function(){
        console.log(this.response);
        location.reload();
    };
    xhr.send(data);
}

function outputsize() {
    newWidth = canvasContainer.offsetWidth * 0.8;
    if (newWidth > 400) newWidth = 400;
    canvas.width = newWidth;
    canvas.height = newWidth; // Square canvas
}
