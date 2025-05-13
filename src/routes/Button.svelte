<script lang="ts">
  export let id: string = '';
  export let addClass: string = '';
  export let onClick: () => void = () => {};
  // export let disabled: boolean = true;
</script>

<button
  id={id}
  onclick={onClick}
  class="text-lg rounded-lg px-4 py-1 cursor-pointer w-full transition duration-200 {addClass}"
>
  <slot />
</button>
