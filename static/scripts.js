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

    // Plot the BER here if you want...

    // Show the output section
    document.getElementById('output-section').classList.remove('hidden');

    // Set the image source to get the new image
    const imageElement = document.getElementById('received-image');
    imageElement.src = '/output_image.png?' + new Date().getTime(); // prevent caching
  } else {
    alert('Simulation failed. Please try again.');
  }
  imageElement.onload = () => {
    console.log("Image loaded!");
  };
  imageElement.src = '/output_image.png?' + Date.now();
  imageElement.onerror = () => {
    console.error("Error loading image.");
  };
  imageElement.addEventListener('load', () => {
    console.log("Image loaded successfully!");
  });  
});
