<script setup lang="ts">
import type { NuxtError } from '#app'

defineProps({
  error: Object as () => NuxtError
})

const handleError = () => clearError({ redirect: '/' })
</script>

<template>
  <div class="min-h-screen">
    <div class="flex flex-col justify-center pt-[20vh] items-center">
      <p class="text-center text-8xl">{{ error.statusCode }}</p>
      <p class="text-center text-2xl">{{ error.message }}</p>
      <Button class="w-full sm:w-60 mt-10" @click="handleError">Back</Button>
    </div>
  </div>
</template>