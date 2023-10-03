function playAudio() {

    fetch('/Users/administrator/Desktop/Projects/djangoProjects/anew_web/backend/frontend/playaudio.py')
        .then(response => response.text())
        .then(data => {
            console.log(data); 
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function pauseAudio() {

}