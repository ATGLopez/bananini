<script lang="ts">
	import '../app.css';

  let activeTab = $state('Home');

  function setActive(tab: string) {
    activeTab = tab;
  }

	let { children } = $props();
</script>

<main class="min-h-screen bg-yellow-50 flex flex-col items-center">
  <!-- Connected Navbar -->
  <nav class="flex mt-6 border border-gray-300 rounded-full overflow-hidden bg-white shadow-sm">
    <a href="/">
      <button 
        class="px-6 py-2 font-semibold transition duration-300 ease-in-out rounded-full cursor-pointer"
        style="background-color: {activeTab === 'Home' ? '#F9D65E' : 'transparent'}"
        onclick={() => setActive('Home')}
      >
        Home
      </button>
    </a>

    <a href="/about">
      <button 
        class="px-6 py-2 font-semibold transition duration-300 ease-in-out rounded-full cursor-pointer"
        style="background-color: {activeTab === 'About' ? '#F9D65E' : 'transparent'}"
        onclick={() => setActive('About')}
      >
        About
      </button>
    </a>

    <a href="/team">
      <button 
        class="px-6 py-2 font-semibold transition duration-300 ease-in-out rounded-full cursor-pointer"
        style="background-color: {activeTab === 'Team' ? '#F9D65E' : 'transparent'}"
        onclick={() => setActive('Team')}
      >
        Team
      </button>
    </a>
  </nav>

  {@render children()}

</main>

