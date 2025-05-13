<script lang="ts">
  import { ChevronDown, ImageUp, Camera, CircleX } from 'lucide-svelte';
  import Button from './Button.svelte';

  const banana = 'bg-[#F9D65E] hover:bg-[#FCE588]';
  const leaf = 'bg-[#AACE70] hover:bg-[#C1DC8E]'

  let activeModel = $state('CNN');
  let imageUrl = $state('');

  function handleFileChange(event: Event) {
    const target = event.target as HTMLInputElement;
    const file = target.files?.[0];
    if (file && file.type.startsWith('image/')) {
      imageUrl = URL.createObjectURL(file);
    }
  }

  function clearImage() {
    imageUrl = '';
    const input = document.getElementById('image-input') as HTMLInputElement | null;
    if (input) input.value = ''; // Reset the input so the same file can be re-uploaded
  }

  function openFilePicker(): void {
    const input = document.getElementById('image-input') as HTMLInputElement | null;
    input?.click();
  }

  function toggleDropdown() {
    const dropdown = document.querySelector('#dropdown-menu');
    if (dropdown) {
      dropdown.classList.toggle('hidden');
    }
  }

  function setModel(model: string) {
    activeModel = model;
    toggleDropdown();
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

        <div class="relative w-full">
          <Button id="dropdown-button" onClick={toggleDropdown} addClass="{banana} flex justify-between items-center">
            {activeModel} <ChevronDown class="w-5 h-5" />
          </Button>

          <div 
            id="dropdown-menu"
            class="hidden absolute top-full left-0 mt-0 w-full rounded-lg text-left bg-white shadow-md z-10"
          >
            <div>
              <button 
                onclick={() => setModel('CNN')}
                class="py-1 px-4 cursor-pointer text-left w-full rounded-lg hover:bg-gray-200"
              >
                CNN
              </button>
            </div>

            <div>
              <button 
                onclick={() => setModel('ViT')}
                class="py-1 px-4 cursor-pointer text-left w-full rounded-lg hover:bg-gray-200"
              >
                ViT
              </button>
            </div>
          </div>
        </div>

      </div>
      
      <div class="grid gap-2">
        <p class="text-xl">
          <b>Step 2.</b> Upload a photo of banana leaf.
        </p>

        <Button id="upload-photo-btn" onClick={openFilePicker} addClass="{banana} flex justify-between items-center">
          Upload photo<ImageUp class="w-5 h-5" />
        </Button>

        <Button id="take-photo-btn" onClick={() => {}} addClass="{banana} flex justify-between items-center">
          Take photo<Camera class="w-5 h-5" />
        </Button>

        <input id="image-input" type="file" accept="image/*" class="hidden" onchange={handleFileChange}/>
      </div>
    </div>

    <div class="flex flex-col gap-4">
      <div class="relative w-full aspect-square border rounded-lg flex items-center justify-center overflow-hidden">
        {#if imageUrl}
          <button
            class="absolute top-2 right-2 z-10 rounded-full p-1 shadow hover:bg-red-300 transition"
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
    </div>
  </div>
</main>
