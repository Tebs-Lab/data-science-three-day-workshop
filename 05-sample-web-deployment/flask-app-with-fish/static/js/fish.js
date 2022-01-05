window.addEventListener('load', function() {
    let button = document.querySelector('#submit');
    let form = this.document.querySelector('form'); // It's the only one, though this is not super robust.

    form.addEventListener('submit', async function(event){
        event.preventDefault();
        const formData = new URLSearchParams(new FormData(form));
        let response = await fetch('/fish', {
            method: "post",
            body: formData
        });

        let returnedData = await response.json()
        document.querySelector('p').innerHTML = `Predicted weight: ${returnedData.weight}`
    });
});