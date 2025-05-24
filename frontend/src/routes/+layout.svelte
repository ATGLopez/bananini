<script lang="ts">
	import '../app.css';

  import { page } from '$app/state';


	let { children } = $props();
</script>

<main class="min-h-screen bg-yellow-50 flex flex-col items-center">
  <nav class="flex mt-6 border border-black rounded-full overflow-hidden bg-white shadow-sm">
    <a href="#home">
      <button 
        class="px-6 py-2 font-semibold transition duration-300 ease-in-out rounded-full cursor-pointer"
        class:!bg-[#F9D65E]={page.url.pathname === '/'}
      >
        Home
      </button>
    </a>

    <a href="#about">
      <button 
        class="px-6 py-2 font-semibold transition duration-300 ease-in-out rounded-full cursor-pointer"
        class:!bg-[#F9D65E]={page.url.pathname === '/about'}
      >
        About
      </button>
    </a>

    <a href="#team">
      <button 
        class="px-6 py-2 font-semibold transition duration-300 ease-in-out rounded-full cursor-pointer"
        class:!bg-[#F9D65E]={page.url.pathname === '/team'}
      >
        Team
      </button>
    </a>
  </nav>

  {@render children()}

</main>

