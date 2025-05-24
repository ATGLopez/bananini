<script lang="ts">
  import { ImageUp, CircleX } from 'lucide-svelte';
  import { classifyImageByCNN } from '$lib/api';
  import Button from '../lib/components/Button.svelte';
  import ImageUploader from '$lib/components/ImageUploader.svelte';
  import DropdownModelSelector from '$lib/components/DropdownModelSelector.svelte';
  import { labelMap, descMap }from '$lib/classification';
  import MemberCard from "$lib/components/MemberCard.svelte";

  const banana = 'bg-[#F9D65E] hover:bg-[#FCE588]';
  const leaf = 'bg-[#AACE70] hover:bg-[#C1DC8E]'

  let activeModel = $state('CNN');
  let imageUrl = $state('');
  let fileName = $state('');
  let imageFile: File | null = null;

  let classificationResult: string | null = $state(null);

  function handleFileChange(event: Event) {
    const target = event.target as HTMLInputElement;
    const file = target.files?.[0];

    console.log('Image uploaded:', file?.name);

    if (file && file.type.startsWith('image/')) {
      imageFile = file;
      imageUrl = URL.createObjectURL(file);
      fileName = file.name;
    }

    classificationResult = null;
  }

  function clearImage() {
    console.log('Image cleared.')
    imageUrl = '';

    const input = document.getElementById('image-input') as HTMLInputElement | null;
    if (input) input.value = '';

    classificationResult = null;
  }

  async function handleClassify() {
    console.log('pressed classify button');
    classificationResult = null;
    if (imageFile && activeModel) {
      try {
        const result = await classifyImageByCNN(imageFile, activeModel);
        console.log('Classification result:', result);
        classificationResult = result.class;
      } catch (error: any) {
        console.error('Error during classification:', error);
        classificationResult = 'Error: ' + error.message;
      }
    } else {
      console.warn('No image selected or model selected');
      classificationResult = null;
    }
  }

</script>

<main class="scroll-smooth">

  <section id="home" class="snap-start flex justify-center px-4 pb-12">
    <div class="w-full max-w-xs md:max-w-3xl min-w-xs md:min-w-2xl">
      <div class="py-12 text-4xl text-center">
        Welcome to <b>Bananini</b>.
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-16">
        {#if classificationResult && imageUrl}
          <div class="flex flex-col gap-6">
            <div class="grid gap-0">
              <p class="text-lg md:text-xl">Classification:<br></p>
              <p class="text-3xl md:text-4xl"><b>{labelMap[classificationResult]}</b></p>
            </div>

            <div class="grid">
              <p class="text-lg md:text-xl">{descMap[classificationResult]}</p>
            </div>
          </div>
        {:else}
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
        {/if}

        <div class="flex items-center flex-col gap-4">
          <div class="relative w-full aspect-square border rounded-lg flex items-center justify-center overflow-hidden max-w-[400px] max-h-[400px]">
            {#if imageUrl}
              <button
                class="absolute top-2 right-2 z-10 p-0.5 rounded-full shadow bg-red-300 hover:bg-red-400 transition"
                onclick={clearImage}
              >
                <CircleX class="w-5 h-5" />
              </button>
              <img src={imageUrl} alt="Preview" class="object-contain w-full h-full" />
            {:else}
              <span><ImageUp /></span>
            {/if}
          </div>
          
          {#if classificationResult && imageUrl}
            <Button id="reset-btn" onClick={clearImage} addClass={leaf}>
              Reset
            </Button>
          {:else}
            <Button id="classify-btn" onClick={handleClassify} disabled={!imageUrl} 
              addClass={imageUrl ? leaf : 'bg-gray-300 cursor-not-allowed'}
            >
              Classify
            </Button>
          {/if}
          
        </div>
      </div>
    </div>
  </section>

  <hr id="about" class="border-t border-gray-300 my-10" />

  <section class="snap-start flex justify-center px-4 pb-12">
    <div>
      <div class="pb-12 text-4xl text-center">
        <b>About</b>
      </div>

      <div class="px-16 md:px-48 text-justify">
        <p>
          Minions ipsum gelatooo uuuhhh para tú bappleees para tú tank yuuu! Gelatooo po kass. 
          Bappleees poopayee tulaliloo pepete belloo! Wiiiii. 
          Baboiii hana dul sae bappleees pepete hana dul sae po kass po kass baboiii.
        </p>

        <br>
        
        <p>
          Belloo! hahaha baboiii poopayee hahaha belloo! La bodaaa bee do bee do bee do chasy. 
          Pepete poopayee tank yuuu! Butt la bodaaa wiiiii aaaaaah ti aamoo! Poulet tikka masala. 
          Tatata bala tu daa ti aamoo! Poulet tikka masala poopayee wiiiii bappleees hana dul sae ti aamoo! Jeje belloo!
        </p>

        <br>

        <p>
          Gelatooo para tú aaaaaah chasy wiiiii wiiiii daa hahaha me want bananaaa! 
          Daa jiji bappleees tank yuuu! Butt po kass gelatooo hahaha. 
          Potatoooo poulet tikka masala butt poopayee uuuhhh po kass. 
          Chasy belloo! Daa baboiii ti aamoo! Daa.
        </p>
      </div>
    </div>
  </section>

  <hr id="team" class="border-t border-gray-300 my-10" />

  <section class="snap-start flex justify-center px-4 pb-12">
    <div>
      <div class="pb-12 text-4xl text-center">
        <b>Team</b>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-16 items-center">
        <MemberCard name="Aneko Delfin" username="EkoChamber"/>
        <MemberCard name="Alec Lopez" username="ATGLopez"/>
        <MemberCard name="Juni Maca" username="junimaca"/>
      </div>
    </div>
  </section>

</main>