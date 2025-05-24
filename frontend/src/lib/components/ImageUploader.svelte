<script lang="ts">
  import { ImageUp } from 'lucide-svelte';
  import Button from './Button.svelte';

  export let imageUrl: string;
  export let fileName: string;
  export let onFileChange: (e: Event) => void;
  export let buttonClass: string;

  function triggerPicker() {
    const input = document.getElementById('image-input') as HTMLInputElement;
    input?.click();
  }
</script>

<Button onClick={triggerPicker} addClass={`${buttonClass} flex justify-between items-center`}>
  {#if imageUrl}
    <p class="flex-1 text-center">{fileName}</p>
  {:else}
    Upload photo <ImageUp class="w-5 h-5 object-cover" />
  {/if}
</Button>

<!-- <Button id="take-photo-btn" onClick={() => {}} addClass="{banana} flex justify-between items-center">
  Take photo<Camera class="w-5 h-5" />
</Button> -->

<input
  id="image-input"
  type="file"
  accept="image/*"
  class="hidden"
  onchange={onFileChange}
/>
