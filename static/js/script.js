document.addEventListener('DOMContentLoaded', function() 
{
    const form = document.getElementById('prediction-form');
    const resultContainer = document.getElementById('prediction-result');
    const audio = document.querySelector('audio');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Process form data and make predictions here
        const predictionResult = /* Your prediction result logic here */;

        // Display animation and result
        resultContainer.innerHTML = `
            <img src="animation.gif" alt="Animation" id="animated-image" class="animation">
            <p class="result-text">Prediction: ${predictionResult}</p>
        `;
        resultContainer.classList.remove('hidden');
        resultContainer.scrollIntoView({ behavior: 'smooth' });

        // Play the appropriate sound effect
        if (predictionResult === 'No Diabetes') {
            audio.src = 'no_diabetes.mp3';
        } else {
            audio.src = 'diabetes.mp3';
        }
        audio.play();
    });
});