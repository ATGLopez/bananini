const BASE_URL = "https://bananini.onrender.com";

export async function classifyImage(imageFile: File, model: string) {
  const formData = new FormData();
  formData.append('file', imageFile);  
  formData.append('model', model);

  let endpoint = '';
  if (model.toLowerCase().includes('cnn')) {
    endpoint = '/cnn-classify';
  } else if (model.toLowerCase().includes('vit')) {
    endpoint = '/vit-classify';
  } else {
    throw new Error('Unsupported model type');
  }

  try {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const result = await response.json();
      return result;
    } else {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to classify image');
    }
  } catch (err) {
    console.error(`Error classifying image with ${model}:`, err);
    throw err;
  }
}
