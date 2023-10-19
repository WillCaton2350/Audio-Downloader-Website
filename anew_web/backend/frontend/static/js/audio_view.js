function playAudio() {
    fetch('/play_audio/') 
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log('Audio played successfully');
            } else {
                console.error('Error:', data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
