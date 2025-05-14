<script lang="ts">
  export let id: string = '';
  export let addClass: string = '';
  export let onClick: (any: any) => any = () => {};
  export let disabled: boolean = false;
</script>

<button
  id={id}
  onclick={onClick}
  disabled={disabled}
  class="text-lg rounded-lg px-4 py-1 cursor-pointer w-full shadow transition duration-200 {addClass}"
>
  <slot />
</button>
