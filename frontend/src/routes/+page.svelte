<script lang="ts">
  import { ChevronDown, ImageUp, Camera, CircleX } from 'lucide-svelte';
  import { classifyImage } from '$lib/api';
  import Button from '../lib/components/Button.svelte';
  import ImageUploader from '$lib/components/ImageUploader.svelte';
  import DropdownModelSelector from '$lib/components/DropdownModelSelector.svelte';

  const banana = 'bg-[#F9D65E] hover:bg-[#FCE588]';
  const leaf = 'bg-[#AACE70] hover:bg-[#C1DC8E]'

  let activeModel = $state('CNN');
  let imageUrl = $state('');
  let fileName = $state('')

  function handleFileChange(event: Event) {
    const target = event.target as HTMLInputElement;
    const file = target.files?.[0];
    if (file && file.type.startsWith('image/')) {
      imageUrl = URL.createObjectURL(file);
      fileName = file.name;
    }
  }

  function clearImage() {
    imageUrl = '';
    const input = document.getElementById('image-input') as HTMLInputElement | null;
    if (input) input.value = '';
  }

</script>

<main>
  <div class="py-12 text-4xl text-center">
    Welcome to <b>Bananapp</b>.
  </div>

  <div class="grid grid-cols-1 md:grid-cols-[230px_230px] gap-8 md:gap-28">
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

    <div class="flex flex-col gap-4">
      <div class="relative w-full aspect-square border rounded-lg flex items-center justify-center overflow-hidden">
        {#if imageUrl}
          <button
            class="absolute top-2 right-2 z-10 p-0.5 rounded-full shadow bg-red-300 hover:bg-red-400 transition"
            onclick={clearImage}
          >
            <CircleX class="w-5 h-5" />
          </button>
          <img src={imageUrl} alt="Preview" class="object-cover w-full h-full" />
        {:else}
          <span><ImageUp /></span>
        {/if}
      </div>

      <Button id="classify-btn" onClick={() => {}} addClass={imageUrl ? leaf : 'bg-gray-300 cursor-not-allowed'}>
        Classify
      </Button>

      <div></div>
    </div>
  </div>
</main>
