export async function classifyImage() {
  if (!imageUrl) return;

  const input = document.getElementById('image-input') as HTMLInputElement;
  const file = input.files?.[0];
  if (!file) return;

  const formData = new FormData();
  formData.append('file', file);

  const res = await fetch('http://localhost:8000/classify', {
    method: 'POST',
    body: formData
  });

  const data = await res.json();
  alert(`Prediction: ${data.class}`);
}