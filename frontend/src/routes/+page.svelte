<script lang="ts">
  import { ImageUp, CircleX } from 'lucide-svelte';
  import { classifyImageByCNN } from '$lib/api';
  import Button from '../lib/components/Button.svelte';
  import ImageUploader from '$lib/components/ImageUploader.svelte';
  import DropdownModelSelector from '$lib/components/DropdownModelSelector.svelte';
  import { labelMap, descMap }from '$lib/classification';

  const banana = 'bg-[#F9D65E] hover:bg-[#FCE588]';
  const leaf = 'bg-[#AACE70] hover:bg-[#C1DC8E]'

  let activeModel = $state('CNN');
  let imageUrl = $state('');
  let fileName = $state('');
  let imageFile: File | null = null;

  let classificationResult: string | null = $state(null);

  function handleFileChange(event: Event) {
    const target = event.target as HTMLInputElement;
    const file = target.files?.[0];

    console.log('Image uploaded:', file?.name);

    if (file && file.type.startsWith('image/')) {
      imageFile = file;
      imageUrl = URL.createObjectURL(file);
      fileName = file.name;
    }

    classificationResult = null;
  }

  function clearImage() {
    console.log('Image cleared.')
    imageUrl = '';

    const input = document.getElementById('image-input') as HTMLInputElement | null;
    if (input) input.value = '';

    classificationResult = null;
  }

  async function handleClassify() {
    console.log('pressed classify button');
    classificationResult = null;
    if (imageFile && activeModel) {
      try {
        const result = await classifyImageByCNN(imageFile, activeModel);
        console.log('Classification result:', result);
        classificationResult = result.class;
      } catch (error: any) {
        console.error('Error during classification:', error);
        classificationResult = 'Error: ' + error.message;
      }
    } else {
      console.warn('No image selected or model selected');
      classificationResult = null;
    }
  }

</script>

<main class="pb-8">
  <div class="py-12 text-4xl text-center">
    Welcome to <b>Bananapp</b>.
  </div>

  <div class="grid grid-cols-[400px] md:grid-cols-[240px_240px] gap-8 md:gap-28">
    {#if classificationResult && imageUrl}
      <div class="flex flex-col gap-6">
        <div class="grid gap-0">
          <p class="text-xl">Classification:<br></p>
          <p class="text-3xl"><b>{labelMap[classificationResult]}</b></p>
        </div>

        <div class="grid">
          <p class="text-lg">{descMap[classificationResult]}</p>
        </div>
      </div>
    {:else}
      <div class="flex flex-col gap-10">
        <div class="grid gap-2">
          <p class="text-xl">
            <b>Step 1.</b> Choose a model for image classification.
          </p>

          <DropdownModelSelector
            activeModel={activeModel}
            onSelect={(model) => (activeModel = model)}
            buttonClass={banana}
          />
        </div>
        
        <div class="grid gap-2">
          <p class="text-xl">
            <b>Step 2.</b> Upload a photo of banana leaf.
          </p>

          <ImageUploader {imageUrl} {fileName} onFileChange={handleFileChange} buttonClass={banana} />
        </div>
      </div>
    {/if}

    <div class="flex items-center flex-col gap-4">
      <div class="relative w-full aspect-square border rounded-lg flex items-center justify-center overflow-hidden max-w-[400px] max-h-[400px]">
        {#if imageUrl}
          <button
            class="absolute top-2 right-2 z-10 p-0.5 rounded-full shadow bg-red-300 hover:bg-red-400 transition"
            onclick={clearImage}
          >
            <CircleX class="w-5 h-5" />
          </button>
          <img src={imageUrl} alt="Preview" class="object-contain w-full h-full" />
        {:else}
          <span><ImageUp /></span>
        {/if}
      </div>
      
      {#if classificationResult && imageUrl}
        <Button id="reset-btn" onClick={clearImage} addClass={leaf}>
          Reset
        </Button>
      {:else}
        <Button id="classify-btn" onClick={handleClassify} disabled={!imageUrl} 
          addClass={imageUrl ? leaf : 'bg-gray-300 cursor-not-allowed'}
        >
          Classify
        </Button>
      {/if}
      
    </div>
  </div>
</main>
