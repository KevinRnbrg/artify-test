<template>
  <main>
    <div v-if="sectorsLoaded" class="flex justify-center">
      <form @submit.prevent="handleSubmit" class="flex flex-col text-left bg-white m-1 sm:m-10 p-5 py-10 sm:p-10 border-y-4 border-blue-600 rounded-md shadow-2xl gap-4">
        <span class="text-3xl font-bold text-blue-600 text-center">Sector Affiliation Form</span>
        <span class="text-center p-1">Please enter your name and pick the Sectors you are currently involved in.</span>
        <hr>
        <div>
          <label for="name" class="block mb-1 text-sm font-medium text-gray-900">Name</label>
          <input id="name" type="text" v-model="name" class="text-gray-900 text-sm rounded-md border-2 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 block w-full p-2.5" placeholder="John Doe" required>
        </div>
        
        <div>
          <label for="sectors-select" class="block mb-1 text-sm font-medium text-gray-900">Sectors</label>
          <select id="sectors-select" multiple size="5" v-model="selectedSectors" class="text-gray-900 text-sm rounded-md border-2 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 block w-full p-2.5" required>
            <option v-for="formattedSector in formattedSectors" :key="formattedSector.id" :value="formattedSector.id" :style="{ 'margin-left': formattedSector.indentation + 'rem' }">
              {{ formattedSector.name }}
            </option>
          </select>
        </div>
        
        <div class="flex items-center mb-2 mt-2">
          <input id="agree-to-terms" type="checkbox" v-model="agree" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600" required>
          <label for="agree-to-terms" class="ms-2 text-sm font-medium text-gray-900">Agree to terms</label>
        </div>
        
        <input type="submit" :value="isUpdateMode ? 'Update' : 'Save'" class="flex w-full justify-center rounded-md bg-blue-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600">
      </form>
    </div>

    <transition name="slide-in">
      <div v-if="showSuccess" class="bg-emerald-200 text-green-900 left-0 bottom-0 m-6 pr-12 pl-4 py-3 border-l-8 border-green-900 rounded absolute" role="alert">
        <strong class="font-bold">Success! </strong>
        <span class="block sm:inline">Your submission has been saved.</span>
        <span class="absolute top-0 bottom-0 right-0 px-4 py-3">
          <svg @click="showSuccess = false" class="fill-current h-6 w-6 text-green-800 cursor-pointer" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><title>Close</title><path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/></svg>
        </span>
      </div>
    </transition>
    <transition name="slide-in">
      <div v-if="showError" class="bg-red-200 text-red-900 left-0 bottom-0 m-6 pr-12 pl-4 py-3 border-l-8 border-red-900 rounded absolute" role="alert">
        <strong class="font-bold">Error! </strong>
        <span class="block sm:inline">Something went wrong.</span>
        <span class="absolute top-0 bottom-0 right-0 px-4 py-3">
          <svg @click="showError = false" class="fill-current h-6 w-6 text-red-800 cursor-pointer" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><title>Close</title><path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/></svg>
        </span>
      </div>
    </transition>
  </main>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';

const name = ref('');
const selectedSectors = ref([]);
const agree = ref(false);
const sectorsLoaded = ref(false);
const isUpdateMode = ref(false);
const showSuccess = ref(false);
const showError = ref(false);
let userID = null;
let sectors = [];

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/sectors', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
    });
    const data = await response.json();
    sectors = data;
    sectorsLoaded.value = true;

  } catch (error) {
    console.error('Error fetching user information:', error); /* exclude from build */
    showError.value = true;
  }
});

const handleSubmit = async () => {
  showSuccess.value = false;
  showError.value = false;
  try {
    if (isUpdateMode.value) {
      await updateForm();
    } else {
      await submitForm();
    }
  } catch (error) {
    showError.value = true;
  }
};

const submitForm = async () => {
  showSuccess.value = false;
  showError.value = false;
  try {
    const response = await fetch('http://127.0.0.1:5000/save-user', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: name.value,
        sectors: selectedSectors.value,
        agree: agree.value
      })
    });
    const data = await response.json();
    userID = data.user_id

    isUpdateMode.value = true;
    showSuccess.value = true;
  } catch (error) {
    console.error('Error submitting form:', error); /* exclude from build */
    showError.value = true;
  }
};

const updateForm = async () => {
  showSuccess.value = false;
  showError.value = false;
  try {
    const response = await fetch('http://127.0.0.1:5000/update-user', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: name.value,
        sectors: selectedSectors.value,
        agree: agree.value,
        user_id: userID
      })
    });
    const data = await response.text();

    showSuccess.value = true;
  } catch (error) {
    console.error('Error updating form:', error); /* exclude from build */
    showError.value = true;
  }
};

const formattedSectors = computed(() => {
  const formatted = [];
  sectors.forEach(sector => {
    let indentation = 0;
    let parent = sector.parent;
    while (parent !== null) {
      indentation++;
      parent = sectors.find(item => item.id === parent)?.parent;
    }
    formatted.push({
      id: sector.id,
      name: sector.name,
      indentation: indentation * 2
    });
  });
  return formatted;
});

</script>

<style scoped>
.slide-in-enter-active {
  animation: slide-in 0.25s ease-out;
}

@keyframes slide-in {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(0);
  }
}
</style>