window.addEventListener('load', function() {
    // Fetch the canvas and drawing context
    let canvas = document.getElementById('canvas');
    let context = canvas.getContext('2d');

    // Make the canvas a white background with a border
    canvas.width = 28*2; // 28x28 is too small for mouse based drawing
    canvas.height = canvas.width;
    canvas.style.border = '1px solid black';
    context.fillStyle = 'white';
    context.fillRect(0, 0, canvas.width, canvas.height);

    // Initialize some drawing values
    let drawingArcRadius = 1; 
    let start = 0;
    let end = Math.PI * 2;
    let mouseIsDown = false;

    // Draw a single point where the mouse currently is
    function drawPoint(event){
        if(mouseIsDown){
            context.fillStyle = 'black';
            context.lineWidth = drawingArcRadius * 2; // line width == diameter of the dots
            context.lineTo(event.offsetX, event.offsetY);
            context.stroke();
            context.beginPath();
            context.arc(event.offsetX, event.offsetY, drawingArcRadius, start, end);
            context.fill();
            context.beginPath();
            context.moveTo(event.offsetX, event.offsetY);
        }
    }

    function dragStart(event){
        mouseIsDown = true;
        drawPoint(event);
    }

    function dragFinish(){
        mouseIsDown = false;
        context.beginPath();
    }

    canvas.addEventListener('mousedown', dragStart);
    canvas.addEventListener('mouseup', dragFinish);
    canvas.addEventListener('mousemove', drawPoint);

    // Clear the canvas if user click the clear button
    this.document.getElementById('clear').addEventListener('click', function(event){
        context.clearRect(0, 0, canvas.width, canvas.height)
        context.fillStyle = 'white';
        context.fillRect(0, 0, canvas.width, canvas.height);
    });

    /*
    ========= End Drawing Section ========
    ========= Begin Image Post Section ========
    */

    async function postImage(event) {
        // toBlob creates an image out of the current state of the canvas
        // and passes it to the provided callback.
        canvas.toBlob(sendData, 'image/jpeg', 1);

        // Actually sends the data to the server
        async function sendData(blob) {
            try {
                let response = await fetch('/mnist', {
                    method: 'POST',
                    body: blob,
                    headers: {
                        "Content-Type": 'image/jpeg'
                    }
                });

                let data = await response.json()
                let formattedResult = `Digit: ${data.digit_prediction}, Conf: ${(data.confidence * 100).toPrecision(4)}%`
                document.getElementById('results').innerText = formattedResult;
            }
            catch (exception) {
                console.warn('Something went wrong.', exception);
            }
        }
    }

    let button = document.getElementById('submit');
    button.addEventListener('click', postImage);
});