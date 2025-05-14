<script lang="ts">
  import { ChevronDown } from 'lucide-svelte';
  import Button from './Button.svelte';

  export let activeModel: string;
  export let onSelect: (model: string) => void;
  export let buttonClass: string;

  let dropdownOpen = false;

  function toggleDropdown() {
    dropdownOpen = !dropdownOpen;
  }

  function selectModel(model: string) {
    onSelect(model);
    dropdownOpen = false;
  }
</script>

<div class="relative w-full">
  <Button onClick={toggleDropdown} addClass={`${buttonClass} flex justify-between items-center`}>
    {activeModel} <ChevronDown class="w-5 h-5" />
  </Button>

  {#if dropdownOpen}
    <div class="absolute top-full left-0 mt-0 w-full rounded-lg text-left bg-white shadow-md z-10">
      <button onclick={() => selectModel('CNN')} class="py-1 px-4 w-full text-left hover:bg-gray-200">CNN</button>
      <button onclick={() => selectModel('ViT')} class="py-1 px-4 w-full text-left hover:bg-gray-200">ViT</button>
    </div>
  {/if}
</div>
