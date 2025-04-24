document.getElementById('upload-form').addEventListener('submit', async function(e) {
  e.preventDefault();

  const imageInput = document.getElementById('image-input');
  const modulationSelect = document.getElementById('modulation-select');

  const formData = new FormData();
  formData.append('image', imageInput.files[0]);
  formData.append('modulation', modulationSelect.value);

  const response = await fetch('/simulate', {
    method: 'POST',
    body: formData
  });

  if (response.ok) {
    const data = await response.json();

    // Show the output section
    document.getElementById('output-section').classList.remove('hidden');

    // Set and monitor the image source
    const imageElement = document.getElementById('received-image');
    const cacheBuster = Date.now();
    imageElement.src = '/output_image.png?' + cacheBuster;

    imageElement.onload = () => {
      console.log("Image loaded!");
    };
    imageElement.onerror = () => {
      console.error("Error loading image.");
    };
    imageElement.addEventListener('load', () => {
      console.log("Image loaded successfully!");
    });
  } else {
    alert('Simulation failed. Please try again.');
  }
});
