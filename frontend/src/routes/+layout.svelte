<script lang="ts">
	import '../app.css';

  import { onMount } from 'svelte';
  import { page } from '$app/state';

  let activeSection = $state('');

	let { children } = $props();

  function scrollIntoView(event: MouseEvent) {
    event.preventDefault();

    const target = event.currentTarget as HTMLAnchorElement;
    const href = target.getAttribute('href');
    if (!href) return;

    const el = document.querySelector(href);
    if (!el) return;

    const yOffset = -80; 
    const y = el.getBoundingClientRect().top + window.scrollY + yOffset;

    window.scrollTo({ top: y, behavior: 'smooth' });

    history.pushState(null, '', href);
  }

  onMount(() => {
    const sections = document.querySelectorAll('section[id]');
    
    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            const id = entry.target.getAttribute('id');
            if (id) activeSection = id;
          }
        }
      },
      { threshold: 0.6 }
    );

    sections.forEach((section) => observer.observe(section));

    return () => observer.disconnect();
  });
</script>

<main class="min-h-screen bg-yellow-50 flex flex-col items-center">
  <nav class="fixed top-4 z-50 left-1/2 transform -translate-x-1/2 flex mt-6 border border-black rounded-full overflow-hidden bg-white shadow-sm">
    <a href="#home" onclick={scrollIntoView}>
      <button 
        class="px-6 py-2 font-semibold transition duration-300 ease-in-out rounded-full cursor-pointer"
        class:!bg-[#F9D65E]={activeSection === 'home' || activeSection === ''}
      >
        Home
      </button>
    </a>

    <a href="#about" onclick={scrollIntoView}>
      <button 
        class="px-6 py-2 font-semibold transition duration-300 ease-in-out rounded-full cursor-pointer"
        class:!bg-[#F9D65E]={activeSection === 'about'}
      >
        About
      </button>
    </a>

    <a href="#team" onclick={scrollIntoView}>
      <button 
        class="px-6 py-2 font-semibold transition duration-300 ease-in-out rounded-full cursor-pointer"
        class:!bg-[#F9D65E]={activeSection === 'team'}
      >
        Team
      </button>
    </a>
  </nav>

  {@render children()}

</main>

