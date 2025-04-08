<script setup lang="ts">
onPrehydrate(() => {
  if (localStorage.theme === "dark" || !("theme" in localStorage)) {
    document.documentElement.classList.add('p-dark')
  } else {
    document.documentElement.classList.remove('p-dark')
  }
})
</script>

<template>
  <div class="bg-surface-100 dark:bg-surface-800 min-h-screen p-2">
    <Toast />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
