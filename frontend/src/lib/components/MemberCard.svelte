<script lang="ts">
import GithubIcon from '$lib/assets/github.svg';

export let name: string = ''
export let username: string = ''

</script>

<main>
  <div class="grid lg:grid-rows-[auto_auto_auto] gap-0 md:gap-1">
    <div class="w-40 h-40 md:w-50 md:h-50 border border-gray-800 rounded-sm">
      <img src={`https://github.com/${username}.png`} alt="GitHub Avatar" class="object-cover rounded-sm w-full h-full" />
    </div>

    <p class="font-bold text-lg text-center">{name}</p>

    <a href="https://github.com/{username}" target="_blank" class="flex justify-center items-center gap-2 text-lg">
      <img src={GithubIcon} class="w-5 fill-[#F9D65E] hover:fill-[#FCE588]" alt="Github icon"/>
      <p class="underline hover:no-underline">{username}</p>
    </a>
  </div>
</main>