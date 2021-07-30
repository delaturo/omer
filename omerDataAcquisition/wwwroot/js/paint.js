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
    w = canvas.width;
    h = canvas.height;

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

    outputsize()
    new ResizeObserver(outputsize).observe(canvasContainer)
});

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

function erase() {
    ctx.clearRect(0, 0, w, h);
}

function send(){
    location.reload();
}

function outputsize() {
    newWidth = canvasContainer.offsetWidth * 0.8;
    if (newWidth > 400) newWidth = 400;
    canvas.width = newWidth;
    canvas.height = newWidth; // Square canvas
}
